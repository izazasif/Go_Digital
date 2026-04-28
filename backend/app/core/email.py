from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from app.core.config import settings

_use_credentials = bool(settings.MAIL_USERNAME and settings.MAIL_PASSWORD)

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=settings.MAIL_STARTTLS,
    MAIL_SSL_TLS=settings.MAIL_SSL_TLS,
    USE_CREDENTIALS=_use_credentials,
    VALIDATE_CERTS=_use_credentials,
)

fm = FastMail(conf)

CYAN = "#00BFFF"
BG = "#0D1117"


def _base_html(title: str, body: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html>
    <head><meta charset="utf-8"><title>{title}</title></head>
    <body style="margin:0;padding:0;background:{BG};font-family:Arial,sans-serif;">
      <div style="max-width:600px;margin:40px auto;background:#111827;border-radius:12px;overflow:hidden;border:1px solid #1f2937;">
        <div style="background:linear-gradient(135deg,#0D1117,#1a2233);padding:30px 40px;border-bottom:2px solid {CYAN};">
          <span style="font-size:24px;font-weight:900;color:{CYAN};letter-spacing:2px;">GO_Digital</span>
        </div>
        <div style="padding:40px;">
          {body}
        </div>
        <div style="padding:20px 40px;border-top:1px solid #1f2937;text-align:center;">
          <p style="color:#4b5563;font-size:12px;margin:0;">© 2025 GO_Digital. All rights reserved.</p>
        </div>
      </div>
    </body>
    </html>
    """


async def send_verification_email(to: str, name: str, token: str):
    verify_url = f"{settings.FRONTEND_URL}/verify-email?token={token}"
    body = f"""
    <h2 style="color:white;margin-top:0;">Verify your email</h2>
    <p style="color:#9ca3af;">Hi {name}, welcome to GO_Digital! Please verify your email to activate your account.</p>
    <a href="{verify_url}" style="display:inline-block;margin:20px 0;padding:14px 32px;background:{CYAN};color:#0D1117;font-weight:700;border-radius:8px;text-decoration:none;">Verify Email</a>
    <p style="color:#6b7280;font-size:13px;">This link expires in 24 hours. If you didn't sign up, ignore this email.</p>
    """
    msg = MessageSchema(subject="Verify your GO_Digital account", recipients=[to], body=_base_html("Verify Email", body), subtype=MessageType.html)
    await fm.send_message(msg)


async def send_newsletter_welcome(to: str):
    body = f"""
    <h2 style="color:white;margin-top:0;">You're subscribed!</h2>
    <p style="color:#9ca3af;">Thanks for joining the GO_Digital newsletter. You'll receive updates on cloud security, AI, and digital innovation.</p>
    <p style="color:#6b7280;font-size:13px;">To unsubscribe, reply to this email.</p>
    """
    msg = MessageSchema(subject="Welcome to GO_Digital Newsletter", recipients=[to], body=_base_html("Newsletter Welcome", body), subtype=MessageType.html)
    await fm.send_message(msg)


async def send_appointment_confirmation(to: str, name: str, service: str, date: str, time: str):
    body = f"""
    <h2 style="color:white;margin-top:0;">Appointment Request Received</h2>
    <p style="color:#9ca3af;">Hi {name}, we've received your appointment request. Here are the details:</p>
    <table style="color:#d1d5db;margin:20px 0;border-collapse:collapse;width:100%;">
      <tr><td style="padding:8px 0;color:#6b7280;width:140px;">Service:</td><td style="color:white;">{service}</td></tr>
      <tr><td style="padding:8px 0;color:#6b7280;">Preferred Date:</td><td style="color:white;">{date}</td></tr>
      <tr><td style="padding:8px 0;color:#6b7280;">Preferred Time:</td><td style="color:white;">{time}</td></tr>
    </table>
    <p style="color:#9ca3af;">Our team will review your request and get back to you shortly.</p>
    """
    msg = MessageSchema(subject="GO_Digital — Appointment Request Received", recipients=[to], body=_base_html("Appointment Confirmation", body), subtype=MessageType.html)
    await fm.send_message(msg)


async def send_appointment_admin_notification(admin_email: str, appointment: dict):
    rows = "".join(f"<tr><td style='padding:6px 0;color:#6b7280;width:140px;'>{k}:</td><td style='color:white;'>{v}</td></tr>" for k, v in appointment.items())
    body = f"""
    <h2 style="color:white;margin-top:0;">New Appointment Request</h2>
    <table style="color:#d1d5db;margin:20px 0;border-collapse:collapse;width:100%;">{rows}</table>
    <p style="color:#6b7280;font-size:13px;">Log in to the admin dashboard to manage this appointment.</p>
    """
    msg = MessageSchema(subject="GO_Digital — New Appointment Request", recipients=[admin_email], body=_base_html("New Appointment", body), subtype=MessageType.html)
    await fm.send_message(msg)


async def send_appointment_reply(to: str, name: str, status: str, admin_message: str):
    status_color = CYAN if status == "confirmed" else "#ef4444"
    body = f"""
    <h2 style="color:white;margin-top:0;">Appointment Update</h2>
    <p style="color:#9ca3af;">Hi {name}, your appointment status has been updated.</p>
    <p style="margin:16px 0;"><span style="background:{status_color};color:#0D1117;font-weight:700;padding:6px 16px;border-radius:20px;">{status.upper()}</span></p>
    <div style="background:#1f2937;border-radius:8px;padding:20px;margin-top:20px;">
      <p style="color:#9ca3af;margin:0;">{admin_message}</p>
    </div>
    """
    msg = MessageSchema(subject=f"GO_Digital — Appointment {status.capitalize()}", recipients=[to], body=_base_html("Appointment Update", body), subtype=MessageType.html)
    await fm.send_message(msg)


async def send_newsletter_broadcast(recipients: list[str], subject: str, content: str):
    body = f"""
    <div style="color:#9ca3af;line-height:1.7;">{content}</div>
    <p style="color:#6b7280;font-size:12px;margin-top:30px;">To unsubscribe, reply to this email.</p>
    """
    msg = MessageSchema(subject=subject, recipients=recipients, body=_base_html(subject, body), subtype=MessageType.html)
    await fm.send_message(msg)
