import json

from twilio.rest import Client
from twilio.rest import Client as TwilioClient

from app.config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_TEMPLATE_CONTENT_SID
from app.utils.logger import create_logger
from app.schemas.phone_number import PhoneNumber
from app.templates.whatsapp_templates import GREETINGS, DEFAULT_RESPONSE, LIST_PICKER_CONTENT_VARIABLES

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
logger = create_logger(__name__)

def send_list_picker(from_number: PhoneNumber, to_number: PhoneNumber):
    try:
        content_sid = TWILIO_TEMPLATE_CONTENT_SID
        
        # Se utilizan las variables externas para el contenido
        content_variables = LIST_PICKER_CONTENT_VARIABLES

        message = client.messages.create(
            to=to_number,
            from_=from_number,
            content_sid=content_sid,
            content_variables=json.dumps(content_variables)
        )

        logger.info(f"List picker sent correctly! SID: {message.sid}")
    except Exception as e:
        logger.error(f"Error trying to send the list picker (check twilio CLI): {e}")


def process_message(twilio_client: TwilioClient, from_number: PhoneNumber, body: str, to_number: PhoneNumber) -> None:
    body = body.strip().lower()
    logger.info(f'Body retrieved: {body}')
    
    # Se verifica si alguno de los saludos de la plantilla se encuentra en el mensaje recibido
    if any(greeting in body for greeting in GREETINGS):
        logger.info("Mensaje reconocido como saludo. Enviando list picker.")
        send_list_picker(from_number=to_number, to_number=from_number)  # Enviar el mensaje interactivo con el list picker
    else:
        try:
            message = client.messages.create(
                from_=to_number,
                body=DEFAULT_RESPONSE,
                to=from_number
            )
            logger.info(f"Response message generated: {message.body}")
        except Exception as e:
            logger.error(f"Error al enviar el mensaje: {e}")