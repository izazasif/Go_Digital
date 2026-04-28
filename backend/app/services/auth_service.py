from datetime import datetime, timezone
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.models.user import User, AdminUser
from app.models.email_verification import EmailVerification
from app.core.security import hash_password, verify_password, generate_verification_token, create_access_token, create_refresh_token
from app.core.config import settings
from app.core import email as mail


async def register_user(db: Session, full_name: str, email: str, password: str) -> User:
    if db.query(User).filter(User.email == email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(email=email, full_name=full_name, hashed_password=hash_password(password))
    db.add(user)
    db.flush()

    token = generate_verification_token()
    verification = EmailVerification(user_id=user.id, token=token, expires_at=EmailVerification.make_expiry(settings.VERIFICATION_TOKEN_EXPIRE_HOURS))
    db.add(verification)
    db.commit()
    db.refresh(user)

    await mail.send_verification_email(email, full_name, token)
    return user


def verify_email_token(db: Session, token: str) -> User:
    record = db.query(EmailVerification).filter(EmailVerification.token == token, EmailVerification.used == False).first()
    if not record:
        raise HTTPException(status_code=400, detail="Invalid or expired verification token")
    if record.expires_at.replace(tzinfo=timezone.utc) < datetime.now(timezone.utc):
        raise HTTPException(status_code=400, detail="Verification token expired")
    record.used = True
    user = db.query(User).filter(User.id == record.user_id).first()
    user.is_verified = True
    db.commit()
    return user


def login_user(db: Session, email: str, password: str) -> dict:
    user = db.query(User).filter(User.email == email, User.is_active == True).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not user.is_verified:
        raise HTTPException(status_code=403, detail="Please verify your email before logging in")
    return {
        "access_token": create_access_token(str(user.id)),
        "refresh_token": create_refresh_token(str(user.id)),
        "token_type": "bearer",
    }


def login_admin(db: Session, email: str, password: str) -> dict:
    admin = db.query(AdminUser).filter(AdminUser.email == email).first()
    if not admin or not verify_password(password, admin.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid admin credentials")
    return {
        "access_token": create_access_token(str(admin.id), extra={"role": "admin"}),
        "token_type": "bearer",
    }
