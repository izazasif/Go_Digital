from fastapi import APIRouter, Depends, Query, HTTPException, Header
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse, UserOut
from app.services import auth_service
from app.core.security import decode_token
from app.models.user import User

router = APIRouter(prefix="/api/auth", tags=["auth"])


def require_user(authorization: str = Header(...), db: Session = Depends(get_db)) -> User:
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")
    payload = decode_token(authorization.split(" ")[1])
    if not payload or payload.get("role") == "admin":
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.id == int(payload["sub"])).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user


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


@router.get("/me", response_model=UserOut)
def me(current_user: User = Depends(require_user)):
    return current_user
