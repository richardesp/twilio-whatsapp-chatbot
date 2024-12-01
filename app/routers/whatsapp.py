import json
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from typing import Callable
from app.schemas.whatsapp_message import WhatsAppMessage
from app.utils.logger import create_logger

logger = create_logger(__name__)
router = APIRouter()


def get_message_processor() -> Callable:
    """
    Provides the message processing function.
    
    Returns:
        Callable: The message processing function.
    """
    from app.services.whatsapp_service import process_message
    return process_message


@router.post(
    "/whatsapp",
    tags=["Webhooks"],
    summary="Process incoming WhatsApp messages",
    description=(
        "Handles webhook events sent by WhatsApp and processes messages based "
        "on the incoming data."
    ),
    response_description="A success message indicating the response was sent.",
    responses={
        200: {
            "description": "Message processed successfully.",
            "content": {"application/json": {"example": {"message": "Response sent successfully"}}},
        },
        500: {"description": "Server error during processing."},
    },
)
async def whatsapp_webhook(
    request: Request,
    message: WhatsAppMessage = Depends(WhatsAppMessage.as_form),
    process_message: Callable = Depends(get_message_processor),
):
    """
    Handles incoming WhatsApp webhook messages.

    This endpoint processes WhatsApp messages received via webhook. It validates
    the message payload, logs relevant details, and calls the processing service.

    Args:
        request (Request): The HTTP request object, used for logging metadata like headers.
        message (WhatsAppMessage): The validated WhatsApp message payload.
        process_message (Callable): The message processing service dependency.

    Returns:
        dict: A success message indicating the message was processed.
    
    Raises:
        HTTPException: If an error occurs during message processing.
        
    Author:
        Ricardo Espantaleón Pérez (@richardesp)
    """
    try:
        # Log the incoming message with structured logging
        logger.info(
            json.dumps({
                "event": "incoming_whatsapp_message",
                "from": message.From,
                "to": message.To,
                "body": message.Body,
                "message_sid": message.MessageSid,
                "request_id": request.headers.get("X-Request-ID", "unknown"),
            })
        )

        # Process the message using the injected function
        process_message(
            from_number=message.From,
            body=message.Body,
            to_number=message.To
        )

    except Exception as e:
        # Handle any exceptions during processing
        logger.error(f"Error processing message: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to process message.",
        )

    # Return a success response
    return {"message": "Response sent successfully"}
