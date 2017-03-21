import logging, json, datetime

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.template import loader
from django.forms import formset_factory
from django.db.models import Q, F, Count, Value, IntegerField, CharField
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from colin_dot_com.serializers.messages import ConversationMessageSerializer, ConversationSerializer
from django.core import serializers
from colin_dot_com.services import email_service

from colin_dot_com.models.message import Message, MessageAttachment
from colin_dot_com.models.colin_user import get_colin_user, ColinUser
from colin_dot_com.forms.message import MessageForm, MessageAttachmentForm

logger = logging.getLogger("colin")

@ensure_csrf_cookie
def send(request, format=""):

    in_reply_to = None
    thread_id = None
    to = None

    in_reply_to_id = request.GET.get("in_reply_to")
    if in_reply_to_id:
        in_reply_to_id = int(in_reply_to_id.strip('/'))
    to_id = request.GET.get("to")

    if in_reply_to_id:
        in_reply_to = Message.objects.get(pk=in_reply_to_id)
        to = in_reply_to.sender

        if in_reply_to.thread_id is not None:
            thread_id = in_reply_to.thread_id

    elif to_id:
        to = User.objects.get(pk=to_id)


    AttachmentFormset = formset_factory(MessageAttachmentForm)

    if request.method == 'POST':
        data = request.POST
        message_form = MessageForm(data)
        if request.FILES:
            message_attachment_formset = AttachmentFormset(request.POST, request.FILES)
        else:
            message_attachment_formset = None

        if message_form.is_valid():
            message = message_form.save(commit=False)
            message.sender = request.user
            message.in_reply_to = in_reply_to
            message.save()

            try:
                ids = request.POST.getlist('attachmentIds[]')
                for id in ids:
                    attachment = MessageAttachment.objects.get(pk=id)
                    attachment.message = message
                    attachment.save()
            except Exception as e:
                pass

            if thread_id:
                message.thread_id = thread_id
            else:
                message.thread_id = message.id
            message.save()
            if message_attachment_formset and message_attachment_formset.is_valid():
                for message_attachment_form in message_attachment_formset:
                    message_attachment = message_attachment_form.save(commit=False)
                    message_attachment.message = message
                    message_attachment.save()
            try:
                notify_user(message, message.recipient)
            except AttributeError:
                logger.debug("Can't send email notifications to this user - not colin user")
            except ConnectionRefusedError:
                logger.debug("Can't send email notifications to this user - connection error")
            if format == 'JSON':
                return HttpResponse("Ok")
            else:
                return HttpResponseRedirect("/messages/")
        else:
            template = loader.get_template('colin_dot_com/message/send_message.full_page.html')
            return HttpResponse(template.render({
                'message_form' : message_form,
                'message_attachment_form' : message_attachment_formset,
                'in_reply_to' : in_reply_to,
                'to' : to
            }, request))
    elif request.method == 'GET':
        message_form = MessageForm(initial={'recipient': to})
        message_attachment_formset = AttachmentFormset()

        template = loader.get_template('colin_dot_com/message/send_message.full_page.html')
        return HttpResponse(template.render({
            'message_form': message_form,
            'message_attachment_form': message_attachment_formset,
            'in_reply_to': in_reply_to,
            'to': to
        }, request))


@login_required(login_url="/login/")
def view(request, message_id):

    template = loader.get_template('colin_dot_com/message/view_message.html')
    user_messages = Message.objects.filter(Q(recipient=request.user) | Q(sender=request.user))
    message = user_messages.get(pk=message_id)
    if message.recipient == request.user:
        message.read = True

    message.save()

    if message:
        return HttpResponse(template.render({
            'message': message
        }, request))
    else:
        return HttpResponseBadRequest("You're trying to access a message you don't have access to")


@ensure_csrf_cookie
def add_attachment(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Only accepts posts.")
    form = MessageAttachmentForm(request.POST, request.FILES)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.save()
        return HttpResponse(photo.id)
    else:
        raise HttpResponseBadRequest(form.errors)


@ensure_csrf_cookie
@login_required(login_url="/login/")
def list_convos(request, type=None):
    template = loader.get_template('colin_dot_com/message/list_messages.html')

    if type == "sent":
        messages = Message.objects.filter(sender=request.user)
        for m in messages:
            m.read = True
    else:
        type = "inbox"
        messages = Message.objects.filter(recipient=request.user)

    convos = messages.values('thread_id').annotate(count=Count('designation'))
    unread = Message.objects.filter(Q(read=False) & Q(recipient=request.user)).count()

    return HttpResponse(template.render({
        'messages': messages,
        'type': type,
        'unread': unread,
        'convos': convos
    }, request))

@ensure_csrf_cookie
@login_required(login_url="/login/")
def list_messages(request, format='html'):
    convos = Message.objects.values('thread_id').annotate(dcount=Count('thread_id'))
    unread = Message.objects.filter(Q(read=False) & Q(recipient=request.user)).count()

    threads = []
    for thread in convos:
        t = Message.objects.filter(thread_id=thread['thread_id'])\
            .annotate(count=Value(thread['dcount'], output_field=IntegerField()))\
            .order_by("-date_sent").first()
        threads.append(t)

    if format == "json":
        for t in threads:
            if t.sender == request.user:
                t.friend = t.get_recipient_name
                t.friend_id = t.recipient.id
            else:
                t.friend = t.get_sender_name
                t.friend_id = t.sender.id
        serializer = ConversationSerializer(threads, many=True)
        return HttpResponse(json.dumps(serializer.data), content_type="application/json")

    template = loader.get_template('colin_dot_com/message/list_messages.html')

    return HttpResponse(template.render({
        'type': type,
        'unread': unread,
        'threads': threads
    }, request))


@login_required(login_url="/login")
def get_conversations(request):
    messages = Message.objects.filter(Q(recipient=request.user) | Q(sender=request.user))
    for m in messages:
        m.set_friend(request.user)

    # friends = messages.values('friend').annotate(friend_count=Count('friend'))
    friends = set([message.friend for message in messages])

    threads = []
    for f in friends:
        convo_items = sorted([m for m in messages if m.friend == f], key=lambda mes: mes.date_sent, reverse=True)
        thread = convo_items[0]
        thread.friend_name = thread.get_friend_name()
        thread.friend_id = thread.friend.id
        thread.count = len(convo_items)
        try:
            thread.avatar = get_colin_user(thread.friend).get_avatar()
        except:
            thread.avatar = None
        # thread = messages.filter(friend=f)\
        #     .annotate(count=Value(f['friend_count'], output_field=IntegerField()))\
        #     .order_by("-date_sent")
        threads.append(thread)

    serializer = ConversationSerializer(sorted(threads, key=lambda t: t.date_sent, reverse=True), many=True)
    return HttpResponse(json.dumps(serializer.data), content_type="application/json")



@login_required(login_url="/login")
def get_convo_items(request, friend_id):
    latest = request.GET.get('latest')
    if not latest:
        latest = 0
    items = Message.objects.filter(
        Q(
            Q(
                Q(recipient=request.user) & Q(sender__id=friend_id)) |
            Q(
                Q(sender=request.user) & Q(recipient__id=friend_id))
        ) & Q(pk__gte=latest)).order_by("-date_sent")
    for i in items:
        i.direction = ("received" if i.sender != request.user else "sent")
        i.sender_name = i.get_sender_name
        i.date_sent = i.date_sent.isoformat()
        colin_user = get_colin_user(i.sender)
        try:
            i.avatar = colin_user.get_avatar()
        except:
            i.avatar = None
        try:
            i.link = colin_user.get_link()
        except:
            i.link = None
    serializer = ConversationMessageSerializer(items, many=True)
    data = json.dumps(serializer.data)
    return HttpResponse(data, content_type="application/json")


@login_required(login_url="/login")
def get_unread_messages(request):
    unreadMessages = Message.objects.filter(Q(read=False) & Q(recipient=request.user))
    count = unreadMessages.count()

    response = {
        'count': count,
        'messages': serializers.serialize('json', unreadMessages[:5])
    }

    return HttpResponse(json.dumps(response), content_type="application/json")


def notify_user(message, user):
    colin_user = get_colin_user(user)
    if colin_user.send_email_notification:
        email_service.send_new_message_notification(message, user)


@login_required(login_url="/login")
def read(request):
    message_id = request.GET.get("id")
    message = Message.objects.get(pk=message_id)
    if message.recipient == request.user and message.read == False:
        message.read = True
        message.date_read = datetime.datetime.now()
        message.save()
    return HttpResponse("Ok")

