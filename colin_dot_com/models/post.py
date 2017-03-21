from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    body = models.TextField()
    featured_image = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)


class GalleryImage(models.Model):
    image = models.ImageField()
    caption = models.TextField(max_length=500)
    post = models.ForeignKey(Post, related_name="gallery")

