from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.schemas.newsletter import SubscribeRequest, SubscriberOut, BroadcastRequest
from app.services import newsletter_service
from app.routers.admin_auth import require_admin

router = APIRouter(prefix="/api/newsletter", tags=["newsletter"])


@router.post("/subscribe", response_model=SubscriberOut, status_code=201)
async def subscribe(body: SubscribeRequest, db: Session = Depends(get_db)):
    return await newsletter_service.subscribe(db, body.email)


@router.get("/", response_model=list[SubscriberOut])
def list_subscribers(_: dict = Depends(require_admin), db: Session = Depends(get_db)):
    return newsletter_service.list_subscribers(db)


@router.delete("/{subscriber_id}")
def remove_subscriber(subscriber_id: int, _: dict = Depends(require_admin), db: Session = Depends(get_db)):
    newsletter_service.remove_subscriber(db, subscriber_id)
    return {"message": "Removed"}


@router.post("/broadcast")
async def broadcast(body: BroadcastRequest, _: dict = Depends(require_admin), db: Session = Depends(get_db)):
    return await newsletter_service.broadcast(db, body.subject, body.content)
