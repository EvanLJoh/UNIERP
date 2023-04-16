/*Trigger to update the credits_taken field in the students table when a student registers for a course:*/
/*Trigger to update student's GPA */
/*Trigger to update major credits taken*/
/*Tigger to update honers credits earned*/
/*Trigger to update total credits earned*/



/*Trigger to update the credits_taken field 
in the students table when a student registers for a course:*/

DELIMITER //
CREATE TRIGGER update_credits_taken AFTER INSERT ON student_registration
FOR EACH ROW 
BEGIN
  UPDATE students
  SET credits_taken = credits_taken + NEW.semester_credits
  WHERE student_id = NEW.student_id;
END;
DELIMITER ;


/* Trigger to update student's GPA  */
DELIMITER //

CREATE TRIGGER update_student_gpa
AFTER INSERT ON student_transcript
FOR EACH ROW
BEGIN
  DECLARE total_credits INT;
  DECLARE total_grade_points FLOAT(3,2);
  SET total_credits = (SELECT SUM(credits_earned) FROM student_transcript WHERE student_id = NEW.student_id);
  SET total_grade_points = (SELECT SUM(CASE grade
        WHEN 'A' THEN 4.0
        WHEN 'B' THEN 3.0
        WHEN 'C' THEN 2.0
        WHEN 'D' THEN 1.0
        ELSE 0.0
        END * credits_earned) FROM student_transcript WHERE student_id = NEW.student_id);
 IF total_credits = 0 THEN
    SET NEW.gpa = 0.0;
  ELSE
    SET NEW.gpa = total_grade_points / total_credits;
  END IF;
END//

DELIMITER ;


/*Trigger to update major credits taken*/
DELIMITER //

CREATE TRIGGER update_major_credits
AFTER INSERT ON student_transcript
FOR EACH ROW
BEGIN
  UPDATE students SET credits_taken = credits_taken + NEW.credits_earned 
  WHERE student_id = NEW.student_id AND major_id = 
  (SELECT major_id FROM courses JOIN major_courses ON courses.course_id = major_courses.course_id 
  WHERE courses.course_id = NEW.course_id);
END//

DELIMITER ;


/*Tigger to update honers credits earned*/

DELIMITER //

CREATE TRIGGER update_honors_credits
AFTER INSERT ON student_transcript
FOR EACH ROW
BEGIN
  UPDATE students SET credits_taken = credits_taken + NEW.credits_earned 
  WHERE student_id = NEW.student_id AND honors_program_id = 
  (SELECT honors_program_id FROM courses WHERE courses.course_id = NEW.course_id AND honors_only = 1);
END//

DELIMITER ;


/*Trigger to update total credits earned*/
DELIMITER //

CREATE TRIGGER update_total_credits
AFTER INSERT ON student_transcript
FOR EACH ROW
BEGIN
  UPDATE students SET credits_taken = credits_taken + NEW.credits_earned 
  WHERE student_id = NEW.student_id;
END//

DELIMITER ;
