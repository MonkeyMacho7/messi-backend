from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.database import get_db
from app.models import MessiStatDB
from app.schemas import MessiStat

router = APIRouter()

@router.get("/stats", response_model=list[MessiStat])
def get_all_stats(db: Session = Depends(get_db)):
    stats = db.query(MessiStatDB).all()
    return stats
