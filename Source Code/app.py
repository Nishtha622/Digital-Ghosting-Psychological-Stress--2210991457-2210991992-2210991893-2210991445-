import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page settings
st.set_page_config(
    page_title="Digital Ghosting Stress Analyzer",
    page_icon="💬",
    layout="wide"
)

# Title
st.title("💬 Digital Ghosting Stress Analyzer")
st.subheader("Research Project Based on AI-Mediated Social Rejection")

st.write("This tool analyzes emotional stress caused when AI systems suddenly stop replying.")

# Sidebar
st.sidebar.header("Navigation")

option = st.sidebar.selectbox(
    "Choose Section",
    ["Home", "Stress Analyzer", "Dashboard", "About"]
)

# Home Page
if option == "Home":
    st.header("Welcome")

    st.write("""
    This mini project is based on the research topic:

    **Digital Ghosting and Psychological Stress:
    Exploring AI-Mediated Social Rejection**

    Use the analyzer to check emotional stress level.
    """)

# Stress Analyzer
elif option == "Stress Analyzer":

    st.header("Stress Analyzer")

    user_input = st.text_area(
        "Describe how you felt when an AI suddenly stopped replying:"
    )

    if st.button("Analyze Stress"):

        text = user_input.lower()

        score = 0

        # Keyword groups
        low_words = [
            "fine", "okay", "normal", "calm",
            "moved on", "not care", "little issue"
        ]

        medium_words = [
            "confused", "sad", "upset",
            "annoyed", "frustrated",
            "silent", "worried"
        ]

        high_words = [
            "ignored", "stress", "stressed",
            "hurt", "depressed",
            "panic", "anxious",
            "cry", "broken",
            "emotional pain"
        ]

        # Low stress words
        for word in low_words:
            if word in text:
                score += 10

        # Medium stress words
        for word in medium_words:
            if word in text:
                score += 25

        # High stress words
        for word in high_words:
            if word in text:
                score += 40

        # If no matching word
        if score == 0:
            score = 15

        # Max limit
        if score > 100:
            score = 100

        st.progress(score)

        # Result levels
        if score <= 30:
            level = "Low Stress 😊"
        elif score <= 65:
            level = "Medium Stress 😐"
        else:
            level = "High Stress 😟"

        st.success(f"Stress Score: {score}%")
        st.info(f"Detected Level: {level}")

# Dashboard
elif option == "Dashboard":

    st.header("Stress Statistics Dashboard")

    data = {
        "Category": ["Low", "Medium", "High"],
        "Users": [18, 27, 12]
    }

    df = pd.DataFrame(data)

    st.table(df)

    fig, ax = plt.subplots()

    ax.bar(df["Category"], df["Users"])

    ax.set_title("Stress Level Distribution")
    ax.set_xlabel("Stress Level")
    ax.set_ylabel("Number of Users")

    st.pyplot(fig)

# About Page
elif option == "About":

    st.header("About Project")

    st.write("""
    This project converts a research paper into a practical software prototype.

    It studies how users feel emotionally when AI systems suddenly stop responding.

    Technologies Used:

    - Python
    - Streamlit
    - Pandas
    - Matplotlib
    """)