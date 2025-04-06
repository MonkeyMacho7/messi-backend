from fastapi import FastAPI
from app.services.stats_repository import MessiRepository
from app.schemas import MessiStat
from typing import List

app = FastAPI()
repo = MessiRepository()

@app.get("/stats", response_model=List[MessiStat])
def read_stats():
    return repo.get_all_stats()
