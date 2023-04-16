


/*updates the student's 
classification (freshman, sophomore, junior, senior) 
based on the number of credits 
they have taken.*/

CREATE TRIGGER update_student_classification
AFTER UPDATE ON student_transcript
FOR EACH ROW
BEGIN
  IF NEW.student_id = OLD.student_id AND NEW.credits_earned != OLD.credits_earned THEN
    IF NEW.credits_earned >= 90 THEN
      UPDATE students SET classification = 'Senior' WHERE student_id = NEW.student_id;
    ELSEIF NEW.credits_earned >= 60 THEN
      UPDATE students SET classification = 'Junior' WHERE student_id = NEW.student_id;
    ELSEIF NEW.credits_earned >= 30 THEN
      UPDATE students SET classification = 'Sophomore' WHERE student_id = NEW.student_id;
    ELSE
      UPDATE students SET classification = 'Freshman' WHERE student_id = NEW.student_id;
    END IF;
  END IF;
END;


