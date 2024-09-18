from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd

# Load your dataset (if not already loaded)
df_students = pd.read_csv('student_data.csv')

# Selecting the features for clustering
features = df_students[['AttendanceRate (%)', 'StudyHoursPerWeek', 'PreviousGrade', 'FinalGrade', 'HomeworkCompletion (%)']]

# Standardizing the data (important for K-Means to work effectively)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Creating and training the K-Means model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(scaled_features)

# Saving the model using pickle
with open('student_clustering_model.pkl', 'wb') as file:
    pickle.dump(kmeans, file)

print("Model saved as 'student_clustering_model.pkl'")
