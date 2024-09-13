import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Data Preparation
def load_and_preprocess_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    
    # Select relevant features for clustering
    features = ['attendance', 'homework_completion', 'test_scores', 'participation']
    X = df[features]
    
    # Normalize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    return X_scaled, df

# Step 2: Implement K-means clustering
def perform_clustering(X_scaled, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X_scaled)
    return cluster_labels

# Function to analyze clusters
def analyze_clusters(df, cluster_labels):
    df['Cluster'] = cluster_labels
    cluster_means = df.groupby('Cluster').mean()
    return cluster_means

# Function to visualize clusters
def visualize_clusters(X_scaled, cluster_labels):
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=cluster_labels, cmap='viridis')
    plt.title('Student Clusters')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.colorbar(scatter)
    return plt

# Main function to run the clustering process
def run_clustering(file_path):
    X_scaled, df = load_and_preprocess_data(file_path)
    cluster_labels = perform_clustering(X_scaled)
    cluster_means = analyze_clusters(df, cluster_labels)
    plt = visualize_clusters(X_scaled, cluster_labels)
    return df, cluster_means, plt

# Example usage
# file_path = 'student_data.csv'
# df, cluster_means, plt = run_clustering(file_path)
# print(cluster_means)
# plt.show()