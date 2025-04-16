from pydantic import BaseModel

class MessiStat(BaseModel):
    id: int
    team: str
    season: str
    matches: int
    goals: int
    assists: int
    
class MessiAllTimeStat(BaseModel):
    goals: int
    assists: int
    games_played: int
    trophies_won: int


    class Config:
        orm_mode = True
