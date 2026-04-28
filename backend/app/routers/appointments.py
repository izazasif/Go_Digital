from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.schemas.appointment import AppointmentCreate, AppointmentOut, AppointmentUpdate
from app.services import appointment_service
from app.routers.admin_auth import require_admin

router = APIRouter(prefix="/api/appointments", tags=["appointments"])


@router.post("/", response_model=AppointmentOut, status_code=201)
async def create_appointment(body: AppointmentCreate, db: Session = Depends(get_db)):
    return await appointment_service.create_appointment(db, body)


@router.get("/", response_model=list[AppointmentOut])
def list_appointments(
    status: Optional[str] = Query(None),
    _: dict = Depends(require_admin),
    db: Session = Depends(get_db),
):
    return appointment_service.list_appointments(db, status)


@router.patch("/{appt_id}", response_model=AppointmentOut)
async def update_appointment(
    appt_id: int,
    body: AppointmentUpdate,
    _: dict = Depends(require_admin),
    db: Session = Depends(get_db),
):
    return await appointment_service.update_appointment(db, appt_id, body)
