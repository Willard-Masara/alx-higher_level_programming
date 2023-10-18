-- Convert the hbtn_0c_0 database, first_table table, and name field to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Alter the database collation


ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter the collation of the first_table table


ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Alter the collation of the name field in the first_table table


ALTER TABLE hbtn_0c_0.first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
