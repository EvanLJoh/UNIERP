import random

# Define the possible grades
grades = ['A', 'B', 'C', 'D', 'F']

# Define the possible semesters
semesters = ['Fall', 'Spring']

# Define the years
years = [2018, 2019, 2020, 2021, 2022]

# Generate 500 rows of data
for j in range(500):
    for i in range(500):
        # Select a random student_id
        student_id = random.randint(1, 100)

        # Select a random course_id
        course_id = random.randint(1, 100)

        # Select a random semester and year
        semester = random.choice(semesters)
        year = random.choice(years)

        # Select a random grade
        grade = random.choice(grades)

        # Generate random credits earned for major, minor, concentration, and honors
        credits_earned = random.randint(1, 4)
        major_credits_earned = random.randint(1, credits_earned)
        minor_credits_earned = random.randint(0, credits_earned - major_credits_earned)
        concentration_credits_earned = random.randint(0, credits_earned - major_credits_earned - minor_credits_earned)
        honors_credits_earned = random.randint(0, credits_earned - major_credits_earned - minor_credits_earned - concentration_credits_earned)

        # Print the row as a MySQL insert statement
        print(f"INSERT INTO student_transcript (student_id, course_id, semester, year, grade, credits_earned, major_credits_earned, minor_credits_earned, concentration_credits_earned, honors_credits_earned) VALUES ({student_id}, {course_id}, '{semester}', {year}, '{grade}', {credits_earned}, {major_credits_earned}, {minor_credits_earned}, {concentration_credits_earned}, {honors_credits_earned});")
