import json
from django import forms
from colin_dot_com.models.message import Message, MessageAttachment
from parsley.decorators import parsleyfy


@parsleyfy
class MessageForm(forms.ModelForm):
    attachmentIds = forms.CharField(required=False)

    class Meta:
        model = Message
        fields = [
            'recipient',
            'subject',
            'body',
        ]


@parsleyfy
class MessageAttachmentForm(forms.ModelForm):
    class Meta:
        model = MessageAttachment
        fields = ['file']