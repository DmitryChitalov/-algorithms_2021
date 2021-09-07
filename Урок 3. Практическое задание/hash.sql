DROP DATABASE IF EXISTS hash;
CREATE DATABASE hash;
USE hash;


DROP TABLE IF EXISTS passwords;
CREATE TABLE passwords (
    id SERIAL,
    password_hash VARCHAR(100) COMMENT 'Хэш пароля'
) COMMENT 'Хэш';
