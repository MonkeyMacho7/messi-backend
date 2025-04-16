from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.stats_routes import router as stats_router

app = FastAPI()

app.include_router(stats_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
