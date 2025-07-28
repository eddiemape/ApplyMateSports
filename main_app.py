import streamlit as st
from predictor import get_daily_predictions

st.set_page_config(page_title="ApplyMate Sports", layout="wide")

st.title("⚾ ApplyMate Sports: Daily MLB Predictions")
st.write("AI + Stats powered picks for today's matchups")

# Predict today's games
predictions = get_daily_predictions()

for game in predictions:
    st.subheader(f"{game['matchup']}")
    st.write(f"✅ Predicted Winner: **{game['winner']}**")
    st.write(f"🧠 Confidence: {game['confidence']}%")
    st.write("---")

import os
from PIL import Image
import datetime

# 📸 Save screenshot to Desktop
if st.button("📷 Save Screenshot"):
    image = Image.new("RGB", (800, 400), color=(73, 109, 137))
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    filename = f"applymate_screenshot_{timestamp}.png"
    full_path = os.path.join(desktop_path, filename)
    image.save(full_path)
    st.success(f"Screenshot saved to Desktop as {filename}")
