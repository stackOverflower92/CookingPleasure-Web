-- MySQL dump 10.13  Distrib 5.6.19, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: CookingPleasure
-- ------------------------------------------------------
-- Server version	5.6.19-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `FirstApp_ingredient`
--

DROP TABLE IF EXISTS `FirstApp_ingredient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FirstApp_ingredient` (
  `Ingredient_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `quantity` varchar(50) NOT NULL,
  `recipes_id` int(11) NOT NULL,
  PRIMARY KEY (`Ingredient_id`),
  KEY `FirstApp_ingredient_ffad1027` (`recipes_id`),
  CONSTRAINT `FirstAp_recipes_id_308a7e3dc3901738_fk_FirstApp_recipe_Recipe_id` FOREIGN KEY (`recipes_id`) REFERENCES `FirstApp_recipe` (`Recipe_id`)
) ENGINE=InnoDB AUTO_INCREMENT=311 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FirstApp_ingredient`
--

LOCK TABLES `FirstApp_ingredient` WRITE;
/*!40000 ALTER TABLE `FirstApp_ingredient` DISABLE KEYS */;
INSERT INTO `FirstApp_ingredient` VALUES (292,'fesa di tacchino','400gr ',167),(293,'zucchine','2 grandi ',167),(294,'polpa di pomodoro','100gr ',167),(295,'soffritto di verdure','50gr ',167),(296,'vino bianco','mezzo bicchiere ',167),(297,'olio','2 cucchiai ',167),(298,'pomodori datterini','770gr ',168),(299,'basilico','10 foglioline ',168),(300,'olio','quanto basta ',168),(301,'aglio','2 spicchi ',168),(302,'spaghetti','400gr ',168),(303,'riso carnaroli','300 gr ',169),(304,'fave','200gr ',169),(305,'piselli','130 gr ',169),(306,'rosmarino fresco','qb ',169),(307,'olio extra vergine','qb ',169),(308,'sale','un pizzico ',169),(309,'pepe','un pizzico ',169),(310,'brodo vegetale','1 ',169);
/*!40000 ALTER TABLE `FirstApp_ingredient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FirstApp_list`
--

DROP TABLE IF EXISTS `FirstApp_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FirstApp_list` (
  `List_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`List_id`),
  KEY `FirstApp_list_e8701ad4` (`user_id`),
  CONSTRAINT `FirstApp_list_user_id_326fc51a830a84f4_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FirstApp_list`
--

LOCK TABLES `FirstApp_list` WRITE;
/*!40000 ALTER TABLE `FirstApp_list` DISABLE KEYS */;
INSERT INTO `FirstApp_list` VALUES (4,'Shopping List for Cena martedì',2),(5,'Shopping List for risotto con fave e piselli al rosmarino',2),(6,'Shopping List for Spaghetti al pomodoro',2);
/*!40000 ALTER TABLE `FirstApp_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FirstApp_list_ingredients`
--

DROP TABLE IF EXISTS `FirstApp_list_ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FirstApp_list_ingredients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `list_id` int(11) NOT NULL,
  `ingredient_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `list_id` (`list_id`,`ingredient_id`),
  KEY `FirstApp_list_ingredients_4da3e820` (`list_id`),
  KEY `FirstApp_list_ingredients_7a06a9e2` (`ingredient_id`),
  CONSTRAINT `D54b0b9bac56ffcc4571d98b1b3c3e39` FOREIGN KEY (`ingredient_id`) REFERENCES `FirstApp_ingredient` (`Ingredient_id`),
  CONSTRAINT `FirstApp_list__list_id_3da660ac33b439f8_fk_FirstApp_list_List_id` FOREIGN KEY (`list_id`) REFERENCES `FirstApp_list` (`List_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FirstApp_list_ingredients`
--

LOCK TABLES `FirstApp_list_ingredients` WRITE;
/*!40000 ALTER TABLE `FirstApp_list_ingredients` DISABLE KEYS */;
INSERT INTO `FirstApp_list_ingredients` VALUES (23,4,298),(21,4,299),(22,4,300),(20,4,301),(24,4,302),(17,4,303),(13,4,304),(16,4,305),(18,4,306),(14,4,307),(19,4,308),(15,4,309),(12,4,310),(30,5,303),(26,5,304),(29,5,305),(31,5,306),(27,5,307),(32,5,308),(28,5,309),(25,5,310),(36,6,298),(34,6,299),(35,6,300),(33,6,301),(37,6,302);
/*!40000 ALTER TABLE `FirstApp_list_ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FirstApp_menu`
--

DROP TABLE IF EXISTS `FirstApp_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FirstApp_menu` (
  `Menu_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`Menu_id`),
  KEY `FirstApp_menu_e8701ad4` (`user_id`),
  CONSTRAINT `FirstApp_menu_user_id_5648d6e4410e7b0f_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FirstApp_menu`
--

LOCK TABLES `FirstApp_menu` WRITE;
/*!40000 ALTER TABLE `FirstApp_menu` DISABLE KEYS */;
INSERT INTO `FirstApp_menu` VALUES (3,'Pranzo sabato',2),(4,'Cena martedì',2);
/*!40000 ALTER TABLE `FirstApp_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FirstApp_menu_recipes`
--

DROP TABLE IF EXISTS `FirstApp_menu_recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FirstApp_menu_recipes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `menu_id` int(11) NOT NULL,
  `recipe_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `menu_id` (`menu_id`,`recipe_id`),
  KEY `FirstApp_menu_recipes_93e25458` (`menu_id`),
  KEY `FirstApp_menu_recipes_da50e9c3` (`recipe_id`),
  CONSTRAINT `FirstApp_menu__menu_id_34287c63bf999a75_fk_FirstApp_menu_Menu_id` FOREIGN KEY (`menu_id`) REFERENCES `FirstApp_menu` (`Menu_id`),
  CONSTRAINT `FirstApp_recipe_id_6e3680941e981158_fk_FirstApp_recipe_Recipe_id` FOREIGN KEY (`recipe_id`) REFERENCES `FirstApp_recipe` (`Recipe_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FirstApp_menu_recipes`
--

LOCK TABLES `FirstApp_menu_recipes` WRITE;
/*!40000 ALTER TABLE `FirstApp_menu_recipes` DISABLE KEYS */;
INSERT INTO `FirstApp_menu_recipes` VALUES (4,3,167),(5,3,169),(7,4,168),(6,4,169);
/*!40000 ALTER TABLE `FirstApp_menu_recipes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FirstApp_recipe`
--

DROP TABLE IF EXISTS `FirstApp_recipe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `FirstApp_recipe` (
  `Recipe_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `author` varchar(100) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`Recipe_id`),
  KEY `FirstApp_recipe_e8701ad4` (`user_id`),
  CONSTRAINT `FirstApp_recipe_user_id_69ca7eea6132513c_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=170 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FirstApp_recipe`
--

LOCK TABLES `FirstApp_recipe` WRITE;
/*!40000 ALTER TABLE `FirstApp_recipe` DISABLE KEYS */;
INSERT INTO `FirstApp_recipe` VALUES (167,'Involtini di carne','appiattite le fettine di tacchino con il batticarne. Tagliate la zucchina a fettine sottili, nel senso della lunghezza. Appoggiate su ciascuna striscia di zucchina una fetta di carne, arrotolatela a involtino e chiudete con uno stecchino.\r\n\r\nScaldate l\'olio in una padella, unite le verdure per soffritto e cuocete un paio di minuti a fuoco basso, mescolando ogni tanto. Unite gli involtini al soffritto e fateli rosolare per 3-4 minuti circa; spruzzate con il vino, fate evaporare e cuocete per 2-3 minuti a fuoco vivo. Unite la polpa di pomodoro, salate e cuocete ancora per 5 minuti.','nonna','Involtini di carne_utente_foto2.jpg',2),(168,'Spaghetti al pomodoro','Lavate bene tutti i pomodori. Buttate i pomodori interi in una pentola con acqua salata in ebollizione, scolateli dopo qualche minuto, lasciateli raffreddare e sbucciateli.\r\n\r\nTagliate i pomodori a pezzi. Prendete una casseruola ampia e antiaderente, versatevi tre cucchiai di olio extravergine di oliva, e portatelo a temperatura. Pelate le cipolle, tritatele. Fatele soffriggere dolcemente nell\'olio. Aggiungete i pomodori e fateli cuocere a fiamma media fino a quando l\'acqua dell\'ortaggio non si rapprende regalandoci una meravigliosa salsa, sempre mescolando di quando in quando (circa 25 minuti).\r\n\r\nAggiungete una presa di zucchero per regolare l\'acidità. Nel frattempo lessate gli spaghetti in abbondante acqua salata in ebollizione, scolateli al dente. A fine cottura dei pomodori freschi, insaporite con sale e basilico sminuzzato. Spegnete i fornelli e lasciate riposare il tutto per qualche minuto. Versate gli spaghetti direttamente nella pentola della salsa (se non dovete conservarla) e mescolate per bene. Impiattate e condite con un filo di olio d\'oliva a crudo.','mamma','Spaghetti al pomodoro_utente_foto1.jpeg',2),(169,'risotto con fave e piselli al rosmarino','Lessiamo le fave e le priviamo della pellicina, sbollentiamo per qualche minuto i piselli. Tostiamo il riso con un filo d’olio, saliamo leggermente, uniamo qualche mestolo di brodo (possiamo prepararlo usando l’acqua di cottura di fave e piselli) e dopo una decina di minuti anche i piselli.\r\n\r\nProseguiamo la cottura unendo liquido quando necessario e nel frattempo frulliamo le fave con un goccio d’olio e un po’ di brodo vegetale in modo da ottenere una crema non troppo liquida, saliamo e regoliamo di pepe. Quando il riso è ormai a cottura uniamo fuori dal fuoco la crema di fave e abbondante rosmarino tritato, mantechiamo. Serviamo il risotto con i fiori di rosmarino, un’abbondante macinata di pepe nero e un filo d’olio a crudo.\r\n ','papà','risotto con fave e piselli al rosmarino_utente_foto3.jpg',2);
/*!40000 ALTER TABLE `FirstApp_recipe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add recipe',7,'add_recipe'),(20,'Can change recipe',7,'change_recipe'),(21,'Can delete recipe',7,'delete_recipe'),(22,'Can add ingredient',8,'add_ingredient'),(23,'Can change ingredient',8,'change_ingredient'),(24,'Can delete ingredient',8,'delete_ingredient'),(25,'Can add menu',9,'add_menu'),(26,'Can change menu',9,'change_menu'),(27,'Can delete menu',9,'delete_menu'),(28,'Can add list',10,'add_list'),(29,'Can change list',10,'change_list'),(30,'Can delete list',10,'delete_list');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$15000$clEz3aqbtDLJ$7wjL+edPib5qmc94Uphrc7f3OR4OnIqT3DLxoK4mUoQ=','2015-09-30 14:43:10',1,'Admin','diego','ballotta','diego.ballotta@gmail.com',1,1,'2015-09-11 09:28:06'),(2,'pbkdf2_sha256$15000$MPNIzbUGx5yg$e4AWmzp2WY7wYOPj5RCmdOcpN8uwVnA6XX4iC+iTbqc=','2015-09-30 14:43:45',0,'utente','Marco','Rossi','mail.utente@gmail.com',0,1,'2015-09-30 14:20:04');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-09-25 07:10:53','4','elisabetta',2,'No fields changed.',4,1),(2,'2015-09-25 07:11:08','4','elisabetta',3,'',4,1),(3,'2015-09-28 13:06:39','3','damiano',3,'',4,1),(4,'2015-09-28 13:06:39','6','elisabetta',3,'',4,1),(5,'2015-09-28 13:06:40','5','gianni',3,'',4,1),(6,'2015-09-28 13:06:40','7','pappa',3,'',4,1),(7,'2015-09-28 13:06:40','2','prova',3,'',4,1),(8,'2015-09-28 13:06:40','8','prova1',3,'',4,1),(9,'2015-09-30 14:33:31','1','Admin',2,'Changed username.',4,1),(10,'2015-09-30 14:43:26','2','utente',2,'Changed first_name and last_name.',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'recipe','FirstApp','recipe'),(8,'ingredient','FirstApp','ingredient'),(9,'menu','FirstApp','menu'),(10,'list','FirstApp','list');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-09-11 09:26:21'),(2,'auth','0001_initial','2015-09-11 09:26:28'),(3,'FirstApp','0001_initial','2015-09-11 09:26:28'),(4,'FirstApp','0002_auto_20150911_0926','2015-09-11 09:26:38'),(5,'admin','0001_initial','2015-09-11 09:26:40'),(6,'sessions','0001_initial','2015-09-11 09:26:41'),(7,'FirstApp','0003_auto_20150911_1222','2015-09-11 12:22:28'),(8,'FirstApp','0004_auto_20150911_1249','2015-09-11 12:49:49'),(9,'FirstApp','0005_auto_20150911_1320','2015-09-11 13:20:38'),(10,'FirstApp','0006_auto_20150930_1426','2015-09-30 14:26:47');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('77p14zk4658v58a3i28rn3mmssrrg13b','OGY0ZjA5ZmZjMmM0MzFiMWE1NDFkMTM5NzNkYmEwNzQyYTg3NDNmNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjU0NjY4NjczMjlmNDgwYWNiZjZjNThlOTA3ZTdhZmUwNTBmOWY3YjAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-10-02 11:18:55'),('hhcd9y3vse7xxw4sn902xlk6a0z34046','OGY0ZjA5ZmZjMmM0MzFiMWE1NDFkMTM5NzNkYmEwNzQyYTg3NDNmNjp7Il9hdXRoX3VzZXJfaGFzaCI6IjU0NjY4NjczMjlmNDgwYWNiZjZjNThlOTA3ZTdhZmUwNTBmOWY3YjAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-10-02 11:18:36'),('r1j0c04j6z7x2p00hqs4pxc2qc12hq9j','MTY0YjY0YzU3MDE4MDVlZGUzMTE5ODE0NDc5MWIzMmQ5NjZhMDQzZDp7fQ==','2015-10-08 20:07:23'),('syyr24fcnua96cjl0cyiu8hsh0082tss','MTY0YjY0YzU3MDE4MDVlZGUzMTE5ODE0NDc5MWIzMmQ5NjZhMDQzZDp7fQ==','2015-10-14 14:43:55');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-09-30 16:47:06
