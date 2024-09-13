import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from clustering import run_clustering

st.title('Student Clustering Analysis')

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df, cluster_means, plt = run_clustering(uploaded_file)
    
    st.subheader('Cluster Analysis')
    st.write(cluster_means)
    
    st.subheader('Cluster Visualization')
    st.pyplot(plt)
    
    st.subheader('Student Data with Cluster Labels')
    st.write(df)
    
    # Download clustered data
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download clustered data as CSV",
        data=csv,
        file_name="clustered_student_data.csv",
        mime="text/csv",
    )