#!/bin/bash
# create_user.sh - Creates a dedicated MySQL user for the grp6employee database.

MYSQL_BIN="/usr/local/mysql/bin/mysql"

if [ ! -x "$MYSQL_BIN" ]; then
    echo "Error: MySQL client not found at $MYSQL_BIN."
    exit 1
fi

echo -n "Enter MySQL root password: "
read -s ROOT_PASS
echo ""

SQL_COMMANDS="
CREATE USER IF NOT EXISTS 'grp6user'@'%' IDENTIFIED BY 'grp6password';
GRANT ALL PRIVILEGES ON grp6employee.* TO 'grp6user'@'%';
FLUSH PRIVILEGES;
"

echo "Executing SQL commands..."
echo "$SQL_COMMANDS" | "$MYSQL_BIN" -u root -p"$ROOT_PASS"

if [ $? -eq 0 ]; then
    echo "User 'grp6user' created and granted privileges successfully on grp6employee."
else
    echo "Error: Failed to create user 'grp6user'."
    exit 1
fi