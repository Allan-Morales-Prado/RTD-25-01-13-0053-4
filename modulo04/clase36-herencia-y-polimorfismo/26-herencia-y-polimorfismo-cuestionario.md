# Cuestionario: Herencia y Polimorfismo en Python

---

## Pregunta 1

**¿Cuál de las siguientes afirmaciones describe correctamente la relación entre herencia y polimorfismo en Programación Orientada a Objetos?**

A) La herencia permite crear nuevas clases a partir de otras, mientras que el polimorfismo permite que objetos de diferentes clases respondan de manera específica al mismo mensaje

B) El polimorfismo es un tipo específico de herencia que solo funciona con clases abstractas

C) La herencia y el polimorfismo son conceptos idénticos que se refieren a la misma característica de la POO

D) El polimorfismo permite heredar múltiples clases padre, mientras que la herencia solo permite heredar una

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La herencia es un mecanismo estructural que permite derivar clases para crear jerarquías y reutilizar código. El polimorfismo es un comportamiento que permite que objetos de diferentes clases en una jerarquía respondan al mismo mensaje (método) de manera específica según su tipo. Son conceptos complementarios pero distintos.

</details>

---

## Pregunta 2

**Dado el siguiente código, ¿cuál será la salida al ejecutarlo?**

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def sonido(self):
        return "Guau"

class Gato(Animal):
    pass

animales = [Perro("Rex"), Gato("Misi"), Animal("Ser")]

for animal in animales:
    print(animal.sonido())
```

A) 
```
Guau
Sonido genérico
Sonido genérico
```

B) 
```
Guau
Sonido genérico
Error
```

C) 
```
Guau
Guau
Sonido genérico
```

D) 
```
Guau
Sonido genérico
Miau
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** 
- Perro: Sobrescribe `sonido()` para retornar "Guau"
- Gato: No sobrescribe `sonido()`, por lo que usa el método de Animal: "Sonido genérico"
- Animal: Instancia directa, usa su propio método: "Sonido genérico"
La salida refleja el polimorfismo: cada objeto responde según su clase real.

</details>

---

## Pregunta 3

**¿Cuál es la sintaxis correcta en Python para definir una clase hija que herede de una clase padre?**

A) 
```python
class ClaseHija extends ClasePadre:
    pass
```

B) 
```python
class ClaseHija(ClasePadre):
    pass
```

C) 
```python
class ClaseHija inherits ClasePadre:
    pass
```

D) 
```python
class ClaseHija <- ClasePadre:
    pass
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** En Python, la herencia se especifica colocando la clase padre entre paréntesis en la definición de la clase hija. Esta es la sintaxis correcta y específica de Python. Las otras opciones corresponden a otros lenguajes (extends en Java, inherits en algunos lenguajes hipotéticos).

</details>

---

## Pregunta 4

**En una jerarquía de herencia múltiple en Python, si una clase hija hereda de dos clases padres y ambas definen el mismo método, ¿qué método se ejecutará al llamarlo desde la clase hija?**

A) El método de la primera clase padre listada en la definición de la clase hija

B) El método de la última clase padre listada en la definición de la clase hija

C) El método que tenga el nombre más corto

D) Se generará un error de ambigüedad

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** En Python, cuando hay conflicto de métodos en herencia múltiple, se utiliza el Method Resolution Order (MRO), que prioriza la primera clase padre listada en la definición de izquierda a derecha. Esto es conocido como "depth-first, left-to-right" y es una característica específica de Python que resuelve la ambigüedad.

</details>

---

## Pregunta 5

**¿Cuál de las siguientes opciones implementa correctamente una clase abstracta con un método abstracto en Python?**

A) 
```python
class Forma:
    def area(self):
        raise NotImplementedError("Método abstracto")
```

B) 
```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
```

C) 
```python
class Forma:
    @abstractmethod
    def area(self):
        pass
```

D) 
```python
from abc import abstractmethod

class Forma:
    @abstractmethod
    def area(self):
        pass
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** Para implementar correctamente una clase abstracta en Python se necesita:
1. Importar `ABC` y `abstractmethod` del módulo `abc`
2. Heredar de `ABC`
3. Usar el decorador `@abstractmethod` en los métodos abstractos
La opción A es una simulación pero no es una clase abstracta verdadera, C y D faltan la herencia de `ABC` o las importaciones necesarias.

</details>

---

## Pregunta 6

**¿Cuál es la principal ventaja de utilizar el polimorfismo en un sistema orientado a objetos?**

A) Permite que las clases hijas hereden automáticamente todos los atributos de la clase padre

B) Facilita la creación de código más flexible y extensible, donde nuevos tipos de objetos pueden ser añadidos sin modificar el código existente

C) Reduce el uso de memoria al compartir métodos entre todas las instancias

D) Elimina la necesidad de definir constructores en las clases hijas

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** El polimorfismo permite escribir código que trabaja con una interfaz común (la clase padre) y puede funcionar con cualquier objeto que implemente esa interfaz. Esto facilita añadir nuevas clases sin modificar el código existente, haciendo el sistema más flexible, mantenible y extensible. Las otras opciones son características de la herencia o simplificaciones incorrectas.

</details>

---

## Pregunta 7

**Dado el siguiente código que implementa un sistema de figuras, ¿cuál será la salida?**

```python
class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def calcular_area(self):
        return 0

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio
    
    def calcular_area(self):
        return 3.14 * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__("Cuadrado")
        self.lado = lado
    
    def calcular_area(self):
        return self.lado * self.lado

figuras = [Circulo(5), Cuadrado(4), Figura("Genérica")]

for f in figuras:
    print(f"{f.nombre}: {f.calcular_area()}")
```

A) 
```
Círculo: 78.5
Cuadrado: 16
Genérica: 0
```

B) 
```
Círculo: 78.5
Cuadrado: 16
Error: la clase Figura no tiene método calcular_area
```

C) 
```
Círculo: 78.5
Cuadrado: 16
Figura: 0
```

D) 
```
Círculo: 78.5
Cuadrado: 16
0
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** 
- Círculo(5): Calcula área = 3.14 * 25 = 78.5
- Cuadrado(4): Calcula área = 4 * 4 = 16
- Figura("Genérica"): Usa el método de la clase padre que retorna 0
El polimorfismo permite que cada objeto use su propia implementación de `calcular_area()`, y `super().__init__()` asegura que los nombres se establezcan correctamente.

</details>

---

## Pregunta 8

**¿Cuál es la forma correcta de invocar al método de la clase padre desde una clase hija en Python?**

A) `Padre.metodo(self)`

B) `super().metodo()`

C) `self.Padre.metodo()`

D) `this.Padre.metodo()`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La función `super()` es el mecanismo estándar en Python para acceder a métodos de la clase padre. Permite invocar métodos de la clase padre sin necesidad de nombrarla explícitamente, lo cual es más mantenible (especialmente en herencia múltiple). La opción A también podría funcionar en algunos casos pero es menos elegante y no recomendada.

</details>

---

## Pregunta 9

**En un sistema de gestión de empleados, se tiene una clase base `Empleado` con un método `calcular_salario()`. Las clases `Gerente` y `Desarrollador` heredan de `Empleado` y sobrescriben el método. Si se tiene una lista de empleados de diferentes tipos y se itera llamando a `calcular_salario()`, ¿qué concepto de POO se está aplicando?**

A) Encapsulamiento

B) Herencia simple

C) Polimorfismo

D) Abstracción

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** Este es un ejemplo clásico de polimorfismo. Aunque todos los objetos en la lista son de tipo `Empleado` (o subtipos), cada uno ejecuta su propia versión del método `calcular_salario()`. El código no necesita saber el tipo específico de cada empleado; cada objeto "sabe" cómo calcular su propio salario. Esto permite tratar a todos los empleados de manera uniforme mientras se mantiene un comportamiento específico por tipo.

</details>

---

## Pregunta 10

**Se necesita implementar un sistema donde una clase `Robot` tenga un método `accion()` que pueda ser sobrescrito por clases específicas como `RobotLimpieza` y `RobotCocina`. Además, se requiere que todos los robots tengan un atributo `nombre`. ¿Cuál opción implementa correctamente esta estructura?**

A) 
```python
class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def accion(self):
        return "Acción genérica"

class RobotLimpieza(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def accion(self):
        return "Limpiando"

class RobotCocina(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def accion(self):
        return "Cocinando"
```

B) 
```python
class Robot:
    def __init__(self, nombre):
        self.nombre = nombre

class RobotLimpieza(Robot):
    def limpiar(self):
        return "Limpiando"

class RobotCocina(Robot):
    def cocinar(self):
        return "Cocinando"
```

C) 
```python
class Robot:
    def accion(self):
        return "Acción genérica"

class RobotLimpieza(Robot):
    def accion(self):
        return "Limpiando"

class RobotCocina(Robot):
    def accion(self):
        return "Cocinando"
```

D) 
```python
class RobotLimpieza:
    def accion(self):
        return "Limpiando"

class RobotCocina:
    def accion(self):
        return "Cocinando"
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La opción A implementa correctamente:
- Una clase base `Robot` con constructor que recibe `nombre`
- Herencia mediante `class RobotLimpieza(Robot)`
- Uso de `super().__init__()` para inicializar el atributo heredado
- Sobrescritura del método `accion()` en las clases hijas
- Polimorfismo: todas las clases tienen el método `accion()`

La opción B cambia el nombre del método (no es polimorfismo), C no incluye el atributo `nombre`, y D no utiliza herencia.

</details>
