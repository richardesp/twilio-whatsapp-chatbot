from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.phone_number import PhoneNumber

class Service(BaseModel):
    service_name: str = Field(
        ..., max_length=24, description="Name of the service (maximum 24 characters).", example="Service 1"
    )
    service_id: str = Field(
        ..., max_length=200, description="Unique identifier for the service (maximum 200 characters).", example="service_1_unique_id"
    )
    service_description: str = Field(
        ..., max_length=72, description="Short description of the service (maximum 72 characters).", example="Brief description of service 1"
    )
    service_price: str = Field(
        ..., max_length=15, description="Price of the service (maximum 15 characters).", example="50€"
    )
    service_duration_minutes: int = Field(
        ..., ge=0, description="Duration of the service in minutes.", example=30
    )


class ServiceSelector(BaseModel):
    body: str = Field(
        ..., max_length=1600, description="Welcome message (maximum 1600 characters).",
        example="Welcome to Business Name. We are here to assist you with our services."
    )
    button_text: str = Field(
        ..., max_length=20, description="Button text to list services (maximum 20 characters).", example="List services"
    )
    services: list[Service] = Field(
        ..., description="List of services offered."
    )


class Business(BaseModel):
    business_id: str = Field(
        ..., max_length=200, description="Unique identifier for the business.", example="business_12345"
    )
    business_name: str = Field(
        ..., max_length=100, description="Name of the business.", example="Business Name"
    )
    business_type: str = Field(
        ..., max_length=50, description="Type of business.", example="Health and Beauty"
    )
    phone_number: PhoneNumber = Field(
        ..., description="Whatsapp phone number associated with the business (has to be unique).", example="whatsapp:+12345678912"
    )
    service_selector: ServiceSelector = Field(
        ..., description="Service selector for the business."
    )


