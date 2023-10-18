-- This script creates a table called first_table in the specified database on the MySQL server

-- The database name is passed as an argument to the MySQL command

-- Check if the table first_table exists
-- If the table does not exist, create it


CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
