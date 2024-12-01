from twilio.rest import Client
from app.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN


def get_twilio_client() -> Client:
    """
    Dependency to provide a Twilio client instance.

    Returns:
        Client: A Twilio client configured with the application's credentials.
    """
    return Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
