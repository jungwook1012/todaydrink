# load_api/main.py

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from load_api.naver_place_loader import search_places_from_naver

app = FastAPI()

# Flutter 연동을 위한 CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/search")
def search_places(query: str = Query(..., description="검색어 예: '안국역 맛집'")):
    results = search_places_from_naver(query)
    return {"results": results}
