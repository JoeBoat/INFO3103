DELIMITER //
DROP PROCEDURE IF EXISTS getSchoolById // 

CREATE PROCEDURE getSchoolById(IN schoolIdIn int)
BEGIN
   SELECT * 
      FROM schools
      WHERE SchoolId = schoolIdIn;
END//
DELIMITER ;
