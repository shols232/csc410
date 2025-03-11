CREATE USER 'grp6user'@'%' IDENTIFIED BY 'grp6password';
GRANT ALL PRIVILEGES ON grp6employee.* TO 'grp6user'@'%';
FLUSH PRIVILEGES;


-- /usr/local/mysql/bin/mysql -u root (Enter root and paste command)
