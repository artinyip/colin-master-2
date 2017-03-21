import logging, json

from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, Http404, HttpResponseServerError, HttpResponseBadRequest
from django.template import loader, RequestContext
from django.views.decorators.csrf import ensure_csrf_cookie
from colin_dot_com.models.company import Company, Photo
from colin_dot_com.serializers.company import PhotoSerializer
from colin_dot_com.forms.company import CompanyImagesForm
from django.views.decorators.csrf import ensure_csrf_cookie
from easy_thumbnails.files import get_thumbnailer

logger = logging.getLogger("colin")

def find(request):

    term = request.GET.get("term")
    company_id = request.GET.get("company_id")

    page = request.GET.get('page')
    logger.debug(page)

    if not page:
        page = "1"
        logger.debug("oh we set it")

    if term:
        photos = Photo.objects.filter(tag__name__contains=term).distinct()
    else:
        photos = Photo.objects.all().order_by("?")

    if company_id:
        photos = photos.filter(company=company_id)

    for photo in photos:
        try:
            photo.thumbnail = get_thumbnailer(photo.image)['medium']
        except:
            photo.thumbnail = None

    paginator = Paginator(photos, 12)

    try:
        results = paginator.page(page)
        next = int(page) + 1;
        logger.debug("INTEGER:: NEXT = " + next.__str__())
    except PageNotAnInteger:
        results = paginator.page(1)
        next = 2;
        logger.debug("NOT AN INTEGER: NEXT = " + next.__str__())
    except EmptyPage:
        results = None;
        next = None;
        logger.debug("EMPTY: NEXT = " + next.__str__())

    serializer = PhotoSerializer(results, many=True)

    data = {
        'next_page': next,
        'results': serializer.data
    }
    return HttpResponse(json.dumps(data), content_type="application/json")

@ensure_csrf_cookie
def add(request, company_id):
    if request.method != 'POST':
        return HttpResponseBadRequest("Only accepts posts.")
    form = CompanyImagesForm(request.POST, request.FILES)
    if form.is_valid():
        photo = form.save(commit=False)
        photo.company = Company.objects.get(pk=company_id)
        photo.save()
        return HttpResponse("Success")
    else:
        raise HttpResponseBadRequest(form.errors)


def delete(request, photo_id):
    photo = Photo.objects.get(pk=photo_id)
    photo.delete()
    return HttpResponse("Success")