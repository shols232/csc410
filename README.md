# Query Router for Sharded MySQL

A CLI tool that routes SQL queries to the appropriate MySQL node based on the target table. In this sharded setup, each MySQL node hosts a single table from our schema. For example, one node may host the `grp6employees` table, another the `grp6departments` table, and another the `grp6salaries` table. The router uses the [sql-metadata](https://pypi.org/project/sql-metadata/) library to extract table names from queries and [mysql-connector-python](https://pypi.org/project/mysql-connector-python/) to connect and execute commands on MySQL servers.

## Prerequisites

- **MySQL Installation (macOS via DMG):**
  - Install MySQL from the [MySQL Community Downloads page](https://dev.mysql.com/downloads/mysql/).
  - Use the MySQL Preference Pane to start the server.
  - Create the database and corresponding table on each node:
    - **Server 1:** Hosts the `grp6employees` table.
    - **Server 2:** Hosts the `grp6departments` table.
    - **Server 3:** Hosts the `grp6salaries` table.
- **Dedicated Database User:**
  On every node, create a user (e.g., `grp6user` with password `grp6password`) and grant privileges on the `grp6employee` database:
  ```sql
  CREATE USER 'grp6user'@'%' IDENTIFIED BY 'grp6password';
  GRANT ALL PRIVILEGES ON grp6employee.* TO 'grp6user'@'%';
  FLUSH PRIVILEGES;
  ```

## Installation and Setup
  - Clone or Download the Source Files:
  - Update Configuration:
    - In config.py, replace the placeholder IP addresses (server1_ip, server2_ip, server3_ip) with your actual MySQL server IP addresses.

Set Up the MySQL Schema on Each Node:

Create the appropriate database and table on each node.
### Server 1 – grp6employees Table:
```sql
DROP DATABASE IF EXISTS grp6employee;
CREATE DATABASE grp6employee;
USE grp6employee;

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
```

### Server 2 – grp6departments Table:
```sql
DROP DATABASE IF EXISTS grp6employee;
CREATE DATABASE IF NOT EXISTS grp6employee;
USE grp6employee;

DROP TABLE IF EXISTS grp6departments;
CREATE TABLE grp6departments (
    dept_no     CHAR(4)         NOT NULL,
    dept_name   VARCHAR(40)     NOT NULL,
    PRIMARY KEY (dept_no),
    UNIQUE KEY (dept_name)
);
```


### Server 3 – grp6salaries Table:
```sql
DROP DATABASE IF EXISTS grp6employee;
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
```
Alternatively, we can use `mysql -u username -p < /path/to/sql/file` to load the data`

## How to Run
```bash
python3 query_router.py
```
Then input your queries. They should be routed to the appropriate database server.