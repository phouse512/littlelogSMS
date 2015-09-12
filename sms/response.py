"""
    Basic message response class to handle communicating with users
"""

from twilio.rest import TwilioRestClient

from littlelogsms.secrets import twilio_credentials

# DEFAULT MESSAGES
DEFAULT_ERROR_MESSAGE = "Sorry, your log failed to send. Tweet @PhilipHouse2 so he fixes it!"
DEFAULT_SUCCESS_MESSAGE = "Your log was stored successfully!"


class TextResponse:

    """
        TextResponse is initialized with a string of the user's phone #
    """
    def __init__(self, recipient):
        self.client = TwilioRestClient(twilio_credentials['ACCOUNT_SID'], twilio_credentials['AUTH_TOKEN'])
        self.recipient = recipient


    def handle_error(self, error=None):
        if not error:
            error = DEFAULT_ERROR_MESSAGE

        self.client.messages.create(
            to=self.recipient,
            from_="LittleLogSMS",
            body=error
        )

    def handle_success(self, message=None):
        if not message:
            message = DEFAULT_SUCCESS_MESSAGE

        self.client.messages.create(
            to=self.recipient,
            from_="LittleLogSMS",
            body=message
        )


