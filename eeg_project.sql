-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 25, 2024 at 09:10 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eeg_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `records`
--

CREATE TABLE `records` (
  `r_id` int(5) NOT NULL,
  `u_id` varchar(5) NOT NULL,
  `r_input1` varchar(50) NOT NULL,
  `r_input2` varchar(50) NOT NULL,
  `r_input3` varchar(50) NOT NULL,
  `r_ouput` varchar(50) NOT NULL,
  `r_dateCreated` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `records`
--

INSERT INTO `records` (`r_id`, `u_id`, `r_input1`, `r_input2`, `r_input3`, `r_ouput`, `r_dateCreated`) VALUES
(1, '1', '-0.090261483', '-0.293381731', '-0.78792476', '0', '2024-04-24 23:43:46'),
(2, '1', '1.271474206', '1.758598102', '2.328840703', '2', '2024-04-24 23:45:09'),
(3, '1', '0.771750796', '0.496655072', '0.264489553', '1', '2024-04-24 23:45:53'),
(4, '2', '-0.556320209', '-0.470159463', '0.871651656', '1', '2024-04-24 23:51:15'),
(5, '2', '2.166012257', '-0.147090208', '1.924065968', '2', '2024-04-24 23:51:34'),
(6, '2', '0.319484693', '0.043619849', '-0.78792476', '0', '2024-04-24 23:51:59'),
(7, '2', '0.749764285', '2.678427511', '1.114516497', '2', '2024-04-24 23:53:45'),
(8, '2', '-0.449845238', '-0.497816924', '1.924065968', '2', '2024-04-25 11:25:33'),
(9, '3', '-0.923375231', '-0.641364265', '-0.383150024', '0', '2024-04-25 12:37:37');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `u_id` int(5) NOT NULL,
  `u_name` varchar(50) NOT NULL,
  `u_email` varchar(200) NOT NULL,
  `u_password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`u_id`, `u_name`, `u_email`, `u_password`) VALUES
(1, 'samyak', 'samyak@gmail.com', 'sam'),
(2, 'samyakfulzele', 'samyakfulzele20@gmail.com', '5214'),
(3, 'sana khan', 'xyzunknown5454@gmail.com', 'sanakhan5454');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `records`
--
ALTER TABLE `records`
  ADD PRIMARY KEY (`r_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`u_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `records`
--
ALTER TABLE `records`
  MODIFY `r_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `u_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
