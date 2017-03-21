
from django import forms
from colin_dot_com.models.company import Company, Photo
from parsley.decorators import parsleyfy


@parsleyfy
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'blurb',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'zip',
            'country',
            'material_focus',
            'instagram'
        ]
        labels = {
            'name' : 'Company name',
            'blurb' : 'A quick blurb about your company (250 characters or less!)'
        }
        exclude = [
            'user',
        ]
        widgets = {
            'blurb': forms.Textarea(attrs={'rows':4 })
        }


@parsleyfy
class CompanyImagesForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'image'
        ]
        exclude = [
            'company'
        ]