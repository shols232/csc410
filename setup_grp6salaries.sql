CREATE DATABASE IF NOT EXISTS grp6employee;
USE grp6employee;

DROP TABLE IF EXISTS grp6salaries;
CREATE TABLE grp6salaries (
    emp_no      INT         NOT NULL,
    salary      INT         NOT NULL,
    from_date   DATE        NOT NULL,
    to_date     DATE        NOT NULL,
    PRIMARY KEY (emp_no, from_date)
);
