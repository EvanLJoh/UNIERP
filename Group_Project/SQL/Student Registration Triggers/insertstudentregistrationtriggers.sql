
/*Trigger to enforce Student pre-reqs*/
/*Trigger to check course quota:*/
/*Trigger to check major-only sections:*/
/*Trigger to check honors-only sections:*/







/* Trigger to enforce Student pre-reqs*/

DELIMITER //
CREATE TRIGGER check_prerequisites
BEFORE INSERT ON student_current_semester_registration
FOR EACH ROW
BEGIN
    DECLARE prereq_count INT;
    SET prereq_count = (SELECT COUNT(*) FROM course_prerequisites WHERE course_id = NEW.section_id);
    IF prereq_count > 0 THEN
        DECLARE completed_count INT;
        SET completed_count = (SELECT COUNT(*) FROM student_transcript WHERE student_id = NEW.student_id AND course_id IN (SELECT prerequisite_id FROM course_prerequisites WHERE course_id = NEW.section_id));
        IF completed_count < prereq_count THEN
            SIGNAL SQLSTATE '45000'
            SET MESSAGE_TEXT = 'Cannot register for section. Prerequisites not met.';
        END IF;
    END IF;
END;

DELIMITER;

/*Trigger to check course quota:*/
DELIMITER //
CREATE TRIGGER check_course_quota
BEFORE INSERT ON student_current_semester_registration
FOR EACH ROW
BEGIN
  DECLARE current_quota INT;
  DECLARE current_registrations INT;
  SELECT course_quota INTO current_quota FROM courses WHERE course_id = NEW.section_id;
  SELECT COUNT(*) INTO current_registrations FROM student_current_semester_registration WHERE section_id = NEW.section_id;
  IF current_registrations >= current_quota THEN
    SIGNAL SQLSTATE '45000' 
    SET MESSAGE_TEXT = 'Course quota has been reached.';
  END IF;
END //
DELIMITER ;



/*Trigger to check major-only sections:*/
DELIMITER //
CREATE TRIGGER check_major_only_sections
BEFORE INSERT ON student_current_semester_registration
FOR EACH ROW
BEGIN
  DECLARE section_major_id INT;
  DECLARE student_major_id INT;
  SELECT major_id INTO section_major_id FROM courses WHERE course_id = NEW.section_id;
  SELECT major_id INTO student_major_id FROM students WHERE student_id = NEW.student_id;
  IF section_major_id IS NOT NULL AND student_major_id IS NOT NULL AND section_major_id <> student_major_id THEN
    SIGNAL SQLSTATE '45000' 
    SET MESSAGE_TEXT = 'This is a major-only section and your major does not match.';
  END IF;
END //
DELIMITER ;


/*Trigger to check honors-only sections:*/
DELIMITER //
CREATE TRIGGER check_honors_only_sections
BEFORE INSERT ON student_current_semester_registration
FOR EACH ROW
BEGIN
  DECLARE section_honors_only INT;
  DECLARE student_honors_program_id INT;
  SELECT honors_only INTO section_honors_only FROM courses WHERE course_id = NEW.section_id;
  SELECT honors_program_id INTO student_honors_program_id FROM students WHERE student_id = NEW.student_id;
  IF section_honors_only = 1 AND student_honors_program_id = 0 THEN
    SIGNAL SQLSTATE '45000' 
    SET MESSAGE_TEXT = 'This is an honors-only section and you are not enrolled in an honors program.';
  END IF;
END //
DELIMITER ;


/*These triggers will be fired before an insertion 
is made to the student_current_semester_registration table,

The first trigger will check if the course quota has been reached for the section being registered 
and prevent the registration from being added if so. 

The second trigger will check if the section is marked 
as "major-only" and if the student's major matches the 
major associated with the section. 
If not, the registration will be prevented from being added. 

The third trigger will check if the section is marked 
as "honors-only" and if the student is enrolled in an 
honors program. If not, the registration will be prevented
 from being added.*/