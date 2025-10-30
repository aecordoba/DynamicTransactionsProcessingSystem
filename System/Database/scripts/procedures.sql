DELIMITER //

CREATE OR REPLACE PROCEDURE get_job_status_list()
    BEGIN
        SELECT * FROM Job_Status;
    END //


DELIMITER ;
