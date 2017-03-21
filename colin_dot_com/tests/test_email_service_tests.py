from django.test import TestCase
from django.contrib.auth.models import User
from colin_dot_com.models.message import Message
from colin_dot_com.services import email_service


class TestBasicEmail(TestCase):

    user = User()
    message = Message()

    def setUp(self):

        self.user = User.objects.create_user(
            username="johnlempka@gmail.com",
            email="johnlempka@gmail.com",
            first_name="John",
            last_name="Lempka",
            password="test.password"
        )

        self.message = Message.objects.create(
            sender=self.user,
            recipient=self.user,
            subject="Mary had a little lamb",
            body="Whose fleece was white as snow bitches"
        )

    def test_send_email(self):
        sent = email_service.send_new_message_notification(self.message, self.user)
        self.assertEqual(sent, 1)