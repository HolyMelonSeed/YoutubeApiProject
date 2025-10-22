from fastapi import APIRouter, Query
from main.core.youtube_service import search_videos, recommend_videos

router = APIRouter()

@router.get("/search")
def search(query: str = Query(..., min_length=2)):
    return search_videos(query)

@router.get("/recommend")
def recommend(video_id: str):
    return recommend_videos(video_id)