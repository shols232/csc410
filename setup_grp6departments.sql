-- Drop the existing database (if any) and create the new one.
CREATE DATABASE IF NOT EXISTS grp6employee;
USE grp6employee;

-- Drop the departments table if it exists.
DROP TABLE IF EXISTS grp6departments;

-- Create the grp6departments table.
CREATE TABLE grp6departments (
    dept_no     CHAR(4)     NOT NULL,
    dept_name   VARCHAR(40) NOT NULL,
    PRIMARY KEY (dept_no),
    UNIQUE KEY (dept_name)
);
