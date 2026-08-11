# DDL y DML - Reforzamiento

---

## ¿Qué es DDL?

**DDL** (Data Definition Language) es el lenguaje de definición de datos que permite:
- Definir las estructuras que almacenarán los datos
- Definir procedimientos o funciones que permitan consultarlos
- **SQL** es también un lenguaje de definición de datos

### Funcionalidades principales del DDL

| Función | Descripción |
|---------|-------------|
| **Creación** | Crear tablas y objetos en la base de datos |
| **Modificación** | Alterar la estructura de objetos existentes |
| **Borrado** | Eliminar tablas y objetos |
| **Otras operaciones** | Gestionar restricciones y definiciones |

---

## Operaciones Básicas sobre una Base de Datos

### Paso 1: Crear una base de datos
```sql
CREATE DATABASE nombre_base_de_datos;
```

### Paso 2: Mostrar todas las tablas
```sql
\dt;
```

### Paso 3: Mostrar una tabla específica
```sql
\dt nombre_tabla;
```

### Paso 4: Eliminar una tabla
```sql
DROP TABLE nombre_tabla;
```

### Paso 5: Modificar un campo de una tabla
```sql
ALTER TABLE nombre_tabla ADD column_name datatype;
```

---

## Creación de una Tabla

### Sintaxis básica
```sql
CREATE TABLE nombre_tabla (
    campo1 tipo_dato restricciones,
    campo2 tipo_dato restricciones,
    campo3 tipo_dato restricciones
);
```

### Ejemplo práctico
```sql
CREATE TABLE clientes (
    id INT UNIQUE NOT NULL PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    rut VARCHAR UNIQUE NOT NULL
);
```

---

## Tipos de Datos en SQL

| Categoría | Tipos de Datos | Descripción |
|-----------|---------------|-------------|
| **Numéricos** | INT, SMALLINT, BIGINT | Números enteros |
| | FLOAT, DOUBLE | Números decimales |
| **Caracteres** | CHAR, VARCHAR | Cadenas de texto |
| **Temporales** | DATE, TIME, TIMESTAMP | Fechas y horas |
| **Booleanos** | BOOLEAN | Verdadero/Falso |
| **Otros** | ARRAY, JSON, UUID | Tipos avanzados |

---

## Restricciones (Constraints)

Las restricciones en SQL se definen como **Constraint** y garantizan que los datos cumplan con ciertos parámetros.

### 1. CHECK
Condición de restricción que se define a una columna. La restricción se aplica cuando la evaluación es verdadera.

```sql
CREATE TABLE productos (
    precio DECIMAL CHECK (precio > 0),
    nombre VARCHAR(100)
);
```

### 2. NOT NULL
Una columna no puede recibir un valor nulo (obliga a ingresar algún dato).

```sql
CREATE TABLE productos (
    product_no INTEGER NOT NULL,
    name VARCHAR(40) NOT NULL
);
```

### 3. UNIQUE
Restricción de seguridad que asegura la información de una columna, previniendo la duplicación de datos.

```sql
CREATE TABLE productos (
    product_no INTEGER UNIQUE,
    name VARCHAR(40)
);
```

### 4. PRIMARY KEY
Restricción que asegura la información de una columna y además le otorga una identificación. Incorpora por defecto NOT NULL y UNIQUE.

```sql
CREATE TABLE productos (
    product_no INTEGER PRIMARY KEY,
    name VARCHAR(40)
);
```

### 5. FOREIGN KEY
Restricción que asegura que los datos de una tabla coincidan con los datos de otra tabla.

```sql
CREATE TABLE pedidos (
    pedido_id INTEGER PRIMARY KEY,
    producto_no INTEGER REFERENCES productos(product_no)
);
```

---

## Descripción de Tablas

Para ver la descripción de una tabla, primero conéctate a la base de datos y luego usa el comando:

```sql
\c nombre_base_datos
\d nombre_tabla
```

La descripción muestra:
- Campos de la tabla
- Tipos de datos
- Restricciones aplicadas

---

## Manejo de Datos Nulos

### Modificar una columna a NOT NULL

Si tienes registros existentes con valores nulos, primero debes actualizarlos:

```sql
-- Paso 1: Crear tabla con columna nullable
CREATE TABLE clientes (
    id INTEGER UNIQUE NOT NULL,
    name VARCHAR(25) NOT NULL,
    email VARCHAR(50)
);

-- Paso 2: Insertar registros
INSERT INTO clientes(id, name) VALUES (1, 'Nombre 1');
INSERT INTO clientes(id, name) VALUES (2, 'Nombre 2');
INSERT INTO clientes(id, name) VALUES (3, 'Nombre 3');

-- Paso 3: Intentar modificar a NOT NULL (genera error)
ALTER TABLE clientes ALTER COLUMN email SET NOT NULL;
-- ERROR: column "email" of relation "clientes" contains null values

-- Paso 4: Actualizar valores nulos
UPDATE clientes SET email = 'correo@ejemplo.com' WHERE email IS NULL;

-- Paso 5: Ahora sí se puede modificar
ALTER TABLE clientes ALTER COLUMN email SET NOT NULL;
```

### Asignar valores predeterminados con COALESCE

```sql
-- Agregar nuevo campo y asignar fecha predeterminada
UPDATE clientes 
SET fecha = COALESCE(fecha, '2024-01-01');
```

---

## Ejercicios Propuestos

### Ejercicio 1: Base de Datos Bancaria

Crear una base de datos que almacene información de clientes bancarios.

#### Tabla Clientes:
```sql
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    apellido VARCHAR NOT NULL,
    rut VARCHAR UNIQUE NOT NULL,
    telefono VARCHAR,
    email VARCHAR
);
```

#### Tabla Cuentas:
```sql
CREATE TABLE cuentas (
    id SERIAL PRIMARY KEY,
    numero_cuenta VARCHAR UNIQUE NOT NULL,
    fecha_creacion DATE NOT NULL,
    balance DECIMAL DEFAULT 0.00,
    cliente_id INTEGER REFERENCES clientes(id)
);
```

### Ejercicio 2: Datos Nulos en Productos

Un cliente tiene un dataset de productos con valores nulos en el campo SKU. Se solicita:

1. Modificar la tabla asignando "Dato no ingresado" a los SKU nulos
2. Impedir que futuros registros tengan SKU nulo

```sql
-- Actualizar valores nulos
UPDATE productos SET sku = COALESCE(sku, 'Dato no ingresado');

-- Modificar columna a NOT NULL
ALTER TABLE productos ALTER COLUMN sku SET NOT NULL;
```

---

## Tablas Relacionadas y Borrado

### Problema al borrar tablas relacionadas

Cuando existe una clave foránea, no se puede eliminar una tabla padre sin antes eliminar la tabla hija.

```sql
-- Error al intentar eliminar autores (tabla padre)
DELETE FROM autores;
-- ERROR: update or delete on table "autores" violates foreign key constraint

-- Primero eliminar la tabla hija
DELETE FROM libros;
-- Luego eliminar la tabla padre
DELETE FROM autores;
```

### Ejemplo completo de tablas relacionadas

```sql
-- Crear tabla autores (padre)
CREATE TABLE autores (
    id INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Crear tabla libros (hija)
CREATE TABLE libros (
    id INT NOT NULL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    autor_id INT NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES autores(id)
);

-- Insertar datos
INSERT INTO autores (id, nombre) VALUES
    (1, 'Juan Pérez'),
    (2, 'María García'),
    (3, 'Pedro Rodríguez');

INSERT INTO libros (id, titulo, autor_id) VALUES
    (1, 'El Quijote', 1),
    (2, 'La Divina Comedia', 2),
    (3, 'Hamlet', 3);

-- Consulta con JOIN
SELECT libros.titulo, autores.nombre
FROM libros
INNER JOIN autores ON libros.autor_id = autores.id;
```

---

## Modificación de Tablas con ALTER TABLE

### Modificar tipo de dato de una columna
```sql
ALTER TABLE phones ALTER COLUMN mac_address TYPE VARCHAR(50);
```

### Agregar restricción NOT NULL
```sql
ALTER TABLE phones ALTER COLUMN mac_address SET NOT NULL;
```

### Agregar nuevas columnas
```sql
ALTER TABLE phones ADD COLUMN memoria_interna VARCHAR(20);
ALTER TABLE phones ADD COLUMN memoria_ram VARCHAR(20);
ALTER TABLE phones ADD COLUMN peso VARCHAR(20);
ALTER TABLE phones ADD COLUMN dimensiones VARCHAR(50);
```

### Modificar columna a SERIAL (autoincremental)
```sql
-- Crear una secuencia
CREATE SEQUENCE phones_id_seq START 1;

-- Asignar valor por defecto
ALTER TABLE phones ALTER COLUMN id SET DEFAULT NEXTVAL('phones_id_seq');
```

---

## DROP TABLE vs TRUNCATE

### DROP TABLE
```sql
DROP TABLE nombre_tabla;
```

**Características:**
- Elimina completamente la tabla y su estructura
- Debe ser ejecutado por un super usuario
- Acción irreversible (sin backup)
- Requiere precaución extrema

### TRUNCATE
```sql
TRUNCATE nombre_tabla;
```

**Características:**
- Similar a DELETE (elimina registros)
- No afecta el schema de la base de datos
- **Reinicio de identidades:** Reinicia automáticamente las secuencias
- **Cascada:** Modifica todas las tablas relacionadas
- No elimina la estructura de la tabla

---

## Ejercicio Práctico Final

### Contexto
Crear una base de datos "mawashi_phones" para una tienda de teléfonos.

**Requisitos iniciales:**
- Dirección MAC (12 dígitos agrupados en pares)
- Modelo del dispositivo
- Año de fabricación

**Campos adicionales solicitados:**
- Memoria interna
- Memoria RAM
- Peso
- Dimensiones

```sql
-- Crear base de datos
CREATE DATABASE mawashi_phones;

-- Conectarse a la base de datos
\c mawashi_phones;

-- Crear tabla inicial
CREATE TABLE phones (
    id SERIAL PRIMARY KEY,
    modelo VARCHAR(50),
    mac_address VARCHAR(50) UNIQUE NOT NULL,
    fecha_fabricacion DATE
);

-- Insertar datos de prueba
INSERT INTO phones (modelo, mac_address, fecha_fabricacion) 
VALUES ('Iphone 14', '1B:2A:3C:4D:5F:6G', '2022-09-09');

-- Agregar nuevas columnas
ALTER TABLE phones ADD COLUMN memoria_interna VARCHAR(20);
ALTER TABLE phones ADD COLUMN memoria_ram VARCHAR(20);
ALTER TABLE phones ADD COLUMN peso VARCHAR(20);
ALTER TABLE phones ADD COLUMN dimensiones VARCHAR(50);

-- Ver estructura de la tabla
\d phones;
```

---

## Resumen de Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| **DDL** | Lenguaje de definición de datos para crear/modificar estructuras |
| **Constraints** | Reglas que garantizan la integridad de los datos |
| **NOT NULL** | Impide valores nulos en una columna |
| **UNIQUE** | Garantiza valores únicos en una columna |
| **PRIMARY KEY** | Identificador único de cada registro |
| **FOREIGN KEY** | Relaciona datos entre tablas |
| **ALTER TABLE** | Modifica la estructura de una tabla existente |
| **DROP TABLE** | Elimina permanentemente una tabla |
| **TRUNCATE** | Elimina todos los registros pero mantiene la estructura |
| **COALESCE** | Asigna valores predeterminados a campos nulos |
