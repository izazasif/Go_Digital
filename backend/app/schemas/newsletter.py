from datetime import datetime
from pydantic import BaseModel, EmailStr


class SubscribeRequest(BaseModel):
    email: EmailStr


class SubscriberOut(BaseModel):
    id: int
    email: str
    subscribed_at: datetime
    is_active: bool

    model_config = {"from_attributes": True}


class BroadcastRequest(BaseModel):
    subject: str
    content: str
