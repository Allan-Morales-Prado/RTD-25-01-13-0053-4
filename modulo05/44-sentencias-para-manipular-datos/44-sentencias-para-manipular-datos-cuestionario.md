# Cuestionario: Manipulación de Datos

---

## Pregunta 1

**Dado el siguiente código:**

```sql
CREATE TABLE categorias (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    descripcion TEXT
);

INSERT INTO categorias (nombre, descripcion) VALUES 
('Electrónica', 'Productos tecnológicos'),
('Hogar', 'Artículos para el hogar'),
('Electrónica', 'Dispositivos y accesorios');
```

**¿Qué ocurre al ejecutar este bloque?**

A) Se crean 3 registros correctamente en la tabla
B) El primer INSERT falla porque la tabla no existe
C) El tercer INSERT falla por violación de UNIQUE en `nombre`
D) Error de sintaxis porque `SERIAL` no puede ser PRIMARY KEY

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**
**Justificación:** La columna `nombre` tiene la restricción `UNIQUE NOT NULL`. El primer INSERT agrega 'Electrónica' correctamente. El tercer INSERT intenta agregar nuevamente 'Electrónica', lo que viola la restricción UNIQUE y genera un error.
</details>

---

## Pregunta 2

**¿Cuál es el propósito principal de la restricción CHECK en SQL?**

A) Verificar que un valor sea único en toda la columna
B) Asegurar que un campo no contenga valores nulos
C) Validar que los valores cumplan una condición booleana específica
D) Establecer una relación entre dos tablas

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**
**Justificación:** La restricción CHECK permite validar que los datos insertados o actualizados cumplan con una condición booleana específica (ej: `CHECK (edad >= 18)`, `CHECK (precio > 0)`). Es una forma de garantizar la integridad de los datos a nivel de columna o tabla.

</details>

---

## Pregunta 3

**¿Cuál de las siguientes sentencias actualiza correctamente el precio de todos los productos de la categoría 'Electrónica', incrementándolos en un 10%?**

A) `UPDATE productos SET precio = precio * 1.10 WHERE categoria_id IN (SELECT id FROM categorias WHERE nombre = 'Electrónica');`
B) `UPDATE productos, categorias SET precio = precio * 1.10 WHERE categoria_id = id AND nombre = 'Electrónica';`
C) `UPDATE productos precio = precio * 1.10 FROM categorias WHERE nombre = 'Electrónica';`
D) `UPDATE productos SET precio = precio * 1.10 WHERE categoria_id = (SELECT id FROM categorias WHERE nombre = 'Electrónica');`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**
**Justificación:** La alternativa A es correcta porque usa una subconsulta con `IN` que permite seleccionar múltiples categorías con nombre 'Electrónica' (aunque sea única). La sintaxis es válida y actualiza todos los productos que pertenecen a esas categorías.

La alternativa B usa sintaxis incorrecta para UPDATE.  
La alternativa C falta `SET`.  
La alternativa D usa `=` que solo funciona si la subconsulta retorna un solo valor.

</details>

---

## Pregunta 4

**Dado el siguiente esquema:**

```
EMPLEADOS (id_emp, nombre, cargo, id_jefe)
DEPARTAMENTOS (id_dept, nombre, id_gerente)
PROYECTOS (id_proy, nombre, id_dept)
ASIGNACIONES (id_asig, id_emp, id_proy, horas)
```

**¿Qué columna representa una clave foránea que garantiza que cada proyecto pertenezca a un departamento existente?**

A) `id_dept` en PROYECTOS
B) `id_gerente` en DEPARTAMENTOS
C) `id_jefe` en EMPLEADOS
D) `id_proy` en ASIGNACIONES

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**
**Justificación:** La columna `id_dept` en la tabla PROYECTOS debe ser una clave foránea que referencia `id_dept` en DEPARTAMENTOS. Esto garantiza que cada proyecto esté asociado a un departamento existente en el sistema.
</details>

---

## Pregunta 5

**Dada la siguiente tabla:**

```sql
CREATE TABLE alumnos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    nota DECIMAL(4,2) CHECK (nota >= 0 AND nota <= 7),
    activo BOOLEAN DEFAULT TRUE
);

INSERT INTO alumnos (nombre, nota, activo) VALUES 
('Ana', 6.5, TRUE),
('Carlos', 4.0, FALSE),
('Diana', 8.0, TRUE);
```

**¿Cuál de los siguientes INSERT generará un error?**

A) `INSERT INTO alumnos (nombre, nota) VALUES ('Luis', 5.5);`
B) `INSERT INTO alumnos (nombre, nota, activo) VALUES ('Marta', -1.0, TRUE);`
C) `INSERT INTO alumnos (nombre, nota) VALUES ('Pedro', 0.0);`
D) `INSERT INTO alumnos (nombre, nota, activo) VALUES ('Sofia', 7.0, NULL);`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**
**Justificación:** La columna `nota` tiene la restricción `CHECK (nota >= 0 AND nota <= 7)`. El valor -1.0 viola esta condición, generando un error. Las demás alternativas cumplen con las restricciones establecidas.
</details>

---

## Pregunta 6

**¿Qué garantiza la combinación de restricciones NOT NULL y UNIQUE en una columna?**

A) Que la columna sea una clave primaria automáticamente
B) Que cada valor sea único y no pueda ser nulo
C) Que los valores puedan repetirse siempre que no sean nulos
D) Que la columna pueda tener valores duplicados pero no nulos

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**
**Justificación:** La combinación de NOT NULL y UNIQUE asegura que todos los valores en la columna sean únicos y que no existan valores nulos. Esta combinación es equivalente a lo que define una clave primaria, aunque técnicamente son restricciones diferentes.
</details>

---

## Pregunta 7

**¿Cuál es la forma correcta de eliminar todos los registros de la tabla `productos` donde el `stock` sea menor que 5?**

A) `DELETE FROM productos WHERE stock < 5;`
B) `REMOVE FROM productos WHERE stock < 5;`
C) `DELETE productos WHERE stock < 5;`
D) `DROP FROM productos WHERE stock < 5;`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**
**Justificación:** La sintaxis correcta para eliminar registros específicos es `DELETE FROM nombre_tabla WHERE condición;`. Las otras alternativas usan palabras clave incorrectas o sintaxis inválida.

</details>

---

## Pregunta 8

**En una base de datos, la tabla `prestamos` tiene las columnas `id_cliente`, `id_libro` y `fecha_prestamo`. Si el `id_cliente` está definido como FOREIGN KEY referenciando a `clientes(id)`, ¿qué sucederá si intentamos eliminar un cliente que tiene préstamos activos?**

A) El cliente se eliminará automáticamente junto con sus préstamos
B) La operación se completará sin problemas
C) Se generará un error de violación de clave foránea
D) El cliente se eliminará pero los préstamos quedarán huérfanos

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**
**Justificación:** Por defecto, las claves foráneas previenen la eliminación de registros padre que tienen registros hijo asociados. Esto mantiene la integridad referencial. Se generará un error indicando que existen préstamos asociados al cliente que se intenta eliminar.

</details>

---

## Pregunta 9

**En un diagrama Entidad-Relación, ¿cómo se representa una relación donde una entidad tiene una subordinación jerárquica consigo misma (ej: empleado con jefe que también es empleado)?**

A) Una relación de muchos a muchos con tabla intermedia
B) Una relación recursiva con clave foránea que referencia a la misma tabla
C) Dos tablas separadas (empleados y jefes)
D) Una relación de uno a uno con la misma tabla

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**
**Justificación:** Las relaciones recursivas se implementan mediante una clave foránea en la misma tabla que referencia a su propia clave primaria. Por ejemplo, en EMPLEADOS, una columna `id_jefe` que referencia a `id_empleado` de la misma tabla.

</details>

---

## Pregunta 10

**Dado el siguiente código:**

```sql
CREATE TABLE inventario (
    id SERIAL PRIMARY KEY,
    producto VARCHAR(100) NOT NULL,
    cantidad INTEGER DEFAULT 0,
    bodega VARCHAR(50)
);

CREATE UNIQUE INDEX idx_producto_bodega ON inventario (producto, bodega);

INSERT INTO inventario (producto, cantidad, bodega) VALUES 
('Laptop', 10, 'Santiago'),
('Laptop', 5, 'Concepción'),
('Mouse', 20, 'Santiago'),
('Mouse', 15, 'Concepción');
```

**¿Cuál de las siguientes inserciones violará el índice único creado?**

A) `INSERT INTO inventario (producto, cantidad, bodega) VALUES ('Teclado', 8, 'Santiago');`
B) `INSERT INTO inventario (producto, cantidad, bodega) VALUES ('Laptop', 3, 'Valparaíso');`
C) `INSERT INTO inventario (producto, cantidad, bodega) VALUES ('Mouse', 25, 'Santiago');`
D) `INSERT INTO inventario (producto, cantidad, bodega) VALUES ('Laptop', 7, 'Santiago');`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: D**
**Justificación:** El índice único se crea sobre la combinación `(producto, bodega)`. La combinación ('Laptop', 'Santiago') ya existe en la tabla (primer INSERT). Cualquier intento de insertar nuevamente esta combinación violará la unicidad. Las demás combinaciones son nuevas y válidas.


</details>

---

## Pregunta 11

**¿Qué caracteriza a la transaccionalidad en bases de datos relacionales?**

A) La capacidad de realizar múltiples consultas simultáneamente
B) El agrupamiento de operaciones que se ejecutan como una unidad atómica
C) La definición de estructuras de almacenamiento físicas
D) La optimización automática de consultas

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**
**Justificación:** La transaccionalidad permite agrupar varias operaciones DML en una unidad que se ejecuta completamente o no se ejecuta en absoluto (principio de atomicidad). Esto garantiza la consistencia de los datos ante fallos o errores.

</details>

---

## Pregunta 12

**Se necesita agregar una restricción para asegurar que el campo `telefono` en la tabla `contactos` tenga exactamente 9 dígitos. ¿Cuál es la sintaxis correcta usando ALTER TABLE?**

A) `ALTER TABLE contactos ADD CHECK (LENGTH(telefono) = 9);`
B) `ALTER TABLE contactos MODIFY COLUMN telefono CHECK (LENGTH(telefono) = 9);`
C) `ALTER TABLE contactos ADD CONSTRAINT ck_telefono CHECK (LENGTH(telefono) = 9);`
D) `ALTER TABLE contactos ADD CONSTRAINT CHECK (LENGTH(telefono) = 9) ON telefono;`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**
**Justificación:** La sintaxis correcta para agregar una restricción CHECK con nombre es:
```sql
ALTER TABLE tabla ADD CONSTRAINT nombre_constraint CHECK (condición);
```
La alternativa C es la única con la sintaxis correcta.


</details>

---

## Pregunta 13

**Dada la siguiente secuencia de comandos:**

```sql
-- Paso 1
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
);

-- Paso 2
INSERT INTO usuarios (username, email) VALUES 
('jperez', 'jperez@mail.com'),
('mgomez', 'mgomez@mail.com'),
('jperez', 'jperez2@mail.com');
```

**¿Cuál es el resultado de ejecutar ambos pasos?**

A) Se crea la tabla y se insertan 3 registros exitosamente
B) Se crea la tabla pero falla el Paso 2 por violación de PRIMARY KEY
C) Se crea la tabla pero falla el Paso 2 por violación de UNIQUE en `username`
D) Se crea la tabla pero falla el Paso 2 por violación de NOT NULL

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**
**Justificación:** El Paso 1 crea la tabla correctamente. En el Paso 2, el tercer INSERT intenta agregar 'jperez' nuevamente, violando la restricción UNIQUE de la columna `username`. Aunque el email es diferente, la restricción UNIQUE en `username` es suficiente para generar el error.

</details>

---

## Pregunta 14

**Dado el siguiente modelo físico:**

```
AUTORES (id_autor PK, nombre, nacionalidad)
EDITORIALES (id_editorial PK, nombre, pais)
LIBROS (id_libro PK, titulo, año, id_autor FK, id_editorial FK)
```

**¿Qué garantiza la integridad referencial en la tabla LIBROS?**

A) Que cada libro tenga un título único
B) Que `id_autor` y `id_editorial` existan en sus respectivas tablas
C) Que el año de publicación sea mayor a 1900
D) Que un libro pueda tener varios autores

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**
**Justificación:** Las claves foráneas `id_autor` y `id_editorial` en LIBROS garantizan que cada libro esté asociado a un autor y editorial existentes en sus respectivas tablas. Esto asegura la integridad referencial en el modelo.

</details>

---

## Pregunta 15

**¿Cuál de las siguientes sentencias elimina correctamente la columna `fecha_nacimiento` de la tabla `empleados`?**

A) `ALTER TABLE empleados DROP COLUMN fecha_nacimiento;`
B) `ALTER TABLE empleados REMOVE COLUMN fecha_nacimiento;`
C) `DELETE COLUMN fecha_nacimiento FROM empleados;`
D) `ALTER TABLE empleados DROP fecha_nacimiento;`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**
**Justificación:** La sintaxis correcta para eliminar una columna es:
```sql
ALTER TABLE nombre_tabla DROP COLUMN nombre_columna;
```
La alternativa A es la única que sigue correctamente esta sintaxis.

</details>

---

## Pregunta 16

**En una base de datos de ventas, si la tabla `ventas` tiene una columna `total` que siempre debe ser igual a la suma de los subtotales de los productos en `detalle_venta`, ¿qué mecanismo de integridad debería implementarse?**

A) Una restricción CHECK
B) Una restricción UNIQUE en `total`
C) Un trigger o función que actualice automáticamente el total
D) Una clave primaria compuesta

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**
**Justificación:** Este escenario requiere un trigger o función que actualice automáticamente el campo `total` al insertar, actualizar o eliminar registros en `detalle_venta`. Las restricciones CHECK no pueden hacer cálculos entre tablas, y UNIQUE solo verifica unicidad.

</details>

---

## Pregunta 17

**Dado el siguiente código:**

```sql
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precio DECIMAL(10,2) DEFAULT 0.00,
    categoria VARCHAR(30)
);

INSERT INTO productos (nombre, precio, categoria) VALUES 
('Smartphone', 599.99, 'Electrónica'),
('Tablet', 299.50, 'Electrónica'),
('Cafetera', 89.90, 'Hogar');
```

**¿Qué ocurre al ejecutar la siguiente sentencia?**

```sql
UPDATE productos SET precio = precio * 1.15 WHERE categoria = 'Electrónica';
```

A) Actualiza solo el precio del Smartphone
B) Actualiza los precios de todos los productos
C) Actualiza los precios de Smartphone y Tablet
D) Genera un error porque el precio tiene un DEFAULT

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**
**Justificación:** La sentencia UPDATE aplicará el incremento del 15% a todos los productos donde `categoria = 'Electrónica'`. Los productos que cumplen esta condición son 'Smartphone' y 'Tablet', por lo que ambos serán actualizados.


</details>

---

## Pregunta 18

**¿Qué relación existe entre una clave primaria y las claves foráneas que la referencian?**

A) Las claves foráneas pueden tener valores que no existan en la clave primaria
B) La clave primaria debe tener valores únicos para que las claves foráneas puedan referenciarla
C) Las claves foráneas son siempre iguales a la clave primaria
D) La clave primaria puede eliminarse aunque tenga claves foráneas asociadas

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**
**Justificación:** Para que una clave foránea pueda referenciar correctamente a otra tabla, la clave primaria referenciada debe garantizar la unicidad de sus valores. La relación implica que cada valor en la clave foránea debe existir en la clave primaria de la tabla referenciada.

</details>

---

## Pregunta 19

**En un diagrama ER, ¿qué significa una línea con un "pata de gallo" al final?**

A) Relación de uno a uno
B) Relación de uno a muchos
C) Relación de muchos a uno
D) Relación de muchos a muchos

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**
**Justificación:** En la notación de "pata de gallo" (crow's foot), la "pata" representa "muchos" y la línea simple representa "uno". Por lo tanto, una línea con una pata de gallo al final y una línea simple al otro extremo representa una relación de "uno a muchos".

</details>

---

## Pregunta 20

**Se necesita crear una tabla `cursos` donde el campo `id_profesor` debe ser opcional, pero si se proporciona, debe referenciar a un profesor existente en la tabla `profesores`. ¿Cuál es la definición correcta?**

A) `id_profesor INTEGER REFERENCES profesores(id) NOT NULL`
B) `id_profesor INTEGER REFERENCES profesores(id)`
C) `id_profesor INTEGER NOT NULL REFERENCES profesores(id)`
D) `id_profesor INTEGER FOREIGN KEY REFERENCES profesores(id)`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**
**Justificación:** Para que el campo sea opcional, no debe tener la restricción NOT NULL. La alternativa B define la clave foránea correctamente sin NOT NULL, permitiendo valores nulos que representan que el curso no tiene profesor asignado.

</details>