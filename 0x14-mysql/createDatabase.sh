# this sql script create a database named 'tyrell_corp'
# a table named 'nexus6' in the above database and
# grants a select permission to the user 'holberton_user'
CREATE DATABASE IF NOT EXISTS tyrell_crop;
USE tyrell_crop;
CREATE TABLE IF NOT EXISTS nexus6(id int auto_increment primary key, name varchar(50));
INSERT INTO nexus6 (name) values ('Leon');
GRANT SELECT ON tyrell_crop.* TO 'holberton_user'@'localhost';
