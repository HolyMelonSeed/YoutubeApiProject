from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main.api.routes_videos import router as video_router

app = FastAPI(title="YouTube Recommender API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev, restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(video_router, prefix="/api/videos")

@app.get("/")
def root():
    return {"message": "YouTube Recommender API running"}