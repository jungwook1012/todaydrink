# app/main.py
from fastapi import FastAPI
from app.api.v1.api_v1 import api_router

app = FastAPI(
    title="회식 장소 추천 API",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")
