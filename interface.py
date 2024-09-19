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

def footer():
    st.markdown("""
    <div class="footer">
        <p>Copyright &copy; 2024 Jayadev & Arbin & Ujwol, Hackademia</p>
    </div>
    """, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

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

if __name__ == '__main__':

    local_css("styles.css")

    # Load the pre-trained clustering model
    with open('student_clustering_model.pkl', 'rb') as file:
        kmeans_model = pickle.load(file)

    # Session state to store the uploaded file or random dataset
    if 'file_data' not in st.session_state:
        st.session_state.file_data = None

    st.title("Identifying At-Risk Students Using Clustering Techniques")
    st.write("Using clustering algorithm k-means to group students based on their performance metrics. The goal is to identify at-risk students early on by categorizing them into groups like 'high-performing,' 'average,' and 'at-risk,' enabling educators to intervene appropriately.")
    
    # Streamlit App Layout
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload your CSV dataset", type="csv")

        # Button to use random dataset
        if st.button("Try Random Dataset",use_container_width=True):
            uploaded_file = 'student_data.csv'
            st.session_state.file_data = pd.read_csv(uploaded_file)  # Load the random dataset

        # Store the uploaded file in session state
        if uploaded_file is not None:
            st.session_state.file_data = pd.read_csv(uploaded_file)

        # Sidebar for cluster visualization
        st.sidebar.markdown("""
    <div class='cluster'>Cluster Visualization Settings</div>
    """, unsafe_allow_html=True)
        col1,col2 = st.columns(2)
        x_axis_feature = col1.selectbox("Select X-Axis Feature", options=['AttendanceRate (%)', 'StudyHoursPerWeek', 'PreviousGrade', 'FinalGrade', 'HomeworkCompletion (%)'])
        y_axis_feature = col2.selectbox("Select Y-Axis Feature", options=['AttendanceRate (%)', 'StudyHoursPerWeek', 'PreviousGrade', 'FinalGrade', 'HomeworkCompletion (%)'])
        
    # Use the data stored in session state
    if st.session_state.file_data is not None:
        user_data = st.session_state.file_data
        st.write("""<div class='cluster'>Dataset Preview</div>""", unsafe_allow_html=True)
        st.dataframe(user_data)

        # Perform clustering on the dataset
        clustered_data = perform_clustering(user_data)

        # Visualize clusters
        st.write("""<div class='cluster'>Clustered Data</div>""", unsafe_allow_html=True)
        st.dataframe(clustered_data)

        # Plot the clusters using Plotly
        st.write("""<div class='cluster'>Cluster Visualization</div>""", unsafe_allow_html=True)
        fig = px.scatter(
            clustered_data, 
            x=x_axis_feature,  # Dynamically chosen feature for x-axis
            y=y_axis_feature,  # Dynamically chosen feature for y-axis
            color='Cluster',
            hover_data=['Name'],
            title=f"Cluster Visualization Based on {x_axis_feature} and {y_axis_feature}"
        )
        st.plotly_chart(fig)
        
        # Filter by cluster
        cluster_option = st.selectbox("Select Cluster to Filter", clustered_data['Cluster'].unique())
        filtered_data = clustered_data[clustered_data['Cluster'] == cluster_option]
        st.write(f"""<div class='cluster'>Details of Students in Cluster: {cluster_option}</div>""", unsafe_allow_html=True)
        st.dataframe(filtered_data)

    else:
        st.divider()
        st.write("""<div class='notFound'>Please Upload Dataset or try the Random Dataset </div>""", unsafe_allow_html=True)

    footer()