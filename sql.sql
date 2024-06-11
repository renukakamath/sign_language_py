/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - signlanguage
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`signlanguage` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `signlanguage`;

/*Table structure for table `frames` */

DROP TABLE IF EXISTS `frames`;

CREATE TABLE `frames` (
  `frames` int(11) NOT NULL AUTO_INCREMENT,
  `uvideo_id` int(11) DEFAULT NULL,
  `frame` varchar(100) DEFAULT NULL,
  `out` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`frames`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `frames` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'user','user','user'),
(3,'hai','hai','user');

/*Table structure for table `subscription` */

DROP TABLE IF EXISTS `subscription`;

CREATE TABLE `subscription` (
  `subscription_id` int(11) NOT NULL AUTO_INCREMENT,
  `subscription` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `planfor` varchar(100) DEFAULT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`subscription_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `subscription` */

insert  into `subscription`(`subscription_id`,`subscription`,`amount`,`planfor`,`user_id`) values 
(2,'ghfhgg','5000','jhkhuy','2');

/*Table structure for table `uploadimage` */

DROP TABLE IF EXISTS `uploadimage`;

CREATE TABLE `uploadimage` (
  `uploadimage_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `uploadvideo_id` int(11) DEFAULT NULL,
  `out` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`uploadimage_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `uploadimage` */

insert  into `uploadimage`(`uploadimage_id`,`user_id`,`uploadvideo_id`,`out`) values 
(1,1,1,'0');

/*Table structure for table `uploadvideo` */

DROP TABLE IF EXISTS `uploadvideo`;

CREATE TABLE `uploadvideo` (
  `uploadvideo_id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`uploadvideo_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `uploadvideo` */

insert  into `uploadvideo`(`uploadvideo_id`,`file`,`date`,`type`) values 
(1,'static/75feff3c-a942-490f-8c3f-2dc44dc2790dcdc-L0jLHqF7Q94-unsplash.jpg','2023-07-05','video');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(200) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,2,'user','qwerty','kerala','2345678907','student@gmail.com'),
(2,3,'user','qwerty','ernakulam1','2345678907','student@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
