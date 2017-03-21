from django.contrib import admin
from colin_dot_com.models.designer import Designer
from colin_dot_com.models.landing import LandingImage
from colin_dot_com.models.message import Message, MessageAttachment
from colin_dot_com.models.post import Post, GalleryImage
from colin_dot_com.models.company import Company, Photo, PhotoTag


class CompanyAdmin(admin.ModelAdmin):
    pass


class PhotoTagAdmin(admin.ModelAdmin):
    pass


class PhotoAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


class MessageAttachmentAdmin(admin.ModelAdmin):
    pass


class DesignerAdmin(admin.ModelAdmin):
    pass


class LandingImageAdmin(admin.ModelAdmin):
    pass


class GalleryImageAdmin(admin.ModelAdmin):
    pass


class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(PhotoTag, PhotoTagAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(MessageAttachment, MessageAttachmentAdmin)
admin.site.register(Designer, DesignerAdmin)
admin.site.register(LandingImage, LandingImageAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Post, PostAdmin)