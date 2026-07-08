# Introducción a la programación orientada a objetos con Python

**1. En el paradigma de Programación Orientada a Objetos (POO), ¿cuál es la principal diferencia con la Programación Estructurada?**

A) La POO utiliza funciones, mientras que la estructurada usa objetos.
B) La POO organiza el programa en torno a objetos que encapsulan datos y comportamiento, mientras que la estructurada se organiza en una secuencia de procedimientos o funciones.
C) La POO se enfoca en la claridad y simplicidad del código, mientras que la estructurada se enfoca en la encapsulación.
D) La POO es más rápida que la programación estructurada.

<details>
<summary><strong>Ver respuesta y justificación</strong></summary>

**Respuesta correcta: B)**

La diferencia fundamental radica en la organización y el enfoque. La POO modela el mundo real mediante objetos que contienen sus propios datos (atributos) y las operaciones que pueden realizar (métodos). La programación estructurada, por otro lado, se centra en escribir procedimientos o funciones que operan sobre datos, los cuales están separados.

</details>

---

**2. ¿Cuál de las siguientes afirmaciones describe mejor la relación entre una clase y un objeto?**

A) Una clase es una instancia específica de un objeto.
B) Un objeto es un "molde" o "plano" para crear clases.
C) Una clase es un "molde" o "plano" que define la estructura y el comportamiento, y un objeto es una instancia creada a partir de ese molde.
D) Una clase y un objeto son el mismo concepto en Python.

<details>
<summary><strong>Ver respuesta y justificación</strong></summary>

**Respuesta correcta: C)**

La analogía del "molde" (clase) y la "galleta" (objeto) es la más común y precisa. La clase define *qué* tendrá el objeto, mientras que el objeto es la realización concreta de esa definición.

</details>

---

**3. Los atributos de clase en Python se caracterizan por:**

A) Definirse siempre dentro del método `__init__`.
B) Pertenecer a la definición de la clase y ser accesibles sin necesidad de crear una instancia.
C) No poder ser modificados después de la creación de la clase.
D) Ser únicos para cada instancia del objeto.

<details>
<summary><strong>Ver respuesta y justificación</strong></summary>

**Respuesta correcta: B)**

Los atributos de clase (o estáticos) son compartidos por todas las instancias de la clase y se definen directamente en el cuerpo de la clase. Por eso, se pueden acceder a ellos usando el nombre de la clase (ej: `MiClase.atributo`) sin necesidad de instanciar un objeto.

</details>

---

**4. En la analogía de la clase `Automóvil` presentada en el material, el método `calcularConsumo(self, distancia)` es un ejemplo de:**

A) Un comportamiento que el objeto `Automóvil` puede realizar.
B) Un atributo de clase.
C) Una característica estática del automóvil.
D) Un constructor de la clase.

<details>
<summary><strong>Ver respuesta y justificación</strong></summary>

**Respuesta correcta: A)**

Los métodos definen las acciones o comportamientos que un objeto puede realizar. `calcularConsumo` es una acción que un automóvil específico (una instancia) puede ejecutar usando sus propios datos (como `consumo_por_km` y la `distancia` proporcionada).

</details>

---

**5. En el contexto de Python, ¿qué significa que "todo es un objeto"?**

A) Que todas las variables deben ser definidas dentro de una clase.
B) Que es obligatorio usar el paradigma de POO para todo programa.
C) Que las funciones no pueden ser tratadas como objetos.
D) Que cada valor en Python tiene un tipo asociado, que está definido por una clase.

<details>
<summary><strong>Ver respuesta y justificación</strong></summary>

**Respuesta correcta: D)**

El principio de que "todo es un objeto" en Python significa que cualquier valor (ya sea un número, una cadena, una lista, una función, o una instancia de una clase personalizada) tiene un tipo, y ese tipo es una clase. Esto permite una gran flexibilidad y consistencia en el lenguaje.

</details>

---

**6. Se tiene el siguiente código:**
```python
class Venta:
    iva = 0.19

    def __init__(self, monto):
        self.monto = monto
        self.impuesto = monto * Venta.iva
```
¿Cuál de las siguientes afirmaciones es correcta?

i. `iva` es un atributo de instancia.
ii. `monto` es un atributo de clase.
iii. `self.impuesto` es un atributo de clase.

A) Sólo i.
B) i y ii.
C) i y iii.
D) Ninguna de las anteriores

<details>
<summary><strong>Ver respuesta y justificación</strong></summary>

**Respuesta correcta: D)**

`iva` está definido directamente en el cuerpo de la clase, por lo que es un atributo de clase (compartido por todas las ventas). `monto` se asigna a `self` dentro del constructor (`__init__`), lo que lo convierte en un atributo de instancia (único para cada objeto `Venta`) al igual que `impuesto`.

</details>

---

**7. ¿Cuál es el propósito principal del método `__init__` en una clase de Python?**

A) Definir los atributos de clase.
B) Inicializar el estado de un nuevo objeto cuando es instanciado.
C) Eliminar un objeto de la memoria.
D) Hacer que la clase sea pública.

<details>
<summary><strong>Ver respuesta y justificación</strong></summary>

**Respuesta correcta: B)**

El método `__init__` es el constructor de la clase. Se ejecuta automáticamente al crear una nueva instancia (`MiClase()`) y su función es establecer los valores iniciales de los atributos de instancia para ese nuevo objeto.

</details>