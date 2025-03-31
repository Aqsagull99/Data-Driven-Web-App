import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App Title
st.title("📊 Simple Data-Driven Web App")

# Upload CSV File
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)  # Read CSV
    st.write("### 📂 Uploaded Data:")
    st.dataframe(df)  # Show Data Table
    
    # Select Column for Analysis
    column = st.selectbox("Select a column for analysis", df.columns)
    
    # Show Summary
    st.write(f"### 📌 Summary of {column}:")
    st.write(df[column].describe())
    
    # Plot Histogram
    fig, ax = plt.subplots()
    df[column].hist(ax=ax, bins=20)
    st.pyplot(fig)



    