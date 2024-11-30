import json

from twilio.rest import Client

from app.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_TEMPLATE_CONTENT_SID
from app.utils.logger import create_logger
from app.schemas.phone_number import PhoneNumber


client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
logger = create_logger(__name__)

def send_list_picker(from_number: PhoneNumber, to_number: PhoneNumber):
    try:
        content_sid = TWILIO_TEMPLATE_CONTENT_SID
        
        content_variables = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e'
        }

        message = client.messages.create(
            to=to_number,
            from_=from_number,
            content_sid=content_sid,
            content_variables=json.dumps(content_variables)
        )

        logger.info(f"List picker sent correctly! SID: {message.sid}")
    except Exception as e:
        logger.error(f"Error trying to send the list picker (check twilio CLI): {e}")

def process_message(from_number: PhoneNumber, body: str, to_number: PhoneNumber) -> None:
    body = body.strip().lower()
    logger.info(f'Body retrieved: {body}')
    
    if "hola" in body or "buenas" in body:
        logger.info(f"Mensaje reconocido como saludo. Enviando list picker.")
        send_list_picker(from_number=to_number, to_number=from_number)  # Enviar el mensaje interactivo con el list picker
    else:
        # Mensaje genérico si no se reconoce el saludo
        response_message = "Lo siento, no entendí tu mensaje. Puedes decir 'Hola' para ver nuestros servicios."
        try:
            message = client.messages.create(
                from_=to_number,
                body=response_message,
                to=from_number
            )
            logger.info(f'Response message generated: {message.body}')
        except Exception as e:
            logger.error(f"Error al enviar el mensaje: {e}")
