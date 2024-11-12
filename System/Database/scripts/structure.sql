CREATE DATABASE dtps;
CREATE USER dtpsapp WITH PASSWORD 'dtpsapp123';
ALTER DATABASE dtps OWNER TO dtpsapp;

CREATE TABLE IF NOT EXISTS Job_Status(
    id INT PRIMARY KEY,
    name VARCHAR(15) NOT NULL
);

CREATE TABLE IF NOT EXISTS Tasks(
    id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    package VARCHAR(30) NOT NULL,
    module VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS Jobs(
    id INT PRIMARY KEY,
    name VARCHAR(30) UNIQUE NOT NULL,
    task INT NOT NULL,
    CONSTRAINT fk_tasks FOREIGN KEY (task) REFERENCES Tasks(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Data(
    job INT NOT NULL,
    sequence INT NOT NULL,
    data VARCHAR(50) NOT NULL,
    CHECK (sequence > 0),
    PRIMARY KEY (job, sequence)
);

CREATE TABLE IF NOT EXISTS Jobs_History(
    id INT PRIMARY KEY,
    job INT NOT NULL,
    status INT NOT NULL,
    time TIMESTAMP NOT NULL,
    CONSTRAINT fk_jobs FOREIGN KEY (job) REFERENCES Jobs(id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT fk_job_status FOREIGN KEY (status) REFERENCES Job_Status(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
