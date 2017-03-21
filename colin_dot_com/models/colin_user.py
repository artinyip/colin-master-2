from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.staticfiles.templatetags.staticfiles import static
import abc


class ColinUser(models.Model):
    __metaclass__ = abc.ABCMeta

    user = models.OneToOneField(User, on_delete=models.CASCADE, null="True")
    send_email_notification = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @abc.abstractmethod
    def get_avatar(self):
        return

    @abc.abstractmethod
    def get_link(self):
        return


def get_colin_user(user):
    try:
        colin_user = user.company
    except ObjectDoesNotExist:
        colin_user = None

    if colin_user is None:
        try:
            colin_user = user.designer
        except ObjectDoesNotExist:
            pass

    if colin_user is None:
        colin_user = user

    return colin_user
