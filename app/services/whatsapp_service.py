from twilio.rest import Client
import os
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER
from utils.logger import get_logger

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

logger = get_logger(__name__)

def process_message(from_number, body):
    body = body.strip().lower()
    
    logger.info(f'Body retrieved: {body}')
    
    if "hola" in body or "buenas" in body:
        response_message = "Buenas, muchas gracias por contactarnos. A continuación te listamos la lista de productos disponibles."
    else:
        response_message = "Lo siento, no entendí tu mensaje. Puedes decir 'Hola' para ver nuestros servicios."

    send_message(TWILIO_WHATSAPP_NUMBER, response_message, from_number)
    return response_message

def send_message(from_, body, to):
    client.messages.create(from_=from_, body=body, to=to)
