from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.database import get_db
from app.models import MessiStatDB
from app.schemas import MessiStat
from app.models import MessiAllTimeStatDB
from app.schemas import MessiAllTimeStat

router = APIRouter()

@router.get("/stats", response_model=list[MessiStat])
def get_all_stats(db: Session = Depends(get_db)):
    stats = db.query(MessiStatDB).all()
    print(" Fetching from Postgres DB!")
    return stats
@router.get("/all-time", response_model=MessiAllTimeStat)
def get_all_time_stats(db: Session = Depends(get_db)):
    stat = db.query(MessiAllTimeStatDB).first()
    return stat