# Cuestionario: Consultando información de una tabla SQL

---

## Pregunta 1

**¿Cuál es el propósito principal de la cláusula GROUP BY en SQL?**

A) Ordenar los resultados de una consulta en orden ascendente o descendente
B) Agrupar filas que tienen los mismos valores en columnas especificadas para aplicar funciones de agregado
C) Filtrar filas antes de que se realice la agrupación de datos
D) Combinar filas de dos o más tablas basándose en una columna relacionada

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** GROUP BY se utiliza específicamente para agrupar registros que comparten valores en columnas determinadas, permitiendo que las funciones de agregado (como SUM, AVG, MAX, MIN, COUNT) operen sobre cada grupo de manera independiente. La opción A describe ORDER BY, la opción C describe WHERE o HAVING, y la opción D describe JOIN.
</details>

---

## Pregunta 2

**Dada la siguiente tabla "pedidos":**

| id_pedido | cliente | total | fecha |
|-----------|---------|-------|-------|
| 1 | Ana | 1500 | 2026-01-10 |
| 2 | Luis | 2300 | 2026-01-12 |
| 3 | Ana | 900 | 2026-01-15 |
| 4 | Carlos | 3100 | 2026-01-18 |
| 5 | Luis | 1750 | 2026-01-20 |

**¿Qué devuelve la siguiente consulta?**

```sql
SELECT cliente, COUNT(*), AVG(total) 
FROM pedidos 
WHERE total > 1000 
GROUP BY cliente;
```

A) Una tabla con el cliente, la cantidad total de pedidos y el promedio de todos los pedidos para aquellos clientes con algún pedido mayor a 1000
B) Una tabla con el cliente, la cantidad de pedidos mayores a 1000 y el promedio de esos pedidos, solo para clientes que tienen al menos un pedido mayor a 1000
C) Una tabla con el cliente, la cantidad total de pedidos y el promedio total, mostrando solo clientes cuyo total de pedidos supera 1000
D) Un error porque COUNT(*) no puede usarse junto con AVG en la misma consulta

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La consulta filtra primero los pedidos con total > 1000 (quedan los pedidos 1, 2, 4, 5), luego agrupa por cliente. Para Ana queda solo el pedido 1 (COUNT=1, AVG=1500), para Luis quedan los pedidos 2 y 5 (COUNT=2, AVG=2025), y para Carlos queda el pedido 4 (COUNT=1, AVG=3100). La opción A es incorrecta porque COUNT y AVG solo consideran los pedidos filtrados (>1000), no todos los pedidos.
</details>

---

## Pregunta 3

**¿Cuál de las siguientes consultas SQL es sintácticamente correcta y devolverá el promedio de precios por categoría, mostrando únicamente categorías cuyo promedio supere 5000?**

A)
```sql
SELECT categoria, AVG(precio) 
FROM productos 
HAVING AVG(precio) > 5000 
GROUP BY categoria;
```

B)
```sql
SELECT categoria, AVG(precio) 
FROM productos 
GROUP BY categoria 
WHERE AVG(precio) > 5000;
```

C)
```sql
SELECT categoria, AVG(precio) 
FROM productos 
GROUP BY categoria 
HAVING AVG(precio) > 5000;
```

D)
```sql
SELECT categoria, AVG(precio) 
FROM productos 
WHERE AVG(precio) > 5000 
GROUP BY categoria;
```

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

**Justificación:** La cláusula HAVING se utiliza específicamente para filtrar resultados después de aplicar GROUP BY y funciones de agregado. La opción A tiene el orden incorrecto (HAVING debe ir después de GROUP BY). La opción B usa WHERE en lugar de HAVING, pero WHERE no puede contener funciones de agregado. La opción D tiene WHERE antes de GROUP BY con una función de agregado, lo cual no es válido sintácticamente.
</details>

---

## Pregunta 4
**En una base de datos relacional, ¿qué ocurre si se intenta insertar un registro con un valor de clave primaria que ya existe en la tabla?**

A) El registro se inserta como un duplicado y se asigna automáticamente un nuevo identificador
B) La base de datos rechaza la operación y genera un error de violación de integridad
C) El registro se inserta pero se marca como inactivo para evitar conflictos
D) La base de datos actualiza el registro existente con los nuevos datos

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La clave primaria impone la unicidad de los valores en una tabla. Si se intenta insertar un valor duplicado, el sistema de gestión de base de datos (como PostgreSQL) rechazará la operación y generará un error de violación de restricción de clave primaria, manteniendo la integridad referencial de los datos.
</details>

---

## Pregunta 5

**Observa la siguiente tabla "ventas":**

| id | producto | cantidad | precio_unitario | fecha_venta |
|----|----------|----------|-----------------|-------------|
| 1 | A | 3 | 2000 | 2026-02-01 |
| 2 | B | 1 | 5000 | 2026-02-02 |
| 3 | A | 2 | 2000 | 2026-02-03 |
| 4 | C | 5 | 1500 | 2026-02-04 |
| 5 | B | 2 | 5000 | 2026-02-05 |

**¿Cuál es el resultado de ejecutar la siguiente consulta?**

```sql
SELECT producto, SUM(cantidad * precio_unitario) AS total_ventas
FROM ventas
WHERE fecha_venta >= '2026-02-03'
GROUP BY producto
ORDER BY total_ventas DESC;
```

A) 
| producto | total_ventas |
|--|--|
| B | 10000 |
| A | 4000 |
| C | 7500 |

B) 
| producto | total_ventas |
|--|--|
| B | 10000 |
| C | 7500 |
| A | 4000 |

C)
| producto | total_ventas |
|--|--|
| C | 7500 |
| B | 10000 |
| A | 4000 |

D)
| producto | total_ventas |
|--|--|
| A | 4000 |
| C | 7500 |
| B | 10000 |

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** El filtro WHERE fecha_venta >= '2026-02-03' incluye solo las ventas de los IDs 3, 4 y 5. Los cálculos son: Producto A: 2 * 2000 = 4000; Producto C: 5 * 1500 = 7500; Producto B: 2 * 5000 = 10000. Luego ORDER BY total_ventas DESC los ordena de mayor a menor: B (10000), C (7500), A (4000). La opción A tiene el orden incorrecto y la opción C también.
</details>

---

## Pregunta 6

**¿Cuál de las siguientes afirmaciones sobre el comodín * (asterisco) en SQL es correcta?**

A) Selecciona todas las columnas de la tabla especificada en la cláusula FROM
B) Selecciona únicamente las columnas que contienen valores numéricos
C) Multiplica los valores de dos columnas en una consulta
D) Se utiliza como comodín en la cláusula WHERE para buscar patrones de texto

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: A**

**Justificación:** En una consulta SELECT, el asterisco (*) es un comodín que indica que se deben seleccionar todas las columnas de la tabla o tablas mencionadas en la cláusula FROM. La opción D describe el uso del % en LIKE (no el *), la opción C describe una operación aritmética, y la opción B es incorrecta porque selecciona todas las columnas, no solo las numéricas.
</details>

---

## Pregunta 7

**¿Qué devuelve la siguiente consulta?**

```sql
SELECT COUNT(DISTINCT categoria) 
FROM productos 
WHERE precio < 10000;
```

A) El número total de productos con precio menor a 10000
B) El número de categorías diferentes que tienen al menos un producto con precio menor a 10000
C) El promedio de precios de las categorías con productos menores a 10000
D) La suma de precios de productos agrupados por categoría

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La función COUNT(DISTINCT categoria) cuenta los valores únicos (no duplicados) de la columna categoria que cumplen con la condición WHERE precio < 10000. Esto devuelve el número de categorías distintas que tienen al menos un producto en ese rango de precios. La opción A sería COUNT(*) y la opción C sería AVG(precio).
</details>

---

## Pregunta 8

**Dada la siguiente tabla "empleados":**

| id | nombre | departamento | salario |
|----|--------|--------------|---------|
| 1 | María | Ventas | 4500 |
| 2 | Juan | TI | 6000 |
| 3 | Pedro | Ventas | 4800 |
| 4 | Laura | TI | 5500 |
| 5 | Carlos | RRHH | 4000 |

**¿Qué consulta permite obtener el salario promedio por departamento y ordenar los resultados de mayor a menor promedio?**

A)
```sql
SELECT departamento, AVG(salario) 
FROM empleados 
GROUP BY departamento 
ORDER BY AVG(salario) DESC;
```

B)
```sql
SELECT departamento, AVG(salario) 
FROM empleados 
ORDER BY AVG(salario) DESC 
GROUP BY departamento;
```

C)
```sql
SELECT departamento, AVG(salario) 
FROM empleados 
GROUP BY salario 
ORDER BY departamento DESC;
```

D)
```sql
SELECT AVG(salario), departamento 
FROM empleados 
ORDER BY AVG(salario) ASC;
```

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La consulta correcta agrupa por departamento usando GROUP BY, calcula el promedio de salario con AVG(salario), y ordena los resultados de mayor a menor con ORDER BY AVG(salario) DESC. La opción B tiene el orden incorrecto de las cláusulas (ORDER BY debe ir después de GROUP BY). La opción C agrupa incorrectamente por salario en lugar de departamento. La opción D no agrupa correctamente y ordena ascendente.
</details>

---

## Pregunta 9

**¿Cuál es la diferencia fundamental entre las cláusulas WHERE y HAVING en SQL?**

A) WHERE se usa con SELECT y HAVING solo con DELETE
B) WHERE filtra filas individuales antes de la agrupación, mientras que HAVING filtra grupos después de la agrupación
C) WHERE funciona solo con datos numéricos y HAVING solo con datos de texto
D) No hay diferencia, son completamente intercambiables

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** WHERE se aplica a filas individuales antes de que se realice cualquier agrupación (GROUP BY), mientras que HAVING se aplica a los grupos después de que se ha realizado la agrupación y solo puede usarse con funciones de agregado. La opción A es incorrecta, la C es falsa, y la D es incorrecta porque no son intercambiables.
</details>

---

## Pregunta 10

**¿Cuál de las siguientes consultas calcularía correctamente el total de ventas (cantidad * precio_unitario) para cada producto en la tabla "ventas", mostrando solo productos con un total superior a 3000?**

A)
```sql
SELECT producto, cantidad * precio_unitario AS total
FROM ventas
HAVING total > 3000;
```

B)
```sql
SELECT producto, cantidad * precio_unitario AS total
FROM ventas
WHERE total > 3000;
```

C)
```sql
SELECT producto, cantidad * precio_unitario AS total
FROM ventas
WHERE cantidad * precio_unitario > 3000;
```

D)
```sql
SELECT producto, cantidad * precio_unitario > 3000 AS total
FROM ventas;
```

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

**Justificación:** Para filtrar el resultado de una expresión calculada (cantidad * precio_unitario), se debe usar WHERE con la expresión completa. Los alias de columna (como "total") no pueden usarse directamente en la cláusula WHERE del mismo nivel de consulta (en la mayoría de motores SQL). La opción A usa HAVING sin GROUP BY, lo cual no es apropiado. La opción B intenta usar el alias en WHERE, lo cual no es válido. La opción D devuelve un booleano, no el cálculo del total.
</details>
