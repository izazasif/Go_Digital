from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.newsletter import NewsletterSubscriber
from app.core import email as mail


async def subscribe(db: Session, subscriber_email: str) -> NewsletterSubscriber:
    existing = db.query(NewsletterSubscriber).filter(NewsletterSubscriber.email == subscriber_email).first()
    if existing:
        if existing.is_active:
            raise HTTPException(status_code=400, detail="Already subscribed")
        existing.is_active = True
        db.commit()
        db.refresh(existing)
        await mail.send_newsletter_welcome(subscriber_email)
        return existing

    subscriber = NewsletterSubscriber(email=subscriber_email)
    db.add(subscriber)
    db.commit()
    db.refresh(subscriber)
    await mail.send_newsletter_welcome(subscriber_email)
    return subscriber


def list_subscribers(db: Session) -> list:
    return db.query(NewsletterSubscriber).order_by(NewsletterSubscriber.subscribed_at.desc()).all()


def remove_subscriber(db: Session, subscriber_id: int):
    sub = db.query(NewsletterSubscriber).filter(NewsletterSubscriber.id == subscriber_id).first()
    if not sub:
        raise HTTPException(status_code=404, detail="Subscriber not found")
    db.delete(sub)
    db.commit()


async def broadcast(db: Session, subject: str, content: str):
    active = db.query(NewsletterSubscriber).filter(NewsletterSubscriber.is_active == True).all()
    if not active:
        raise HTTPException(status_code=400, detail="No active subscribers")
    recipients = [s.email for s in active]
    await mail.send_newsletter_broadcast(recipients, subject, content)
    return {"sent_to": len(recipients)}
