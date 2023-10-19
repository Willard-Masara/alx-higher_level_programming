-- This script lists records with score >= 10 from the table second_table 
-- in the specified database on the MySQL server

-- The database name is passed as an argument to the MySQL command

-- Select score and name from second_table where score >= 10, ordered by score (top first)
SELECT score, name
FROM hbtn_0c_0.second_table
WHERE score >= 10
ORDER BY score DESC;
