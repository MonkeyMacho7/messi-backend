from pydantic import BaseModel
from typing import Optional

class MessiStat(BaseModel):
    season: str
    team: str
    goals: int
    assists: int
    matches: int
