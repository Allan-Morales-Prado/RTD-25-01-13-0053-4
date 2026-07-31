# 📝 Cuestionario: Bases de Datos Relacionales

---

## Pregunta 1

**¿Cuál de las siguientes afirmaciones describe correctamente el rol de una base de datos relacional en una organización?**

A) Almacena únicamente la interfaz visual de las aplicaciones para que los usuarios puedan interactuar con ella.

B) Permite que las aplicaciones contengan información de los usuarios y facilita la obtención de datos mediante análisis y consultas específicas.

C) Se encarga exclusivamente del diseño gráfico y la experiencia de usuario en el frontend de una aplicación.

D) Reemplaza completamente la necesidad de contar con servidores web en el backend de una aplicación.


<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

*Justificación:* Las bases de datos son el elemento fundamental que permite a las aplicaciones web, móviles y de escritorio contener la información de los usuarios. Además, a partir de análisis y consultas específicas, se pueden obtener datos pertinentes con la lógica y objetivo de negocio de todo producto o servicio.

</details>

---

## Pregunta 2

**En el contexto de las bases de datos relacionales, ¿qué representan las filas dentro de una tabla?**

A) Los atributos que definen la estructura de la información almacenada.

B) Los tipos de datos que puede contener cada campo de la tabla.

C) Cada registro ingresado en la base de datos, donde se visualiza la información de manera listada.

D) Las relaciones establecidas entre diferentes tablas de la base de datos.


<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

*Justificación:* Las filas son la representación de cada registro ingresado en la base de datos. En ellas se puede visualizar de manera listada la información correspondiente a una entidad específica.

</details>

---

## Pregunta 3

**Una empresa desea almacenar información de sus empleados, donde cada empleado pertenece a un solo departamento, pero cada departamento puede tener múltiples empleados. ¿Qué característica de las bases de datos relacionales permite modelar esta situación?**

A) La capacidad de crear múltiples bases de datos independientes dentro de un mismo motor.

B) La organización de los datos en tablas con columnas que almacenan atributos específicos.

C) La operación relacional que permite vincular registros entre diferentes tablas.

D) La eliminación automática de registros duplicados en la base de datos.


<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

*Justificación:* En el ejemplo de Twitter, los tweets se relacionan con el usuario que los crea mediante una operación relacional. Esta misma característica permite modelar la relación entre empleados y departamentos, vinculando registros de diferentes tablas.

</details>

---

## Pregunta 4

**En una base de datos relacional, se tiene una tabla "productos" con las columnas "id", "nombre" y "precio". Si se desea consultar únicamente los nombres y precios de todos los productos, ¿cuál de las siguientes sentencias SQL sería la adecuada?**

A) `SELECT id, nombre, precio FROM productos;`

B) `SELECT nombre, precio FROM productos;`

C) `SELECT * FROM productos WHERE precio;`

D) `INSERT INTO productos (nombre, precio) VALUES ('Lápiz', 500);`


<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

*Justificación:* La sentencia `SELECT nombre, precio FROM productos;` permite consultar exclusivamente las columnas "nombre" y "precio" de la tabla "productos", omitiendo la columna "id". Esto se alinea con la capacidad de las bases de datos de obtener datos específicos mediante consultas.

</details>

---

## Pregunta 5

**¿Cuál de las siguientes afirmaciones representa correctamente la relación entre un motor de base de datos, las bases de datos y las tablas?**

A) Un motor puede contener múltiples bases de datos, y cada base de datos puede contener múltiples tablas.

B) Cada tabla puede contener múltiples motores de base de datos independientes.

C) Una base de datos puede contener múltiples motores, pero solo una tabla.

D) Un motor solo puede contener una base de datos, y cada base de datos solo una tabla.


<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: A**

*Justificación:* En un motor de base de datos podemos tener múltiples bases de datos. Dentro de estas podemos tener diversas tablas, y en cada tabla pueden haber diferentes registros. Esta jerarquía es fundamental en los sistemas de bases de datos relacionales.

</details>

---

## Pregunta 6

**Las columnas en una tabla de una base de datos relacional cumplen la función de:**

A) Almacenar registros individuales de información.

B) Mostrar un conjunto de datos en función de los campos definidos durante la creación de la tabla.

C) Establecer conexiones con otras bases de datos externas.

D) Definir la contraseña de acceso a la base de datos.


<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

*Justificación:* Las columnas muestran un conjunto de datos en función de los campos que se hayan definido durante la creación de las tablas. Cada columna representa un atributo específico de la entidad que se está modelando.

</details>

---

## Pregunta 7

**Una empresa necesita agregar un nuevo cliente a su sistema. La tabla "clientes" ya ha sido creada previamente. ¿Qué operación debe realizar para añadir los datos del nuevo cliente?**

A) `SELECT * FROM clientes;`

B) `CREATE TABLE clientes (nombre VARCHAR(50));`

C) `INSERT INTO clientes (nombre, apellido) VALUES ('María', 'González');`

D) `DELETE FROM clientes WHERE nombre = 'María';`


<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

*Justificación:* La sentencia `INSERT INTO` permite agregar nuevos registros a una tabla existente. En este caso, se inserta un nuevo cliente con nombre "María" y apellido "González" en la tabla "clientes".

</details>