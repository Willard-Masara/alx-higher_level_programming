-- This script computes the average score of all records in the table second_table 
-- in the specified database on the MySQL server

-- The database name is passed as an argument to the MySQL command

-- Compute the average score from the second_table and set the result column name to 'average'
SELECT AVG(score) AS average
FROM hbtn_0c_0.second_table;
