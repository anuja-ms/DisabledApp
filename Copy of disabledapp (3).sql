-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 27, 2025 at 03:21 PM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `disabledapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_category`
--

DROP TABLE IF EXISTS `adminapp_tbl_category`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_category` (
  `categoryid` int(11) NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(40) NOT NULL,
  `categoryimage` varchar(100) NOT NULL,
  `categorydesc` varchar(300) NOT NULL,
  PRIMARY KEY (`categoryid`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_category`
--

INSERT INTO `adminapp_tbl_category` (`categoryid`, `categoryname`, `categoryimage`, `categorydesc`) VALUES
(6, 'Sensory Disabilities', 'sensory_UyJ6afA.png', 'Impact senses like sight and hearing, including blindness, low vision, deafness, and hard of hearing. '),
(5, 'Physical Disabilities', 'physical_UjJAaVt.jpg', 'Affect mobility and movement, including conditions like spinal cord injuries, cerebral palsy, amputations, and limb impairments. '),
(7, 'Intellectual Disabilities', 'intellectual_B6FNT5x.jpg', 'Affect cognitive abilities and learning potential, including developmental delays and intellectual disability. '),
(8, 'Developmental Disabilities', 'developmental_rDcinv9.jpg', 'Impact development across various areas like motor skills, communication, and social interaction, including autism spectrum disorder and Down syndrome. '),
(9, 'Mental health Disabilities', 'mentalhealth_A9z4jjh.jpg', 'Include conditions like depression, anxiety, bipolar disorder, and schizophrenia.');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_district`
--

DROP TABLE IF EXISTS `adminapp_tbl_district`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_district` (
  `district_id` int(11) NOT NULL AUTO_INCREMENT,
  `district_name` varchar(25) NOT NULL,
  PRIMARY KEY (`district_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_district`
--

INSERT INTO `adminapp_tbl_district` (`district_id`, `district_name`) VALUES
(1, 'Idukki'),
(3, 'Alappuzha'),
(4, 'Kottayam'),
(5, 'Kollam'),
(6, 'Ernakulam'),
(7, 'Thiruvananthapuram'),
(8, 'Kannur'),
(9, 'Kasaragod'),
(10, 'Kozhikode'),
(11, 'Malappuram'),
(12, 'Palakkad'),
(13, 'Pathanamthitta'),
(14, 'Thrissur'),
(15, 'Wayanad');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_equipment`
--

DROP TABLE IF EXISTS `adminapp_tbl_equipment`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_equipment` (
  `equipmentid` int(11) NOT NULL AUTO_INCREMENT,
  `equipmentname` varchar(25) NOT NULL,
  `equipmentimage` varchar(100) NOT NULL,
  `equipmentdesc` varchar(300) NOT NULL,
  `equipmentstock` int(11) NOT NULL,
  `amount` int(11) NOT NULL,
  PRIMARY KEY (`equipmentid`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_equipment`
--

INSERT INTO `adminapp_tbl_equipment` (`equipmentid`, `equipmentname`, `equipmentimage`, `equipmentdesc`, `equipmentstock`, `amount`) VALUES
(1, 'Wheelchair', 'Wheelchair_W6IszMV.webp', 'A wheelchair is a mobility device.', 0, 4000),
(4, 'Walking Aids', 'Walking_Aids.webp', 'Walking aids are designed to assist individuals with mobility challenges, helping them maintain balance, stability, and independence while walking. ', 1, 450),
(5, 'Hearing Aids', 'Hearing_Aids.jpg', 'Small electronic devices worn in or behind the ear that amplify sound for individuals with hearing loss.', 8, 1338);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_location`
--

DROP TABLE IF EXISTS `adminapp_tbl_location`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_location` (
  `locationid` int(11) NOT NULL AUTO_INCREMENT,
  `locationname` varchar(25) NOT NULL,
  `district_id_id` int(11) NOT NULL,
  PRIMARY KEY (`locationid`),
  KEY `AdminApp_tbl_location_district_id_id_006b89d6` (`district_id_id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_location`
--

INSERT INTO `adminapp_tbl_location` (`locationid`, `locationname`, `district_id_id`) VALUES
(1, 'Thodupuzha', 1),
(4, 'sample', 1),
(5, 'Kochi', 6),
(6, 'Poojapura', 7),
(7, 'Murinjapalam', 7),
(8, 'Kakkanad', 6),
(9, 'Malappuram', 11),
(10, 'Kaloor', 6),
(11, 'Thiruvalla', 4),
(12, 'Thrippunithura', 6),
(13, 'Manakala', 13),
(14, 'Attingal', 7),
(15, 'Pangappara', 7),
(16, 'Perumbaikad', 4),
(17, 'Kollapally', 4),
(18, 'Changanassery', 4);

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_scholarship`
--

DROP TABLE IF EXISTS `adminapp_tbl_scholarship`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_scholarship` (
  `scholarshipid` int(11) NOT NULL AUTO_INCREMENT,
  `scholarshipname` varchar(100) NOT NULL,
  `scholarshipdesc` varchar(300) NOT NULL,
  `criteria` varchar(300) NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  `link` varchar(300) NOT NULL,
  `categoryid_id` int(11) NOT NULL,
  PRIMARY KEY (`scholarshipid`),
  KEY `AdminApp_tbl_scholarship_categoryid_id_6c555103` (`categoryid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_scholarship`
--

INSERT INTO `adminapp_tbl_scholarship` (`scholarshipid`, `scholarshipname`, `scholarshipdesc`, `criteria`, `startdate`, `enddate`, `link`, `categoryid_id`) VALUES
(5, 'Pre matric Scholarship', 'Scholarships for Students with Disabilities', 'Students with at least 40% disability', '2025-02-24', '2025-03-20', 'https://example.com', 5),
(6, 'National Scholarship for Persons with Disabilities', 'Financial assistance for tuition fees, books, and assistive devices.', 'Students with at least 40% disability pursuing post-matric and higher education.', '2025-03-18', '2025-04-25', 'https://example.com', 8),
(7, 'NHFDC Scholarships', 'Covers tuition, books, and maintenance costs.\r\n', 'Students with 40% or more disability, family income below 3 lakh per annum.', '2025-03-18', '2025-06-01', 'https://example.com', 6),
(8, 'Scholarships by State Governments', 'State Government Disability Scholarships', 'Students with 40% or more disability, family income below 3 lakh per annum.', '2025-03-18', '2025-07-20', 'https://example.com', 7),
(9, 'AICTE Saksham Scholarship Scheme', 'Provided by: All India Council for Technical Education (AICTE)', 'Minimum 40% disability, family income < 8 lakh per annum.', '2025-03-18', '2025-05-20', 'https://example.com', 9),
(10, 'Indira Gandhi National Disability Scholarship', '3,000 per month for post-graduate students.\r\n', '40% or more disability, enrolled in a recognized PG program.', '2025-03-18', '2025-11-01', 'https://example.com', 5);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=89 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tbl_login', 7, 'add_tbl_login'),
(26, 'Can change tbl_login', 7, 'change_tbl_login'),
(27, 'Can delete tbl_login', 7, 'delete_tbl_login'),
(28, 'Can view tbl_login', 7, 'view_tbl_login'),
(29, 'Can add tbl_district', 8, 'add_tbl_district'),
(30, 'Can change tbl_district', 8, 'change_tbl_district'),
(31, 'Can delete tbl_district', 8, 'delete_tbl_district'),
(32, 'Can view tbl_district', 8, 'view_tbl_district'),
(33, 'Can add tbl_category', 9, 'add_tbl_category'),
(34, 'Can change tbl_category', 9, 'change_tbl_category'),
(35, 'Can delete tbl_category', 9, 'delete_tbl_category'),
(36, 'Can view tbl_category', 9, 'view_tbl_category'),
(37, 'Can add tbl_location', 10, 'add_tbl_location'),
(38, 'Can change tbl_location', 10, 'change_tbl_location'),
(39, 'Can delete tbl_location', 10, 'delete_tbl_location'),
(40, 'Can view tbl_location', 10, 'view_tbl_location'),
(41, 'Can add tbl_equipment', 11, 'add_tbl_equipment'),
(42, 'Can change tbl_equipment', 11, 'change_tbl_equipment'),
(43, 'Can delete tbl_equipment', 11, 'delete_tbl_equipment'),
(44, 'Can view tbl_equipment', 11, 'view_tbl_equipment'),
(45, 'Can add tbl_scholarship', 12, 'add_tbl_scholarship'),
(46, 'Can change tbl_scholarship', 12, 'change_tbl_scholarship'),
(47, 'Can delete tbl_scholarship', 12, 'delete_tbl_scholarship'),
(48, 'Can view tbl_scholarship', 12, 'view_tbl_scholarship'),
(49, 'Can add tbl_institution', 13, 'add_tbl_institution'),
(50, 'Can change tbl_institution', 13, 'change_tbl_institution'),
(51, 'Can delete tbl_institution', 13, 'delete_tbl_institution'),
(52, 'Can view tbl_institution', 13, 'view_tbl_institution'),
(53, 'Can add tbl_disabledperson', 14, 'add_tbl_disabledperson'),
(54, 'Can change tbl_disabledperson', 14, 'change_tbl_disabledperson'),
(55, 'Can delete tbl_disabledperson', 14, 'delete_tbl_disabledperson'),
(56, 'Can view tbl_disabledperson', 14, 'view_tbl_disabledperson'),
(57, 'Can add tbl_enquiry', 15, 'add_tbl_enquiry'),
(58, 'Can change tbl_enquiry', 15, 'change_tbl_enquiry'),
(59, 'Can delete tbl_enquiry', 15, 'delete_tbl_enquiry'),
(60, 'Can view tbl_enquiry', 15, 'view_tbl_enquiry'),
(61, 'Can add tbl_schedule', 16, 'add_tbl_schedule'),
(62, 'Can change tbl_schedule', 16, 'change_tbl_schedule'),
(63, 'Can delete tbl_schedule', 16, 'delete_tbl_schedule'),
(64, 'Can view tbl_schedule', 16, 'view_tbl_schedule'),
(65, 'Can add tbl_request', 17, 'add_tbl_request'),
(66, 'Can change tbl_request', 17, 'change_tbl_request'),
(67, 'Can delete tbl_request', 17, 'delete_tbl_request'),
(68, 'Can view tbl_request', 17, 'view_tbl_request'),
(69, 'Can add tbl_payment', 18, 'add_tbl_payment'),
(70, 'Can change tbl_payment', 18, 'change_tbl_payment'),
(71, 'Can delete tbl_payment', 18, 'delete_tbl_payment'),
(72, 'Can view tbl_payment', 18, 'view_tbl_payment'),
(73, 'Can add tbl_request2', 19, 'add_tbl_request2'),
(74, 'Can change tbl_request2', 19, 'change_tbl_request2'),
(75, 'Can delete tbl_request2', 19, 'delete_tbl_request2'),
(76, 'Can view tbl_request2', 19, 'view_tbl_request2'),
(77, 'Can add tbl_payment2', 20, 'add_tbl_payment2'),
(78, 'Can change tbl_payment2', 20, 'change_tbl_payment2'),
(79, 'Can delete tbl_payment2', 20, 'delete_tbl_payment2'),
(80, 'Can view tbl_payment2', 20, 'view_tbl_payment2'),
(81, 'Can add tbl_jobposting', 21, 'add_tbl_jobposting'),
(82, 'Can change tbl_jobposting', 21, 'change_tbl_jobposting'),
(83, 'Can delete tbl_jobposting', 21, 'delete_tbl_jobposting'),
(84, 'Can view tbl_jobposting', 21, 'view_tbl_jobposting'),
(85, 'Can add tbl_scholarshipreq', 22, 'add_tbl_scholarshipreq'),
(86, 'Can change tbl_scholarshipreq', 22, 'change_tbl_scholarshipreq'),
(87, 'Can delete tbl_scholarshipreq', 22, 'delete_tbl_scholarshipreq'),
(88, 'Can view tbl_scholarshipreq', 22, 'view_tbl_scholarshipreq');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `disabledpersonapp_tbl_enquiry`
--

DROP TABLE IF EXISTS `disabledpersonapp_tbl_enquiry`;
CREATE TABLE IF NOT EXISTS `disabledpersonapp_tbl_enquiry` (
  `enquiryid` int(11) NOT NULL AUTO_INCREMENT,
  `enquiry` varchar(100) NOT NULL,
  `status` varchar(25) NOT NULL,
  `institutionid_id` int(11) NOT NULL,
  `personid_id` int(11) NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`enquiryid`),
  KEY `DisabledPersonApp_tbl_enquiry_institutionid_id_1f4c05c3` (`institutionid_id`),
  KEY `DisabledPersonApp_tbl_enquiry_personid_id_2395b105` (`personid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `disabledpersonapp_tbl_enquiry`
--

INSERT INTO `disabledpersonapp_tbl_enquiry` (`enquiryid`, `enquiry`, `status`, `institutionid_id`, `personid_id`, `date`) VALUES
(1, 'I am Preethi Srinivasan.', 'Accepted', 3, 3, '2025-02-03'),
(2, 'hhhh', 'Rejected', 4, 3, '2025-02-11'),
(3, 'hfhvgrrbkjfv', 'Rejected', 4, 3, '2025-02-21'),
(4, 'I am interested to know more.', 'Not Confirmed', 4, 3, '2025-03-03'),
(5, 'nn', 'Accepted', 4, 6, '2025-03-20'),
(6, 'I am a disabled student interested in study opportunities at your institution.', 'Not Confirmed', 4, 6, '2025-03-21');

-- --------------------------------------------------------

--
-- Table structure for table `disabledpersonapp_tbl_payment`
--

DROP TABLE IF EXISTS `disabledpersonapp_tbl_payment`;
CREATE TABLE IF NOT EXISTS `disabledpersonapp_tbl_payment` (
  `paymentid` int(11) NOT NULL AUTO_INCREMENT,
  `paymentdate` date NOT NULL,
  `status` varchar(25) NOT NULL,
  `amount` int(11) NOT NULL,
  `requestid_id` int(11) NOT NULL,
  PRIMARY KEY (`paymentid`),
  KEY `DisabledPersonApp_tbl_payment_requestid_id_cd15895c` (`requestid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `disabledpersonapp_tbl_payment`
--

INSERT INTO `disabledpersonapp_tbl_payment` (`paymentid`, `paymentdate`, `status`, `amount`, `requestid_id`) VALUES
(1, '2025-02-16', 'Paid', 450, 2),
(2, '2025-02-21', 'Paid', 4000, 1),
(3, '2025-03-03', 'Paid', 1338, 6),
(4, '2025-03-03', 'Paid', 1338, 3);

-- --------------------------------------------------------

--
-- Table structure for table `disabledpersonapp_tbl_request`
--

DROP TABLE IF EXISTS `disabledpersonapp_tbl_request`;
CREATE TABLE IF NOT EXISTS `disabledpersonapp_tbl_request` (
  `requestid` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `status` varchar(25) NOT NULL,
  `requesteddate` date DEFAULT NULL,
  `equipmentid_id` int(11) NOT NULL,
  `personid_id` int(11) NOT NULL,
  `count` int(11) DEFAULT NULL,
  `totalamount` int(11) DEFAULT NULL,
  PRIMARY KEY (`requestid`),
  KEY `DisabledPersonApp_tbl_request_equipmentid_id_a25aa119` (`equipmentid_id`),
  KEY `DisabledPersonApp_tbl_request_personid_id_f856624a` (`personid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `disabledpersonapp_tbl_request`
--

INSERT INTO `disabledpersonapp_tbl_request` (`requestid`, `date`, `status`, `requesteddate`, `equipmentid_id`, `personid_id`, `count`, `totalamount`) VALUES
(1, '2025-02-11', 'Accepted', '2025-02-11', 1, 3, NULL, NULL),
(2, '2025-02-13', 'Accepted', '2025-02-13', 4, 3, NULL, NULL),
(3, '2025-02-13', 'paid', '2025-02-13', 5, 3, NULL, NULL),
(4, '2025-03-03', 'Rejected', NULL, 4, 3, NULL, NULL),
(5, '2025-03-03', 'Rejected', NULL, 5, 3, NULL, NULL),
(6, '2025-03-03', 'Accepted', '2025-03-29', 5, 3, NULL, NULL),
(7, '2025-03-06', 'Accepted', '2025-03-02', 1, 4, NULL, NULL),
(8, '2025-03-07', 'Accepted', '2025-03-28', 5, 5, NULL, NULL),
(9, '2025-03-12', 'Not Confirmed', '2025-03-21', 4, 3, NULL, NULL),
(10, '2025-03-20', 'Accepted', '2025-03-21', 1, 6, NULL, NULL),
(11, '2025-03-24', 'Not Confirmed', '2025-04-30', 5, 6, NULL, NULL),
(12, '2025-03-24', 'Accepted', '2025-03-31', 4, 6, NULL, NULL),
(14, '2025-03-24', 'Accepted', '2025-03-27', 1, 6, 2, 8000);

-- --------------------------------------------------------

--
-- Table structure for table `disabledpersonapp_tbl_scholarshipreq`
--

DROP TABLE IF EXISTS `disabledpersonapp_tbl_scholarshipreq`;
CREATE TABLE IF NOT EXISTS `disabledpersonapp_tbl_scholarshipreq` (
  `requestid` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(25) NOT NULL,
  `course` varchar(25) NOT NULL,
  `income` int(11) NOT NULL,
  `accountno` bigint(20) NOT NULL,
  `institutionid_id` int(11) NOT NULL,
  `personid_id` int(11) NOT NULL,
  `scholarshipid_id` int(11) NOT NULL,
  PRIMARY KEY (`requestid`),
  KEY `DisabledPersonApp_tbl_scholarshipreq_institutionid_id_9d1b2bcf` (`institutionid_id`),
  KEY `DisabledPersonApp_tbl_scholarshipreq_personid_id_f728e5ee` (`personid_id`),
  KEY `DisabledPersonApp_tbl_scholarshipreq_scholarshipid_id_791183c6` (`scholarshipid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `disabledpersonapp_tbl_scholarshipreq`
--

INSERT INTO `disabledpersonapp_tbl_scholarshipreq` (`requestid`, `status`, `course`, `income`, `accountno`, `institutionid_id`, `personid_id`, `scholarshipid_id`) VALUES
(1, 'Accepted', 'ug', 200000, 345678, 5, 3, 5),
(2, 'Not Confirmed', 'BCA', 12000, 34526, 3, 3, 5),
(3, 'Not Confirmed', 'bca', 10000, 456376345267, 3, 6, 7);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'GuestApp', 'tbl_login'),
(8, 'AdminApp', 'tbl_district'),
(9, 'AdminApp', 'tbl_category'),
(10, 'AdminApp', 'tbl_location'),
(11, 'AdminApp', 'tbl_equipment'),
(12, 'AdminApp', 'tbl_scholarship'),
(13, 'GuestApp', 'tbl_institution'),
(14, 'GuestApp', 'tbl_disabledperson'),
(15, 'DisabledPersonApp', 'tbl_enquiry'),
(16, 'InstitutionApp', 'tbl_schedule'),
(17, 'DisabledPersonApp', 'tbl_request'),
(18, 'DisabledPersonApp', 'tbl_payment'),
(19, 'InstitutionApp', 'tbl_request2'),
(20, 'InstitutionApp', 'tbl_payment2'),
(21, 'InstitutionApp', 'tbl_jobposting'),
(22, 'DisabledPersonApp', 'tbl_scholarshipreq');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'GuestApp', '0001_initial', '2025-01-08 08:47:51.132140'),
(2, 'contenttypes', '0001_initial', '2025-01-08 08:47:51.160201'),
(3, 'auth', '0001_initial', '2025-01-08 08:47:51.287524'),
(4, 'admin', '0001_initial', '2025-01-08 08:47:51.321390'),
(5, 'admin', '0002_logentry_remove_auto_add', '2025-01-08 08:47:51.325283'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2025-01-08 08:47:51.335342'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-01-08 08:47:51.355291'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-01-08 08:47:51.371872'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-01-08 08:47:51.387998'),
(10, 'auth', '0004_alter_user_username_opts', '2025-01-08 08:47:51.388644'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-01-08 08:47:51.405706'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-01-08 08:47:51.415147'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-01-08 08:47:51.431471'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-01-08 08:47:51.438775'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-01-08 08:47:51.455265'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-01-08 08:47:51.478435'),
(17, 'auth', '0011_update_proxy_permissions', '2025-01-08 08:47:51.485709'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-01-08 08:47:51.488630'),
(19, 'sessions', '0001_initial', '2025-01-08 08:47:51.505208'),
(20, 'GuestApp', '0002_tbl_login_status', '2025-01-08 08:56:29.536840'),
(21, 'AdminApp', '0001_initial', '2025-01-08 10:14:10.286851'),
(22, 'AdminApp', '0002_tbl_category', '2025-01-09 10:09:16.248871'),
(23, 'AdminApp', '0003_tbl_location', '2025-01-14 05:53:58.532003'),
(24, 'AdminApp', '0004_tbl_equipment', '2025-01-16 08:43:18.691557'),
(25, 'AdminApp', '0005_alter_tbl_equipment_equipmentdesc_tbl_scholarship', '2025-01-17 04:39:20.647461'),
(26, 'AdminApp', '0006_alter_tbl_scholarship_enddate_and_more', '2025-01-17 05:53:49.609967'),
(27, 'GuestApp', '0003_tbl_institution', '2025-01-21 05:55:08.695633'),
(28, 'GuestApp', '0004_tbl_disabledperson', '2025-01-22 07:27:21.273967'),
(29, 'GuestApp', '0005_alter_tbl_disabledperson_email', '2025-01-24 04:54:01.909978'),
(30, 'DisabledPersonApp', '0001_initial', '2025-01-28 07:14:31.176416'),
(31, 'AdminApp', '0007_alter_tbl_scholarship_startdate', '2025-01-29 09:04:28.235078'),
(32, 'DisabledPersonApp', '0002_tbl_enquiry_date', '2025-01-30 08:45:31.048987'),
(33, 'InstitutionApp', '0001_initial', '2025-02-04 09:16:26.948571'),
(34, 'AdminApp', '0008_tbl_equipment_amount', '2025-02-11 06:47:53.473307'),
(35, 'DisabledPersonApp', '0003_tbl_request', '2025-02-11 07:06:10.695228'),
(36, 'DisabledPersonApp', '0004_tbl_payment', '2025-02-13 08:47:46.199519'),
(37, 'InstitutionApp', '0002_tbl_request2_tbl_payment2', '2025-02-21 04:43:07.076927'),
(38, 'InstitutionApp', '0003_tbl_jobposting', '2025-02-26 05:33:46.722458'),
(39, 'InstitutionApp', '0004_alter_tbl_jobposting_deadline', '2025-02-27 09:35:21.022096'),
(40, 'DisabledPersonApp', '0005_alter_tbl_request_requesteddate', '2025-03-03 04:19:52.417448'),
(41, 'InstitutionApp', '0005_alter_tbl_request2_requesteddate', '2025-03-03 04:52:52.359202'),
(42, 'DisabledPersonApp', '0006_tbl_scholarshipreq', '2025-03-12 06:06:43.838006'),
(43, 'DisabledPersonApp', '0007_alter_tbl_scholarshipreq_accountno', '2025-03-24 06:26:12.325217'),
(44, 'DisabledPersonApp', '0008_tbl_request_count', '2025-03-24 06:58:55.233630'),
(45, 'DisabledPersonApp', '0009_tbl_request_totalamount', '2025-03-24 07:07:57.890574'),
(46, 'InstitutionApp', '0006_tbl_request2_count_tbl_request2_totalamount', '2025-03-24 07:20:15.161257');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('yw0urk2fserbpzeuh66bksnywaqx6y0c', 'eyJsb2dpbmlkIjoxfQ:1tVSNG:ixsgqN-brsor6qKSfjiuD2_-YSJEjm8UO1WKUQKnUoo', '2025-01-22 09:29:14.985367'),
('bffdpomwt32gro68qb0u7x69iql977et', 'eyJsb2dpbmlkIjo3fQ:1tbFym:k8EfRm4So23_4mz9LoGXYCElxuEjjPdI7QWkbSHXr98', '2025-02-07 09:27:56.475554'),
('vg33sirufufd04s1om35qu0h6f3n5i7i', 'eyJsb2dpbmlkIjo3LCJjYXRlZ29yeWlkIjoiMyJ9:1tcfha:h6huST0062CG64OkyLJZV5m-s70ticFu13pv0Hh4G78', '2025-02-11 07:08:02.349522'),
('svqc5makb9vto56ug52iahpi28jdv4w0', 'eyJsb2dpbmlkIjoxfQ:1twy7b:WWwsmxJTWYFbCIveuEi96QCs2u-dzlG1uLFbVxf377U', '2025-04-08 06:50:47.663682'),
('fg167btwkwwewi11jk2dl6m06s6bty39', 'eyJsb2dpbmlkIjoxLCJpbnN0aXR1dGlvbmlkIjoiNCJ9:1tlMQP:E7qM-EvEIcNwg3ercfICzbheYaQ6ZlrHK2GMt_TL3w4', '2025-03-07 06:22:13.730660');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_disabledperson`
--

DROP TABLE IF EXISTS `guestapp_tbl_disabledperson`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_disabledperson` (
  `personid` int(11) NOT NULL AUTO_INCREMENT,
  `personname` varchar(25) NOT NULL,
  `address` varchar(25) NOT NULL,
  `contactno` bigint(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `percentage` varchar(25) NOT NULL,
  `disabilitydetails` varchar(300) NOT NULL,
  `pname` varchar(25) NOT NULL,
  `pcontact` bigint(20) NOT NULL,
  `dob` date NOT NULL,
  `idproof` varchar(100) NOT NULL,
  `categoryid_id` int(11) NOT NULL,
  `locationid_id` int(11) NOT NULL,
  `loginid_id` int(11) NOT NULL,
  PRIMARY KEY (`personid`),
  KEY `GuestApp_tbl_disabledperson_categoryid_id_9909d4bd` (`categoryid_id`),
  KEY `GuestApp_tbl_disabledperson_locationid_id_4d9b5647` (`locationid_id`),
  KEY `GuestApp_tbl_disabledperson_loginid_id_b8501024` (`loginid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_disabledperson`
--

INSERT INTO `guestapp_tbl_disabledperson` (`personid`, `personname`, `address`, `contactno`, `email`, `percentage`, `disabilitydetails`, `pname`, `pcontact`, `dob`, `idproof`, `categoryid_id`, `locationid_id`, `loginid_id`) VALUES
(3, 'Preethi Srinivasan', 'Chennai', 9876787556, 'jensonjames543212345@gmail.com', '60%', 'Spinal cord injuries', 'Vijayalakshmi Srinivasan', 7678565449, '1979-09-05', 'idproof_DBduAcO', 5, 7, 11),
(6, 'Sudha Chandran', 'Mumbai', 787654678, 'sudha@gmail.com', '40', 'Gangrene ', 'Chandran', 9987654566, '1965-09-27', 'Aadhaar_28X8vB3.png', 6, 5, 26);

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_institution`
--

DROP TABLE IF EXISTS `guestapp_tbl_institution`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_institution` (
  `institutionid` int(11) NOT NULL AUTO_INCREMENT,
  `institutionname` varchar(75) NOT NULL,
  `regnumber` varchar(25) NOT NULL,
  `contactno` bigint(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `percentage` varchar(25) NOT NULL,
  `institutiondesc` varchar(300) NOT NULL,
  `websiteurl` varchar(50) NOT NULL,
  `institutionimage` varchar(100) NOT NULL,
  `categoryid_id` int(11) NOT NULL,
  `locationid_id` int(11) NOT NULL,
  `loginid_id` int(11) NOT NULL,
  PRIMARY KEY (`institutionid`),
  KEY `GuestApp_tbl_institution_categoryid_id_e722640b` (`categoryid_id`),
  KEY `GuestApp_tbl_institution_locationid_id_9abea25f` (`locationid_id`),
  KEY `GuestApp_tbl_institution_loginid_id_32be6cac` (`loginid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_institution`
--

INSERT INTO `guestapp_tbl_institution` (`institutionid`, `institutionname`, `regnumber`, `contactno`, `email`, `percentage`, `institutiondesc`, `websiteurl`, `institutionimage`, `categoryid_id`, `locationid_id`, `loginid_id`) VALUES
(3, 'Amritha Institute For Differently Abled', 'SR-123/2020', 7034028105, 'aida@amrita.ind.in', '75%', 'Special education school in Kochi, Kerala', 'https://www.amrita.ind.in/', 'amrita_TG1GCFe.jpg', 9, 5, 12),
(4, 'Centre of Excellence for Differently Abled Studies', '002/EDU/KIT/2021', 4712345627, 'cedstvpm@gmail.com', '60%', 'Centre of Excellence for Differently Abled Studies with Concentration on Innovations in Rehabilitation Technology is established in Thiruvananthapuram as a part of LBS Centre for Science and Technology, Thiruvananthapuram.', 'http://ceds.kerala.gov.in/cds/', 'ceds_ftnnaS6.jpg', 5, 6, 13),
(5, 'Snehabhavan Special School for the Mentally Challenged', 'K221/90', 9496224332, 'jensonjames543212345@gmail.com', '40', 'A home of loving care for the differently abled.', 'https://www.snehabhavanktm.org/', 'snehabhavan_uq8a99u.avif', 9, 16, 16),
(11, 'Smrithi', 'SR-123/2020', 9048763931, 'smrithi@gmail.com', '60', 'School for Children with Special Needs', 'https://www.facebook.com/@smrithispecialschool', 'smrithi_AxdFEt7.png', 9, 10, 24),
(10, 'Central Institute on Mental Retardation', 'K221/90', 4712445796, 'cimrdirector@gmail.com', '40', 'Special education school in Thiruvananthapuram, Kerala\r\n', 'https://www.cimr.info/contact-us/', 'CIMR_vPKgLuC.jpeg', 9, 7, 23),
(12, 'Deepti Special School and Rehabilitation Centre', 'SR-123/2020', 4734231765, 'mail.deepticentre@gmail.com', '40', 'Enabling the present, Enlightening the future', 'http://deepticentre.com/reach-us/', 'Deepti_6CSos50.png', 5, 13, 25);

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_login`
--

DROP TABLE IF EXISTS `guestapp_tbl_login`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `role` varchar(25) NOT NULL,
  `status` varchar(25) NOT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_login`
--

INSERT INTO `guestapp_tbl_login` (`loginid`, `username`, `password`, `role`, `status`) VALUES
(1, 'admin', 'admin', 'admin', 'conformed'),
(2, 'uuuu', 'uuuu', 'institution', ''),
(3, 'jenson', 'jenson', 'institution', 'Not Confirmed'),
(4, 'ghh', 'hhh', 'institution', 'Accepted'),
(5, 'hhh', 'hhhh', 'disabledperson', 'Not Confirmed'),
(6, 'fff', 'ddd', 'disabledperson', 'Not Confirmed'),
(7, 'hh', 'dff', 'disabledperson', 'Confirmed'),
(8, 'new', 'new', 'institution', 'Accepted'),
(12, 'Amritha', 'Amritha', 'institution', 'Accepted'),
(13, 'ceds', 'ceds', 'institution', 'Accepted'),
(11, 'preethi', 'preethi', 'disabledperson', 'Confirmed'),
(16, 'Snehabhavan ', 'Snehabhavan ', 'institution', 'Accepted'),
(17, 'yyuu', 'uuuu', 'institution', 'Rejected'),
(18, 'jjfj', 'jjffj', 'institution', 'Rejected'),
(19, 'hhhh', 'jjjj', 'institution', 'Accepted'),
(20, 'jenson10', 'jenson10', 'disabledperson', 'Confirmed'),
(21, 'keerthana', 'keerthana', 'disabledperson', 'Confirmed'),
(22, 'meera', 'meera', 'institution', 'Accepted'),
(23, 'CIMR', 'CIMR', 'institution', 'Accepted'),
(24, 'Smrithi', 'Smrithi', 'institution', 'Accepted'),
(25, 'Deepti ', 'Deepti ', 'institution', 'Accepted'),
(26, 'Sudha ', 'Sudha ', 'disabledperson', 'Confirmed'),
(27, 'Deepti123', 'Deepti123', 'institution', 'Rejected');

-- --------------------------------------------------------

--
-- Table structure for table `institutionapp_tbl_jobposting`
--

DROP TABLE IF EXISTS `institutionapp_tbl_jobposting`;
CREATE TABLE IF NOT EXISTS `institutionapp_tbl_jobposting` (
  `jobid` int(11) NOT NULL AUTO_INCREMENT,
  `jobtitle` varchar(50) NOT NULL,
  `jobdesc` varchar(100) NOT NULL,
  `requirments` varchar(100) NOT NULL,
  `deadline` date DEFAULT NULL,
  `contactemail` varchar(50) NOT NULL,
  `jobimage` varchar(100) NOT NULL,
  `institutionid_id` int(11) NOT NULL,
  PRIMARY KEY (`jobid`),
  KEY `InstitutionApp_tbl_jobposting_institutionid_id_9144b817` (`institutionid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `institutionapp_tbl_jobposting`
--

INSERT INTO `institutionapp_tbl_jobposting` (`jobid`, `jobtitle`, `jobdesc`, `requirments`, `deadline`, `contactemail`, `jobimage`, `institutionid_id`) VALUES
(1, 'Data Entry Clerk', 'Enter and manage company data', 'Typing, MS Excel', '2025-02-26', 'careers@xyz.org', 'jobimg5.webp', 4),
(2, 'Software Developer', 'Develop accessible web applications', 'HTML, CSS, JS, PHP', '2025-02-26', 'hr@techfirm.com', 'jobimg4.jpg', 4),
(3, 'Customer Support Representative', 'Provide customer support via email and chat for an e-commerce company.', 'Good communication skills, basic computer knowledge', '2025-03-31', 'supportjobs@ecommerce.com', 'jobimg6_Iz3AmFL.jpg', 3);

-- --------------------------------------------------------

--
-- Table structure for table `institutionapp_tbl_payment2`
--

DROP TABLE IF EXISTS `institutionapp_tbl_payment2`;
CREATE TABLE IF NOT EXISTS `institutionapp_tbl_payment2` (
  `paymentid` int(11) NOT NULL AUTO_INCREMENT,
  `paymentdate` date NOT NULL,
  `status` varchar(25) NOT NULL,
  `amount` int(11) NOT NULL,
  `requestid_id` int(11) NOT NULL,
  PRIMARY KEY (`paymentid`),
  KEY `InstitutionApp_tbl_payment2_requestid_id_f88213fd` (`requestid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `institutionapp_tbl_payment2`
--

INSERT INTO `institutionapp_tbl_payment2` (`paymentid`, `paymentdate`, `status`, `amount`, `requestid_id`) VALUES
(1, '2025-03-03', 'Paid', 4000, 1);

-- --------------------------------------------------------

--
-- Table structure for table `institutionapp_tbl_request2`
--

DROP TABLE IF EXISTS `institutionapp_tbl_request2`;
CREATE TABLE IF NOT EXISTS `institutionapp_tbl_request2` (
  `requestid` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `status` varchar(25) NOT NULL,
  `requesteddate` date DEFAULT NULL,
  `equipmentid_id` int(11) NOT NULL,
  `institutionid_id` int(11) NOT NULL,
  `count` int(11) DEFAULT NULL,
  `totalamount` int(11) DEFAULT NULL,
  PRIMARY KEY (`requestid`),
  KEY `InstitutionApp_tbl_request2_equipmentid_id_02d7d5e9` (`equipmentid_id`),
  KEY `InstitutionApp_tbl_request2_institutionid_id_9fbdab7c` (`institutionid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `institutionapp_tbl_request2`
--

INSERT INTO `institutionapp_tbl_request2` (`requestid`, `date`, `status`, `requesteddate`, `equipmentid_id`, `institutionid_id`, `count`, `totalamount`) VALUES
(1, '2025-02-21', 'paid', '2025-02-21', 1, 4, NULL, NULL),
(2, '2025-02-25', 'Not Confirmed', '2025-02-25', 5, 4, NULL, NULL),
(3, '2025-03-03', 'Not Confirmed', '2025-04-24', 4, 4, NULL, NULL),
(4, '2025-03-03', 'Not Confirmed', '2025-03-27', 1, 4, NULL, NULL),
(5, '2025-03-03', 'Not Confirmed', '2025-03-27', 4, 4, NULL, NULL),
(6, '2025-03-06', 'Accepted', '2025-03-22', 4, 8, NULL, NULL),
(7, '2025-03-07', 'Rejected', '2025-03-13', 1, 9, NULL, NULL),
(8, '2025-03-07', 'Accepted', '2025-03-28', 1, 3, NULL, NULL),
(9, '2025-03-07', 'Rejected', '2025-03-28', 4, 3, NULL, NULL),
(10, '2025-03-24', 'Not Confirmed', '2025-04-05', 5, 3, NULL, NULL),
(11, '2025-03-24', 'Not Confirmed', '2025-04-20', 4, 10, NULL, NULL),
(13, '2025-03-24', 'Accepted', '2025-03-26', 4, 4, 1, 450);

-- --------------------------------------------------------

--
-- Table structure for table `institutionapp_tbl_schedule`
--

DROP TABLE IF EXISTS `institutionapp_tbl_schedule`;
CREATE TABLE IF NOT EXISTS `institutionapp_tbl_schedule` (
  `scheduleid` int(11) NOT NULL AUTO_INCREMENT,
  `scheduledate` date NOT NULL,
  `status` varchar(25) NOT NULL,
  `enquiryid_id` int(11) NOT NULL,
  PRIMARY KEY (`scheduleid`),
  KEY `InstitutionApp_tbl_schedule_enquiryid_id_30d78215` (`enquiryid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `institutionapp_tbl_schedule`
--

INSERT INTO `institutionapp_tbl_schedule` (`scheduleid`, `scheduledate`, `status`, `enquiryid_id`) VALUES
(1, '2025-02-20', 'confirmed', 1),
(3, '2025-03-21', 'confirmed', 5);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
