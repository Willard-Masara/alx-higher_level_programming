-- This script lists records with both score and name from the table second_table
-- excluding rows without a name value, in the specified database on the MySQL server

-- The database name is passed as an argument to the MySQL command

-- Select score and name from second_table excluding rows without a name value, ordered by score (top first)
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
