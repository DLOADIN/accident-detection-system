-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 22, 2025 at 04:50 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `accident_detection`
--

-- --------------------------------------------------------

--
-- Table structure for table `accidents`
--

CREATE TABLE `accidents` (
  `id` int(11) NOT NULL,
  `timestamp` datetime NOT NULL,
  `location` varchar(255) NOT NULL,
  `severity_level` enum('low','medium','high') NOT NULL,
  `severity_score` float NOT NULL,
  `video_path` varchar(255) NOT NULL,
  `accuracy` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `accidents`
--

INSERT INTO `accidents` (`id`, `timestamp`, `location`, `severity_level`, `severity_score`, `video_path`, `accuracy`) VALUES
(1, '2025-02-21 23:40:39', 'Intersection A', 'medium', 50.2, 'accident_2025-02-21 23:40:39.mp4', 100),
(2, '2025-02-21 23:40:43', 'Intersection A', 'medium', 50.69, 'accident_2025-02-21 23:40:43.mp4', 100),
(3, '2025-02-21 23:40:44', 'Intersection A', 'medium', 50.27, 'accident_2025-02-21 23:40:44.mp4', 100),
(4, '2025-02-21 23:40:47', 'Intersection A', 'medium', 50.69, 'accident_2025-02-21 23:40:47.mp4', 100),
(5, '2025-02-21 23:40:50', 'Intersection A', 'medium', 51.44, 'accident_2025-02-21 23:40:50.mp4', 100),
(6, '2025-02-21 23:40:51', 'Intersection A', 'medium', 50.11, 'accident_2025-02-21 23:40:51.mp4', 100),
(7, '2025-02-21 23:40:52', 'Intersection A', 'medium', 50.41, 'accident_2025-02-21 23:40:52.mp4', 100),
(8, '2025-02-21 23:40:53', 'Intersection A', 'medium', 52.56, 'accident_2025-02-21 23:40:53.mp4', 100),
(9, '2025-02-21 23:40:54', 'Intersection A', 'medium', 52.32, 'accident_2025-02-21 23:40:54.mp4', 100),
(10, '2025-02-21 23:40:54', 'Intersection A', 'medium', 50.94, 'accident_2025-02-21 23:40:54.mp4', 100),
(11, '2025-02-22 16:08:16', 'Intersection A', 'medium', 50.2, 'accident_2025-02-22 16:08:16.mp4', 100),
(12, '2025-02-22 16:08:22', 'Intersection A', 'medium', 50.69, 'accident_2025-02-22 16:08:22.mp4', 100),
(13, '2025-02-22 16:08:23', 'Intersection A', 'medium', 50.27, 'accident_2025-02-22 16:08:23.mp4', 100),
(14, '2025-02-22 16:08:25', 'Intersection A', 'medium', 50.69, 'accident_2025-02-22 16:08:25.mp4', 100),
(15, '2025-02-22 16:08:28', 'Intersection A', 'medium', 51.44, 'accident_2025-02-22 16:08:28.mp4', 100),
(16, '2025-02-22 16:08:29', 'Intersection A', 'medium', 50.11, 'accident_2025-02-22 16:08:29.mp4', 100),
(17, '2025-02-22 16:08:30', 'Intersection A', 'medium', 50.41, 'accident_2025-02-22 16:08:30.mp4', 100),
(18, '2025-02-22 16:08:31', 'Intersection A', 'medium', 52.56, 'accident_2025-02-22 16:08:31.mp4', 100),
(19, '2025-02-22 16:08:32', 'Intersection A', 'medium', 52.32, 'accident_2025-02-22 16:08:32.mp4', 100),
(20, '2025-02-22 16:08:33', 'Intersection A', 'medium', 50.94, 'accident_2025-02-22 16:08:33.mp4', 100);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accidents`
--
ALTER TABLE `accidents`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accidents`
--
ALTER TABLE `accidents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
