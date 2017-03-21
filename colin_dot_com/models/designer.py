from colin_dot_com.models.colin_user import ColinUser
from colin_dot_com.models.materials import Materials
from easy_thumbnails.fields import ThumbnailerImageField
from django.db import models
from multiselectfield import MultiSelectField


class Designer(ColinUser):
    avatar = ThumbnailerImageField(null=True)
    blurb = models.TextField(default="", max_length=500)
    interest = MultiSelectField("Material Focus", choices=Materials.OPTIONS, default="N/A")
    position = models.TextField(default="", max_length=100)
    firm = models.TextField(default="", max_length=200)
    city = models.CharField(max_length=1000, default="")
    state = models.CharField(max_length=2, default="")

    def get_avatar(self):
        return self.avatar

    def get_link(self):
        return "/designers/%s" % self.id

    def __str__(self):
        return self.user.username if self.user else "Unknown"

