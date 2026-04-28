from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.appointment import Appointment, AppointmentStatus
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate
from app.core import email as mail
from app.core.config import settings

SERVICE_LABELS = {
    "cloud-infra": "Cloud Infrastructure",
    "cloud-security": "Cloud Security",
    "cybersecurity": "Cybersecurity",
    "ai": "AI Solutions",
    "ai-security": "AI Security",
}


async def create_appointment(db: Session, data: AppointmentCreate) -> Appointment:
    appt = Appointment(**data.model_dump())
    db.add(appt)
    db.commit()
    db.refresh(appt)

    service_label = SERVICE_LABELS.get(data.service_type.value, data.service_type.value)
    await mail.send_appointment_confirmation(data.email, data.name, service_label, data.preferred_date, data.preferred_time)
    await mail.send_appointment_admin_notification(settings.ADMIN_EMAIL, {
        "Name": data.name,
        "Email": data.email,
        "Phone": data.phone,
        "Service": service_label,
        "Date": data.preferred_date,
        "Time": data.preferred_time,
        "Message": data.message or "—",
    })
    return appt


def list_appointments(db: Session, status: str = None) -> list:
    q = db.query(Appointment)
    if status:
        q = q.filter(Appointment.status == status)
    return q.order_by(Appointment.created_at.desc()).all()


async def update_appointment(db: Session, appt_id: int, data: AppointmentUpdate) -> Appointment:
    appt = db.query(Appointment).filter(Appointment.id == appt_id).first()
    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")
    appt.status = data.status
    if data.admin_reply:
        appt.admin_reply = data.admin_reply
    db.commit()
    db.refresh(appt)

    if data.send_email and data.admin_reply:
        await mail.send_appointment_reply(appt.email, appt.name, data.status.value, data.admin_reply)
    return appt
