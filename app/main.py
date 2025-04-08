from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.stats_repository import MessiRepository
from app.schemas import MessiStat
from typing import List

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
repo = MessiRepository()

@app.get("/stats", response_model=List[MessiStat])
def read_stats():
    return repo.get_all_stats()
