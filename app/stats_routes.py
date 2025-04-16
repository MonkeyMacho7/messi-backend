from fastapi import APIRouter
from app.services.stats_service import get_all_stats

router = APIRouter()

@router.get("/stats")
def read_stats():
    return get_all_stats()
