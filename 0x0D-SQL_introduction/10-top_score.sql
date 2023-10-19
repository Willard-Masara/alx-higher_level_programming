-- This script lists all records of the table second_table from the specified database on the MySQL server

-- The database name is passed as an argument to the MySQL command

-- Select score and name from the second_table, ordered by score (top first)
SELECT score, name
FROM hbtn_0c_0.second_table
ORDER BY score DESC;
