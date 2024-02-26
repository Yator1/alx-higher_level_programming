-- a script that lists all the cities of California hbtn_0d_usa DB

USE hbtn_0d_usa;

SET @state_id = (SELECT id FROM states WHERE name = California);

SELECT cities.*
FROM cities, states
WHERE cities.state_id = @state_id
AND state.name = California
ORDER BY cities.id ASC;
