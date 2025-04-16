from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MessiStat(Base):
    __tablename__ = "messi_stats"

    id = Column(Integer, primary_key=True, index=True)
    team = Column(String)
    season = Column(String)
    matches = Column(Integer)
    goals = Column(Integer)
    assists = Column(Integer)
