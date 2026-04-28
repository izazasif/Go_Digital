from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.db.base import get_db
from app.schemas.auth import AdminLoginRequest, AdminTokenResponse, UserOut
from app.schemas.appointment import AdminUserOut
from app.services import auth_service
from app.core.security import decode_token
from app.models.user import User

router = APIRouter(prefix="/api/admin", tags=["admin"])
bearer = HTTPBearer()


def require_admin(creds: HTTPAuthorizationCredentials = Depends(bearer)):
    payload = decode_token(creds.credentials)
    if not payload or payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return payload


@router.post("/login", response_model=AdminTokenResponse)
def admin_login(body: AdminLoginRequest, db: Session = Depends(get_db)):
    return auth_service.login_admin(db, body.email, body.password)


@router.get("/users", response_model=list[AdminUserOut])
def list_users(_: dict = Depends(require_admin), db: Session = Depends(get_db)):
    return db.query(User).order_by(User.created_at.desc()).all()


@router.patch("/users/{user_id}")
def update_user(user_id: int, is_active: bool, _: dict = Depends(require_admin), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.is_active = is_active
    db.commit()
    return {"message": "Updated"}


@router.delete("/users/{user_id}")
def delete_user(user_id: int, _: dict = Depends(require_admin), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": "Deleted"}
