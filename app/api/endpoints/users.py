from fastapi import APIRouter
from typing import List
from app.models.notification import NotificationDb

router = APIRouter()

# todo integrate db
notifications_store = {}


@router.get("/{user_id}/notifications", response_model=List[NotificationDb])
def get_user_notifications(user_id: int):
    return notifications_store.get(user_id, [])
