# load_api/naver_place_loader.py

import requests
import urllib.parse
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

def search_places_from_naver(query: str, display: int = 10):
    url = "https://openapi.naver.com/v1/search/local.json"
    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET
    }

    params = {
        "query": query,
        "display": display,
        "sort": "comment"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        items = response.json().get("items", [])
        places = []
        for item in items:
            places.append({
                "name": item.get("title", "").replace("<b>", "").replace("</b>", ""),
                "category": item.get("category"),
                "address": item.get("roadAddress"),
                "phone": item.get("telephone"),
                "map_link": item.get("link"),
                "mapx": item.get("mapx"),
                "mapy": item.get("mapy")
            })
        return places
    else:
        return {"error": f"API 호출 실패: {response.status_code}"}
