from pydantic import BaseModel

class MessiStat(BaseModel):
    id: int
    team: str
    season: str
    matches: int
    goals: int
    assists: int

    class Config:
        orm_mode = True
