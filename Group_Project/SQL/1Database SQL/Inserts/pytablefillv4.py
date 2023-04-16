import random
import datetime
import pandas as pd

# Schools
schools = [f"School {i + 1}" for i in range(20)]

# Honors Programs
honors_programs = [f"Honors Program {i + 1}" for i in range(20)]
honors_programs_df = pd.DataFrame(honors_programs, columns=["honors_program_name"])

# Semester months
semesters = {
    "Fall": range(8, 13),
    "Spring": range(1, 5),
    "Summer": range(5, 8)
}

# courses
courses = [(f"Course {i + 1}",
            f"Description for Course {i + 1}",
            max(min(random.randint(1, 4), 5), 1),
            random.randint(10, 50),
            random.choice([0, 1]),
            random.choice([0, 1]),
            [random.randint(1, i) for _ in range(random.randint(1, 3))] if i > 0 else [],
            random.sample(list(semesters.keys()), random.randint(1, len(semesters))))
           for i in range(900)]

courses_df = pd.DataFrame(courses, columns=["course_name", "course_description", "credits", "course_quota", "major_only", "honors_only", "prerequisites", "available_semesters"])

# course prerequisites
course_prerequisites = [(course_id+1, prerequisite_id) for course_id, course in enumerate(courses) for prerequisite_id in course[6]]

course_prereqs_df = pd.DataFrame(course_prerequisites, columns=["course_id", "prerequisite_id"])

# Major 
majors = [(f"Major {i + 1}", random.randint(120, 140)) for i in range(60)]
majors_df = pd.DataFrame(majors, columns=["major_name", "credits_required"])

#Major Requirements
major_requirements = [(i + 1, random.randint(1, 900)) for i in range(60) for _ in range(random.randint(5, 15))]
major_requirements_df = pd.DataFrame(major_requirements, columns=["major_id", "course_id"])

# Minors
minors = [f"Minor {i + 1}" for i in range(20)]
minors_df = pd.DataFrame(minors, columns=["minor_name"])

# Minor Requirements
minor_requirements = [(i + 1, random.randint(1, 900)) for i in range(20) for _ in range(random.randint(3, 7))]
minor_requirements_df = pd.DataFrame(minor_requirements, columns=["minor_id", "course_id"])

# Concentrations
concentrations = [f"Concentration {i + 1}" for i in range(20)]
concentrations_df = pd.DataFrame(concentrations, columns=["concentration_name"])

# Concentration Requirements
concentration_requirements = [(i + 1, random.randint(1, 900)) for i in range(20) for _ in range(random.randint(2 , 5))]
concentration_requirements_df = pd.DataFrame(concentration_requirements, columns=["concentration_id", "course_id"])

#Honors Program Requirements
honors_program_requirements = [(i + 1, course_id) for i in range(20) for course_id in random.sample(list(courses_df.index), random.randint(3, 8))]
honors_program_requirements_df = pd.DataFrame(honors_program_requirements, columns=["honors_program_id", "course_id"])

#Merge tables
df1 = pd.merge(major_requirements_df, majors_df, left_on="major_id", right_index=True).drop(columns=["major_id"]).rename(columns={"major_name": "requirement"})
df2 = pd.merge(minor_requirements_df, minors_df, left_on="minor_id", right_index=True).drop(columns=["minor_id"]).rename(columns={"minor_name": "requirement"})
df3 = pd.merge(concentration_requirements_df, concentrations_df, left_on="concentration_id", right_index=True).drop(columns=["concentration_id"]).rename(columns={"concentration_name": "requirement"})
df4 = pd.merge(honors_program_requirements_df, honors_programs_df, left_on="honors_program_id", right_index=True).drop(columns=["honors_program_id"]).rename(columns={"honors_program_name": "requirement"})

requirements_df = pd.concat([df1, df2, df3, df4]).reset_index(drop=True)

#Students
students = [(f"Student {i + 1}", random.choice(schools), random.choice(majors)[0], random.sample(list(minors), random.randint(0, 2)), random.sample(list(concentrations), random.randint(0, 2)), random.choice(honors_programs) if random.randint(0, 1) else None) for i in range(2000)]
students_df = pd.DataFrame(students, columns=["student_name", "school_name", "major_name", "minor_names", "concentration_names", "honors_program_name"])

#Enrollments
enrollments = [(random.randint(1, 900), student_id, random.choice(list(semesters.keys()))) for student_id in range(1, 2001) for _ in range(random.randint(2, 5))]
enrollments_df = pd.DataFrame(enrollments, columns=["course_id", "student_id", "semester"])

#Output data
students_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/students.xlsx", index=False)
courses_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/courses.xlsx", index=False)
enrollments_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/enrollments.xlsx", index=False)
majors_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/majors.xlsx", index=False)
requirements_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/requirements.xlsx", index=False)

print("Data generated and saved successfully!")
