-- script that creates the database hbtn_0d_usa and the table states
-- id INT unique, auto generated, can’t be null and is a primary key
-- name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    id INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
