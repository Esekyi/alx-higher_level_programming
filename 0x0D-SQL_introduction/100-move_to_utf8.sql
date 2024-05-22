-- Script to convert hbtn_0c_0 database and its components to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)

-- Convert the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert specific field in the table
ALTER TABLE first_table MODIFY name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
