-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 19, 2021 at 11:44 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 7.4.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db`
--

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `bid` varchar(20) DEFAULT NULL,
  `title` varchar(30) DEFAULT NULL,
  `author` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`bid`, `title`, `author`, `status`) VALUES
('IDB123456', 'The Picture Of Dorian Gray', 'Oscar Wilde', 'avail'),
('IBD123457', 'Harry Potter', 'J.K Rowling', 'avail'),
('IBD1234510', 'Matilda ', 'Roahl dahl', 'avail');

-- --------------------------------------------------------

--
-- Table structure for table `book_issued`
--

CREATE TABLE `book_issued` (
  `bid` varchar(20) DEFAULT NULL,
  `issued_to` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `username` varchar(30) NOT NULL,
  `emailid` char(200) NOT NULL,
  `password` varchar(20) NOT NULL,
  `confirmpassword` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`username`, `emailid`, `password`, `confirmpassword`) VALUES
('aniketk', 'aniketkhetan@gmail.com', 'abcdefgh', 'abcdefgh'),
('jaykaria', 'jaykaria1289@gmail.com', 'abcdefgh', 'abcdefgh'),
('aashayk', 'aashaykhot03@gmail.com', 'abcdefgh', 'abcdefgh'),
('Preethirani', 'preethirani@gmail.id', 'abcdefgh', 'abcdefgh');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `sid` varchar(20) DEFAULT NULL,
  `name` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`sid`, `name`) VALUES
('70321019048', 'Aniket Khetan'),
('70321019049', 'Aashay Khot'),
('703311019014', 'Jay Karia'),
('70321019032', 'Preet Hirani');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
