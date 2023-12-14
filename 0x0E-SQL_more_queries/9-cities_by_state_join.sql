--
SELECT cities.id, cities.name, states.name
FROM states
LEFT JOIN cities
ON states.id = cities.state_id
ORDER BY cities.id;
