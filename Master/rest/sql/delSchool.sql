DELIMITER //
DROP PROCEDURE IF EXISTS delSchool //

CREATE PROCEDURE delSchool(IN schoolIdIn int)
BEGIN
   DELETE
      FROM schools
      WHERE SchoolId = schoolIdIn;
END//
DELIMITER ;
