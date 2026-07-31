# Consultando información relacionada en varias tablas

## Modelos de datos

Un **modelo de datos** se refiere a una representación estructurada y organizada de los datos que se almacenan en una base de datos relacional. Define la estructura lógica de la base de datos, incluyendo la forma en que se organizan los datos.

### Componentes principales

- **Tablas:** Son la estructura básica en un modelo de datos relacional. Representan entidades específicas o tipos de datos y están organizadas en filas y columnas.
  - Cada fila representa una instancia individual de la entidad.
  - Cada columna representa un atributo o característica de esa entidad.

>[!NOTE]
> En próximas sesiones revisaremos en detalle otros aspectos de los modelos de datos.

---

### Modelo físico

El modelo de datos físicos representa cómo se construirá el modelo de la base de datos. Se especifican las tablas, columnas, claves primarias y foráneas, así como otras restricciones.

---

## Integridad referencial

**Integridad de datos = datos correctos + datos completos**

Problemas de diseño de una base de datos pueden causar problemas de integridad. En esta clase aprenderemos a evitar algunos de ellos.

---

### Ejercicio guiado: Modificación de campos NULL a NOT NULL

**Paso 1:** Crear la tabla `clientes`

```sql
CREATE TABLE clientes (
  id INTEGER UNIQUE NOT NULL,
  name VARCHAR(25) NOT NULL,
  email VARCHAR(50)
);
```

**Paso 2:** Insertar registros sin email

```sql
INSERT INTO clientes (id, name) VALUES (1, 'Nombre 1');
INSERT INTO clientes (id, name) VALUES (2, 'Nombre 2');
INSERT INTO clientes (id, name) VALUES (3, 'Nombre 3');
```

**Paso 3:** Intentar modificar la columna `email` a `NOT NULL`

```sql
ALTER TABLE clientes ALTER COLUMN email SET NOT NULL;
```

>`ERROR: column "email" of relation "clientes" contains null values`

**Paso 4:** Actualizar los registros nulos

```sql
UPDATE clientes SET email = 'correo@ejemplo.com' WHERE email IS NULL;
```

**Paso 5:** Volver a ejecutar la modificación

```sql
ALTER TABLE clientes ALTER COLUMN email SET NOT NULL;
```

---

## Subconsultas (Queries anidadas)

Una **subconsulta** es una consulta dentro de otra consulta. Permite seleccionar registros en función de los resultados de otra consulta.

### Ejemplo: Personas que ganan sobre el promedio

```sql
SELECT *
FROM empleados
WHERE sueldo > (
  SELECT AVG(sueldo) FROM empleados
);
```

- **Consulta interior:** `SELECT AVG(sueldo) FROM empleados`
- **Consulta exterior:** `SELECT * FROM empleados WHERE sueldo > ...`

---

### Ejercicio guiado: Subconsultas con dos tablas

**Tablas:** `Clientes` y `Pedidos`

**Problema:** Obtener clientes que hayan realizado al menos un pedido con monto > 1000.

**Subconsulta:**

```sql
SELECT cliente_id FROM pedidos WHERE monto > 1000
```

**Consulta exterior:**

```sql
SELECT *
FROM clientes
WHERE cliente_id IN (
  SELECT cliente_id
  FROM pedidos
  WHERE monto > 1000
);
```

---

### Subconsultas en el FROM

Permiten tratar el resultado de una subconsulta como una tabla temporal.

**Ejemplo:** Calcular el monto promedio vendido por vendedor

```sql
SELECT AVG(total_venta) AS promedio_ventas
FROM (
  SELECT empleado_id, SUM(monto) AS total_venta
  FROM ventas
  GROUP BY empleado_id
);
```

---

### Ejercicio práctico

Tienes las tablas `productos` y `pedidos_detalle`. Encuentra los productos que se han pedido más de una vez.

---

## Operaciones de unión entre tablas (JOIN)

| Tipo de JOIN | Descripción |
|--------------|-------------|
| **INNER JOIN** | Unifica filas de dos o más tablas si existe una columna que las relacione. |
| **LEFT JOIN** | Muestra todos los registros de la tabla izquierda y las coincidencias de la tabla derecha. |
| **RIGHT JOIN** | Muestra todos los registros de la tabla derecha y las coincidencias de la tabla izquierda. |
| **FULL OUTER JOIN** | Retorna todos los registros que coincidan en ambas tablas. |

---

### Ejercicio guiado: Tipos de JOIN

**Tablas:** `Clientes` y `Productos`

#### INNER JOIN

```sql
SELECT clientes.cliente_id, clientes.nombre, productos.id, productos.monto
FROM clientes
INNER JOIN productos ON clientes.cliente_id = productos.cliente_id;
```

#### LEFT JOIN

```sql
SELECT clientes.nombre, productos.id, productos.monto
FROM clientes
LEFT JOIN productos ON clientes.cliente_id = productos.cliente_id;
```

#### RIGHT JOIN

```sql
SELECT clientes.nombre, productos.id, productos.monto
FROM clientes
RIGHT JOIN productos ON clientes.cliente_id = productos.cliente_id;
```

#### FULL OUTER JOIN

```sql
SELECT clientes.cliente_id, clientes.nombre, productos.id, productos.monto
FROM clientes
FULL OUTER JOIN productos ON clientes.cliente_id = productos.cliente_id;
```

---

### Lectura de datos y claves comunes

Para realizar un JOIN, es esencial que exista un campo común entre las tablas (como un `id`). Sin este punto de conexión, no es posible cruzar datos entre tablas.

---

### Ejercicio práctico

En una empresa, hay dos tablas: `empleados` y `departamentos`. Ambas contienen la columna `empleado_id`.

Crea una consulta SQL para obtener todos los empleados junto con sus respectivos departamentos.

**Pregunta:** ¿Qué tipo de JOIN debes utilizar?