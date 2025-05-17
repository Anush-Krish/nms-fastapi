from http.client import HTTPException

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.core.kafka_producer import send_to_kafka

router = APIRouter()


class NotificationRequest(BaseModel):
    user_id: int
    type: str
    message: str
    email: EmailStr
    phone_number: str


@router.post("/")
async def send_notification(payload: NotificationRequest):
    try:
        send_to_kafka("notification", payload.model_dump())
        return
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
