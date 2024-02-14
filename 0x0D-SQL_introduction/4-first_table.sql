-- Creating 1st table with id and name parameter
-- the script should not fail if table exists

CREATE TABLE IF NOT EXISTS first_table(
	id INT,
	name VARCHAR(256)
	);
