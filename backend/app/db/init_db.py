from sqlalchemy.orm import Session
from app.models.user import AdminUser
from app.core.security import hash_password
from app.core.config import settings


def seed_admin(db: Session):
    existing = db.query(AdminUser).filter(AdminUser.email == settings.ADMIN_EMAIL).first()
    if not existing:
        admin = AdminUser(email=settings.ADMIN_EMAIL, hashed_password=hash_password(settings.ADMIN_PASSWORD))
        db.add(admin)
        db.commit()
        print(f"Admin seeded: {settings.ADMIN_EMAIL}")
