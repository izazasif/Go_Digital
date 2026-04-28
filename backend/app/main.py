from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.db.base import engine, SessionLocal, Base
from app.db.init_db import seed_admin

import app.models.user  # noqa: F401 — register models with Base
import app.models.email_verification  # noqa: F401
import app.models.newsletter  # noqa: F401
import app.models.appointment  # noqa: F401

from app.routers import auth, admin_auth, newsletter, appointments

app = FastAPI(title=settings.APP_NAME, docs_url="/api/docs", redoc_url="/api/redoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost", settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(admin_auth.router)
app.include_router(newsletter.router)
app.include_router(appointments.router)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        seed_admin(db)


@app.get("/api/health")
def health():
    return {"status": "ok", "app": settings.APP_NAME}
