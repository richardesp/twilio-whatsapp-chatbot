from fastapi import APIRouter, Request
from services.whatsapp_service import process_message
from utils.logger import get_logger

logger = get_logger(__name__)

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    incoming_msg = await request.form()
    
    logger.info(f'Incoming message received: {incoming_msg}')
    
    response_message = process_message(incoming_msg['From'], incoming_msg['Body'])
    return {"message": "Response sent successfully"}
