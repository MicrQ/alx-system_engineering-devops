# 0x14-mysql

On this project I installed MySQL 5.7.x on my web-01 and web-02 servers. to do so, use the following <a href="https://docs.google.com/document/d/1btVRofXP75Cj90_xq2x8AmzuMPOKq6D_Dt_SCDD6GrU/edit#heading=h.nu0sqigqw1o9">guideline</a>.

## Usage:
After installing MySQL server successfully, I created a user named `holberton_user` with the password `projectcorrection280hbtn` and given the permission to the ALX checker to access the replication status on both servers.<br><br>
To create the user and grant the permission, I wrote the script <a href="https://github.com/MicrQ/alx-system_engineering-devops/blob/master/0x14-mysql/user4Checker.sh">user4Checker.sh</a>. The can execute it on your server as the follow:
`cat path/user4Checker.sh | sudo mysql`.
You can check the permission of the user by running `mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"` and enter the password of the created user.<br><br>
In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from. 
The script <a href="https://github.com/MicrQ/alx-system_engineering-devops/blob/master/0x14-mysql/createDatabase.sh">createDatabase.sh</a> creates a database named `tyrell_corp` and a table `nexus6` in the database. It also grants the user 'holberton_user' a select permission.<br>
To check if the user `holberton_user` have the permission to select, run: `mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"` on web-01.<br><br>