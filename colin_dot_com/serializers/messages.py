from colin_dot_com.models.message import Message, MessageAttachment
from colin_dot_com.models.company import Photo
from rest_framework import serializers


class ConversationSerializer(serializers.ModelSerializer):
    friend_name = serializers.CharField(max_length=255)
    friend_id = serializers.CharField(max_length=255)
    date_sent = serializers.DateTimeField(format="%c")
    count = serializers.IntegerField()
    avatar = serializers.ImageField(allow_empty_file=True)

    class Meta:
        model = Message
        fields = ['friend_name', 'avatar', 'friend_id', 'count', 'subject', 'body', 'date_sent', 'date_read', 'read', 'in_reply_to', 'thread_id']


class AttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MessageAttachment
        fields = ['file']


class ConversationMessageSerializer(serializers.ModelSerializer):
    date_sent = serializers.DateTimeField(format="%c")
    direction = serializers.CharField(max_length=255)
    sender_name = serializers.CharField(max_length=255)
    avatar = serializers.ImageField(allow_empty_file=True)
    link = serializers.CharField(max_length=3000)
    attachments = AttachmentSerializer(many=True)

    class Meta:
        model = Message
        fields = ['id', 'direction', 'attachments', 'avatar', 'link', 'sender_name', 'sender', 'subject', 'body', 'date_sent', 'date_read', 'read', 'in_reply_to', 'thread_id']
