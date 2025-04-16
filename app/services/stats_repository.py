from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import MessiStat  # SQLAlchemy DB model

class MessiRepository:
    def __init__(self):
        self.db: Session = SessionLocal()

    def get_all_stats(self):
        return self.db.query(MessiStat).all()
