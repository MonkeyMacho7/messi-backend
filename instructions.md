# Messi Backend - Instructions

## Overview
This is the backend for the Lord Messi website project. It is built using FastAPI and follows the Repository Pattern. The backend serves season statistics data about Lionel Messi, stored in a local JSON file (`messi_stats.json`).

## How to Run Locally

### Prerequisites
- Python 3.9+
- `pip`
- `uvicorn`
- `fastapi`
- `pydantic`

### Steps
1. Clone the repo:
   ```bash
   git clone https://github.com/MonkeyMacho7/messi-backend.git
   cd messi-backend
2. Install dependencies: pip install -r requirements.txt
3. Run the server: uvicorn app.main:app --reload
4. Locally will run on this "http://127.0.0.1:8000/stats" but with my ec2 running, it will be on this: "http://3.144.172.68:8000/stats"
