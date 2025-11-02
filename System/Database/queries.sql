INSERT INTO tasks(name, package, module)
	VALUES('tarea', 'paquete', 'modulo');

INSERT INTO jobs(name, task, status)
	VALUES('trabajo', 
		(SELECT id FROM tasks WHERE name = 'tarea'),
		(SELECT id FROM job_status WHERE name = 'CREATED'));

SELECT * FROM jobs_history;

UPDATE jobs 
	SET status = (SELECT id FROM job_status WHERE name = 'INITIALIZING')
		WHERE name = 'trabajo';

SELECT * FROM jobs;