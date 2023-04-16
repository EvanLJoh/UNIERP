import pandas as pd
import random

# courses
courses = []
for i in range(900):
    course_name = f"Course {i + 1}"
    course_description = f"Description for Course {i + 1}"
    credits = random.randint(1, 4)
    course_quota = random.randint(10, 50)
    major_only = random.choice([0, 1])
    honors_only = random.choice([0, 1])

    # randomly select prerequisites from previously created courses
    prerequisites = []
    if i > 0:
        num_prerequisites = random.randint(1, 3)
        for j in range(num_prerequisites):
            prerequisite_id = random.randint(1, i)
            prerequisites.append(prerequisite_id)

    courses.append((course_name, course_description, credits, course_quota, major_only, honors_only, prerequisites))

# Define the majors
majors = [("Accounting", 120), ("Biology", 128), ("Business Administration", 120),
          ("Chemistry", 128), ("Computer Science", 120), ("Criminal Justice", 120),
          ("Economics", 120), ("Education", 120), ("Electrical Engineering", 128),
          ("English", 120), ("Environmental Science", 128), ("Finance", 120),
          ("History", 120), ("Information Technology", 120), ("Management", 120),
          ("Marketing", 120), ("Mathematics", 120), ("Mechanical Engineering", 128),
          ("Music", 120), ("Nursing", 128), ("Philosophy", 120),
          ("Physics", 128), ("Political Science", 120), ("Psychology", 120),
          ("Public Health", 120), ("Social Work", 120), ("Sociology", 120),
          ("Statistics", 120), ("Theater", 120), ("Visual Arts", 120)]

# Define the path to save the Excel files
path = "/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/"

# Loop through each major and generate its curriculum requirements
for major in majors:
    # Extract the major name and credit requirements
    major_name, credits_required = major

    # Generate a random number of courses required for the major
    num_courses_required = random.randint(10, 20)

    # Create a list of tuples for the major requirements
    major_requirements = []

    # Select random courses to fulfill the major requirements
    while sum([int(course[2]) for course in major_requirements]) < credits_required:
        # Shuffle the list of courses to select from randomly
        random.shuffle(courses)

        # Select a random course
        course = courses[random.randint(0, len(courses)-1)]

        # If the course is not already in the major requirements list, add it
        if course not in major_requirements:
            major_requirements.append(course)

    # Create a pandas DataFrame for the major requirements and save it to an Excel file
    major_df = pd.DataFrame(major_requirements, columns=["course_name", "description", "credits", "quota", "major_only", "honors_only", "prerequisites"])
    major_df[["course_name", "description", "quota", "major_only", "honors_only", "prerequisites"]] = major_df[["course_name", "description", "quota", "major_only", "honors_only", "prerequisites"]].applymap(str)
    major_df.to_excel(path + major_name + ".xlsx", index=False)
    



print("Data generated and saved successfully!")
