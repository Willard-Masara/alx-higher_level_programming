-- This script prints the full description of the table first_table from the specified database on the MySQL server

-- The database name is passed as an argument to the MySQL command

-- Select the table information from the INFORMATION_SCHEMA database
-- to get the full description of the first_table


SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'hbtn_0c_0' AND TABLE_NAME = 'first_table';
