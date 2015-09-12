"""
    Basic message response class to handle communicating with users
"""
import logging
logger = logging.getLogger(__name__)

from twilio.twiml import Response

# DEFAULT MESSAGES
DEFAULT_ERROR_MESSAGE = "Sorry, your log failed to send. Tweet @PhilipHouse2 so he fixes it!"
DEFAULT_SUCCESS_MESSAGE = "Your log was stored successfully!"


class TextResponse:

    """
        TextResponse is initialized with a string of the user's phone #
    """
    def __init__(self, recipient):
        self.recipient = recipient


    def handle_error(self, error=None):
        if not error:
            error = DEFAULT_ERROR_MESSAGE

        response = Response()
        response.message(error)
        logger.info(response)

        return response

    def handle_success(self, message=None):
        if not message:
            message = DEFAULT_SUCCESS_MESSAGE

        response = Response()
        response.message(message)
        logger.info(response)

        return response

