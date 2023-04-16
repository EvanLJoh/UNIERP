
CREATE DATABASE UNIERPv3;

Use UNIERPv3;

CREATE TABLE schools (
school_id INT(11) NOT NULL AUTO_INCREMENT,
school_name VARCHAR(50) NOT NULL,
PRIMARY KEY (school_id)
);

CREATE TABLE honors_programs (
program_id INT(11) NOT NULL AUTO_INCREMENT,
program_name VARCHAR(50) NOT NULL,
school_id INT(11) NOT NULL,
PRIMARY KEY (program_id),
FOREIGN KEY (school_id) REFERENCES schools (school_id)
);

CREATE TABLE majors (
major_id INT(11) NOT NULL AUTO_INCREMENT,
major_name VARCHAR(50) NOT NULL,
major_credits_required INT(11) NOT NULL,
school_id INT(11) NOT NULL,
FOREIGN KEY (school_id) REFERENCES schools (school_id),
PRIMARY KEY (major_id)
);

CREATE TABLE courses (
  course_id INT AUTO_INCREMENT PRIMARY KEY,
  course_code VARCHAR(10) NOT NULL,
  course_name VARCHAR(255) NOT NULL,
  credits INT NOT NULL,
  major_only TINYINT DEFAULT 0, -- 0 means not restricted to specific major, 1 means restricted
  honors_only TINYINT DEFAULT 0, -- 0 means not restricted to honors program, 1 means restricted
  UNIQUE (course_code)
);

CREATE TABLE course_prerequisites (
course_id INT(11) NOT NULL,
prerequisite_id INT(11) NOT NULL,
PRIMARY KEY (course_id, prerequisite_id),
FOREIGN KEY (course_id) REFERENCES courses (course_id),
FOREIGN KEY (prerequisite_id) REFERENCES courses (course_id)
);

CREATE TABLE major_requirements (
major_requirement_id INT(11) NOT NULL AUTO_INCREMENT,
major_id INT(11) NOT NULL,
course_id INT(11) NOT NULL,
PRIMARY KEY (major_requirement_id),
FOREIGN KEY (major_id) REFERENCES majors (major_id),
FOREIGN KEY (course_id) REFERENCES courses (course_id)
);

CREATE TABLE minors (
minor_id INT(11) NOT NULL,
minor_name VARCHAR(50) NOT NULL,
PRIMARY KEY (minor_id)
);

CREATE TABLE minor_requirements (
minor_requirement_id INT(11) NOT NULL AUTO_INCREMENT,
minor_id INT(11) NOT NULL,
course_id INT(11) NOT NULL,
PRIMARY KEY (minor_requirement_id),
FOREIGN KEY (minor_id) REFERENCES minors (minor_id),
FOREIGN KEY (course_id) REFERENCES courses (course_id)
);

CREATE TABLE concentrations (
concentration_id INT(11) NOT NULL,
concentration_name VARCHAR(50) NOT NULL,
PRIMARY KEY (concentration_id)
);

CREATE TABLE concentration_requirements (
concentration_requirement_id INT(11) NOT NULL AUTO_INCREMENT,
concentration_id INT(11) NOT NULL,
course_id INT(11) NOT NULL,
PRIMARY KEY (concentration_requirement_id),
FOREIGN KEY (concentration_id) REFERENCES concentrations (concentration_id),
FOREIGN KEY (course_id) REFERENCES courses (course_id)
);

CREATE TABLE honors_program_requirement (
requirement_id INT(11) NOT NULL AUTO_INCREMENT,
program_id INT(11) NOT NULL,
course_id INT(11) NOT NULL,
PRIMARY KEY (requirement_id),
FOREIGN KEY (program_id) REFERENCES honors_programs (program_id),
FOREIGN KEY (course_id) REFERENCES courses (course_id)
);


CREATE TABLE students (
  student_id INT(11) NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  major_id INT(11) NOT NULL,
  honors_program_id INT(11) DEFAULT NULL,
  transfer TINYINT(1) NOT NULL,
  gpa FLOAT(3, 2) NOT NULL,
  credits_taken INT(11) NOT NULL,
  classification VARCHAR(50) NOT NULL,
  registration_pin VARCHAR(255) NOT NULL,
  FOREIGN KEY (major_id) REFERENCES majors (major_id),
  FOREIGN KEY (honors_program_id) REFERENCES honors_programs (program_id),
  PRIMARY KEY (student_id)
);



CREATE TABLE professors (
professor_id INT(11) NOT NULL AUTO_INCREMENT,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
PRIMARY KEY (professor_id)
);

CREATE TABLE admins (
admin_id INT(11) NOT NULL AUTO_INCREMENT,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
PRIMARY KEY (admin_id)
);


CREATE TABLE sections (
  section_id INT AUTO_INCREMENT PRIMARY KEY,
  course_id INT,
  professor_id INT,
  semester VARCHAR(50),
  year INT,
  section_number INT,
  start_time TIME,
  end_time TIME,
  room_number VARCHAR(50),
  capacity INT,
  days_of_week VARCHAR(50),
  building VARCHAR(50),
  FOREIGN KEY (course_id) REFERENCES courses(course_id),
  FOREIGN KEY (professor_id) REFERENCES professors(professor_id)
);






CREATE TABLE student_current_semester_registration (
registration_id INT(11) NOT NULL AUTO_INCREMENT,
student_id INT(11) NOT NULL,
section_id INT(11) NOT NULL,
semester_credits INT(11) NOT NULL DEFAULT 0,
grade VARCHAR(1) DEFAULT NULL,
PRIMARY KEY (registration_id),
FOREIGN KEY (student_id) REFERENCES students (student_id),
FOREIGN KEY (section_id) REFERENCES sections (section_id)
);

CREATE TABLE student_minors (
student_id INT(11) NOT NULL,
minor_id INT(11) NOT NULL,
PRIMARY KEY (student_id, minor_id),
FOREIGN KEY (student_id) REFERENCES students (student_id),
FOREIGN KEY (minor_id) REFERENCES minors (minor_id)
);

CREATE TABLE student_concentrations (
student_id INT(11) NOT NULL,
concentration_id INT(11) NOT NULL,
PRIMARY KEY (student_id, concentration_id),
FOREIGN KEY (student_id) REFERENCES students (student_id),
FOREIGN KEY (concentration_id) REFERENCES concentrations (concentration_id)
);


CREATE TABLE student_transcript (
transcript_id INT(11) NOT NULL AUTO_INCREMENT,
student_id INT(11) NOT NULL,
course_id INT(11) NOT NULL,
semester VARCHAR(50) NOT NULL,
year INT(11) NOT NULL,
grade VARCHAR(1) NOT NULL,
credits_earned INT(11) NOT NULL,
major_credits_earned INT(11) NOT NULL,
minor_credits_earned INT(11) NOT NULL,
concentration_credits_earned INT(11) NOT NULL,
honors_credits_earned INT(11) NOT NULL,
PRIMARY KEY (transcript_id),
FOREIGN KEY (student_id) REFERENCES students (student_id),
FOREIGN KEY (course_id) REFERENCES courses (course_id)
);

CREATE TABLE class_roster (
section_id INT(11) NOT NULL,
student_id INT(11) NOT NULL,
PRIMARY KEY (section_id, student_id),
FOREIGN KEY (section_id) REFERENCES sections (section_id),
FOREIGN KEY (student_id) REFERENCES students (student_id)
);


CREATE TABLE grade_reports (
student_id INT(11) NOT NULL,
section_id INT(11) NOT NULL,
grade VARCHAR(1) NOT NULL,
PRIMARY KEY (student_id, section_id),
FOREIGN KEY (student_id) REFERENCES students (student_id),
FOREIGN KEY (section_id) REFERENCES sections (section_id)
);











































