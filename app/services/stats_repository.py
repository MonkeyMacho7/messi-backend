import os
import json

class MessiRepository:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))  
        project_root = os.path.abspath(os.path.join(base_dir, "../../")) 
        data_path = os.path.join(project_root, "data", "messi_stats.json")

        print("Loading from:", data_path)  

        with open(data_path, "r") as f:
            self.stats = json.load(f)

    def get_all_stats(self):
        return self.stats
