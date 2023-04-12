-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS data_stor_eng_dev_db;
CREATE USER IF NOT EXISTS 'data_stor_eng_dev'@'localhost' IDENTIFIED BY 'dse_dev_pwd';
GRANT ALL PRIVILEGES ON `data_stor_eng_dev_db`.* TO 'data_stor_eng_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'data_stor_eng_dev'@'localhost';
FLUSH PRIVILEGES;
