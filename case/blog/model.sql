-- https://codeshack.io/login-system-python-flask-mysql/

CREATE DATABASE IF NOT EXISTS `blog` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `blog`;

-- tabel users/ authors 
CREATE TABLE IF NOT EXISTS `authors` (
	`id_author` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id_author`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `authors` (`id_author`, `username`, `password`, `email`) VALUES (1, 'admin', '12345', 'admin@gmail.com');


-- table category 
CREATE TABLE IF NOT EXISTS `categories` (
	`id_cat` int(11) NOT NULL AUTO_INCREMENT,
  	`name_cat` varchar(50) NOT NULL,
    PRIMARY KEY (`id_cat`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `categories` (`name_cat`) VALUES 
('Teknologi'),
('Politik'),
('Olahraga'),
('Otomatif');

-- table articles
CREATE TABLE IF NOT EXISTS `articles` (
	`id_art` int(11) NOT NULL AUTO_INCREMENT,
  	`title` varchar(50) NOT NULL,
	`description` text NOT NULL,
  	`datetime` datetime NOT NULL,
  	`author` int(11) NOT NULL,
	`category` int(11) NOT NULL,
	FOREIGN KEY(author) REFERENCES authors(id_author),
    FOREIGN KEY(category) REFERENCES categories(id_cat),
    PRIMARY KEY (`id_art`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
