from pydantic import BaseModel

class NotificationDb(BaseModel):
    type: str
    msg: str