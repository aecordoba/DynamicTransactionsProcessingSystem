-- -----------------------------------------------------
-- Schema DTPS
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS DTPS ;
CREATE SCHEMA DTPS ;
USE DTPS;

-- -----------------------------------------------------
-- User
-- -----------------------------------------------------
CREATE OR REPLACE USER dtpsapp@localhost
    IDENTIFIED BY 'dtpsapp123';
GRANT ALL PRIVILEGES ON DTPS.* TO dtpsapp@localhost;
FLUSH PRIVILEGES;

-- -----------------------------------------------------
-- Tables
-- -----------------------------------------------------

CREATE OR REPLACE TABLE Job_Status(
    id INT PRIMARY KEY,
    name VARCHAR(15) NOT NULL
);

CREATE OR REPLACE TABLE Tasks(
    id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    package VARCHAR(30) NOT NULL,
    module VARCHAR(30) NOT NULL
);

CREATE OR REPLACE TABLE Jobs(
    id INT PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL,
    task INT NOT NULL,
    CONSTRAINT fk_tasks FOREIGN KEY (task) REFERENCES Tasks(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE OR REPLACE TABLE Data(
    job INT NOT NULL,
    arg_order INT NOT NULL,
    data VARCHAR(50) NOT NULL,
    CHECK (arg_order > 0),
    PRIMARY KEY (job, arg_order),
    CONSTRAINT fk_jobs1 FOREIGN KEY (job) REFERENCES Jobs(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE OR REPLACE TABLE Jobs_History(
    id INT PRIMARY KEY,
    job INT NOT NULL,
    status INT NOT NULL,
    time TIMESTAMP NOT NULL,
    CONSTRAINT fk_jobs2 FOREIGN KEY (job) REFERENCES Jobs(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_job_status FOREIGN KEY (status) REFERENCES Job_Status(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
