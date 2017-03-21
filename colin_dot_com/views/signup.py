import logging

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.template import loader
from django.forms import formset_factory
from django.contrib.auth.forms import UserCreationForm
from parsley.mixins import parsleyfy
from django.contrib.auth.models import User

from colin_dot_com.forms.company import CompanyForm, CompanyImagesForm

logger = logging.getLogger("colin")


def signup(request):
    formset = formset_factory(CompanyImagesForm)

    PUserCreationForm = parsleyfy(UserCreationForm)

    if request.method == 'POST':
        user_form = PUserCreationForm(request.POST)
        company_form = CompanyForm(request.POST)
        image_form = formset(request.POST, request.FILES)

        if user_form.is_valid() and company_form.is_valid() and image_form.is_valid():
            user = user_form.save()
            user.email = user.username
            user.save()
            company = company_form.save(commit=False)
            company.user = user
            company.save()
            for form in image_form:
                image = form.save(commit=False)
                image.company = company
                image.save()

            return HttpResponseRedirect("/preview/" + company.id.__str__())
        else:
            template = loader.get_template('colin_dot_com/registration/mfg.html')
            return HttpResponse(template.render({
                'company_form': company_form,
                'user_form': user_form,
                'image_form': image_form
            }, request))
    else:
        user_form = PUserCreationForm()
        company_form = CompanyForm()
        image_form = formset()
        template = loader.get_template('colin_dot_com/registration/mfg.html')
        return HttpResponse(template.render({
            'company_form': company_form,
            'user_form': user_form,
            'image_form': image_form
        }, request))


def is_available(request):
    found = User.objects.filter(username=request.GET.get("username"))
    if found.count() > 0:
        return HttpResponseServerError("Email address already taken.")
    return HttpResponse("OK")