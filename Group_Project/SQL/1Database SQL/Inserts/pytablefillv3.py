import random
import datetime
import pandas as pd

# Schools
schools = []
for i in range(20):
    schools.append(f"School {i + 1}")

# Honors Programs
honors_programs = []
for i in range(20):
    honors_programs.append(f"Honors Program {i + 1}")

# Majors
majors = []
credits_required = []
for i in range(60):
    major_name = f"Major {i + 1}"
    credits_required.append(random.randint(120, 140))
    majors.append((major_name, credits_required[-1]))

# Add credits_required column to majors_df DataFrame
majors_df["credits_required"] = credits_required

# Schools, Honors Programs, and Majors code is the same

# courses
courses = []
course_prereqs = {}
for i in range(900):
    course_name = f"Course {i + 1}"
    course_description = f"Description for Course {i + 1}"
    credits = random.randint(1, 4)
    credits = max(min(credits, 5), 1)  # Ensure credits are between 1 and 5, inclusive
    course_quota = random.randint(10, 50)
    major_only = random.choice([0, 1])
    honors_only = random.choice([0, 1])
    available_semesters = random.sample(list(semesters.keys()), random.randint(1, len(semesters)))

    prereqs = []
    if i > 0:
        num_prerequisites = random.randint(1, 3)
        for j in range(num_prerequisites):
            prerequisite_id = random.randint(1, i)
            prereqs.append(prerequisite_id)
            course_prereqs.setdefault(prerequisite_id, []).append(i + 1)

    courses.append((course_name, course_description, credits, course_quota, major_only, honors_only, prereqs, available_semesters))

# course prerequisites
course_prerequisites = []
for course_id, course in enumerate(courses):
    for prerequisite_id in course[6]:
        course_prerequisites.append((course_id+1, prerequisite_id))



# Major Requirements
major_requirements = []
for i in range(60):
    major_id = i + 1
    for j in range(random.randint(5, 15)):
        course_id = random.randint(1, 900)
        major_requirements.append((major_id, course_id))

# Minors
minors = []
for i in range(20):
    minors.append(f"Minor {i + 1}")

# Minor Requirements
minor_requirements = []
for i in range(20):
    minor_id = i + 1
    for j in range(random.randint(3, 7)):
        course_id = random.randint(1, 900)
        minor_requirements.append((minor_id, course_id))

# Concentrations
concentrations = []
for i in range(20):
    concentrations.append(f"Concentration {i + 1}")

# Concentration Requirements
concentration_requirements = []
for i in range(20):
    concentration_id = i + 1
    for j in range(random.randint(2, 5)):
        course_id = random.randint(1, 900)
        concentration_requirements.append((concentration_id, course_id))

## Major Requirements, Minors, and Concentrations code is the same

# Honors Program Requirements
honors_program_requirements = []
for i in range(20):
    program_id = i + 1
    for j in range(random.randint(2, 5)):
        course_id = random.randint(1, 900)
        if course_prereqs.get(course_id) is None or all(prereq in student_transcript_df[student_transcript_df["student_id"] == student_id]["course_id"].tolist() for prereq in course_prereqs[course_id]):
            honors_program_requirements.append((program_id, course_id))


# Students
students = []
for i in range(1, 2001):
    first_name = f"First Name {i}"
    last_name = f"Last Name {i}"
    email = f"email{i}@example.com"
    major_id = random.randint(1, 60)
    honors_program_id = random.choice([0] * 8 + list(range(1, 21)))
    transfer = random.choice([0, 1])
    gpa = round(random.uniform(2.0, 4.0), 2)
    
    # Calculate credits completed based on student's transcript
    transcript = student_transcript_df[student_transcript_df["student_id"] == i]
    credits_completed = transcript["credits"].sum()
    
    # Calculate credits required based on student's major
    major_credits_required = majors_df[majors_df["major_id"] == major_id]["credits_required"].iloc[0]
    
    # Add new column to students_df called credits_completed which is the total number of credits the student has completed
    students_df.at[i, "credits_completed"] = credits_completed
    
    # Only assign courses if it won't exceed credits required
    available_courses = courses_df[courses_df["credits"].between(1, 5)]
    available_courses = available_courses[available_courses["available_semesters"].apply(lambda x: "Spring" in x)]
    available_courses = available_courses[available_courses["majors_allowed"].apply(lambda x: major_id in x)]
    available_courses = available_courses[available_courses["credits"].apply(lambda x: x + credits_completed <= major_credits_required)]
    
    for j in range(random.randint(3, 5)):
        if available_courses.empty:
            break
        course_id = random.choice(available_courses["course_id"])
        available_courses = available_courses[available_courses["course_id"] != course_id]
        
        section = sections_df[(sections_df["course_id"] == course_id) & (sections_df["semester"] == "Spring")]
        if section.empty:
            continue
        
        section_id = section["section_id"].iloc[0]
        semester_credits = section["credits"].iloc[0]
        grade = random.choice([None] * 4 + ["A", "B", "C", "D", "F"])
        if credits_completed + semester_credits > major_credits_required:
            continue
        
        student_current_semester_registration.append((i, section_id, semester_credits, grade))
    
    # Add new column to students_df called credits_completed which is the total number of credits the student has completed
    students_df.at[i, "credits_completed"] = credits_completed + sum([registration[2] for registration in student_current_semester_registration if registration[0] == i])
    
    # Add new column to students_df called credits_required which is the total number of credits required for the major
    students_df.at[i, "credits_required"] = major_credits_required
    
    # Add row to students list
    classification = None
    credits_taken = credits_completed + sum([registration[2] for registration in student_current_semester_registration if registration[0] == i])
    if credits_taken >= 90:
        classification = "Senior"
    elif credits_taken >= 60:
        classification = "Junior"
    elif credits_taken >= 30:
        classification = "Sophomore"
    else:
        classification = "Freshman"
    students.append((first_name, last_name, email, major_id, honors_program_id, transfer, gpa, credits_taken, classification, credits_completed))

#Professors
professors = []
for i in range(1, 301):
    first_name = f"First Name {i}"
    last_name = f"Last Name {i}"
    email = f"email{i}@example.com"
    professors.append((first_name, last_name, email))
print(professors)

#Admins
admins = [("Admin", "Admin", "admin@example.com")]


# Semester months
semesters = {
    "Fall": range(8, 13),
    "Spring": range(1, 5),
    "Summer": range(5, 8)
}

# Sections
sections = []

# Get current semester and year
now = datetime.datetime.now()
for i in range(400):
    while True:
        # Choose a random semester
        semester = random.choice(list(semesters.keys()))
        # Check if the current month is within the range of the chosen semester
        if now.month in semesters[semester]:
            year = now.year if semester != "Fall" else now.year + 1
            break

    # Choose an existing course_id and get its credits and major/honors program restrictions
    available_courses = courses_df[courses_df.available_semesters.apply(lambda x: semester in x)]
    if available_courses.empty:
        continue
    row = available_courses.sample()
    course_id = row.iloc[0]['course_id']
    credits = random.randint(1, 4)
    if credits is None:
        continue

    # Choose an existing professor_id and get their name
    professor_id = random.choice(professors_df['professor_id'])

    # Check if the student's major and honors program are allowed to take the course
    student_id = i % len(students_df) + 1
    major_id = students_df[students_df.index == student_id]['major_id'].iloc[0]
    honors_program_id = students_df[students_df.index == student_id]['honors_program_id'].iloc[0]
    majors_allowed = majors_df[majors_df.index == major_id]['courses_allowed'].iloc[0]
    honors_programs_allowed = honors_programs_df[honors_programs_df.index == honors_program_id]['courses_allowed'].iloc[0]
    if majors_allowed is None or honors_programs_allowed is None:
        continue

    # Check if all prerequisites are passed by the student
    prerequisites = row.iloc[0]['prerequisites']
    all_prerequisites_passed = True
    for prerequisite_id in prerequisites:
        prerequisite_course = courses_df[courses_df.course_id == prerequisite_id]
        if prerequisite_course.empty:
            continue
        passed = False
        for registration in student_current_semester_registration_df[student_current_semester_registration_df["student_id"] == student_id].values.tolist():
            if registration[1] == prerequisite_course.iloc[0]['course_id']:
                if registration[3] in ["A", "B", "C", "D"]:
                    passed = True
                break
        if not passed:
            all_prerequisites_passed = False
            break

    if not all_prerequisites_passed:
        continue

    # Compute section start time and end time based on credits
    start_hour = random.randint(8, 12)
    start_minute = random.choice([0, 30])
    end_hour = start_hour + credits
    end_minute = start_minute
    if end_hour >= 24:
        end_hour -= 12
        semester = "Spring" if semester == "Fall" else "Fall"
        year += 1

    section_number = i + 1
    start_time = f"{start_hour}:{start_minute:02d}:00"
    end_time = f"{end_hour}:{end_minute:02d}:00"
    room_number = f"Room {random.randint(1, 100)}"

    # Get credits required for major and completed by student
    credits_required = majors_df[majors_df.index == major_id]['credits_required'].iloc[0]
    credits_completed = student_transcript_df[student_transcript_df["student_id"] == student_id]['credits'].sum()

    # Only assign course to student if it will not exceed their credit requirements
    if credits_completed + credits > credits_required:
    

        # Add section to list of sections
        section = {
            'section_number': section_number,
            'course_id': course_id,
            'professor_id': professor_id,
            'semester': semester,
            'year': year,
            'start_time': start_time,
            'end_time': end_time,
            'room_number': room_number
        }
        sections.append(section)

        # Add section to student's current semester registration
        registration = {
            'student_id': student_id,
            'section_number': section_number,
            'course_id': course_id,
            'credits': credits,
            'grade': None
        }
        student_current_semester_registration_df = student_current_semester_registration_df.append(registration, ignore_index=True)




# Student Current Semester Registration
student_current_semester_registration = []
for student in students:
    student_id = students.index(student) + 1
    credits_completed = student_transcript_df[student_transcript_df["student_id"] == student_id]["credits"].sum()
    credits_required = majors_df[majors_df.index == student["major_id"]]["credits_required"].iloc[0]
    available_credits = credits_required - credits_completed
    if available_credits > 0:
        for i in range(random.randint(3, 5)):
            available_courses = courses_df[courses_df.credits.between(1, available_credits)]
            if available_courses.empty:
                break
            row = available_courses.sample()
            course_id = row.iloc[0]['course_id']
            section_id = sections_df[(sections_df.course_id == course_id) & (sections_df.semester == "Spring")]["section_number"].iloc[0]
            semester_credits = row.iloc[0]['credits']
            if credits_completed + semester_credits > credits_required:
                break
            grade = random.choice([None] * 4 + ["A", "B", "C", "D", "F"])
            student_current_semester_registration.append((student_id, section_id, semester_credits, grade))


#Student Minors
student_minors = []
for student in students:
    student_id = students.index(student) + 1
minor_id = random.randint(1, 20)
student_minors.append((student_id, minor_id))
print(student_minors)

#Student Concentrations
student_concentrations = []
for student in students:
    student_id = students.index(student) + 1
concentration_id = random.randint(1, 20)
student_concentrations.append((student_id, concentration_id))
print(student_concentrations)

# Student Transcript
student_transcript = []
for student in students:
    student_id = students.index(student) + 1
    section_id = None
    for registration in student_current_semester_registration:
        if registration[0] == student_id:
            section_id = registration[1]
    if section_id is not None:
        course_id = sections[section_id - 1][0]
        grade = registration[3]
        if grade:
            student_transcript.append((student_id, course_id, grade))
    for minor in student_minors:
        if minor[0] == student_id:
            minor_id = minor[1]
            for req in minor_requirements:
                if req[0] == minor_id:
                    course_id = req[1]
                    grade = random.choice(["A", "B", "C", "D", "F"])
                    student_transcript.append((student_id, course_id, grade))
    for concentration in student_concentrations:
        if concentration[0] == student_id:
            concentration_id = concentration[1]
            for req in concentration_requirements:
                if req[0] == concentration_id:
                    course_id = req[1]
                    grade = random.choice(["A", "B", "C", "D", "F"])
                    student_transcript.append((student_id, course_id, grade))


#Convert data into pandas dataframes
schools_df = pd.DataFrame(schools, columns=["name"])
honors_programs_df = pd.DataFrame(honors_programs, columns=["name"])
majors_df = pd.DataFrame(majors, columns=["name"])
courses_df = pd.DataFrame(courses, columns=["name", "description", "credits", "quota", "major_only", "honors_only","prerequisites"])
course_prerequisites_df = pd.DataFrame(course_prerequisites, columns=["course_id", "prerequisite_id"])
major_requirements_df = pd.DataFrame(major_requirements, columns=["major_id", "course_id"])
minors_df = pd.DataFrame(minors, columns=["name"])
minor_requirements_df = pd.DataFrame(minor_requirements, columns=["minor_id", "course_id"])
concentrations_df = pd.DataFrame(concentrations, columns=["name"])
concentration_requirements_df = pd.DataFrame(concentration_requirements, columns=["concentration_id", "course_id"])
honors_program_requirements_df = pd.DataFrame(honors_program_requirements, columns=["program_id", "course_id"])
students_df = pd.DataFrame(students, columns=["first_name", "last_name", "email", "major_id", "honors_program_id", "transfer", "gpa", "credits_taken", "classification"])
professors_df = pd.DataFrame(professors, columns=["first_name", "last_name", "email"])
admins_df = pd.DataFrame(admins, columns=["first_name", "last_name", "email"])
sections_df = pd.DataFrame(sections, columns=["course_id", "professor_id", "semester", "year", "section_number", "start_time", "end_time", "room_number"])
student_current_semester_registration_df = pd.DataFrame(student_current_semester_registration, columns=["student_id", "section_id", "semester_credits", "grade"])
student_minors_df = pd.DataFrame(student_minors, columns=["student_id", "minor_id"])
student_concentrations_df = pd.DataFrame(student_concentrations, columns=["student_id", "concentration_id"])
student_transcript_df = pd.DataFrame(student_transcript, columns=["student_id", "course_id", "grade"])




# Export dataframes as Excel xlsx files
schools_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/schools.xlsx", index=False)
honors_programs_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/honors_programs.xlsx", index=False)
majors_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/majors.xlsx", index=False)
courses_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/courses.xlsx", index=False)
course_prerequisites_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/course_prerequisites.xlsx", index=False)
major_requirements_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/major_requirements.xlsx", index=False)
minors_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/minors.xlsx", index=False)
minor_requirements_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/minor_requirements.xlsx", index=False)
concentrations_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/concentrations.xlsx", index=False)
concentration_requirements_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/concentration_requirements.xlsx", index=False)
honors_program_requirements_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/honors_program_requirements.xlsx", index=False)
students_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/students.xlsx", index=False)
professors_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/professors.xlsx", index=False)
admins_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/admins.xlsx", index=False)
sections_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/sections.xlsx", index=False)
student_current_semester_registration_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/student_current_semester_registration.xlsx", index=False)
student_minors_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/student_minors.xlsx", index=False)
student_concentrations_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/student_concentrations.xlsx", index=False)
student_transcript_df.to_excel("/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/student_transcript.xlsx", index=False)







