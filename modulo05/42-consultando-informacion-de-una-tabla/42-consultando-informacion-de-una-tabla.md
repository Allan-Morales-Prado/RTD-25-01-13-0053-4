# Consultando información de una tabla - Bases de Datos Relacionales

---

# El Lenguaje Estructurado de Consultas SQL

## ¿Qué es SQL?

- Está diseñado para el uso específico de administración y consulta de información en sistemas de gestión de bases de datos como PostgreSQL.
- Se utiliza para **definir**, **manipular** y **controlar** los datos.

### Operaciones principales con SQL:

| Operación | Descripción |
|-----------|-------------|
| **CREATE** | Crear registros |
| **READ** | Leer la información |
| **UPDATE** | Actualizar los datos |
| **DELETE** | Eliminar uno o un conjunto de datos |

---

## Cargando el Dataset

A continuación utilizaremos el dataset definido dentro de *"Material de apoyo - Consultando información de una tabla"*, el cual está disponible en la plataforma.

### Paso 1:
Carga el archivo comprimido del material de apoyo en una nueva base de datos en tu computador. Si tuviste problemas con la instalación, puedes ocupar **sqliteonline**.

### Paso 2:
Probemos nuestro dataset con:
```sql
SELECT * FROM productos LIMIT 10;
```

---

# Nuestra primera consulta SQL con PostgreSQL

## Pasos para realizar una consulta

### Paso 1:
Acceder a **sqlite-online** y seleccionar **PostgreSQL** como motor de base de datos.

### Paso 2:
Hacemos click en **Connect**. Una vez conectados vamos a escribir la siguiente sentencia SQL para obtener todos los datos que están almacenados en **Demo**:

```sql
SELECT * FROM Demo;
```

### Resultado de ejecución
Al realizar la consulta, obtenemos todos los registros almacenados en `demo`.

---

## Análisis de la primera consulta

### Insensibilidad a mayúsculas/minúsculas

```sql
SELECT * FROM demo;
```
Es lo mismo que:
```sql
select * from demo;
```

### Paso 3:
Extraer el campo **ID** y su información almacenada en la tabla demo:
```sql
SELECT ID FROM DEMO;
```

### Paso 4:
Extraer la información de **ID** y **Name**:
```sql
SELECT ID, NAME FROM DEMO;
```

---

# Recuperando información de una tabla

## Implementando consultas a partir de condiciones

### Paso 1:
Ingresar a **sqliteonline**, seleccionar **PostgreSQL** y conectarse a la tabla demo.

### Paso 2:
Seleccionar aquellos ID que sean mayores o iguales a 4:
```sql
SELECT * FROM demo WHERE id >= 4;
```

---

## Consulta con condición

```sql
SELECT * FROM tabla
WHERE c4 = True;
```

---

## Llaves primarias

> Una **clave primaria** identifica de manera exclusiva una fila de la tabla.

Una base de datos relacional está diseñada para imponer la exclusividad de las claves primarias, permitiendo que haya sólo una fila con un valor de clave primaria específico en una tabla.

*Fuente: Documentación IBM*

> [!NOTE]
>  En el ejercicio hicimos la suposición de que la columna ID y sus valores son la clave primaria. Más adelante profundizaremos en este tema.

---

## Consultas especificando límites

En SQL también podemos limitar consultas para que se retornen la *n* cantidad de elementos definidos. Para ello podemos utilizar **LIMIT**.

### Paso 3:
Limitar el retorno de registros en la tabla demo para que muestre únicamente 2 elementos:
```sql
SELECT * FROM demo LIMIT 2;
```

### Sintaxis general:
```sql
SELECT * FROM tabla
LIMIT 2;
```

---

# Utilización de funciones en las consultas

Existen distintos tipos de funciones que podemos utilizar.

### Ejemplo: Ordenar por largo del nombre

Queremos ordenar los productos por el largo del nombre:
```sql
SELECT * FROM productos ORDER BY LENGTH(nombre_producto);
```

Incluso podríamos agregar una columna mostrando el largo para poder observar mejor los resultados:
```sql
SELECT *, LENGTH(nombre_producto) FROM productos ORDER BY LENGTH(nombre_producto);
```

---

## Ejercicio guiado

Utilizando lo aprendido, selecciona todos los datos de los productos junto a un código. Este código está compuesto por las primeras 3 letras de la categoría.

---

# Implementar funciones de agregado sobre una tabla

## Funciones de agregado

Las **funciones de agregado** son un tipo especial de función en SQL que operan sobre un conjunto de valores y devuelven un único valor resumido o agregado.

### Ejemplo:
```sql
SELECT SUM(valor) FROM tabla_ejemplo;
-- Resultado: 210
```

---

## Utilizando el dataset

### Ejercicios:

| N° | Pregunta | Pista |
|----|----------|-------|
| 1 | Calcula el precio mínimo | - |
| 2 | Calcula el precio máximo | - |
| 3 | Calcula el precio promedio | - |
| 4 | Cuenta la cantidad de productos con stock | Combinar funciones de agregado con WHERE |
| 5 | Cuenta la cantidad de precios sobre 7000 | - |
| 6 | Calcula el promedio de los productos que tienen stock | - |

---

# GROUP BY

## Agrupación de datos

Ejemplo: Nos piden el precio más alto de cada producto por categoría:
```sql
SELECT max(precio) FROM productos GROUP BY categoria;
```

Podemos mostrar la categoría junto al precio:
```sql
SELECT categoria, max(precio) FROM productos GROUP BY categoria;
```

---

## Regla importante

> No podemos mostrar campos no agrupados salvo que estén en funciones de agregado.

### ❌ Consulta incorrecta:
```sql
SELECT nombre_producto, max(precio) FROM productos GROUP BY categoria;
```

### ⚠️ Error:
```
ERROR: column "productos.nombre_producto" must appear in the GROUP BY clause or be used in an aggregate function
```

---

## Utilizando el dataset de la tabla ventas

| N° | Pregunta |
|----|----------|
| 1 | ¿Cuál es el promedio de ventas? |
| 2 | ¿Cuál es el promedio de ventas por producto? |
| 3 | ¿Cuál es el promedio de ventas por producto después del '2024-01-05'? |
| 4 | ¿Qué tipo de producto generó la venta más alta? *(Pista: La venta se calcula como cantidad * precio_unitario)* |
| 5 | ¿Cuántos productos se vendieron en cada fecha? |

---

# Ideas Clave

## Lenguaje de Consultas Estructuradas (SQL)

- Se utiliza para **definir**, **manipular** y **controlar** los datos.
- Con la sintaxis estructural del lenguaje podemos:
  - Crear registros
  - Leer la información
  - Actualizar los datos
  - Eliminar uno o un conjunto de datos

---

## Elementos de la sentencia SELECT

| Elemento | Descripción |
|----------|-------------|
| **SELECT** | Indica que la consulta a realizar será de selección |
| **\*** | Comodín para indicar que se deben seleccionar todos los campos (todas las columnas de la tabla) |
| **FROM** | Indica de qué tabla específica se va a seleccionar |
| **demo** | Nombre de la tabla. En este caso viene precargada en sqliteonline |
| **;** | Una consulta termina con un punto y coma para separar varias instrucciones |

---

## Clave primaria

> Una **clave primaria** identifica de manera exclusiva una fila de la tabla.

Una base de datos relacional está diseñada para imponer la exclusividad de las claves primarias, permitiendo que haya solo una fila con un valor de clave primaria específico en una tabla.
