# Sentencias para la Manipulación de Datos (Parte I)
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

- **Reconocer** la sintaxis básica para la construcción de sentencias DML que resuelven un requerimiento de manipulación de datos.
- **Utilizar** sentencias de ingreso, actualización y borrado de registros en una tabla utilizando lenguaje DML de acuerdo a las condiciones solicitadas.

---

## 💡 Preguntas Clave

> ¿Qué permite la definición de una clave primaria en una tabla?

> ¿Qué sentencia utilizamos para eliminar todos los registros de una tabla?

---

## 🗄️ DML - Data Manipulation Language

**DML** es un lenguaje que proporcionan los sistemas de gestión de base de datos como **PostgreSQL**.

Permite:
- Realizar **consultas**
- **Manipular** los datos

> El lenguaje más popular para la manipulación de datos es **SQL**

---

## 🔧 Operaciones en una Base de Datos

Con SQL podemos realizar:

| Operación | Sentencia | Descripción |
|-----------|-----------|-------------|
| **Insertar** | `INSERT` | Ingresar registros a una tabla |
| **Actualizar** | `UPDATE` | Actualizar los registros de una tabla |
| **Eliminar** | `DELETE` | Eliminar registros |

---

## 🍽️ Ejercicio Guiado: "Realizando operaciones en una base de datos"

### Paso 1: Crear la base de datos

```sql
CREATE DATABASE comidas_tipicas;
```

### Paso 2: Crear la tabla

```sql
CREATE TABLE cocina_chilena (
    id INT, 
    nombre VARCHAR(50)
);
```

### Paso 3: Insertar registros

```sql
INSERT INTO cocina_chilena (id, nombre) VALUES ('1', 'Pastel de choclo');
INSERT INTO cocina_chilena (id, nombre) VALUES ('2', 'Umitas');
```

> **Nota:** El segundo registro tiene un error intencional ("Umitas" en lugar de "Humitas")

---

## ✏️ Actualizando Información

### Paso 4: UPDATE

```sql
UPDATE cocina_chilena 
SET nombre = 'Humitas' 
WHERE id = 2;
```

**Componentes del UPDATE:**
1. Sentencia `UPDATE`
2. Nombre de la tabla
3. `SET` + columna y nuevo valor
4. `WHERE` para seleccionar el registro específico

---

## 🎯 Ejercicio Propuesto 1

> **"Ingresa 3 registros más a la tabla e intenciona el UPDATE en al menos 2 de ellos"**

❓ **Reflexión:** ¿Por qué es importante saber el ID al momento de actualizar un registro?

---

## 🗑️ Borrando Información

### Paso 5: DELETE

```sql
DELETE FROM cocina_chilena WHERE id = 2;
```

> **Importante:** Así como con UPDATE, utilizamos el `id` para capturar un registro puntual.

---

## ⚠️ ¿Qué sucede si usamos DELETE o UPDATE sin WHERE?

### Paso 6: Insertar más registros

```sql
INSERT INTO cocina_chilena (id, nombre) VALUES ('2', 'Humitas');
INSERT INTO cocina_chilena (id, nombre) VALUES ('3', 'Cazuela');
INSERT INTO cocina_chilena (id, nombre) VALUES ('4', 'Empanada chilena');
INSERT INTO cocina_chilena (id, nombre) VALUES ('5', 'Charquicán');
```

### Eliminar múltiples registros con IN

```sql
DELETE FROM cocina_chilena WHERE id IN (3, 4, 5);
```

> **`IN`** permite seleccionar múltiples elementos para eliminar.

---

## 🐾 Ejercicio Propuesto 2: "Aplicando lo aprendido"

### Crear una base de datos para mascotas

**Campos requeridos:**
- ID
- Nombre
- Raza
- Edad

**Acciones a realizar:**
1. Ingresar al menos 5 registros
2. Intencionar acciones de **UPDATE**
3. Intencionar acciones de **DELETE**

---

## 📝 Ejercicio Propuesto 3: "Actualizando varios registros"

### Actualización masiva

Utilizando la base de datos de perros o gatos, realiza una **actualización masiva** al campo edad.

> **Tip:** Puedes asignar la misma edad a todos los registros.

---

## 🤔 Preguntas de Reflexión

1. ¿Qué sucedería si al momento de borrar un registro no indicamos algún campo identificador?

2. ¿Cuál fue el concepto que más te costó comprender?

---

## 💎 Ideas Clave

- Las sentencias DML (**INSERT**, **UPDATE**, **DELETE**, **SELECT**) se enfocan en la manipulación directa de los datos almacenados.

- Aprendimos a realizar operaciones de:
  - **Inserción** de registros
  - **Actualización** de registros
  - **Eliminación** de registros

- Es fundamental utilizar **integridad referencial** donde cada registro tenga su respectivo identificador.

---

## 📋 Resumen de Sentencias DML

| Sentencia | Sintaxis Básica | Uso |
|-----------|-----------------|-----|
| **INSERT** | `INSERT INTO tabla (columnas) VALUES (valores)` | Agregar nuevos registros |
| **UPDATE** | `UPDATE tabla SET columna = valor WHERE condición` | Modificar registros existentes |
| **DELETE** | `DELETE FROM tabla WHERE condición` | Eliminar registros |
| **SELECT** | `SELECT columnas FROM tabla WHERE condición` | Consultar datos |

---

> ✅ **Objetivo logrado:** Utilizar sentencias de ingreso, actualización y borrado de registros utilizando lenguaje DML para manipular la información de tablas con integridad referencial de acuerdo a un modelo de datos existente.