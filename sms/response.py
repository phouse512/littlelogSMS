"""
    Basic message response class to handle communicating with users
"""

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

        return str(Response().message(error))

    def handle_success(self, message=None):
        if not message:
            message = DEFAULT_SUCCESS_MESSAGE

        return str(Response().message(message))

