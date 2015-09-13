"""
    Basic message self.response class to handle communicating with users
"""
import logging
logger = logging.getLogger(__name__)

from twilio.twiml import Response

# DEFAULT MESSAGES
DEFAULT_ERROR_MESSAGE = "Sorry, your log failed to send. Tweet @PhilipHouse2 so he fixes it!"
DEFAULT_SUCCESS_MESSAGE = "Your log was stored successfully!"
DEFAULT_HELP_MESSAGE = "Stuck? Enter your alias with a space before you type your log! Ex:" +  \
    "'phil #working on little logs'."
DEFAULT_NOT_FOUND_MESSAGE = "Your alias wasn't found. Go to the site and make sure you registered correctly?"
DEFAULT_IMPROPER_MESSAGE = "Sorry, your message wasn't properly formatted. Type 'helpme' for help"


class TextResponse:

    """
        Textself.Response is initialized with a string of the user's phone #
    """
    def __init__(self, locale=None):
        self.locale = locale
        self.response = Response()

    def error(self, error=None):
        if not error:
            error = DEFAULT_ERROR_MESSAGE

        self.response.message(error)
        logger.info(self.response)

        return self.response

    def success(self, message=None):
        if not message:
            message = DEFAULT_SUCCESS_MESSAGE

        self.response.message(message)
        logger.info(self.response)

        return self.response

    def help(self, message=None):
        if not message:
            message = DEFAULT_HELP_MESSAGE

        self.response.message(message)
        logger.info("Help message sent: %s" % message)
        return self.response

    def improper_format(self, message=None):
        if not message:
            message = DEFAULT_IMPROPER_MESSAGE

        self.response.message(message)
        logger.info("Improper format message sent: %s" % message)
        return self.response

    def alias_not_found(self, message=None):
        if not message:
            message = "NOT FOUND YO"

        self.response.message(message)
        logger.info("")
        return self.response