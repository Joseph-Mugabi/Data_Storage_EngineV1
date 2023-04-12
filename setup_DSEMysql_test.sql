-- Prepares a MySQL Server for the project

CREATE DATABASE IF NOT EXISTS data_stor_eng_test_db;
CREATE USER IF NOT EXISTS 'data_stor_eng_test'@'localhost' IDENTIFIED BY 'dse_test_pwd';
GRANT ALL PRIVILEGES ON `data_stor_eng_test_db`.* TO 'data_stor_eng_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'data_stor_eng_test'@'localhost';
FLUSH PRIVILEGES;
