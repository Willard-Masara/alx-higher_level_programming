-- This script removes all records with score <= 5 from the table second_table 
-- in the specified database on the MySQL server

-- The database name is passed as an argument to the MySQL command

-- Delete records with score <= 5 from the second_table
DELETE FROM hbtn_0c_0.second_table
WHERE score <= 5;
