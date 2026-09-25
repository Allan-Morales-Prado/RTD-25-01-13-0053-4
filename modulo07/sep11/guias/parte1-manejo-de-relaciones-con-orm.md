# Modelos de datos y el ORM de Django
## Manejo de relaciones en el ORM de Django (Parte I)

---

## Índice de Contenidos

- [Modelos de datos y el ORM de Django](#modelos-de-datos-y-el-orm-de-django)
  - [Manejo de relaciones en el ORM de Django (Parte I)](#manejo-de-relaciones-en-el-orm-de-django-parte-i)
  - [Índice de Contenidos](#índice-de-contenidos)
  - [1. Introducción y Objetivos](#1-introducción-y-objetivos)
  - [2. Manejo de relaciones en el ORM de Django](#2-manejo-de-relaciones-en-el-orm-de-django)
  - [3. Relación Muchos a Uno (Many to One)](#3-relación-muchos-a-uno-many-to-one)
    - [3.1. ¿Qué es una Relación Muchos a Uno?](#31-qué-es-una-relación-muchos-a-uno)
    - [3.2. Ejemplos en la Vida Real](#32-ejemplos-en-la-vida-real)
    - [3.3. Ejemplos en Aplicaciones Web](#33-ejemplos-en-aplicaciones-web)
    - [3.4. Beneficios de las Relaciones Muchos a Uno](#34-beneficios-de-las-relaciones-muchos-a-uno)
    - [3.5. Más Ejemplos Prácticos](#35-más-ejemplos-prácticos)
    - [3.6. ¿Cómo se Implementa en Django?](#36-cómo-se-implementa-en-django)
    - [3.7. Definición de Borrado en Cascada](#37-definición-de-borrado-en-cascada)
  - [4. Ejercicio Guiado: Relación Muchos a Uno](#4-ejercicio-guiado-relación-muchos-a-uno)
  - [5. Relación Uno a Uno (One to One)](#5-relación-uno-a-uno-one-to-one)
    - [5.1. OneToOneField - ¿Cuándo se utiliza?](#51-onetoonefield---cuándo-se-utiliza)
    - [5.2. OneToOneField - Ejemplo en Django](#52-onetoonefield---ejemplo-en-django)
    - [5.3. Parámetros del OneToOneField](#53-parámetros-del-onetoonefield)
    - [5.4. Opciones de on\_delete](#54-opciones-de-on_delete)
  - [6. Ejercicio Guiado: OneToOneField](#6-ejercicio-guiado-onetoonefield)
  - [7. Resumen de la Sesión](#7-resumen-de-la-sesión)
  - [8. Próxima Sesión](#8-próxima-sesión)

---

## 1. Introducción y Objetivos

**Objetivo General:**
Implementar la capa de modelo de acceso a datos del aplicativo utilizando entidades con relaciones uno a uno, uno a muchos y muchos a muchos para dar solución a una problemática.

**¿Qué aprenderás en esta sesión?**
- Identificar un modelo con entidades que tienen relaciones uno a uno para resolver un problema determinado acorde al framework Django.
- Definir un modelo con entidades que tienen relaciones muchos a uno para resolver un problema determinado acorde al framework Django.

---

## 2. Manejo de relaciones en el ORM de Django

Revisaremos 2 tipos de relaciones muy utilizadas en los proyectos Django:
- **Many to one (Muchos a uno)**
- **One to One (uno a uno)**

Este tipo de relaciones nos permiten modelar entidades con relaciones simples como un usuario con su computador asignado o relaciones más complejas como una orden de compra con la cantidad de productos que pedimos en ella.

---

## 3. Relación Muchos a Uno (Many to One)

### 3.1. ¿Qué es una Relación Muchos a Uno?

Una relación Muchos a Uno es un tipo de asociación entre dos entidades donde múltiples registros en una tabla pueden estar asociados a un solo registro en otra tabla. Este tipo de relación es fundamental en el diseño de bases de datos relacionales y es ampliamente utilizado para representar la relación entre entidades de datos.

### 3.2. Ejemplos en la Vida Real

- **Biblioteca y Libros:** Una biblioteca tiene muchos libros, pero cada libro pertenece a una única biblioteca.
- **Ciudades y Países:** Muchas ciudades pueden estar en un mismo país, pero cada ciudad está asociada a un solo país.

### 3.3. Ejemplos en Aplicaciones Web

**Publicaciones de Blog:**
En un sistema de gestión de contenido, podrías tener un modelo `Publicación` y un modelo `Autor`. Cada `Publicación` está escrita por un solo `Autor`, pero un `Autor` puede escribir muchas `Publicaciones`.

```python
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

class Publicacion(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
```

Cada comentario está asociado a una única publicación, pero una publicación puede tener muchos comentarios.

### 3.4. Beneficios de las Relaciones Muchos a Uno

- **Organización de Datos:** Permite una estructura de datos más organizada y evita la duplicación.
- **Integridad Referencial:** Asegura la coherencia de los datos, donde las referencias entre tablas se mantienen consistentes.
- **Eficiencia en Consultas:** Facilita consultas eficientes a través de la base de datos, permitiendo extraer información relacionada de manera sencilla.

### 3.5. Más Ejemplos Prácticos

- **Gestión de Pedidos:** En un sistema de comercio electrónico, cada pedido puede contener varios artículos, pero cada artículo pertenece a un solo pedido.
- **Organización de Contenido:** En un CMS, múltiples artículos o publicaciones pueden ser escritos por un único autor, ilustrando cómo un autor se relaciona con muchos artículos.

Las relaciones Muchos a Uno se utilizan cuando necesitamos representar una estructura de datos donde un objeto puede pertenecer o estar asociado a un solo objeto de otro tipo, pero este último puede tener múltiples asociaciones. Este tipo de relación es uno de los pilares fundamentales en el modelado de bases de datos relacionales y es esencial para reflejar la naturaleza de muchas relaciones del mundo real en el diseño de nuestras aplicaciones.

### 3.6. ¿Cómo se Implementa en Django?

En Django, las relaciones Muchos a Uno se implementan utilizando el campo `ForeignKey`, que establece un vínculo entre dos modelos. Este campo indica que cada instancia del modelo donde se define puede estar asociada a una instancia del modelo al que apunta la `ForeignKey`.

En este ejemplo, múltiples productos pueden asociarse a una única categoría, creando una relación Muchos a Uno entre `Producto` y `Categoría`.

```python
from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
```

### 3.7. Definición de Borrado en Cascada

El borrado en cascada, representado por la opción `on_delete=models.CASCADE` en un campo `ForeignKey` de Django, asegura que cuando el objeto referenciado (el "padre") se elimine, todos los objetos asociados (los "hijos") también se eliminen. Esta es una estrategia clave para mantener la integridad referencial de la base de datos, evitando que queden registros huérfanos.

**Importancia del Borrado en Cascada:**
- **Integridad de Datos:** Evita la inconsistencia en la base de datos al eliminar automáticamente todos los objetos relacionados con el objeto que se está borrando.
- **Simplicidad de Mantenimiento:** Reduce la necesidad de escribir procedimientos de limpieza adicionales para eliminar manualmente los objetos relacionados.

---

## 4. Ejercicio Guiado: Relación Muchos a Uno

**Aplicación Blog y Entradas**

Consideremos una aplicación de blog donde múltiples entradas (posts) pueden ser escritas por un solo autor.

```python
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField()

class Entrada(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
```

**¿Cómo Funciona? Analicemos el modelo.**
- **Modelo Autor:** Representa a los autores en nuestro blog. Cada autor puede escribir varias entradas.
- **Modelo Entrada:** Cada entrada está vinculada a un autor a través de `ForeignKey`, estableciendo una relación Muchos a Uno. `on_delete=models.CASCADE` indica que, si se elimina un autor, todas sus entradas relacionadas también se eliminarán.

---

## 5. Relación Uno a Uno (One to One)

Mirando las relaciones desde el punto de vista de las bases de datos relacionales, podemos decir que una relación One to One existe cuando cada fila (registro) en una tabla, tiene solo una fila relacionada en una segunda tabla.

Por ejemplo, una empresa podría decidir asignar una oficina a solamente un empleado. Entonces, un empleado puede tener solo una oficina. La misma empresa podría también decidir que un departamento puede tener solo un gerente, entonces un gerente puede dirigir solamente un departamento.

### 5.1. OneToOneField - ¿Cuándo se utiliza?

Ahora, si llevamos esto al ORM, podemos decir que las filas son objetos, por lo tanto, el objeto tiene un campo de un tipo especial que lo relaciona con otro objeto.

El tipo especial de campo del que hablamos se llama `OneToOneField`.

Este campo nos permite relacionar dos objetos entre sí (uno a uno), por ejemplo un empleado con su oficina, o un autor con un perfil.

Se diferencia del campo `ForeignKey` en que `OneToOne` nos permite realizar solamente una relación uno a uno y en la query se devolverá solamente un objeto relacionado.

### 5.2. OneToOneField - Ejemplo en Django

En el ejemplo de uso podemos ver una serie de elementos. El primero es el nombre de la relación, el cual es una instancia del campo `OneToOneField`, a través del cual se tendrá acceso al campo relacionado.

```python
class Modelo1(models.Model):
    nombre_relacion = OneToOneField(Modelo2, blank=False, null=False, on_delete=models.CASCADE)
```

### 5.3. Parámetros del OneToOneField

En la instanciación del campo podemos ver algunos parámetros que describimos a continuación:

- **Modelo2:** El primer parámetro corresponde al modelo al cual se relacionarán, en este caso relacionamos `Modelo1 -> Modelo2`.
- **blank=False:** Utilizamos este parámetro para validar desde el ORM que no se permita el ingreso de un dato en blanco, en este caso nos obliga a agregar el dato relacionado cuando se crea el modelo.
- **null=False:** Al igual que el parámetro anterior, nos impide que dejemos este campo en blanco o nulo cuando creamos el objeto, pero la diferencia, es que la validación realizada para este campo, es realizada directamente por la base de datos.
- **on_delete:** Es un parámetro obligatorio con el cual asignamos el comportamiento que tomará la relación cuando se elimina el objeto relacionado.

### 5.4. Opciones de on_delete

Para el parámetro `on_delete` Django nos provee 6 opciones de comportamiento dependiendo de nuestros requerimientos:

- **CASCADE:** Cuando se elimina el objeto al que se hace referencia, también elimina los objetos que tienen referencias a él (cuando elimina una publicación de blog, por ejemplo, es posible que también desee eliminar los comentarios). Equivalente de SQL: `CASCADE`.
- **PROTECT:** Prohíbe la eliminación del objeto referenciado. Para eliminarlo, tendrá que eliminar todos los objetos que hacen referencia a él manualmente. Equivalente de SQL: `RESTRICT`.
- **SET_NULL:** Establece la referencia en NULL (requiere que el campo sea anulable). Por ejemplo, cuando se elimina un usuario, es posible que desee mantener los comentarios que publicó en las publicaciones del blog, pero digamos que fue publicado por un usuario anónimo (o eliminado). Equivalente de SQL: `SET_NULL`.
- **SET_DEFAULT:** Establece el valor por defecto. Equivalente de SQL: `SET_DEFAULT`.
- **SET(...):** Establece un valor dado. Esto no es parte del SQL estándar, es manejado completamente por Django.
- **DO_NOTHING:** Probablemente sea una muy mala idea ya que esto crearía problemas de integridad en la base de datos (haciendo referencia a un objeto que en realidad no existe). Equivalente de SQL: `NO_ACTION`.

El uso de las opciones anteriores, va a depender de los requerimientos que tengamos, pero una de las más comúnmente usadas es `CASCADE` ya que nos permite eliminar datos y no dejar datos relacionados huérfanos o corruptos, la cual la utilizaremos en el ejercicio guiado.

---

## 6. Ejercicio Guiado: OneToOneField

Crearemos dos modelos: uno **Cliente** y otro **Dirección**.
Entre estos habrá una relación One to One, ya que una dirección pertenece a un cliente y un cliente tiene asociada solo una dirección. (Para efectos prácticos del ejercicio, excluimos la posibilidad que dos o más clientes vivan en la misma dirección.)

**Paso 1:** Crear un entorno virtual, un proyecto y una app (que debe ser registrada en `settings.py`). En este caso la app se llamará `unidad02p01`. Utilizaremos SQLite3.

**Paso 2:** Definir los modelos.

```python
class Cliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellido = models.CharField(max_length=50, blank=False, null=False)
    edad = models.IntegerField(null=True, blank=True)
    creación = models.DateTimeField(auto_now_add=True)
    actualización = models.DateTimeField(auto_now=True)

class Direccion(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, primary_key=True)
    calle = models.CharField(max_length=100, blank=False, null=False)
    numero = models.CharField(max_length=10, blank=False, null=False)
    dpto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=100, blank=False, null=False)
    ciudad = models.CharField(max_length=100, blank=False, null=False)
```

**Paso 3:** Ejecutar migraciones.

```bash
python manage.py makemigrations
python manage.py migrate
```

**Paso 4:** Entrar al shell de Django y crear objetos.

```python
>>> from cap02p1.models import Cliente, Direccion
>>> cliente = Cliente(nombre="Juan", apellido="Perez", edad=30)
>>> cliente.save()
>>> direccion = Direccion(cliente=cliente, calle="alguna calle", numero="1234", dpto="1234", comuna="Santiago", ciudad="Santiago")
>>> direccion.save()
```

**Paso 5:** Revisar la bidireccionalidad.

```python
>>> print(cliente.direccion.__dict__)
{'__state': <django.db.models.base.ModelState object at 0x7f8ce78f5c40>, 'id': 1, 'cliente_id': 1, 'calle': 'alguna calle', 'numero': '1234', 'dpto': '1234', 'comuna': 'Santiago', 'ciudad': 'Santiago'}

>>> print(direccion.cliente.__dict__)
{'__state': <django.db.models.base.ModelState object at 0x7f8ce78f5b20>, 'cliente_id': 1, 'nombre': 'Juan', 'apellido': 'Perez', 'edad': 30, 'creacion': datetime.datetime(2021, 7, 28, 12, 27, 6, 310520, tzinfo=<UTC>), 'actualizacion': datetime.datetime(2021, 7, 28, 12, 27, 6, 310587, tzinfo=<UTC>)}
```

**Paso 6:** Probar el borrado en cascada.

```python
>>> cliente.delete()
(2, {'cap01p2.Direccion': 1, 'cap01p2.Cliente': 1})
```

---

## 7. Resumen de la Sesión

**Relaciones Muchos a Uno**
- **Esencia:** Vínculos de múltiples instancias a una única instancia de otro modelo.
- **Implementación:** A través de `ForeignKey`.
- **Borrado en Cascada:** `on_delete=models.CASCADE` asegura la integridad eliminando objetos relacionados si se borra el objeto referenciado.

**Relaciones Uno a Uno**
- **Esencia:** Asociación biunívoca entre una instancia de un modelo y otra.
- **Implementación:** Mediante `OneToOneField`.

**Claves del Manejo de Relaciones**
- La elección correcta entre Muchos a Uno y Uno a Uno impacta directamente en el diseño y la funcionalidad de la aplicación.
- La integridad de datos y la eficiencia en el modelado son fundamentales para construir aplicaciones robustas con Django.

---

## 8. Próxima Sesión

**Relaciones Muchos a Muchos:** Definirás un modelo con entidades que tienen relaciones muchos a muchos para resolver un problema determinado acorde al framework Django.

---

**{desafio} latam_**
Academia de talentos digitales