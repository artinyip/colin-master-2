# custom_storages.py
from storages.backends.s3boto import S3BotoStorage
from django.conf import settings


class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION