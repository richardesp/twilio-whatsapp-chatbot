import re

from pydantic import BaseModel, ValidationError, field_validator

class PhoneNumber(BaseModel):
    phone: str

    @field_validator('phone')
    def validate_phone(cls, v):
        # Regular expression pattern for validating the phone number
        pattern = r'^whatsapp:\+\d{10,15}$'
        
        # Check if the phone number matches the pattern
        if not re.match(pattern, v):
            raise ValidationError('Must be a valid WhatsApp phone number in the format "whatsapp:+12345678912"')
        return v