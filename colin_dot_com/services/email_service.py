import logging

from colin_dot_com.models.message import Message
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from colin_dot_com.models.colin_user import get_colin_user
logger = logging.getLogger("colin")

def send_new_message_notification(message, user):

    logger.debug("eat shit")

    subject = "[colin] New message from: " + message.sender.username
    body = message.body

    html = render_to_string('colin_dot_com/email_service/new_message_notification.html', {
        'message': message
    })
    
    logger.debug("hey bitches")

    email = EmailMessage(
        subject=subject,
        body=html,
        from_email="notifications@hellocolin.com",
        to=[user.email]
    )
    email.content_subtype = "html"
    return email.send(fail_silently=False)


