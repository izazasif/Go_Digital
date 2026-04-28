from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from app.models.appointment import ServiceType, AppointmentStatus


class AppointmentCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    service_type: ServiceType
    preferred_date: str
    preferred_time: str
    message: Optional[str] = None


class AppointmentOut(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    service_type: ServiceType
    preferred_date: str
    preferred_time: str
    message: Optional[str]
    status: AppointmentStatus
    admin_reply: Optional[str]
    created_at: datetime

    model_config = {"from_attributes": True}


class AppointmentUpdate(BaseModel):
    status: AppointmentStatus
    admin_reply: Optional[str] = None
    send_email: bool = True


class AdminUserOut(BaseModel):
    id: int
    email: str
    full_name: str
    is_verified: bool
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}
