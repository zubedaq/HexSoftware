from googleapiclient.discovery import build
import streamlit as st

API_KEY = "YOUR_NEW_API_KEY"

youtube = build("youtube", "v3", developerKey=API_KEY)

channel_id = "UCX6OQ3DkcsbYNE6H8uQQuVA"

request = youtube.channels().list(
    part="snippet,statistics",
    id=channel_id
)

response = request.execute()

channel = response["items"][0]

name = channel["snippet"]["title"]
subs = int(channel["statistics"]["subscriberCount"])
views = int(channel["statistics"]["viewCount"])
videos = int(channel["statistics"]["videoCount"])

st.title("YouTube Data Dashboard")

st.subheader(name)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Subscribers", f"{subs:,}")

with col2:
    st.metric("Total Views", f"{views:,}")

with col3:
    st.metric("Videos", f"{videos:,}")
