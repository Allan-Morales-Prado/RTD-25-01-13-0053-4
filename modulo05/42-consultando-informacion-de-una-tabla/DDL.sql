-- Database: newdb

-- DROP DATABASE IF EXISTS newdb;

CREATE DATABASE newdb
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE categorias (
    id_categoria SERIAL PRIMARY KEY,
    nombre_categoria VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT,
    estado VARCHAR(20) DEFAULT 'activo',
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,           -- PostgreSQL (AUTO_INCREMENT en MySQL)
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    direccion TEXT,
    fecha_registro DATE DEFAULT CURRENT_DATE,
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE empleados (
    id_empleado SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    telefono VARCHAR(20),
    cargo VARCHAR(50) NOT NULL,
    fecha_contratacion DATE DEFAULT CURRENT_DATE,
    salario DECIMAL(10,2),
    estado VARCHAR(20) DEFAULT 'activo'
);

CREATE TABLE proveedores (
    id_proveedor SERIAL PRIMARY KEY,
    nombre_proveedor VARCHAR(150) NOT NULL,
    contacto VARCHAR(100),
    telefono VARCHAR(20),
    email VARCHAR(150),
    direccion TEXT,
    condiciones_pago TEXT,
    calificacion INTEGER CHECK (calificacion >= 1 AND calificacion <= 5)
);

CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    id_categoria INTEGER REFERENCES categorias(id_categoria),
    codigo_barras VARCHAR(50) UNIQUE,
    nombre_producto VARCHAR(200) NOT NULL,
    descripcion TEXT,
    precio_compra DECIMAL(10,2) NOT NULL,
    precio_venta DECIMAL(10,2) NOT NULL,
    stock_actual INTEGER DEFAULT 0,
    stock_minimo INTEGER DEFAULT 10,
    unidad_medida VARCHAR(20) DEFAULT 'unidad',
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    id_empleado INTEGER REFERENCES empleados(id_empleado),
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contraseña_hash VARCHAR(255) NOT NULL,     -- Almacenar hash, no texto plano
    rol VARCHAR(30) DEFAULT 'usuario',         -- admin, supervisor, vendedor
    ultimo_acceso TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);

CREATE TABLE ventas (
    id_venta SERIAL PRIMARY KEY,
    id_cliente INTEGER REFERENCES clientes(id_cliente),
    id_empleado INTEGER REFERENCES empleados(id_empleado),
    numero_factura VARCHAR(20) UNIQUE NOT NULL,
    fecha_venta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_venta DECIMAL(12,2) NOT NULL,
    metodo_pago VARCHAR(30) DEFAULT 'efectivo',
    estado VARCHAR(20) DEFAULT 'completada',
    observaciones TEXT
);

CREATE TABLE compras (
    id_compra SERIAL PRIMARY KEY,
    id_proveedor INTEGER REFERENCES proveedores(id_proveedor),
    numero_orden VARCHAR(20) UNIQUE NOT NULL,
    fecha_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_compra DECIMAL(12,2) NOT NULL,
    estado VARCHAR(20) DEFAULT 'pendiente'
);

CREATE TABLE detalle_ventas (
    id_detalle SERIAL PRIMARY KEY,
    id_venta INTEGER REFERENCES ventas(id_venta),
    id_producto INTEGER REFERENCES productos(id_producto),
    cantidad INTEGER NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(12,2) NOT NULL,
    descuento DECIMAL(10,2) DEFAULT 0,
    total_linea DECIMAL(12,2) NOT NULL
);

CREATE TABLE auditoria (
    id_auditoria SERIAL PRIMARY KEY,
    tabla_afectada VARCHAR(50) NOT NULL,
    accion VARCHAR(20) NOT NULL,              -- INSERT, UPDATE, DELETE
    id_registro INTEGER NOT NULL,
    usuario VARCHAR(100) DEFAULT CURRENT_USER,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    datos_anteriores JSONB,                   -- PostgreSQL
    datos_nuevos JSONB                         -- PostgreSQL
);

-- Índices para consultas rápidas
CREATE INDEX idx_ventas_cliente ON ventas(id_cliente);
CREATE INDEX idx_ventas_fecha ON ventas(fecha_venta);
CREATE INDEX idx_productos_categoria ON productos(id_categoria);
CREATE INDEX idx_productos_nombre ON productos(nombre_producto);
CREATE INDEX idx_detalle_venta ON detalle_ventas(id_venta);
CREATE INDEX idx_detalle_producto ON detalle_ventas(id_producto);

