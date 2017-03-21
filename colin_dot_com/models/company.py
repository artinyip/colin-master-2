from django.db import models
from django_countries.fields import CountryField
from colin_dot_com.models.colin_user import ColinUser
from colin_dot_com.models.materials import Materials
from easy_thumbnails.fields import ThumbnailerImageField

class Company(ColinUser):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField("date_added", auto_now_add=True)
    blurb = models.TextField(max_length=450, default="")
    address_line_1 = models.CharField(max_length=1000, default="", blank=True)
    address_line_2 = models.CharField(max_length=1000, default="", blank=True)
    city = models.CharField(max_length=1000, default="")
    state = models.CharField(max_length=2, default="")
    zip = models.CharField(max_length=5, default="", blank="True")
    country = CountryField(default="US")
    logo = models.ImageField(null=True, blank=True)
    default_image = models.CharField(blank=True, max_length=1000)
    material_focus = models.CharField("Material Focus", max_length=3, choices=Materials.OPTIONS, default="N/A")
    instagram = models.CharField("Instagram Handle", max_length=250, default="", blank=True)

    def __str__(self):
        return "%s [%s] (%s)" % (self.name, self.id, self.user)

    def get_avatar(self):
        if self.default_image:
            return self.photo_set.get(pk=self.default_image).image
        elif self.photo_set.count() > 0:
            return self.photo_set.first().image
        else:
            return None

    def get_link(self):
        return "/companies/%s" % self.id


class PhotoTag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Photo(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    image = ThumbnailerImageField(null=False)
    caption = models.CharField(max_length=250, null=True, blank=True)
    tag = models.ManyToManyField(PhotoTag, blank=True)
    company = models.ForeignKey(Company, null=True)

    def __str__(self):
        return self.image.name