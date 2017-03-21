from django.contrib.auth.forms import UserCreationForm
from parsley.mixins import parsleyfy
from django.template import loader
from colin_dot_com.forms.designer import DesignerForm
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from colin_dot_com.models.designer import Designer
from PIL import Image, ImageOps
from colin_dot_com.models import materials

def signup(request):
    PUserCreationForm = parsleyfy(UserCreationForm)

    if request.POST:
        user_form = PUserCreationForm(request.POST)
        designer_form = DesignerForm(request.POST)

        if user_form.is_valid() and designer_form.is_valid():
            user = user_form.save(commit=False)
            user.email = user.username
            user.first_name = designer_form.data['first_name']
            user.last_name = designer_form.data['last_name']
            user.save()
            Designer.objects.create(user=user)
            return HttpResponseRedirect("/", request)

        else:
            template = loader.get_template("colin_dot_com/registration/designer.html")
            return HttpResponse(template.render({
                'user_form': user_form,
                'designer_form': designer_form
            }, request))
    else:
        user_form = PUserCreationForm()
        designer_form = DesignerForm()
        template = loader.get_template("colin_dot_com/registration/designer.html")
        return HttpResponse(template.render({
            'user_form': user_form,
            'designer_form': designer_form
        }, request))


def show(request, designer_id):
    designer = Designer.objects.get(pk=designer_id)
    try:
        interests = [materials.get_display(x) for x in designer.interest]
    except KeyError:
        interests = None
    designer.interest = interests
    template = loader.get_template("colin_dot_com/designer/designer_profile.html")
    return HttpResponse(template.render({
        'designer': designer,
    }, request))


