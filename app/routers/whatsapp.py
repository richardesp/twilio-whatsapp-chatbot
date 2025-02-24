import json
from typing import Callable

from fastapi import APIRouter, Depends, HTTPException, status
from twilio.rest import Client as TwilioClient
from redis import Redis as RedisClient
from openai import OpenAI as OpenAIClient

from app.schemas.whatsapp_message import WhatsAppMessage
from app.utils.logger import create_logger
from app.dependencies import get_twilio_client, get_redis_client, get_openai_client

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
            "content": {
                "application/json": {
                    "example": {"message": "Response sent successfully"}
                }
            },
        },
        500: {"description": "Server error during processing."},
    },
)
async def whatsapp_webhook(
    message: WhatsAppMessage = Depends(WhatsAppMessage.as_form),
    process_message: Callable = Depends(get_message_processor),
    twilio_client: TwilioClient = Depends(get_twilio_client),
    redis_client: RedisClient = Depends(get_redis_client),
    openai_client: OpenAIClient = Depends(get_openai_client),
):
    """
    Handles incoming WhatsApp webhook messages.

    This endpoint processes WhatsApp messages received via webhook. It validates
    the message payload, logs relevant details, and calls the processing service.

    Args:
        request (Request): The HTTP request object, used for logging metadata like headers.
        message (WhatsAppMessage): The validated WhatsApp message payload.
        process_message (Callable): The message processing service dependency.
        twilio_client (TwilioClient): Twilio's client for processing all whatsapp messages.

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
            json.dumps(
                {
                    "event": "incoming_whatsapp_message",
                    "from": message.From,
                    "to": message.To,
                    "body": message.Body,
                    "message_sid": message.MessageSid,
                }
            )
        )

        # Process the message using the injected function
        process_message(
            twilio_client=twilio_client,
            redis_client=redis_client,
            openai_client=openai_client,
            from_number=message.From,
            body=message.Body,
            to_number=message.To,
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
