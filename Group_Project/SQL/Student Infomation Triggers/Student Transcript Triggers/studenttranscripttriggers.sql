




/*updates the student's credits_taken and 
GPA whenever a new grade is added to the transcript. */

DELIMITER //
CREATE TRIGGER update_student_transcript
AFTER INSERT ON student_transcript
FOR EACH ROW
BEGIN
  UPDATE students SET credits_taken = credits_taken + NEW.credits_earned, gpa = (gpa * credits_taken + NEW.grade * NEW.credits_earned) / (credits_taken + NEW.credits_earned) WHERE student_id = NEW.student_id;
END;

DELIMITER ;