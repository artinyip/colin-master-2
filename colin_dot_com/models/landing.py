from django.db import models
from colin_dot_com.models.company import Company

class LandingImage(models.Model):
    image = models.ImageField()
    company = models.ForeignKey(Company, null=True, blank=True, related_name="company")
    caption = models.CharField(max_length=300)

    def __str__(self):
        return "%s [%s] (%s)" % (self.image, self.id, self.caption)