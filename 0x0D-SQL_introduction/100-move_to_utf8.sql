-- Script to convert hbtn_0c_0 database and its components to UTF8
-- Convert the database
USE hbtn_0c_0
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
