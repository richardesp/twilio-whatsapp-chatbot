from typing import Optional

from fastapi import Form
from pydantic import BaseModel, Field


class WhatsAppMessage(BaseModel):
    SmsMessageSid: str = Field(
        default=..., description="Unique identifier for the SMS message."
    )
    NumMedia: int = Field(default=..., description="Number of media attachments.")
    ProfileName: Optional[str] = Field(None, description="Profile name of the sender.")
    MessageType: str = Field(
        default=..., description="Type of the message (e.g., text)."
    )
    SmsSid: str = Field(default=..., description="Unique identifier for the SMS.")
    WaId: str = Field(default=..., description="WhatsApp ID of the sender.")
    SmsStatus: str = Field(
        default=..., description="Status of the SMS (e.g., received)."
    )
    Body: str = Field(default=..., description="Body of the message.")
    To: str = Field(
        default=..., description="Recipient's phone number in WhatsApp format."
    )
    NumSegments: int = Field(default=..., description="Number of segments in the SMS.")
    ReferralNumMedia: int = Field(
        default=..., description="Number of referral media attachments."
    )
    MessageSid: str = Field(
        default=..., description="Unique identifier for the message."
    )
    AccountSid: str = Field(
        default=..., description="Account SID associated with the message."
    )
    From: str = Field(
        default=..., description="Sender's phone number in WhatsApp format."
    )
    ApiVersion: str = Field(
        default=..., description="API version used to send the message."
    )

    @classmethod
    def as_form(
        cls,
        SmsMessageSid: str = Form(...),
        NumMedia: int = Form(...),
        ProfileName: Optional[str] = Form(None),
        MessageType: str = Form(...),
        SmsSid: str = Form(...),
        WaId: str = Form(...),
        SmsStatus: str = Form(...),
        Body: str = Form(...),
        To: str = Form(...),
        NumSegments: int = Form(...),
        ReferralNumMedia: int = Form(...),
        MessageSid: str = Form(...),
        AccountSid: str = Form(...),
        From: str = Form(...),
        ApiVersion: str = Form(...),
    ):
        """
        A helper method to parse form-encoded data into the model.
        """
        return cls(
            SmsMessageSid=SmsMessageSid,
            NumMedia=NumMedia,
            ProfileName=ProfileName,
            MessageType=MessageType,
            SmsSid=SmsSid,
            WaId=WaId,
            SmsStatus=SmsStatus,
            Body=Body,
            To=To,
            NumSegments=NumSegments,
            ReferralNumMedia=ReferralNumMedia,
            MessageSid=MessageSid,
            AccountSid=AccountSid,
            From=From,
            ApiVersion=ApiVersion,
        )
