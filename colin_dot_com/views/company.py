import logging, json

from django.core import serializers
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, Http404, HttpResponseServerError, HttpResponseBadRequest, HttpResponseRedirect
from django.template import loader, RequestContext
from django.forms import formset_factory
from django.views.decorators.csrf import ensure_csrf_cookie
from colin_dot_com.models.company import Company
from colin_dot_com.models import materials
from colin_dot_com.forms.message import MessageForm, MessageAttachmentForm
from colin_dot_com.forms.company import CompanyForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import FieldDoesNotExist
from PIL import Image

logger = logging.getLogger("colin")


@ensure_csrf_cookie
def show(request, company_id=None, preview=False):
    logger.debug("user " + request.user.username.__str__())

    edit_mode = False
    company = None
    request_company = None

    if company_id is not None:
        company = Company.objects.get(pk=company_id)
    try:
        request_company = request.user.company
    except Company.DoesNotExist:
        pass

    if company is None:
        company = request_company

    if (request_company is not None) and (company == request_company):
        edit_mode = True
    elif request.user.is_superuser:
        edit_mode = True

    if company is None:
        raise Http404("Company not found.")

    message_form = MessageForm(initial={'recipient': company})
    AttachmentFormset = formset_factory(MessageAttachmentForm)
    message_attachment_formset = AttachmentFormset()

    company_form = CompanyForm(instance=company)

    password_change_form = PasswordChangeForm(user=request.user)

    message_template = loader.render_to_string('colin_dot_com/message/send_message.modal.html', {
        'message_form': message_form,
        'message_attachment_form': message_attachment_formset,
        'to': company.user
    }, request=request)

    advanced_template = loader.render_to_string('colin_dot_com/company/company_advanced.modal.html',
                                                {'company_form': company_form, 'password_change_form': password_change_form, 'company': company}, request=request)

    template = loader.get_template('colin_dot_com/company/show_company.html')
    context = {
        'company': company,
        'edit_mode': edit_mode,
        'preview': preview,
        'new_message_template': message_template,
        'password_change_form': password_change_form,
        'advanced_settings_template': advanced_template,
        'materials': json.dumps(materials.get_options_as_array(), separators=(',', ':'))
    }
    return HttpResponse(template.render(context, request))


def find(request, query=None):
    logger.debug(query)

    name = request.GET.get('company_name')

    if name:
        # return HttpResponse(name)
        # companies = Company.objects.filter(Q(photo__tag__name__contains=query) | Q(name=request.get))
        companies = Company.objects.filter(name__contains=name)
        # companies = Company.objects.filter(photo__tag__name__contains=name)
    else:
        companies = Company.objects.all()

    company_list = list(companies)

    for company in company_list:
        image = company.get_default_image.image
        # pil_image = Image.open(image.file)
        # shorter_side = min(pil_image.size)
        # cropped = pil_image.crop((0,0,shorter_side, shorter_side))
        # filename = "CROPPED_" + image.name
        # cropped.save(filename)
        company.default_image = image  # filename

    if company_list.__len__() > 0:
        data = serializers.serialize('json', company_list)

        return HttpResponse(data, content_type="application/json")
    else:
        raise Http404()


def list_companies(request):
    companies = Company.objects.order_by("-date_added")[:100]
    template = loader.get_template('colin_dot_com/company/company_list.html')
    context = {
        'companies': companies,
    }
    return HttpResponse(template.render(context, request))


def set_default_image(request, image_id):
    if request.method != 'POST':
        return HttpResponseBadRequest("Only POST request are accepted.")
    try:
        company = request.user.company
        photo = company.photo_set.get(pk=image_id)
        company.default_image = photo.id
        company.save()
        return HttpResponse("Success")
    except:
        raise HttpResponseServerError("Invalid request.")


def update_field(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Only POST request are accepted.")
    try:
        company = Company.objects.get(pk=request.POST.get('pk'))
        if request.user.company != company:
            raise HttpResponseServerError("You can only edit your own company.")
        setattr(company, request.POST.get('name'), request.POST.get('value'))
        company.save()
        return HttpResponse("Success")
    except:
        return HttpResponseBadRequest("Update request failed.")


@login_required
def update(request):
    if request.method != 'POST':
        return HttpResponseBadRequest("Only POST request are accepted.")

    company = Company.objects.get(pk=request.POST.get("pk"))
    company_form = CompanyForm(request.POST, instance=company)
    if company_form.is_valid():
        company = company_form.save(commit=False)
        company.user = request.user
        try:
            company.save()
            return HttpResponseRedirect("/explore")
        except BaseException as e:
            return HttpResponse(e)
    else:
        template = loader.get_template("colin_dot_com/company/show_company.html")
        return HttpResponse(template, {
            'company': company_form,
            'advanced_template': loader.render_to_string('colin_dot_com/company/company_advanced.modal.html',
                                                         {'company_form': company_form}, request=request)
        }, request)
