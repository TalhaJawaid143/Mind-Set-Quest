import streamlit as st
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import random

# --- Page Setup ---
st.set_page_config(page_title="Growth Mindset Journal", layout="centered")
st.title("🧠 Daily Growth Mindset Tracker")
st.subheader("Reflect, Track, and Grow Every Day 💪")

# --- Quote of the Day ---
quotes = [
    "Mistakes are proof that you are trying.",
    "Challenges are opportunities in disguise.",
    "Effort is the path to mastery.",
    "You can learn anything with persistence.",
    "Feedback is a gift for growth."
]
st.info("🌟 " + random.choice(quotes))

# --- Initialize session state ---
if "journal" not in st.session_state:
    st.session_state.journal = []

# --- Today's Input ---
st.markdown("### ✍️ Today's Reflection")
with st.form("reflection_form"):
    date = datetime.today().strftime('%Y-%m-%d')
    reflection = st.text_area("What did you learn or overcome today?", height=150)
    mindset_score = st.slider("How strong was your growth mindset today?", 0, 10, 5)
    submit = st.form_submit_button("Save Entry")

if submit and reflection:
    st.session_state.journal.append({
        "Date": date,
        "Reflection": reflection,
        "Mindset Score": mindset_score
    })
    st.success("Reflection saved!")

# --- Show Journal Table ---
if st.session_state.journal:
    st.markdown("### 📘 Your Reflection History")
    df = pd.DataFrame(st.session_state.journal)
    st.dataframe(df)

    # --- Mood Chart ---
    st.markdown("### 📊 Mindset Trend")
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Mindset Score"], marker='o', color='teal')
    ax.set_ylabel("Mindset Score (0-10)")
    ax.set_xlabel("Date")
    ax.set_title("Growth Mindset Over Time")
    ax.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # --- Download Option ---
    st.markdown("### 📤 Download Your Reflections")
    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    st.download_button(
        label="Download CSV",
        data=buffer,
        file_name="growth_mindset_journal.csv",
        mime="text/csv"
    )
else:
    st.warning("No entries yet. Start reflecting today! 🌱")
