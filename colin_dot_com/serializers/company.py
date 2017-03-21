from colin_dot_com.models.company import Photo, Company
from rest_framework import serializers

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'date_added',
            'blurb',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'zip',
            'country',
            'logo',
            'default_image',
            'user',
            'material_focus',
            'instagram'
        )


class PhotoSerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=True)
    thumbnail = serializers.ImageField()

    class Meta:
        model = Photo
        fields = ('id', 'date_added', 'thumbnail', 'image', 'caption', 'tag', 'company')

        # name = models.CharField(max_length=200)
        # date_added = models.DateTimeField("date_added", auto_now_add=True)
        # blurb = models.TextField(max_length=350, default="")
        # address_line_1 = models.CharField(max_length=1000, default="", blank=True)
        # address_line_2 = models.CharField(max_length=1000, default="", blank=True)
        # city = models.CharField(max_length=1000, default="")
        # state = models.CharField(max_length=2, default="")
        # zip = models.CharField(max_length=5, default="", blank="True")
        # country = CountryField(default="US")
        # logo = models.ImageField(null=True, blank=True)
        # default_image = models.CharField(blank=True, max_length=1000)
        # user = models.OneToOneField(User, on_delete=models.CASCADE, null="True")
        # material_focus = models.CharField("Material Focus", max_length=3, choices=MATERIAL_FOCUSES, default="N/A")
        # instagram = models.CharField("Instagram Handle", max_length=250, default="", blank=True)