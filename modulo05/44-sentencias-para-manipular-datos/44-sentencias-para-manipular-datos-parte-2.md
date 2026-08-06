# Sentencias para la Manipulación de Datos (Parte II)
## Manipulación de datos y transaccionalidad en las operaciones

---

## 📚 Contenido del Curso

### Unidades:
1. **Bases de datos relacionales**
2. **Manipulación de datos y transaccionalidad en las operaciones** ← Ubicación actual
3. Definición de tablas
4. Modelos Entidad-Relación y Relacional

---

## 🎯 Objetivos de Aprendizaje

- **Utilizar** sentencias de ingreso, actualización y borrado de registros utilizando lenguaje DML para manipular la información de tablas con integridad referencial de acuerdo a un modelo de datos existente.

---

## 📊 Tipos de Datos Frecuentemente Utilizados

| Categoría | Tipos de Datos | Descripción |
|-----------|----------------|-------------|
| **Tipos numéricos** | `INT` / `SMALLINT` / `BIGINT` | Números enteros |
| | `FLOAT` / `DOUBLE` | Números decimales |
| **Tipos de caracteres** | `CHAR` / `VARCHAR` | Cadenas de texto |
| | `TEXT` | Texto largo |
| **Tipos temporales** | `DATE` | Solo fecha |
| | `TIME` | Solo hora |
| | `TIMESTAMP` | Fecha y hora |
| **Tipos booleanos** | `BOOLEAN` | Verdadero/Falso |
| **Avanzados** | `ARRAY`, `JSON`, `UUID` | No se cubren en este curso |

> **Importante:** Al definir el tipo de dato evitamos que se guarden datos de tipo distinto, protegiendo así los datos.

---

## 🔒 Restricciones (Constraints)

Las restricciones nos permiten agregar **"protecciones" adicionales** para cuidar los datos.

### Integridad de datos = Correctitud + Completitud

| Restricción | Descripción | Ejemplo |
|-------------|-------------|---------|
| **NOT NULL** | Impide valores nulos | `nombre VARCHAR NOT NULL` |
| **UNIQUE** | Asegura valores únicos | `rut VARCHAR UNIQUE` |
| **PRIMARY KEY** | NOT NULL + UNIQUE | `id SERIAL PRIMARY KEY` |
| **FOREIGN KEY** | Relaciona tablas | `autor_id REFERENCES autores(id)` |

---

## 🛡️ Restricción NOT NULL

### Ejemplo de error con NOT NULL

```sql
-- Tabla con restricción NOT NULL en nombre
CREATE TABLE empleados (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50),
    rut VARCHAR(20) UNIQUE
);

-- ❌ Esto generará un error
INSERT INTO empleados(apellido) VALUES ('Gómez');
```

**Error esperado:**
```
ERROR:  null value in column "nombre" violates not-null constraint
```

---

## 🔐 Restricción UNIQUE

### Ejemplo de error con UNIQUE

```sql
-- Insert correcto
INSERT INTO empleados (nombre, apellido, rut) 
VALUES ('Juan', 'Gonzalez', 'RUT1');

-- Insert correcto
INSERT INTO empleados (nombre, apellido, rut) 
VALUES ('Maria', 'Perez', 'RUT2');

-- ❌ Esto generará un error (RUT duplicado)
INSERT INTO empleados (nombre, apellido, rut) 
VALUES ('Pedro', 'Fuentes', 'RUT2');
```

**Error esperado:**
```
ERROR:  duplicate key value violates unique constraint "empleados_rut_key"
DETAIL:  Key (rut)=(RUT2) already exists.
```

---

## 🔗 PRIMARY KEY y FOREIGN KEY

### Estructura de tablas relacionadas

**Tabla Autores:**
```sql
CREATE TABLE Autores (
    AutorID INT PRIMARY KEY,
    NombreAutor VARCHAR(50)
);
```

**Tabla Libros:**
```sql
CREATE TABLE Libros (
    LibroID INT PRIMARY KEY,
    Titulo VARCHAR(100),
    AutorID INT,
    FOREIGN KEY (AutorID) REFERENCES Autores(AutorID)
);
```

---

## ⚠️ Ejemplos de Errores con PK y FK

### Error 1: Violación de PRIMARY KEY
```sql
-- ❌ Error: AutorID 2 ya existe
INSERT INTO Autores (AutorID, NombreAutor) 
VALUES (2, 'Nuevo autor');
```

### Error 2: Violación de FOREIGN KEY
```sql
-- ❌ Error: AutorID 1 no existe en Autores
INSERT INTO Libros (LibroID, Titulo, AutorID) 
VALUES (101, 'Libro Ejemplo', 1);
```

### Error 3: Violación al eliminar con FK
```sql
-- ❌ Error: El autor tiene libros asociados
DELETE FROM Autores WHERE AutorID = 2;
```

---

## 🤔 Pregunta Clave

> ¿Por qué son importantes las restricciones?

**Respuesta:** Las restricciones garantizan la **integridad de los datos**, evitando:
- Datos nulos en campos requeridos
- Duplicación de información
- Relaciones inválidas entre tablas
- Inconsistencias en la base de datos

---

## 🔢 Identificadores Auto Incrementados

### ¿Por qué usar SERIAL?

Hasta ahora, al definir el campo ID, lo hacíamos manualmente.  
**SERIAL** automatiza la definición de identificadores únicos.

### Ejemplo con SERIAL

```sql
-- Paso 1: Crear base de datos
CREATE DATABASE restricciones_psql;

-- Paso 2: Crear tabla con SERIAL
CREATE TABLE company (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL UNIQUE
);

-- Paso 3: Insertar registros (sin definir ID)
INSERT INTO company(nombre) VALUES('Amazon');
INSERT INTO company(nombre) VALUES('Apple');

-- Los IDs se generan automáticamente: 1, 2, 3, ...
```

---

## ✅ Validación de Restricciones

### Probando UNIQUE con SERIAL

```sql
-- ❌ Error: nombre duplicado
INSERT INTO company(nombre) VALUES('Apple');
```

**Error esperado:**
```
ERROR:  duplicate key value violates unique constraint "company_nombre_key"
DETAIL:  Key (nombre)=(Apple) already exists.
```

---

## 🎯 Ejercicio Propuesto

### "Comprueba la restricción NOT NULL del campo nombre"

**Objetivo:** Verificar que la restricción NOT NULL funciona correctamente.

```sql
-- Intenta insertar un registro sin nombre
INSERT INTO company(nombre) VALUES(NULL);
```

> ❓ **Reflexión:** ¿Por qué es importante la integridad referencial en las tablas?

---

## 📝 Ejercicio: Agregando Campos y Operando Registros

### Paso 1: Agregar nuevos campos con ALTER TABLE

```sql
-- Agregar dirección
ALTER TABLE company ADD COLUMN direccion VARCHAR(100);

-- Agregar años de servicio
ALTER TABLE company ADD COLUMN anios_servicio INTEGER;

-- Agregar nómina
ALTER TABLE company ADD COLUMN nomina DECIMAL(10,2);
```

### Paso 2: Eliminar datos existentes

```sql
-- Eliminar todos los registros
DELETE FROM company;
```

### Paso 3: Insertar nuevos registros con todos los campos

```sql
INSERT INTO company (nombre, direccion, anios_servicio, nomina) 
VALUES 
('Amazon', 'Seattle, WA', 29, 1000000),
('Apple', 'Cupertino, CA', 45, 1500000),
('Google', 'Mountain View, CA', 25, 1200000);
```

### Paso 4: Validar restricción NOT NULL

```sql
-- ❌ Esto debería fallar
INSERT INTO company (nombre, anios_servicio, nomina) 
VALUES ('Microsoft', 46, 800000);
```

---

## 🤔 Preguntas de Reflexión

1. ¿Cuál fue el concepto que más te costó comprender?

2. ¿Por qué es importante la integridad referencial en las tablas?

3. ¿Qué sucede si intentamos insertar un registro que viola una restricción?

---

## 💎 Ideas Clave

1. **Las restricciones** nos permiten agregar protecciones adicionales para cuidar los datos.

2. Al crear tablas, podemos añadir **constraints** a las columnas para evitar que se ingresen datos que no cumplan ciertas condiciones.

3. Las restricciones y el correcto uso de tipos de datos nos ayudan a evitar **problemas de integridad de datos**.

4. En SQL es posible **automatizar** la definición de identificadores utilizando la sentencia **`SERIAL`**.

---

## 📋 Resumen de Restricciones

| Restricción | Sintaxis | Propósito |
|-------------|----------|-----------|
| **NOT NULL** | `columna tipo NOT NULL` | El campo no puede estar vacío |
| **UNIQUE** | `columna tipo UNIQUE` | El valor debe ser único |
| **PRIMARY KEY** | `columna tipo PRIMARY KEY` | Identificador único + NOT NULL |
| **FOREIGN KEY** | `FOREIGN KEY (col) REFERENCES tabla(col)` | Relaciona tablas |
| **CHECK** | `CHECK (condición)` | Valida condiciones específicas |
| **DEFAULT** | `columna tipo DEFAULT valor` | Valor por defecto |

---

## 🔍 Tipos de Datos y Restricciones en la Práctica

### Ejemplo completo

```sql
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    precio DECIMAL(10,2) DEFAULT 0.00 CHECK (precio >= 0),
    stock INTEGER NOT NULL CHECK (stock >= 0),
    categoria VARCHAR(50),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 📎 Guía de Ejercicios

Para practicar, utiliza los materiales de apoyo:
- **"Material de apoyo - Restricciones not null y unique"**
- **"Material de apoyo - Restricciones pk y fk"**

---

> ✅ **Objetivo logrado:** Utilizar sentencias de ingreso, actualización y borrado de registros utilizando lenguaje DML para manipular la información de tablas con integridad referencial de acuerdo a un modelo de datos existente.