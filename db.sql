-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         8.0.28 - MySQL Community Server - GPL
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para facereco
CREATE DATABASE IF NOT EXISTS `facereco` /*!40100 DEFAULT CHARACTER SET latin1 COLLATE latin1_spanish_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `facereco`;

-- Volcando estructura para tabla facereco.cliente
CREATE TABLE IF NOT EXISTS `cliente` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `CI` char(10) COLLATE latin1_spanish_ci NOT NULL DEFAULT '0',
  `Nombre` char(50) COLLATE latin1_spanish_ci NOT NULL DEFAULT '0',
  `Apellido` char(50) COLLATE latin1_spanish_ci NOT NULL DEFAULT '0',
  `Telefono` char(50) COLLATE latin1_spanish_ci DEFAULT '0',
  `Direccion` char(100) COLLATE latin1_spanish_ci DEFAULT '0',
  `Activo` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla facereco.cliente: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` (`id`, `CI`, `Nombre`, `Apellido`, `Telefono`, `Direccion`, `Activo`) VALUES
	(1, '4555666', 'Marcelo', 'González', '0981333555', 'José María Alfonzo Godoy', 1),
	(2, '5333000', 'Pedro', 'Martínez', '0981000111', 'Calle Giménez', 1),
	(4, '523455', 'Alfredo', 'agaggdfg', 'fgsghs', 'sefrsfh dfgfdfg', 1);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;

-- Volcando estructura para tabla facereco.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE latin1_spanish_ci NOT NULL DEFAULT '',
  `pass` varchar(50) COLLATE latin1_spanish_ci NOT NULL DEFAULT '',
  `privilegio` varchar(50) COLLATE latin1_spanish_ci NOT NULL DEFAULT '',
  `activo` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- Volcando datos para la tabla facereco.usuario: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` (`id`, `nombre`, `pass`, `privilegio`, `activo`) VALUES
	(1, 'admin', '123', 'Administrador', 1),
	(2, 'noelia', '123456', 'Usuario', 1);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
