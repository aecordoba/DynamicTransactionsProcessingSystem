DROP DATABASE IF EXISTS dtps;
DROP ROLE IF EXISTS dtpsapp;

-- -----------------------------------------------------
-- Database dtps
-- -----------------------------------------------------
CREATE DATABASE dtps;

-- -----------------------------------------------------
-- Role
-- -----------------------------------------------------
CREATE ROLE dtpsapp WITH LOGIN PASSWORD 'dtpsapp123';
GRANT ALL PRIVILEGES ON DATABASE dtps TO dtpsapp;
\c dtps

-- -----------------------------------------------------
-- Tables
-- -----------------------------------------------------

CREATE TABLE Job_Status(
    id SERIAL PRIMARY KEY,
    name VARCHAR(15) NOT NULL
);

CREATE TABLE Tasks(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    package VARCHAR(30) NOT NULL,
    module VARCHAR(30) NOT NULL
);

CREATE TABLE Jobs(
    id SERIAL PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL,
    task INT NOT NULL,
    status INT NOT NULL,
    CONSTRAINT fk_jobs_tasks FOREIGN KEY (task) REFERENCES Tasks(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_jobs_job_status FOREIGN KEY (status) REFERENCES Job_Status(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Data(
    job SERIAL NOT NULL,
    arg_order INT NOT NULL,
    data VARCHAR(50) NOT NULL,
    CHECK (arg_order > 0),
    PRIMARY KEY (job, arg_order),
    CONSTRAINT fk_data_jobs FOREIGN KEY (job) REFERENCES Jobs(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Jobs_History(
    id SERIAL PRIMARY KEY,
    job INT NOT NULL,
    status INT NOT NULL,
    time TIMESTAMP NOT NULL,
    CONSTRAINT fk_jobs_history_jobs FOREIGN KEY (job) REFERENCES Jobs(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_job_history_job_status FOREIGN KEY (status) REFERENCES Job_Status(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

GRANT ALL ON ALL TABLES IN SCHEMA public TO dtpsapp;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO dtpsapp;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public TO dtpsapp;
