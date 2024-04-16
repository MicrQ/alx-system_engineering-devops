# this bash script create a user named 'holberton_user' with
# the hostname 'localhost' and password 'projectcorrection280hbtn'.
# it also has permission to check the primary/replica status of your databases.
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';