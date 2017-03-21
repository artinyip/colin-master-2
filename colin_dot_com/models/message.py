from django.db import models
from colin_dot_com.models.colin_user import ColinUser
from django.contrib.auth.models import User
from enum import Enum


class MessageParticipant(Enum):
    sender = 1
    recipient = 2


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="Sender")
    recipient = models.ForeignKey(User, related_name="Recipient")
    subject = models.CharField(max_length=1000, default="", blank=True)
    body = models.TextField(default="")
    date_sent = models.DateTimeField(auto_now_add=True)
    date_read = models.DateTimeField(blank=True, null=True)
    read = models.BooleanField(default=False)
    in_reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    thread_id = models.CharField(blank=True, null=True, max_length=1000)
    email_notification_sent = models.BooleanField(default=False)

    def __str__(self):
        if self.subject:
            return "%s [%s]" % (self.subject, self.id)
        else:
            return "No subject"

    def __get_name(self, participant):
        if participant == MessageParticipant.sender:
            user = self.sender
        else:
            user = self.recipient
        try:
            return user.company.name
        except AttributeError:
            name = user.first_name + ' ' + user.last_name
            return name if (name != ' ') else user.email

    def get_sender_name(self):
        return self.__get_name(MessageParticipant.sender)

    def get_recipient_name(self):
        return self.__get_name(MessageParticipant.recipient)

    def set_friend(self, user):
        self.friend = self.sender if self.recipient == user else self.recipient

    def get_friend_name(self):
        try:
            return self.friend.company.name
        except AttributeError:
            name = self.friend.first_name + ' ' + self.friend.last_name
            return name if (name != ' ') else self.friend.email
        except:
            return ''

    def get_avatar(self):
        try:
            return self.friend.company.get_avatar()
        except AttributeError:
            pass
        try:
            return self.friend.designer.get_avatar()
        except AttributeError:
            pass
        return None



class MessageAttachment(models.Model):
    file = models.FileField(blank=True, null=True)
    message = models.ForeignKey(Message, null=True, related_name="attachments")

    def __str__(self):
        return self.file.name

    def is_image(self):
        name = self.file.name
        if name.endswith(".gif"):
            return True
        elif name.endswith(".png"):
            return True
        elif name.endswith(".jpg"):
            return True
        elif name.endswith(".jpeg"):
            return True
        else:
            return False