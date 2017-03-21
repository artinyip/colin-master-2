import random
from django.http import HttpResponse
from django.template import loader
from colin_dot_com.models.landing import LandingImage


def landing(request):
    thanks = request.GET.get('thanks')
    template = loader.get_template('colin_dot_com/landing/landing.html')
    try:
        image = random.choice(LandingImage.objects.all())
    except IndexError:
        image = None
    return HttpResponse(template.render({
        'thanks': thanks,
        'image': image
    }, request))

