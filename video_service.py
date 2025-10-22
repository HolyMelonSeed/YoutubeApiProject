import streamlit as st
import pandas as pd
import plotly.express as px
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv("data.env")
API_KEY = st.secrets("YOUTUBE_API_KEY")


def search_videos(query, max_results=10):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results
    )
    response = request.execute()

    videos = []
    for item in response["items"]:
        video = {
            "title": item["snippet"]["title"],
            "videoId": item["id"]["videoId"],
            "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"],
            "channel": item["snippet"]["channelTitle"]
        }
        videos.append(video)
    return videos


def get_related_videos(video_id, max_results=5):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.search().list(
        relatedToVideoId=video_id,
        part="snippet",
        type="video",
        maxResults=max_results
    )
    response = request.execute()

    related = []
    for item in response["items"]:
        related.append({
            "title": item["snippet"]["title"],
            "videoId": item["id"]["videoId"],
            "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"]
        })
    return related
