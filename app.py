import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="World Cup Dashboard", layout="wide")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>⚽ World Cup Interactive Dashboard</h1>", unsafe_allow_html=True)

# Upload or use default dataset
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except:
        df = pd.read_csv(uploaded_file, encoding='latin1')
else:
    df = pd.read_csv("world_cup_data.csv")

# Sidebar filters
st.sidebar.header("🔍 Filters")

if "Year" in df.columns:
    year = st.sidebar.selectbox("Select Year", df["Year"].unique())
    df = df[df["Year"] == year]

# KPIs
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

if "Goals_Scored" in df.columns:
    col1.metric("Total Goals", int(df["Goals_Scored"].sum()))

if "Matches_Played" in df.columns:
    col2.metric("Matches Played", int(df["Matches_Played"].sum()))

if "Winner" in df.columns:
    col3.metric("Winner", df["Winner"].iloc[0])

# Data preview
st.subheader("📄 Dataset Preview")
st.dataframe(df)

# Visualization
st.subheader("📈 Visualization")

column = st.selectbox("Choose column", df.columns)

fig, ax = plt.subplots()

if pd.api.types.is_numeric_dtype(df[column]):
    df[column].plot(kind='bar', ax=ax)
else:
    df[column].value_counts().plot(kind='bar', ax=ax)

ax.set_title(f"{column} Analysis", color="green")
st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
