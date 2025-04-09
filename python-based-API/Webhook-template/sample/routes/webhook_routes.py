from fastapi import APIRouter, Request, Depends
from app.services.webhook_handler import verify_signature
from app.models import WebhookEvent
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/webhook", tags=["Webhook"])

@router.post("/")
async def receive_webhook(request: Request, db: Session = Depends(get_db)):
    raw_body = await request.body()
    verify_signature(request, raw_body)

    data = await request.json()
    event = WebhookEvent(
        source=data.get("source", "unknown"),
        event_type=data.get("type", "generic"),
        payload=str(data)
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return {"status": "received", "id": event.id}
