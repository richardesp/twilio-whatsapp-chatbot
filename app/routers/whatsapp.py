from fastapi import APIRouter, Request
from app.services.whatsapp_service import process_message
from app.utils.logger import create_logger

logger = create_logger(__name__)

router = APIRouter()

@router.post("/whatsapp")
async def whatsapp_webhook(request: Request):
    incoming_msg = await request.form()
    
    logger.info(f'Incoming message received: {incoming_msg}')
    
    process_message(incoming_msg['From'], incoming_msg['Body'])
    return {"message": "Response sent successfully"}
