-- tabel users/ authors 
use loginweb;

CREATE TABLE IF NOT EXISTS `transaction` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`product` varchar(50) NOT NULL,
  	`price` int NOT NULL,
	`qty` int NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
