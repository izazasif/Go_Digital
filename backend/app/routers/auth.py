from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse, UserOut
from app.services import auth_service

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=UserOut, status_code=201)
async def register(body: RegisterRequest, db: Session = Depends(get_db)):
    user = await auth_service.register_user(db, body.full_name, body.email, body.password)
    return user


@router.get("/verify-email")
def verify_email(token: str = Query(...), db: Session = Depends(get_db)):
    auth_service.verify_email_token(db, token)
    return {"message": "Email verified successfully. You can now log in."}


@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest, db: Session = Depends(get_db)):
    return auth_service.login_user(db, body.email, body.password)
