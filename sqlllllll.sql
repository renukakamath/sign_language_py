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
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `frames` */

insert  into `frames`(`frames`,`uvideo_id`,`frame`,`out`) values 
(1,33,'static/uploads/bef3fe28-e2a2-41fe-83af-a8aec127b1ca.jpg','11'),
(2,34,'static/uploads/3aaa3939-7faf-4426-a543-b78996b28c3c.jpg','11'),
(3,35,'static/uploads/964a4d20-800c-4cdb-8980-db5c5defcb4d.jpg','11'),
(4,36,'static/uploads/fb3aad3b-db3b-4825-b6a7-88d5b5cdcd0f.jpg','11'),
(5,37,'static/uploads/830a299e-3b40-4935-9940-546d2b327c20.jpg','r'),
(6,38,'static/uploads/4b415c6a-9e2b-4a36-9548-4df9239151f9.jpg','m'),
(7,39,'static/uploads/61784bd7-cade-44f1-a576-ac526bc5e447.jpg','m'),
(8,40,'static/uploads/7ff302dc-7a8a-439e-b6ba-350517ec4dbd.jpg','m'),
(9,41,'static/uploads/f312d71c-ad31-4e19-87e8-ebf96b15878c.jpg','m'),
(10,42,'static/uploads/8933dbbd-4b8b-4eee-bd78-0095533ac20f.jpg','r');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin','admin','admin'),
(2,'user','user','user'),
(3,'hai','hai','user'),
(4,'hh','hh','User'),
(5,'hh1','hh1','User'),
(9,'hello','hello','user');

/*Table structure for table `subscription` */

DROP TABLE IF EXISTS `subscription`;

CREATE TABLE `subscription` (
  `subscription_id` int(11) NOT NULL AUTO_INCREMENT,
  `subscription` varchar(100) DEFAULT NULL,
  `amount` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`subscription_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `subscription` */

insert  into `subscription`(`subscription_id`,`subscription`,`amount`,`date`,`user_id`,`status`) values 
(3,'ghfhgg','5000','2023-07-14','7','subscribe');

/*Table structure for table `uploadimage` */

DROP TABLE IF EXISTS `uploadimage`;

CREATE TABLE `uploadimage` (
  `uploadimage_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `uploadvideo_id` int(11) DEFAULT NULL,
  `out` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`uploadimage_id`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;

/*Data for the table `uploadimage` */

insert  into `uploadimage`(`uploadimage_id`,`user_id`,`uploadvideo_id`,`out`) values 
(1,1,1,'0'),
(2,2,2,'H'),
(3,2,3,'E'),
(4,2,4,'E'),
(5,2,5,'E'),
(6,2,6,'B'),
(7,NULL,9,'G'),
(8,NULL,10,'C'),
(9,NULL,11,'C'),
(10,3,12,'C'),
(11,3,13,'22'),
(12,3,14,'10'),
(13,3,15,'22'),
(14,3,16,'m'),
(15,3,17,'a'),
(16,3,18,'m'),
(17,3,19,'m'),
(18,3,20,'w'),
(19,3,21,'o'),
(20,3,22,'w'),
(21,3,23,'a'),
(22,3,24,'e'),
(23,3,25,'a'),
(24,3,26,'a'),
(25,3,27,'g'),
(26,3,28,'a'),
(27,3,29,'t'),
(28,3,30,'y'),
(29,7,35,'11'),
(30,7,36,'11'),
(31,7,37,'r'),
(32,7,38,'m'),
(33,7,39,'m'),
(34,7,40,'m'),
(35,7,41,'m'),
(36,7,42,'r'),
(37,7,43,'q'),
(38,7,44,'f');

/*Table structure for table `uploadvideo` */

DROP TABLE IF EXISTS `uploadvideo`;

CREATE TABLE `uploadvideo` (
  `uploadvideo_id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(1000) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`uploadvideo_id`)
) ENGINE=MyISAM AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

/*Data for the table `uploadvideo` */

insert  into `uploadvideo`(`uploadvideo_id`,`file`,`date`,`type`) values 
(1,'static/75feff3c-a942-490f-8c3f-2dc44dc2790dcdc-L0jLHqF7Q94-unsplash.jpg','2023-07-05','video'),
(2,'static/uploads/15931787-0279-4c8c-a66b-d256e48fd3a9abc (1).jpg','2023-07-08','image'),
(3,'static/uploads/90f21a21-90fd-4dc2-a7e9-cbec822a38a90.jpg','2023-07-08','image'),
(4,'static/uploads/a596797e-fbfd-4407-962f-7f47f0e5587724.jpg','2023-07-08','image'),
(5,'static/uploads/460647c0-3e5d-49c3-9107-11a58701f05a0.jpg','2023-07-08','image'),
(6,'static/uploads/3dcbca90-063a-43f2-8b3e-9267e7e0cee70.jpg','2023-07-08','image'),
(7,'static/uploads/93d46c6c-5800-4dea-befc-d2b87297677eabc.jpg','2023-07-19','image'),
(8,'static/uploads/1fd082db-1c20-4f4a-82fc-7bf2822858fdabc.jpg','2023-07-19','image'),
(9,'static/uploads/4c497956-232c-46e9-841a-bcf683ff19fdabc.jpg','2023-07-19','image'),
(10,'static/uploads/f1baa53d-8124-45ce-8488-35f043c29555abc.jpg','2023-07-19','image'),
(11,'static/uploads/46216b88-0184-4e75-9345-a65a9e009de1abc.jpg','2023-07-19','image'),
(12,'static/uploads/fa5019a0-6cf6-41a7-955b-39761c846c7fabc.jpg','2023-07-19','image'),
(13,'static/uploads/b9c15f16-261a-4deb-baf5-566a81768e94abc.jpg','2023-07-22','image'),
(14,'static/uploads/575da9ec-18c6-4afe-94ef-29aff67430fdabc.jpg','2023-07-22','image'),
(15,'static/uploads/2ec5383c-d46b-4775-80da-e4829343f445abc.jpg','2023-07-22','image'),
(16,'static/uploads/f80e61f7-f7de-4d87-ac03-b9c71ebf942cabc.jpg','2023-07-22','image'),
(17,'static/uploads/19ad7ef1-45d8-42d8-89d2-c1307acf0f00abc.jpg','2023-07-22','image'),
(18,'static/uploads/f194085b-13e8-4619-94d4-38cf3cfe7591abc.jpg','2023-07-22','image'),
(19,'static/uploads/80297d8a-c5f1-43a0-a842-aff8d056578cabc.jpg','2023-07-22','image'),
(20,'static/uploads/06c1eb5d-81d6-41e3-b7e2-b750bdd1f67babc.jpg','2023-07-22','image'),
(21,'static/uploads/6cf6c241-8edd-4d34-be17-be6bb4186c8fabc.jpg','2023-07-22','image'),
(22,'static/uploads/715260e3-e50b-4178-bb06-0acaf597a205abc.jpg','2023-07-22','image'),
(23,'static/uploads/68f6f9d4-d249-46e2-bd36-9b9ac7ddf4baabc.jpg','2023-07-22','image'),
(24,'static/uploads/6d25f408-7161-4fd1-8f24-459d48364b5dabc.jpg','2023-07-22','image'),
(25,'static/uploads/554c2613-19a6-4b15-917d-1ff92e82077aabc.jpg','2023-07-22','image'),
(26,'static/uploads/28be1432-30fa-4bc8-8127-cf29ebfacf90abc.jpg','2023-07-22','image'),
(27,'static/uploads/69c5a9dc-6bf5-45a7-a7f8-a89b1d81dbb1abc.jpg','2023-07-22','image'),
(28,'static/uploads/d9252a3d-a547-40c7-abe0-e672ff52463eabc.jpg','2023-07-22','image'),
(29,'static/uploads/67d3fb60-51ef-4b87-854e-9f77d3a0b012abc.jpg','2023-07-22','image'),
(30,'static/uploads/ad4c99c1-fbfd-4aa5-b229-dedc928faf6babc.jpg','2023-07-22','image'),
(31,'static/uploads/5993c48a-6ab3-4438-be28-bf76ce1ade1e.jpg','2023-07-24','video'),
(32,'static/uploads/08d60756-d42b-44bb-9a24-68ec1db68d3f.jpg','2023-07-24','video'),
(33,'static/uploads/bef3fe28-e2a2-41fe-83af-a8aec127b1ca.jpg','2023-07-24','video'),
(34,'static/uploads/3aaa3939-7faf-4426-a543-b78996b28c3c.jpg','2023-07-24','video'),
(35,'static/uploads/964a4d20-800c-4cdb-8980-db5c5defcb4d.jpg','2023-07-24','video'),
(36,'static/uploads/fb3aad3b-db3b-4825-b6a7-88d5b5cdcd0f.jpg','2023-07-24','video'),
(37,'static/uploads/830a299e-3b40-4935-9940-546d2b327c20.jpg','2023-07-24','video'),
(38,'static/uploads/9d80dd01-50bb-4e87-aeea-8c0c1e00cc63abc.mp4','2023-07-24','video'),
(39,'static/uploads/94edad86-0be4-4546-b272-90adbdcb907fabc.mp4','2023-07-24','video'),
(40,'static/uploads/93477635-ad58-4f7e-ab3b-3daa1565b381abc.mp4','2023-07-24','video'),
(41,'static/uploads/96f3bbcc-d8b3-49ab-8aa4-6afe24cc5223abc.mp4','2023-07-24','video'),
(42,'static/uploads/08d3ce7d-243a-4635-b4c8-914f46f2704aabc.mp4','2023-07-24','video'),
(43,'static/uploads/910da601-be83-4ffe-a912-e41584c27a7aabc.jpg','2023-07-24','image'),
(44,'static/uploads/5132cf96-9fd1-40b4-bac6-2be69a5aa283abc.jpg','2023-07-24','image');

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
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values 
(4,6,'Renuka Kamath','Renuka Kamath','dghdj','1234567890','renukakamath2@gmail.com'),
(2,3,'user','qwerty','ernakulam1','2345678907','student@gmail.com'),
(3,5,'dudu','dudy','dye','9876666688','ejjeddd@hds.com'),
(5,7,'Renuka Kamath','Renuka Kamath','dghdj','1234567890','renukakamath2@gmail.com'),
(6,8,'Renuka Kamath','Renuka Kamath','dhjj','1234567890','renukakamath2@gmail.com'),
(7,9,'Renuka Kamath','Renuka Kamath','bcbdb','1234567890','renukakamath2@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
