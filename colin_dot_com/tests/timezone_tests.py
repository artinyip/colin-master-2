from django.test.testcases import TestCase
from colin_dot_com.tests import test_tools
from django.utils import timezone
from colin_dot_com.models.message import Message

class TimezoneTests(TestCase):


    def test_current_timezone(self):
        company1 = test_tools.add_company()
        company2 = test_tools.add_company()

        msg = Message(
            sender=company1.user,
            recipient=company2.user,
            subject="Zoot suit riot",
            body="Throw back a bottle of beer"
        )

        msg.save()

        now = timezone.now()

        self.assertTrue(now.hour == msg.date_sent.hour)