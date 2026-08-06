-- Database: comidas_tipicas

-- DROP DATABASE IF EXISTS comidas_tipicas;

CREATE DATABASE comidas_tipicas
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE cocina_chilena(
	id INT,
	nombre VARCHAR(50)
);

INSERT INTO cocina_chilena VALUES
(1, 'Pastel de choclo'),
(2, 'Umitas');

SELECT * FROM cocina_chilena;

-- MODIFICAR EL VALOR 'Umitas' DEL SEGUNDO REGISTRO
UPDATE cocina_chilena SET nombre = 'Humitas' WHERE id = 2;

INSERT INTO cocina_chilena VALUES
(3, 'Pantrucas'), -- Es patrucas o pancutras
(4, 'Casuela'),
(5, 'Zopaipas');

UPDATE cocina_chilena SET nombre = 'Cazuela' WHERE id = 4;
UPDATE cocina_chilena SET nombre = 'Sopaipillas' WHERE id = 5;

DELETE FROM cocina_chilena
WHERE id = 2;

DELETE FROM cocina_chilena
WHERE id in (3, 4, 5);