-- This script displays the number of records with id=89 in the table first_table 
-- from the specified database on the MySQL server

-- The database name is passed as an argument to the MySQL command

-- Count the number of records with id=89 in the first_table
SELECT COUNT(*) AS record_count
FROM hbtn_0c_0.first_table
WHERE id = 89;
