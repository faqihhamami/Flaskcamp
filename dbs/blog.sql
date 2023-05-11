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
-- Database: `blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `articles`
--

CREATE TABLE `articles` (
  `id_art` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `description` text NOT NULL,
  `datetime` datetime NOT NULL,
  `author` int(11) NOT NULL,
  `category` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `articles`
--

INSERT INTO `articles` (`id_art`, `title`, `description`, `datetime`, `author`, `category`) VALUES
(3, 'berita dua', 'ini adalah berita kedua. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum repudiandae provident ullam ad harum autem repellendus, assumenda ipsum eius cupiditate soluta iure cum quia accusamus consequuntur at laborum! Culpa, magnam?', '2023-05-06 13:03:42', 1, 3),
(4, 'olahraga 45', 'ini adalah berita olahraga panahan 45. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum repudiandae provident ullam ad harum autem repellendus, assumenda ipsum eius cupiditate soluta iure cum quia accusamus consequuntur at laborum! Culpa, magnam?', '2023-05-06 13:04:09', 1, 2),
(5, 'judul empat 1', 'empat desc 1Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum repudiandae provident ullam ad harum autem repellendus, assumenda ipsum eius cupiditate soluta iure cum quia accusamus consequuntur at laborum! Culpa, magnam?', '2023-05-06 20:31:44', 1, 5),
(6, 'Judul 5', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum repudiandae provident ullam ad harum autem repellendus, assumenda ipsum eius cupiditate soluta iure cum quia accusamus consequuntur at laborum! Culpa, magnam?\r\nLorem ipsum dolor sit, amet consectetur adipisicing elit. Distinctio, explicabo. Exercitationem voluptate adipisci vel harum libero nulla ipsa dolore beatae, molestias magnam, repellendus, doloribus minus minima iure quaerat voluptas sint!', '2023-05-06 20:43:18', 1, 2),
(7, 'Judul 6', 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum repudiandae provident ullam ad harum autem repellendus, assumenda ipsum eius cupiditate soluta iure cum quia accusamus consequuntur at laborum! Culpa, magnam?', '2023-05-06 20:44:48', 1, 4),
(8, 'Presiden ke Lampung', 'lorem ipsum lampung jalan raya. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum repudiandae provident ullam ad harum autem repellendus, assumenda ipsum eius cupiditate soluta iure cum quia accusamus consequuntur at laborum! Culpa, magnam?', '2023-05-06 21:07:33', 2, 3),
(9, 'Flask python', 'artikel ini akan membahas tentang flask python. Lorem ipsum dolor sit amet consectetur, adipisicing elit. Eum repudiandae provident ullam ad harum autem repellendus, assumenda ipsum eius cupiditate soluta iure cum quia accusamus consequuntur at laborum! Culpa, magnam?', '2023-05-11 15:59:40', 1, 4);

-- --------------------------------------------------------

--
-- Table structure for table `authors`
--

CREATE TABLE `authors` (
  `id_author` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `authors`
--

INSERT INTO `authors` (`id_author`, `username`, `password`, `email`) VALUES
(1, 'admin', '827ccb0eea8a706c4c34a16891f84e7b', 'admin@gmail.com'),
(2, 'ina', '827ccb0eea8a706c4c34a16891f84e7b', 'ina@gmail.com'),
(3, 'toni', '827ccb0eea8a706c4c34a16891f84e7b', 'toni@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id_cat` int(11) NOT NULL,
  `name_cat` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id_cat`, `name_cat`) VALUES
(2, 'Teknologi'),
(3, 'Politik'),
(4, 'Olahraga'),
(5, 'Otomatif');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id_art`),
  ADD KEY `author` (`author`),
  ADD KEY `category` (`category`);

--
-- Indexes for table `authors`
--
ALTER TABLE `authors`
  ADD PRIMARY KEY (`id_author`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id_cat`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `articles`
--
ALTER TABLE `articles`
  MODIFY `id_art` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `authors`
--
ALTER TABLE `authors`
  MODIFY `id_author` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id_cat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `articles`
--
ALTER TABLE `articles`
  ADD CONSTRAINT `articles_ibfk_1` FOREIGN KEY (`author`) REFERENCES `authors` (`id_author`),
  ADD CONSTRAINT `articles_ibfk_2` FOREIGN KEY (`category`) REFERENCES `categories` (`id_cat`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
