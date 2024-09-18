import random
import pandas as pd

# Helper functions to generate random data for each field
def generate_name():
    first_names = ['John', 'Jane', 'Alex', 'Emily', 'Michael', 'Sarah', 'David', 'Jessica', 'Daniel', 'Emma']
    last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_id():
    return f"S{random.randint(1000, 9999)}"

def generate_gender():
    return random.choice(['Male', 'Female'])

def generate_attendance_rate():
    return round(random.uniform(60, 100), 2)  # Percentage between 60% and 100%

def generate_study_hours_per_week():
    return round(random.uniform(5, 30), 1)  # Hours between 5 and 30

def generate_previous_grade():
    return random.randint(50, 100)  # Grade between 50 and 100

def generate_extracurricular_activities():
    return random.choice(['None', 'Sports', 'Music', 'Art', 'Debate', 'Community Service'])

def generate_parental_support():
    return random.choice(['Low', 'Medium', 'High'])

def generate_final_grade():
    return random.randint(50, 100)  # Final Grade between 50 and 100

def generate_homework_completion():
    return round(random.uniform(50, 100), 2)  # Homework completion percentage

# Create a dataset with 100 students
def generate_dataset():
    num_students = 100
    students_data = {
        "Name": [generate_name() for _ in range(num_students)],
        "ID": [generate_id() for _ in range(num_students)],
        "Gender": [generate_gender() for _ in range(num_students)],
        "AttendanceRate (%)": [generate_attendance_rate() for _ in range(num_students)],
        "StudyHoursPerWeek": [generate_study_hours_per_week() for _ in range(num_students)],
        "PreviousGrade": [generate_previous_grade() for _ in range(num_students)],
        "ExtracurricularActivities": [generate_extracurricular_activities() for _ in range(num_students)],
        "ParentalSupport": [generate_parental_support() for _ in range(num_students)],
        "FinalGrade": [generate_final_grade() for _ in range(num_students)],
        "HomeworkCompletion (%)": [generate_homework_completion() for _ in range(num_students)],
    }

    df_students = pd.DataFrame(students_data)
    df_students.head()

    return df_students
