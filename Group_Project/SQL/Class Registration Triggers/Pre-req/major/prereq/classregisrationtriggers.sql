/*Trigger to add courses to major_requirements table when a course is added to a major:*/
/*Trigger to add courses to minor_requirements table when a course is added to a minor:*/
/*Trigger to add courses to concentration_requirements table when a course is added to a concentration:*/






/*Trigger to add courses to major_requirements table when a course is added to a major:*/

DELIMITER //
CREATE TRIGGER add_major_requirement AFTER INSERT ON major_courses
FOR EACH ROW 
BEGIN
  INSERT INTO major_requirements (major_id, course_id)
  VALUES (NEW.major_id, NEW.course_id);
END;

DELIMITER ;

/*Trigger to add courses to minor_requirements table when a course is added to a minor:*/

DELIMITER //
 TRIGGER add_minor_requirement AFTER INSERT ON minors
FOR EACH ROW 
BEGIN
  INSERT INTO minor_requirements (minor_id, course_id)
  VALUES (NEW.minor_id, NEW.course_id);
END;
DELIMITER ;



/*Trigger to  add courses to concentration_requirements table when a course is added to a concentration:*/

DELIMITER //

CREATE TRIGGER add_concentration_requirement AFTER INSERT ON concentration_courses
FOR EACH ROW 
BEGIN
  INSERT INTO concentration_requirements (concentration_id, course_id)
  VALUES (NEW.concentration_id, NEW.course_id);
END;
DELIMITER ;
