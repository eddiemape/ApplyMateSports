
import streamlit as st
import datetime

st.set_page_config(page_title="ApplyMate Sports - MLB Predictor", layout="wide")

st.title("⚾ ApplyMate Sports: MLB Winner Predictor")

st.markdown("Welcome! This app predicts the winners of upcoming MLB games using real-time and historical statistics.")

# Placeholder for upcoming games logic
today = datetime.date.today()
future_dates = [today + datetime.timedelta(days=i) for i in range(3)]

st.subheader("Upcoming MLB Matchups")
for date in future_dates:
    st.write(f"🔜 Games on {date.strftime('%A, %B %d, %Y')} (Live stats and predictions coming soon)")
