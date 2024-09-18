import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import plotly.express as px

# Configure page setup
st.set_page_config(
    page_title="Student Clustering",
    layout="wide",  # Set to wide mode
    initial_sidebar_state="expanded",
)

# Load the pre-trained clustering model
with open('student_clustering_model.pkl', 'rb') as file:
    kmeans_model = pickle.load(file)

# Function to generate random dataset (similar to the one we saved earlier)
def generate_random_dataset():
    data = {
        'Name': ['John Doe', 'Jane Smith', 'Alex Johnson', 'Emily Davis', 'Michael Brown'],
        'AttendanceRate (%)': [85, 90, 78, 92, 70],
        'StudyHoursPerWeek': [15, 20, 10, 22, 18],
        'PreviousGrade': [75, 85, 65, 88, 70],
        'FinalGrade': [80, 88, 72, 90, 75],
        'HomeworkCompletion (%)': [85, 92, 70, 95, 78]
    }
    return pd.DataFrame(data)

# Function to map cluster numbers to meaningful names
def map_cluster_labels(cluster_number):
    if cluster_number == 0:
        return "High-Performing"
    elif cluster_number == 1:
        return "Average"
    else:
        return "At-Risk"

# Function to perform clustering
def perform_clustering(df):
    features = df[['AttendanceRate (%)', 'StudyHoursPerWeek', 'PreviousGrade', 'FinalGrade', 'HomeworkCompletion (%)']]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    clusters = kmeans_model.predict(scaled_features)
    df['Cluster'] = clusters
    df['Cluster'] = df['Cluster'].apply(map_cluster_labels)  # Map clusters to meaningful labels
    return df

# Streamlit App Layout
st.title("Student Clustering App")
st.write("This app allows you to cluster students based on their performance metrics and identify at-risk students.")

# File uploader for user's dataset
uploaded_file = st.file_uploader("Upload your CSV dataset", type="csv")

if st.button("Try Random Dataset"):
    uploaded_file = 'student_data.csv'

if uploaded_file is not None:
    # If the user uploads a dataset
    user_data = pd.read_csv(uploaded_file)
    st.write("Uploaded Dataset:")
    st.dataframe(user_data)

    # Perform clustering on the uploaded dataset
    clustered_data = perform_clustering(user_data)
else:
    st.write("Or use the sample dataset.")
    # Generate random dataset
    random_data = generate_random_dataset()
    st.write("Sample Dataset:")
    st.dataframe(random_data)

    # Perform clustering on the sample dataset
    clustered_data = perform_clustering(random_data)

# Visualize clusters
st.write("Clustered Data:")
st.dataframe(clustered_data)

# Filter by cluster
cluster_option = st.selectbox("Select Cluster to Filter", clustered_data['Cluster'].unique())
filtered_data = clustered_data[clustered_data['Cluster'] == cluster_option]

st.write(f"Details of Students in Cluster: {cluster_option}")
st.dataframe(filtered_data)

# Plot the clusters using Plotly
st.write("Cluster Visualization:")
fig = px.scatter()
