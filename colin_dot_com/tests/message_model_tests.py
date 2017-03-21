from django.test import TestCase
from colin_dot_com.models.message import Message
from colin_dot_com.tests import test_tools


class MessageModelTests(TestCase):
    def test_get_friend(self):
        company1 = test_tools.add_company()
        company2 = test_tools.add_company()

        user1 = company1.user
        user2 = company2.user

        message = Message(
            sender=user1,
            recipient=user2,
            subject="Mary had a little lamb",
            body="Whose fleece was white as snow bitches"
        )

        message.set_friend(user2)
        self.assertEqual(user1, message.friend)
        message.set_friend(user1)
        self.assertEqual(user2, message.friend)