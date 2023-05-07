-- https://codeshack.io/login-system-python-flask-mysql/

CREATE DATABASE IF NOT EXISTS `loginweb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `loginweb`;

CREATE TABLE IF NOT EXISTS `multiaccounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
	`level` int NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `multiaccounts` (`username`, `password`, `email`, `level`) VALUES ('admin', md5('12345'), 'admin@gmail.com',1);


-- level 
-- 1 : admin 
-- 2 : contributor