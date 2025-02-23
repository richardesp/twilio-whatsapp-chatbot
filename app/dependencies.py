from twilio.rest import Client as TwilioClient
import redis
from redis import Redis as RedisClient
from openai import OpenAI as OpenAIClient
import openai

from app.config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    REDIS_HOSTNAME,
    REDIS_PORT,
    OPENAI_APIKEY,
)


def get_twilio_client() -> TwilioClient:
    """
    Dependency to provide a Twilio client instance.

    Returns:
        TwilioClient: A Twilio client configured with the application's credentials.
    """
    return TwilioClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def get_redis_client() -> RedisClient:
    """
    Dependency to provide a redis client instance.

    Return:
        RedisClient: A redis client configured with the application's host params.
    """
    return redis.StrictRedis(
        host=REDIS_HOSTNAME,  # Nombre del servicio definido en docker-compose.yml
        port=REDIS_PORT,
        decode_responses=True,
    )


def get_openai_client() -> OpenAIClient:
    """
    Dependency to provide an openai client instance.

    Return:
        OpenAIClient: An openai client configured with the application's credential.
    """
    return openai.OpenAI(api_key=OPENAI_APIKEY)
