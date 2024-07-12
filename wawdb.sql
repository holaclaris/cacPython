-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 12-07-2024 a las 04:52:37
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `wawdb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paquetes`
--

CREATE TABLE `paquetes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `destino` varchar(100) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `imagen` text DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `disponible` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `paquetes`
--

INSERT INTO `paquetes` (`id`, `nombre`, `destino`, `descripcion`, `imagen`, `precio`, `disponible`) VALUES
(1, 'Tour por la Gran Muralla China', 'China', 'Explora la antigua Gran Muralla China en un recorrido de 5 días.', 'https://plus.unsplash.com/premium_photo-1664304488525-44a96338c0cc?q=80&w=1775&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 1200.00, 1),
(2, 'Vacaciones en Bali', 'Indonesia', 'Disfruta de las hermosas playas y la cultura única de Bali en un viaje de 7 días.', 'https://static.saltinourhair.com/wp-content/uploads/2023/02/24124740/DSC9452.jpg', 1400.00, 1),
(3, 'Visita a las Pirámides de Giza', 'Egipto', 'Descubre las maravillas del antiguo Egipto en un tour de 6 días.', 'https://images.unsplash.com/photo-1539768942893-daf53e448371?q=80&w=1771&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 1600.00, 1),
(4, 'Aventura en el Amazonas', 'Brasil', 'Explora la selva amazónica en una aventura de 8 días llena de naturaleza y emoción.', 'https://fotografias.larazon.es/clipping/cmsimages01/2022/08/14/B83143A1-02B4-4874-B656-CF0E2F9FAD06/98.jpg?crop=4551,2561,x0,y236&width=1900&height=1069&optimize=low&format=webply', 1700.00, 0),
(5, 'Ruta del Vino en Mendoza', 'Argentina', 'Disfruta de una experiencia única de 4 días en los viñedos de Mendoza.', 'data:image/jpeg;base64,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', 1200.00, 1),
(6, 'Safari en el Serengeti', 'Tanzania', 'Experimenta un safari increíble en el parque nacional del Serengeti durante 6 días.', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9JDemE3FNf9rAE5CgdJOs_VsLa50A_E9Gnw&s', 2000.00, 1),
(7, 'Descubre Nueva York', 'Estados Unidos', 'Explora la ciudad de Nueva York en un viaje de 5 días lleno de actividades y visitas turísticas.', 'https://hips.hearstapps.com/hmg-prod/images/nueva-york-1521191396.jpg?crop=1.00xw:0.751xh;0,0.0933xh&resize=2048:*', 1800.00, 1),
(8, 'Escapada a París', 'Francia', 'Visita la ciudad del amor en un recorrido de 4 días por París.', 'https://images.unsplash.com/photo-1499856871958-5b9627545d1a?q=80&w=1720&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 1500.00, 1),
(9, 'Trekking en los Andes', 'Perú', 'Realiza un trekking de 7 días por los impresionantes Andes peruanos, incluyendo una visita a Machu Picchu.', 'https://images.unsplash.com/photo-1565451987600-ea251b7eabcf?q=80&w=1879&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 1900.00, 1);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `paquetes`
--
ALTER TABLE `paquetes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `paquetes`
--
ALTER TABLE `paquetes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
