-- -----------------------------------------------------
-- Job_History
-- -----------------------------------------------------

CREATE OR REPLACE FUNCTION jobs_history_update()
    RETURNS TRIGGER
    AS $$
BEGIN
    INSERT INTO Jobs_History(job, status, time)
        VALUES(NEW.id, NEW.status, now());
    RETURN NEW;
END;
$$ LANGUAGE PLPGSQL;

CREATE OR REPLACE TRIGGER jobs_history_update_trigger
    AFTER INSERT OR UPDATE
    ON Jobs
    FOR EACH ROW
    EXECUTE PROCEDURE jobs_history_update();

