import streamlit as st
import pandas as pd

# --- Streamlit UI ---
import video_service

st.title("🎬 Custom YouTube Recommender")

query = st.text_input("Search for videos:")
if query:
    videos = video_service.search_videos(query)
    for v in videos:
        st.image(v["thumbnail"], width=200)
        st.markdown(f"**[{v['title']}](https://www.youtube.com/watch?v={v['videoId']})**")
        st.caption(f"Channel: {v['channel']}")
        with st.expander("Show related videos"):
            related = video_service.get_related_videos(v["videoId"])
            for r in related:
                st.image(r["thumbnail"], width=150)
                st.markdown(f"- [{r['title']}](https://www.youtube.com/watch?v={r['videoId']})")
