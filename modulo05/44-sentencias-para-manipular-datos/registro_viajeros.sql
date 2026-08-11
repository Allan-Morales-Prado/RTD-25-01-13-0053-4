-- Crear tabla Viajeros
CREATE TABLE viajeros(
    viajero_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    genero CHAR(5) NOT NULL,
    email VARCHAR(250),
    telefono CHAR(50) NOT NULL,
    rut CHAR(10) NOT NULL UNIQUE
);

-- Crear tabla Destinos
CREATE TABLE destinos(
    destino_id SERIAL PRIMARY KEY,
    nombre_destino VARCHAR(100) NOT NULL,
    ciudad VARCHAR(50),
    pais VARCHAR(50)
);

-- Crear tabla Tickets
CREATE TABLE tickets(
    ticket_id SERIAL PRIMARY KEY,
    viajero_id INTEGER REFERENCES viajeros(viajero_id),
    destino_id INTEGER REFERENCES destinos(destino_id),
    fecha_emision DATE,
    fecha_retorno DATE,
    fecha_salida DATE,
    numero_boleto VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE pais(
    pais_id SERIAL PRIMARY KEY,
    nombre_pais VARCHAR(30) NOT NULL,
    ciudad VARCHAR(50) NOT NULL,
    codigo_postal INTEGER NOT NULL
);

INSERT INTO pais (nombre_pais, ciudad, codigo_postal) VALUES
('México', 'Ciudad de México', 1000),
('Perú', 'Lima', 15001),
('Chile', 'Santiago', 8320000),
('Australia', 'Canberra', 2600),
('Nepal', 'Katmandú', 44600),
('Grecia', 'Atenas', 10431),
('Marruecos', 'Rabat', 10000),
('Japón', 'Tokio', 1000001);