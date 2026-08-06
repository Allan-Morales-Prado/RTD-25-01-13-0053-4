-- Database: mascotas

-- DROP DATABASE IF EXISTS mascotas;

CREATE DATABASE mascotas
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE animal(
	id INTEGER,
	nombre VARCHAR(15),
	raza VARCHAR(30),
	edad INTEGER
);

--- Inserción de datos
INSERT INTO animal (id, nombre, raza, edad) VALUES
(1, 'Firulais', 'Pastor Aleman', 4), -- ERROR
(2, 'Luna', 'Labrador Retriever', 2),
(3, 'Mishi', 'Persa', 5),
(4, 'Rocky', 'Bóxer', 3),
(5, 'Nala', 'Siames', 2), -- ERROR
(6, 'Toby', 'Bulldog Francés', 6),
(7, 'Simba', 'Maine Coon', 4),
(8, 'Lola', 'Pug', 3),
(9, 'Sasha', 'Husky Siberiano', 5),
(10, 'Garfiel', 'Naranja', 7), -- ERROR
(11, 'Miarucio', 'Bombai', 5), --ERROR
(12, 'Pugberto', 'Pug', 5);

SELECT * FROM animal ORDER BY id;

-- UPDATES
UPDATE animal SET raza = 'Pastor Alemán' WHERE id = 1;
UPDATE animal SET nombre = 'Garfield' WHERE id = 10;
UPDATE animal SET nombre = 'Mauricio' WHERE id = 11;

-- DELETE
DELETE FROM animal WHERE id in (5, 7, 8);

-- Actualización masiva de la edad
UPDATE animal SET edad = 3;

DELETE FROM animal;