DROP DATABASE IF EXISTS users;
CREATE DATABASE users;
USE users;
DROP TABLE IF EXISTS user_info;
CREATE TABLE user_info(
id serial PRIMARY KEY,
user_login varchar(150) UNIQUE,
user_password varchar(15000),
INDEX user_login_idx(user_login)
);
