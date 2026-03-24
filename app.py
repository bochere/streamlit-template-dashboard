import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Universal Dashboard", layout="wide")

st.title("📊 Universal CSV Interactive Dashboard")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except:
        df = pd.read_csv(uploaded_file, encoding='latin1')

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe(include='all'))

    column = st.selectbox("Select a column to visualize", df.columns)

    if column:
        st.subheader(f"Visualization of {column}")

        fig, ax = plt.subplots()

        if pd.api.types.is_numeric_dtype(df[column]):
            df[column].hist(ax=ax, bins=20)
            ax.set_ylabel("Frequency")
        else:
            df[column].value_counts().plot(kind='bar', ax=ax)

        st.pyplot(fig)
