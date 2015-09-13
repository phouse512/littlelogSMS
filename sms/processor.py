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
FEEDBACK_SUBJECT = 'LSMS Feedback <3'
ADMIN_EMAIL = ['philiphouse2015@u.northwestern.edu']


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
        message_info[0] = message_info[0].lower()

        # if asking for help and alias is not 'helpme'
        if message_info[0] == 'helpme' and len(message_info) < 2:
            return self.response_handler.help()

        # if empty message or improper format beyond this point
        if len(message_info) < 2:
            return self.response_handler.improper_format()

        given_alias = message_info[0]
        given_log = message_info[1]

        # handle gaining feedback
        if given_alias == 'feedback':
            return self._send_feedback(given_log)

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
            logger.info("Log stored successfully: %s" % given_log)
            return self.response_handler.success()
        except SMTPException:
            logger.error("Email failed to send")
            return self.response_handler.error()


    """
        Private method to send a feedback email
    """
    def _send_feedback(self, message):
        try:
            send_mail(FEEDBACK_SUBJECT, message, FROM_EMAIL, ADMIN_EMAIL)
            return self.response_handler.feedback_success()
        except SMTPException:
            logger.error("Feedback email failed to send")
            return self.response_handler.error()


