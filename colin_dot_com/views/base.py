
import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from colin_dot_com.models.message import Message
from colin_dot_com.services import email_service
from django.contrib.auth.decorators import login_required

logger = logging.getLogger("colin")


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/dashboard")
    else:
        template = loader.get_template("colin_dot_com/home.html")
        return HttpResponse(template.render(context=None, request=request))

@login_required(login_url="/login/")
def dashboard(request):
    if request.user.is_authenticated():
        template = loader.get_template('colin_dot_com/dashboard.html')
        return HttpResponse(template.render(context=None, request=request))
    else:
        return HttpResponseRedirect("/")


def manifesto(request):
    template = loader.get_template("colin_dot_com/manifesto.html")
    return HttpResponse(template.render(request=request))


def explore(request):
    template = loader.get_template("colin_dot_com/explore.html")
    return HttpResponse(template.render(request=request))


def send_test_mail(request):
    msg = Message(sender=request.user, recipient=request.user, subject="Test", body="Test")
    sent = email_service.send_new_message_notification(message=msg, user=request.user)

    return HttpResponse(sent)

def deactivate(request):
    return HttpResponse("21")
