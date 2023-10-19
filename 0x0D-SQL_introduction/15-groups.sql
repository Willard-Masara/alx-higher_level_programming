-- This script lists the number of records with the same score in the table second_table
-- in the specified database on the MySQL server

-- The database name is passed as an argument to the MySQL command

-- Select score and count the number of records for each score, label the count as 'number'
SELECT score, COUNT(*) AS number
FROM hbtn_0c_0.second_table
GROUP BY score
ORDER BY number DESC;
