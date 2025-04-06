import json
from typing import List
from pathlib import Path
from .schemas import MessiStat

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "messi_stats.json"

class MessiRepository:
    def __init__(self, data_path=DATA_PATH):
        self.data_path = data_path

    def get_all_stats(self) -> List[MessiStat]:
        with open(self.data_path, "r") as file:
            data = json.load(file)
        return [MessiStat(**item) for item in data]
