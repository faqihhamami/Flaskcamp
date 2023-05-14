-- tabel users/ authors 
use loginweb;

CREATE TABLE IF NOT EXISTS `payment` (
	`id_payment` int(11) NOT NULL AUTO_INCREMENT,
	`name_payment` varchar(50) NOT NULL,
    PRIMARY KEY (`id_payment`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8

INSERT INTO `payment` (`name_payment`) VALUES 
('dana'),
('ovo'),
('gopay');

CREATE TABLE IF NOT EXISTS `_singletransaction` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`invoicenumber` varchar(50) NOT NULL,
  	`buyer` varchar(50) NOT NULL,
  	`payment` int NOT NULL,
	`total` int NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `_detailtransaction` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`invoicenumber` varchar(50) NOT NULL,
  	`product` int(10) NOT NULL,
  	`price` int NOT NULL,
	`qty` int NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `product` (
	`id_product` int(11) NOT NULL AUTO_INCREMENT,
	`name_product` varchar(50) NOT NULL,
    PRIMARY KEY (`id_product`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

INSERT INTO `product` (`name_product`) VALUES 
('Milo'),
('Coklat'),
('Susu'),
('Roti'),
('Aqua');