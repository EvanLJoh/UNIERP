import pandas as pd



# Define the non-major requirements
non_major_reqs = [("First Year Seminar", 4), ("Writing Seminar", 4), ("Lab Science", 8),("Quantitative Reasoning", 4),
                   ("Humanities", 4), ("Social Sciences", 4),("Foreign Language", 4), ("Fine Arts", 4), ("Diversity Studies", 4),("Physical Education", 2)]

# Define the school requirements
school_reqs = {
    
    "School of Business": [("Introduction to Accounting", 4), ("Introduction to Economics", 4), ("Introduction to Finance", 4), ("Introduction to Marketing", 4)],

    "School of Engineering": [("Introduction to Engineering", 4), ("Engineering Mathematics", 8),("Physics for Scientists and Engineers", 8)],

    "School of Arts and Sciences": [("Introduction to Psychology", 4), ("Introduction to Sociology", 4),("Introduction to Philosophy", 4), ("Introduction to History", 4)],
    
    "School of Nursing": [("Anatomy and Physiology", 4), ("Fundamentals of Nursing", 4),("Pharmacology", 4), ("Medical-Surgical Nursing", 4)],

    "School of Education": [("Educational Psychology", 4), ("Instructional Design", 4),("Teaching Methods", 4), ("Classroom Management", 4)],

    "School of Law": [("Introduction to Law", 4), ("Legal Research and Writing", 4),("Constitutional Law", 4), ("Civil Procedure", 4)],

    "School of Communications": [("Media and Society", 4), ("Writing for Mass Media", 4), ("Public Relations Principles and Practices", 4), ("Digital Media Production", 4)],
    
    "School of Public Health": [("Epidemiology", 4), ("Biostatistics", 4),("Environmental Health", 4), ("Global Health", 4)],

    "School of Social Work": [("Introduction to Social Work", 4), ("Human Behavior and the Social Environment", 4),("Social Work Research Methods", 4), ("Social Policy and Advocacy", 4)],

    "School of Hospitality Management": [("Introduction to Hospitality and Tourism Management", 4), ("Food and Beverage Operations Management", 4),("Hotel and Resort Management", 4), ("Event Planning and Management", 4)],

    "School of Environmental Science": [("Environmental Science Fundamentals", 4), ("Natural Resource Management", 4),("Environmental Policy and Law", 4), ("Environmental Geology", 4)]
}
    


# Define the major requirements
major_reqs = {
    "Accounting": [("Intermediate Accounting I", 4), ("Intermediate Accounting II", 4),
                   ("Advanced Accounting", 4), ("Auditing", 4)],

    "Biology": [("General Biology I", 4), ("General Biology II", 4), ("Cell Biology", 4),
                ("Genetics", 4), ("Ecology", 4), ("Evolutionary Biology", 4)],

    "Business Administration": [("Business Ethics", 4), ("Organizational Behavior", 4),
                                ("Operations Management", 4), ("Strategic Management", 4)],

    "Chemistry": [("General Chemistry I", 4), ("General Chemistry II", 4), ("Organic Chemistry I", 4),
                  ("Organic Chemistry II", 4), ("Physical Chemistry I", 4), ("Physical Chemistry II", 4)],

    "Computer Science": [("Introduction to Programming", 4), ("Data Structures", 4),
                         ("Computer Organization and Assembly Language", 4), ("Operating Systems", 4)],

    "Criminal Justice": [("Introduction to Criminal Justice", 4), ("Criminology", 4),
                         ("Criminal Law and Procedure", 4), ("Corrections", 4)],

    "Economics": [("Intermediate Microeconomics", 4), ("Intermediate Macroeconomics", 4),
                  ("Econometrics", 4), ("Public Finance", 4)],

    "Education": [("Child Development", 4), ("Curriculum and Instruction", 4),
                  ("Educational Psychology", 4), ("Educational Technology", 4)],

    "Electrical Engineering": [("Circuits and Electronics", 4), ("Signals and Systems", 4),
                               ("Digital Systems Design", 4), ("Power Systems", 4)],

    "English": [("Introduction to Literature", 4), ("Creative Writing", 4),
                ("British Literature to 1800", 4), ("American Literature to 1865", 4)],

    "Environmental Science": [("Environmental Chemistry", 4), ("Ecology", 4),
                              ("Environmental Policy and Law", 4), ("Environmental Science Capstone", 4)],

    "Finance": [("Financial Markets and Institutions", 4), ("Investment Analysis", 4),  ("Corporate Finance", 4), ("Derivatives and Risk Management", 4)],

    "History": [("Western Civilization to 1648", 4), ("Western Civilization since 1648", 4), ("American History to 1865", 4), ("American History since 1865", 4)],
    
    "Information Technology": [("Database Management Systems", 4), ("Systems Analysis and Design", 4),  ("Web Development", 4), ("Networking and Data Communications", 4)],
    
    "Management": [("Human Resource Management", 4), ("International Business", 4),  ("Small Business Management", 4), ("Entrepreneurship", 4)],
    
    "Marketing": [("Consumer Behavior", 4), ("Marketing Research", 4), ("Marketing Strategy and Planning", 4), ("Digital Marketing", 4)],
   
    "Mathematics": [("Calculus I", 4), ("Calculus II", 4), ("Linear Algebra", 4), ("Differential Equations", 4), ("Abstract Algebra", 4), ("Real Analysis", 4)],
   
    "Mechanical Engineering": [("Statics", 4), ("Dynamics", 4), ("Thermodynamics", 4), ("Fluid Mechanics", 4)],
    
    "Music": [("Music Theory I", 4), ("Music Theory II", 4), ("Aural Skills I", 4),("Aural Skills II", 4), ("Music History I", 4), ("Music History II", 4)],
  
    "Nursing": [("Fundamentals of Nursing", 4), ("Health Assessment", 4), ("Medical-Surgical Nursing I", 4), ("Medical-Surgical Nursing II", 4)],
   
    "Philosophy": [("Introduction to Ethics", 4), ("Introduction to Philosophy", 4), ("Symbolic Logic", 4), ("Philosophy of Religion", 4)],
    
    "Physics": [("General Physics I", 4), ("General Physics II", 4), ("Modern Physics", 4), ("Electromagnetic Theory", 4), ("Quantum Mechanics", 4)],
   
    "Political Science": [("Introduction to American Government", 4), ("Introduction to Comparative Politics", 4),("International Relations", 4), ("Political Theory", 4)],
    
    "Psychology": [("Introduction to Psychology", 4), ("Abnormal Psychology", 4), ("Social Psychology", 4), ("Cognitive Psychology", 4)],
    
    "Public Health": [("Introduction to Public Health", 4), ("Epidemiology", 4),("Global Health Issues", 4), ("Public Health Capstone", 4)],
   
    "Social Work": [("Introduction to Social Work", 4), ("Social Work Practice I", 4), ("Social Work Practice II", 4), ("Social Welfare Policy and Services", 4)],
    
    "Sociology": [("Introduction to Sociology", 4), ("Social Inequality", 4), ("Social Psychology", 4), ("Sociological Theory", 4)],
   
    "Statistics": [("Introduction to Statistics", 4), ("Statistical Methods I", 4),("Statistical Methods II", 4), ("Applied Regression Analysis", 4)],
    
    "Theater": [("Introduction to Theater", 4), ("Acting I", 4), ("Technical Theater", 4), ("Theater History and Literature", 4)],
    
    "Visual Arts": [("Drawing I", 4), ("Painting I", 4), ("Sculpture I", 4),("Photography I", 4), ("Visual Arts Capstone", 4)],


    }




# Define a function to sort the classes by priority
def sort_classes(classes):
    # Define a function to calculate the priority of a class
    def get_priority(cls):
        # Get the number of time slots the class is offered
        num_time_slots = len(cls["time_slots"])
        # Get the number of time slots the class overlaps with other classes
        num_overlaps = 0
        for other_cls in classes:
            if other_cls != cls:
                if len(set(cls["time_slots"]).intersection(set(other_cls["time_slots"]))) > 0:
                    num_overlaps += 1
        # Return the priority score
        return num_time_slots + num_overlaps

    # Sort the classes by priority
    return sorted(classes, key=get_priority)

# Define a function to create a schedule for a list of classes
def create_schedule(classes):
    # Sort the classes by priority
    sorted_classes = sort_classes(classes)
    # Initialize the schedule
    schedule = []
    # Loop through each class
    for cls in sorted_classes:
        # If the class does not overlap with any existing classes in the schedule, add it
        if all(len(set(cls["time_slots"]).intersection(set(existing_cls["time_slots"]))) == 0 for existing_cls in schedule):
            schedule.append(cls)
    # Return the schedule
    return schedule




# Save the requirements to an Excel file
df = pd.DataFrame({
    'Requirement': ['Non-Major'] * len(non_major_reqs) + \
                   ['School of Business'] * len(school_reqs['School of Business']) + \
                   ['School of Engineering'] * len(school_reqs['School of Engineering']) + \
                   ['School of Arts and Sciences'] * len(school_reqs['School of Arts and Sciences']) + \
                   ['School of Nursing'] * len(school_reqs['School of Nursing']) + \
                   ['School of Education'] * len(school_reqs['School of Education']) + \
                   ['School of Law'] * len(school_reqs['School of Law']) + \
                   ['School of Communications'] * len(school_reqs['School of Communications']) + \
                   ['School of Public Health'] * len(school_reqs['School of Public Health']) + \
                   ['School of Social Work'] * len(school_reqs['School of Social Work']) + \
                   ['School of Hospitality Management'] * len(school_reqs['School of Hospitality Management']) + \
                   ['School of Environmental Science'] * len(school_reqs['School of Environmental Science']) + \
                   list(major_reqs.keys()),
    'Major': [''] * (len(non_major_reqs) + sum(len(val) for val in school_reqs.values())) + \
             list(major_reqs.keys()),
    'Course': [req[0] for req in non_major_reqs] + \
              [req[0] for req in school_reqs['School of Business']] + \
              [req[0] for req in school_reqs['School of Engineering']] + \
              [req[0] for req in school_reqs['School of Arts and Sciences']] + \
              [req[0] for req in school_reqs['School of Nursing']] + \
              [req[0] for req in school_reqs['School of Education']] + \
              [req[0] for req in school_reqs['School of Law']] + \
              [req[0] for req in school_reqs['School of Communications']] + \
              [req[0] for req in school_reqs['School of Public Health']] + \
              [req[0] for req in school_reqs['School of Social Work']] + \
              [req[0] for req in school_reqs['School of Hospitality Management']] + \
              [req[0] for req in school_reqs['School of Environmental Science']] + \
              [req[0] for reqs in major_reqs.values() for req in reqs],
              
    'Credits': [req[1] for req in non_major_reqs] + \
               [req[1] for req in school_reqs['School of Business']] + \
               [req[1] for req in school_reqs['School of Engineering']] + \
               [req[1] for req in school_reqs['School of Arts and Sciences']] + \
               [req[1] for req in school_reqs['School of Nursing']] + \
               [req[1] for req in school_reqs['School of Education']] + \
               [req[1] for req in school_reqs['School of Law']] + \
               [req[1] for req in school_reqs['School of Communications']] + \
               [req[1] for req in school_reqs['School of Public Health']] + \
               [req[1] for req in school_reqs['School of Social Work']] + \
               [req[1] for req in school_reqs['School of Hospitality Management']] + \
               [req[1] for req in school_reqs['School of Environmental Science']] + \
               [req[1] for reqs in major_reqs.values() for req in reqs] +

                })

                

#Save the dataframe to an Excel file
path = "/Applications/XAMPP/xamppfiles/htdocs/SAD ASSIGMENTS/Group Project/SQL/1Database SQL/Inserts/excel data/requirements.xlsx"
df.to_excel(path, index=False)