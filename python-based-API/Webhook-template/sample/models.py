from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base

class WebhookEvent(Base):
    __tablename__ = "webhook_events"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    event_type = Column(String)
    payload = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
