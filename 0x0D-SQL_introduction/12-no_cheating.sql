-- This script updates the score of Bob to 10 in the table second_table 
-- based on the name field in the specified database on the MySQL server

-- The database name is passed as an argument to the MySQL command

-- Update the score of Bob to 10 in the second_table


UPDATE hbtn_0c_0.second_table
SET score = 10
WHERE name = 'Bob';
