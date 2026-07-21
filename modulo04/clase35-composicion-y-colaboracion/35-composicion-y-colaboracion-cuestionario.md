# Cuestionario: Colaboración y Composición en POO con Python

---

## Pregunta 1

**¿Cuál de las siguientes afirmaciones describe correctamente la diferencia fundamental entre colaboración y composición en Programación Orientada a Objetos?**

A) En la colaboración los objetos dependen jerárquicamente unos de otros, mientras que en la composición los objetos son completamente independientes

B) La colaboración se basa en la herencia de clases para compartir comportamiento, mientras que la composición utiliza la delegación de responsabilidades

C) La colaboración implica objetos independientes que interactúan mediante mensajes, mientras que la composición establece una relación de dependencia existencial donde el componente no puede vivir sin el compuesto

D) La colaboración requiere que un objeto contenga físicamente al otro, mientras que la composición solo requiere comunicación temporal entre objetos

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** La colaboración se caracteriza por la interacción entre objetos independientes que se comunican mediante el paso de mensajes (llamadas a métodos). La composición, por otro lado, es una relación estructural donde el componente (objeto contenido) depende del compuesto (objeto contenedor) para existir, compartiendo su ciclo de vida. La opción C describe correctamente ambas relaciones.

</details>

---

## Pregunta 2

**Dado el siguiente código, ¿cuál será la salida al ejecutarlo?**

```python
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
    
    def encender(self):
        return f"Motor {self.tipo} encendido"

class Coche:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        self.motor = Motor(tipo_motor)
    
    def arrancar(self):
        return f"{self.marca}: {self.motor.encender()}"

coche = Coche("Toyota", "V8")
print(coche.arrancar())
```

A) Error: el objeto Motor no puede ser creado

B) Toyota: Motor V8 encendido

C) Coche: Motor V8 encendido

D) Toyota: encendido

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** El código muestra una relación de composición donde Coche contiene un Motor. El motor se crea dentro del constructor de Coche con el tipo "V8". Cuando se llama a arrancar(), se accede al motor y se invoca su método encender(), que retorna "Motor V8 encendido". El método arrancar() concatena la marca del coche con este mensaje, produciendo "Toyota: Motor V8 encendido".

</details>

---

## Pregunta 3

**Se necesita implementar un sistema donde un objeto Curso contenga una lista de Estudiantes. Los estudiantes pueden existir independientemente del curso y pueden estar inscritos en múltiples cursos simultáneamente. ¿Cuál opción implementa correctamente esta relación?**

A) 
```python
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.curso = None

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiante = Estudiante("Juan")
```

B) 
```python
class Estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
```

C) 
```python
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre, estudiante):
        self.nombre = nombre
        self.estudiante = estudiante
```

D) 
```python
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
    
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** La opción D implementa correctamente una agregación porque:
- Los estudiantes se crean externamente y se pasan al curso mediante el método agregar_estudiante
- El curso mantiene una lista de estudiantes
- Los estudiantes pueden existir sin el curso (relación débil)
- Un mismo estudiante podría estar en múltiples cursos

Las otras opciones presentan problemas: A y B son relaciones uno a uno rígidas, C es una composición (crea el estudiante dentro del curso).

</details>

---

## Pregunta 4

**En un sistema de gestión de pedidos, se tienen las clases Pedido, ItemPedido y Producto. El Pedido contiene una lista de ItemPedido, y cada ItemPedido referencia a un Producto. Si se elimina un Pedido, sus ItemPedido también deben eliminarse, pero los Productos deben permanecer en el sistema. ¿Qué tipo de relación debe existir entre Pedido-ItemPedido e ItemPedido-Producto respectivamente?**

A) Composición y Agregación

B) Agregación y Composición

C) Colaboración y Composición

D) Composición y Colaboración

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** 
- Pedido → ItemPedido: Debe ser **Composición** porque los ítems del pedido no tienen sentido sin el pedido mismo; su ciclo de vida está ligado al pedido.
- ItemPedido → Producto: Debe ser **Agregación** porque los productos existen independientemente de cualquier pedido específico; un producto puede estar en múltiples pedidos y permanecer en el sistema aunque se elimine un pedido.

</details>

---

## Pregunta 5

**Dada la siguiente clase, ¿cuál es la forma correcta de implementar un método que permita acceder al atributo privado `__saldo` y otro que permita modificarlo con validación (no permitir valores negativos)?**

```python
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial
```

A) 
```python
def get_saldo(self):
    return self.__saldo

def set_saldo(self, nuevo_saldo):
    self.__saldo = nuevo_saldo
```

B) 
```python
@property
def saldo(self):
    return self.__saldo

@saldo.setter
def saldo(self, nuevo_saldo):
    if nuevo_saldo >= 0:
        self.__saldo = nuevo_saldo
```

C) 
```python
def obtener_saldo(self):
    return self.__saldo

def modificar_saldo(self, nuevo_saldo):
    if nuevo_saldo >= 0:
        self.__saldo = nuevo_saldo
    else:
        raise ValueError("Saldo no puede ser negativo")
```

D) 
```python
@property
def saldo(self):
    return self.__saldo

def cambiar_saldo(self, nuevo_saldo):
    if nuevo_saldo >= 0:
        self.__saldo = nuevo_saldo
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La opción B es la implementación correcta de propiedades en Python:
- El decorador `@property` permite acceder al atributo como si fuera público mediante `cuenta.saldo`
- El decorador `@saldo.setter` permite modificar el atributo con validación mediante `cuenta.saldo = nuevo_valor`
- La validación asegura que el saldo no sea negativo

La opción A no tiene validación, C usa métodos tradicionales en lugar de propiedades (menos "pythónico"), y D tiene un setter sin el decorador apropiado.

</details>

---

## Pregunta 6

**Dado el siguiente código que implementa un sistema de gestión de tareas, ¿cuál será la salida?**

```python
class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False
    
    def marcar_completada(self):
        self.completada = True
        return f"Tarea '{self.descripcion}' completada"

class Proyecto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__tareas = []
    
    def agregar_tarea(self, descripcion, prioridad):
        tarea = Tarea(descripcion, prioridad)
        self.__tareas.append(tarea)
        return tarea
    
    def completar_tarea(self, indice):
        if 0 <= indice < len(self.__tareas):
            return self.__tareas[indice].marcar_completada()
        return "Tarea no encontrada"

proyecto = Proyecto("Python")
t1 = proyecto.agregar_tarea("Escribir documentación", "Alta")
t2 = proyecto.agregar_tarea("Revisar código", "Media")
print(proyecto.completar_tarea(0))
print(proyecto.completar_tarea(1))
```

A) 
```
True
True
```

B) 
```
Tarea completada
Tarea completada
```

C) 
```
Tarea 'Escribir documentación' completada
Tarea 'Revisar código' completada
```

D) 
```
Escribir documentación completada
Revisar código completada
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** El código implementa una relación de composición donde Proyecto contiene Tareas. Al agregar una tarea, se crea una instancia de Tarea internamente. Cuando se llama a completar_tarea(0), se accede a la primera tarea y se invoca su método marcar_completada(), que retorna el mensaje formateado con la descripción de la tarea entre comillas simples. Lo mismo ocurre con la segunda tarea. La opción C muestra exactamente el mensaje retornado por cada tarea.

</details>

---

## Pregunta 7

**En una relación de composición entre la clase A y la clase B, ¿cuál de las siguientes afirmaciones es correcta?**

A) La clase A debe implementar todos los métodos de la clase B para que funcionen correctamente

B) La clase B es creada típicamente dentro del constructor de la clase A y su ciclo de vida está ligado al de A

C) La clase B puede existir y ser utilizada sin que exista una instancia de la clase A

D) La clase A puede crear múltiples instancias de B y todas compartirán el mismo estado

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La característica fundamental de la composición es que el componente (clase B) es creado y gestionado por el compuesto (clase A), típicamente en su constructor. El ciclo de vida del componente está ligado al compuesto: cuando el compuesto se destruye, el componente también. Las opciones A y C son incorrectas (el componente no existe independientemente y no necesita implementar todos los métodos), mientras que D es incorrecta porque cada instancia de A tiene sus propias instancias de B.

</details>

---

## Pregunta 8

**Se necesita implementar un sistema de reservas de vuelos donde un Vuelo contiene una lista de Pasajeros. Cada Pasajero puede estar en múltiples vuelos y debe poder existir independientemente. ¿Cuál opción implementa correctamente esta relación?**

A) 
```python
class Pasajero:
    def __init__(self, nombre, pasaporte):
        self.nombre = nombre
        self.pasaporte = pasaporte

class Vuelo:
    def __init__(self, numero, destino):
        self.numero = numero
        self.destino = destino
        self.pasajeros = []
    
    def agregar_pasajero(self, pasajero):
        if pasajero not in self.pasajeros:
            self.pasajeros.append(pasajero)
            return True
        return False
```

B) 
```python
class Pasajero:
    def __init__(self, nombre, pasaporte, vuelo):
        self.nombre = nombre
        self.pasaporte = pasaporte
        self.vuelo = vuelo

class Vuelo:
    def __init__(self, numero, destino):
        self.numero = numero
        self.destino = destino
        self.pasajero = Pasajero("Juan", "ABC123", self)
```

C) 
```python
class Pasajero:
    def __init__(self, nombre, pasaporte):
        self.nombre = nombre
        self.pasaporte = pasaporte

class Vuelo:
    def __init__(self, numero, destino):
        self.numero = numero
        self.destino = destino
        self.pasajeros = []
    
    def agregar_pasajero(self, nombre, pasaporte):
        pasajero = Pasajero(nombre, pasaporte)
        self.pasajeros.append(pasajero)
        return pasajero
```

D) 
```python
class Pasajero:
    def __init__(self, nombre, pasaporte):
        self.nombre = nombre
        self.pasaporte = pasaporte
        self.vuelos = []

class Vuelo:
    def __init__(self, numero, destino):
        self.numero = numero
        self.destino = destino
    
    def agregar_pasajero(self, pasajero):
        pasajero.vuelos.append(self)
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La opción A implementa correctamente una agregación donde:
- Los pasajeros se crean externamente y se pasan al vuelo mediante el método agregar_pasajero
- El vuelo mantiene una lista de pasajeros
- Los pasajeros pueden existir sin el vuelo
- Un pasajero puede estar en múltiples vuelos

La opción B es composición (crea el pasajero internamente y solo permite uno), la C también es composición (crea el pasajero dentro de agregar_pasajero), y la D aunque permite múltiples vuelos, no mantiene la lista de pasajeros en el vuelo, lo que dificulta consultar quiénes están en un vuelo específico.

</details>

---

## Pregunta 9

**¿Cuál es la diferencia clave entre agregación y composición en términos de implementación en Python?**

A) En composición siempre se usa el decorador @property, en agregación no

B) La agregación requiere herencia múltiple mientras que la composición no

C) En agregación, el componente se pasa como argumento al constructor; en composición, el componente se crea dentro del constructor

D) La agregación usa listas mientras que la composición usa diccionarios para almacenar los componentes

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** La diferencia clave en la implementación es:
- **Agregación**: El componente se crea fuera (independientemente) y se pasa al constructor del compuesto como argumento.
- **Composición**: El componente se crea dentro del constructor del compuesto, lo que liga su ciclo de vida al del compuesto.

Las otras opciones son incorrectas: el uso de @property es independiente del tipo de relación, ninguna requiere herencia múltiple, y ambas pueden usar cualquier estructura de datos.

</details>

---

## Pregunta 10

**Dado el siguiente código de un sistema de gestión de biblioteca digital, ¿qué tipo de relación existe entre Usuario-Libro y Biblioteca-Usuario?**

```python
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []
    
    def solicitar_prestamo(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            return f"{self.nombre} tomó prestado {libro.titulo}"
        return f"{libro.titulo} no está disponible"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []
        self.catalogo = []
    
    def registrar_usuario(self, usuario):
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
            return f"Usuario {usuario.nombre} registrado"
        return "Usuario ya registrado"
    
    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        return f"Libro {libro.titulo} agregado al catálogo"
```

A) Usuario-Libro: Colaboración, Biblioteca-Usuario: Agregación

B) Usuario-Libro: Composición, Biblioteca-Usuario: Agregación

C) Usuario-Libro: Agregación, Biblioteca-Usuario: Colaboración

D) Usuario-Libro: Colaboración, Biblioteca-Usuario: Composición

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** 
- **Usuario-Libro: Colaboración**: Los usuarios interactúan con los libros mediante el método solicitar_prestamo, pero los libros existen independientemente de los usuarios. Un libro puede existir sin un usuario, y un usuario puede existir sin libros. Hay interacción mediante paso de mensajes, no una relación estructural de pertenencia.
- **Biblioteca-Usuario: Agregación**: Los usuarios se registran en la biblioteca (se pasan como argumento al método registrar_usuario), pero pueden existir fuera de ella. Un usuario podría pertenecer a múltiples bibliotecas y la biblioteca puede existir sin usuarios.

</details>