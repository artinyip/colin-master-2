import json
from django.test.testcases import TestCase
from django.test import RequestFactory
from colin_dot_com.tests import test_tools
from colin_dot_com.models.message import Message
from colin_dot_com.views import message as message_views


class ConversationApiTests(TestCase):

    def test_get_conversations(self):
        company1 = test_tools.add_company()
        company2 = test_tools.add_company()
        company3 = test_tools.add_company()

        user1 = company1.user
        user2 = company2.user
        user3 = company3.user

        thread_id = 4

        message1 = Message(
            sender=user1,
            recipient=user2,
            subject="Mary had a little lamb",
            body="Whose fleece was white as snow bitches",
            thread_id=thread_id
        )
        message1.save()

        message2 = Message(
            sender=user2,
            recipient=user1,
            subject="The itsy bitsy spider",
            body="Went down the water spout",
            thread_id=thread_id
        )
        message2.save()

        message3 = Message(
            sender=user1,
            recipient=user2,
            subject="Jesus didn't make me",
            body="For a sunbeam",
            thread_id=thread_id
        )
        message3.save()

        message4 = Message(
            sender=user1,
            recipient=user3,
            subject="Please excuse",
            body="My dear Aunt Sally",
            thread_id=5
        )
        message4.save()

        request = RequestFactory()
        request.user = user1
        response = message_views.get_conversations(request)

        convo_json = response.content.decode(response.charset)

        convos = json.loads(convo_json)

        self.assertEqual(len(convos), 2)


