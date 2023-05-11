-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 11, 2023 at 11:16 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `loginweb`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts`
--

CREATE TABLE `accounts` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `accounts`
--

INSERT INTO `accounts` (`id`, `username`, `password`, `email`) VALUES
(1, 'admin', '827ccb0eea8a706c4c34a16891f84e7b', 'admin@gmail.com'),
(4, 'ina', '827ccb0eea8a706c4c34a16891f84e7b', 'ina@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `detailtransaction`
--

CREATE TABLE `detailtransaction` (
  `id` int(11) NOT NULL,
  `invoicenumber` varchar(50) NOT NULL,
  `product` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `detailtransaction`
--

INSERT INTO `detailtransaction` (`id`, `invoicenumber`, `product`, `price`, `qty`) VALUES
(1, '19585794', 'eskrim', 5000, 2),
(2, '19585794', 'coklat', 10000, 3),
(3, '46591785', 'eskrim', 5000, 10),
(4, '46591785', 'susu', 10000, 2),
(5, '46591785', 'ciki', 1000, 5),
(6, '35333055', 'milo', 5000, 2),
(7, '35333055', 'susu', 10000, 5),
(8, '97630553', 'milo', 5000, 2),
(9, '97630553', 'coklat', 5000, 2),
(10, '26766772', 'milo', 5000, 1),
(11, '91493477', 'milo', 5000, 1),
(12, '92164897', 'milo', 5000, 3),
(13, '22629420', 'eskrim', 5000, 2),
(14, '12583691', 'milo', 5000, 4),
(15, '58784414', 'milo', 5000, 3),
(16, '58784414', 'coklat', 4000, 4);

-- --------------------------------------------------------

--
-- Table structure for table `multiaccounts`
--

CREATE TABLE `multiaccounts` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL,
  `level` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `multiaccounts`
--

INSERT INTO `multiaccounts` (`id`, `username`, `password`, `email`, `level`) VALUES
(2, 'admin', '827ccb0eea8a706c4c34a16891f84e7b', 'admin@gmail.com', 1),
(3, 'ina', '827ccb0eea8a706c4c34a16891f84e7b', 'ina@gmail.com', 2);

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id_payment` int(11) NOT NULL,
  `name_payment` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id_payment`, `name_payment`) VALUES
(2, 'dana'),
(3, 'ovo'),
(4, 'gopay');

-- --------------------------------------------------------

--
-- Table structure for table `singletransaction`
--

CREATE TABLE `singletransaction` (
  `id` int(11) NOT NULL,
  `invoicenumber` varchar(50) NOT NULL,
  `buyer` varchar(50) NOT NULL,
  `payment` int(11) NOT NULL,
  `total` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `singletransaction`
--

INSERT INTO `singletransaction` (`id`, `invoicenumber`, `buyer`, `payment`, `total`) VALUES
(2, '19585794', 'Faqih', 2, 40000),
(3, '46591785', 'Joni', 4, 75000),
(4, '35333055', 'Andi', 2, 60000),
(5, '97630553', 'dani', 2, 20000),
(6, '26766772', 'dani', 2, 5000),
(7, '91493477', 'dani', 2, 5000),
(8, '92164897', 'Faqih', 3, 15000),
(9, '22629420', 'Faqih', 3, 10000),
(10, '12583691', 'Faqih', 4, 20000),
(11, '58784414', 'Faqih', 4, 31000);

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `product` varchar(50) NOT NULL,
  `price` int(11) NOT NULL,
  `qty` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`id`, `product`, `price`, `qty`) VALUES
(1, 'milo', 4000, 2),
(2, 'milo', 4000, 2),
(3, 'milo', 4000, 2),
(4, 'eskrim', 4000, 5),
(5, 'coklat', 10000, 10),
(6, 'manisan', 2000, 5),
(7, '1', 2, 3),
(8, '4', 5, 6),
(9, 'sosis', 500, 4),
(10, 'sosis 2', 5000, 5),
(11, 'eskrim', 5000, 6),
(12, '1', 1, 1),
(13, '2', 2, 2),
(14, '3', 3, 3),
(15, 'ikan1', 500, 4),
(16, 'ikan2', 1000, 8),
(17, 'ikan3', 2000, 16),
(18, 'ikan4', 4000, 32);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts`
--
ALTER TABLE `accounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `detailtransaction`
--
ALTER TABLE `detailtransaction`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `multiaccounts`
--
ALTER TABLE `multiaccounts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id_payment`);

--
-- Indexes for table `singletransaction`
--
ALTER TABLE `singletransaction`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts`
--
ALTER TABLE `accounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `detailtransaction`
--
ALTER TABLE `detailtransaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `multiaccounts`
--
ALTER TABLE `multiaccounts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `id_payment` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `singletransaction`
--
ALTER TABLE `singletransaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
