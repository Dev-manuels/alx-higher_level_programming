-- script that shows all the tables in a databases in a MySQL server
SET @database_name = IFNULL(ARGV[1], CURRENT_DATABASE());
SHOW TABLES FROM @database_name;
