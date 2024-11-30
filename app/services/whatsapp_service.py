from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER, TWILIO_TEMPLATE_CONTENT_SID
from utils.logger import get_logger
import json

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
logger = get_logger(__name__)

def send_list_picker(to_number):
    try:
        content_sid = TWILIO_TEMPLATE_CONTENT_SID
        
        content_variables = {
            '1': '',
            '2': '',
            '3': '',
            '4': '',
            '5': ''
        }

        message = client.messages.create(
            to=to_number,
            from_=TWILIO_WHATSAPP_NUMBER,
            content_sid=content_sid,
            content_variables=json.dumps(content_variables)
        )

        logger.info(f"List picker enviado con SID: {message.sid}")
    except Exception as e:
        logger.error(f"Error al enviar list picker: {e}")

def process_message(from_number, body) -> None:
    body = body.strip().lower()
    logger.info(f'Body retrieved: {body}')
    
    if "hola" in body or "buenas" in body:
        logger.info(f"Mensaje reconocido como saludo. Enviando list picker.")
        send_list_picker(from_number)  # Enviar el mensaje interactivo con el list picker
    else:
        # Mensaje genérico si no se reconoce el saludo
        response_message = "Lo siento, no entendí tu mensaje. Puedes decir 'Hola' para ver nuestros servicios."
        try:
            message = client.messages.create(
                from_=TWILIO_WHATSAPP_NUMBER,
                body=response_message,
                to=from_number
            )
            logger.info(f'Response message generated: {message.body}')
        except Exception as e:
            logger.error(f"Error al enviar el mensaje: {e}")
