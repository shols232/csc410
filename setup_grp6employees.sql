-- Drop any existing database and re-create it.
CREATE DATABASE IF NOT EXISTS grp6employee;
USE grp6employee;

-- Drop and re-create the grp6employees table.
DROP TABLE IF EXISTS grp6employees;
CREATE TABLE grp6employees (
    emp_no      INT             NOT NULL,
    birth_date  DATE            NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      ENUM('M','F')   NOT NULL,
    hire_date   DATE            NOT NULL,
    PRIMARY KEY (emp_no)
);