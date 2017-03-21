from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from parsley.decorators import parsleyfy


@parsleyfy
class DesignerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]

    def __init__(self, *args, **kwargs):
        super(DesignerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
