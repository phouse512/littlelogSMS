"""
    Basic message processor class
"""

import logging
logger = logging.getLogger(__name__)

from django.core.mail import send_mail
from smtplib import SMTPException

from response import TextResponse
from sms.models import LittleLogAlias
from sms.models import LittleLogHistory

FROM_EMAIL = 'phouse512@gmail.com'
SUBJECT = 'AUTO_LLSMS'


class MessageProcessor:

    def __init__(self, message):
        self.message = message
        self.response_handler = TextResponse()

    """
       process: publicly available class method that handles the message and returns
            a response object to be used
    """

    def handle(self):
        # handle empty cases
        message_info = self.message.split(" ", 1)

        # if asking for help and alias is not 'help'
        if message_info[0] == 'help' and len(message_info) < 2:
            return self.response_handler.help()

        # if empty message or improper format beyond this point
        if len(message_info) < 2:
            return self.response_handler.improper_format()

        given_alias = message_info[0]
        given_log = message_info[1]

        alias = LittleLogAlias.objects.filter(alias=given_alias)
        if not alias:
            return self.response_handler.alias_not_found()

        given_alias = alias[0]

        new_log = LittleLogHistory(
            alias_id=given_alias.id,
            log_text=given_log
        ).save()

        recipient_list = [given_alias.email_secret]

        try:
            send_mail(SUBJECT, given_log, FROM_EMAIL, recipient_list)
            return self.response_handler.success()
        except SMTPException:
            logger.error("Email failed to send")
            return self.response_handler.error()


#

