# Cuestionario: Sobreescritura de Métodos en Python

---

## Pregunta 1

**¿Cuál es el propósito principal de la sobreescritura de métodos en Programación Orientada a Objetos?**

A) Permitir que una clase hija herede automáticamente todos los métodos de la clase padre sin necesidad de definirlos

B) Proporcionar una implementación específica de un método en una clase hija, diferenciándola del comportamiento de la clase padre

C) Eliminar métodos no deseados de la clase padre en la clase hija

D) Crear nuevos métodos con nombres diferentes a los de la clase padre

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La sobreescritura de métodos permite que una clase hija proporcione su propia implementación de un método heredado, manteniendo el mismo nombre pero con comportamiento específico. Esto es fundamental para el polimorfismo, ya que permite que objetos de diferentes clases respondan al mismo mensaje de manera diferente.

</details>

---

## Pregunta 2

**Dado el siguiente código, ¿cuál será la salida al ejecutarlo?**

```python
class Dispositivo:
    def __init__(self, marca):
        self.marca = marca
    
    def encender(self):
        return "Dispositivo encendido"

class Telefono(Dispositivo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    
    def encender(self):
        return f"Teléfono {self.modelo} encendido"

class Tablet(Dispositivo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

dispositivos = [
    Dispositivo("Genérica"),
    Telefono("Samsung", "Galaxy"),
    Tablet("Apple", "iPad")
]

for d in dispositivos:
    print(d.encender())
```

A) 
```
Dispositivo encendido
Teléfono Galaxy encendido
Dispositivo encendido
```

B) 
```
Dispositivo encendido
Teléfono Galaxy encendido
Tablet iPad encendido
```

C) 
```
Dispositivo encendido
Dispositivo encendido
Dispositivo encendido
```

D) 
```
Teléfono Galaxy encendido
Dispositivo encendido
Dispositivo encendido
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** 
- Dispositivo: Usa su propio método `encender()` → "Dispositivo encendido"
- Teléfono: Sobrescribe `encender()` → "Teléfono Galaxy encendido"
- Tablet: No sobrescribe `encender()` → usa el método heredado → "Dispositivo encendido"
La salida demuestra cómo la sobreescritura permite comportamiento específico en clases hijas.

</details>

---

## Pregunta 3

**¿Cuál es la sintaxis correcta para sobrescribir un método en una clase hija en Python?**

A) 
```python
class Hija(Padre):
    override def metodo(self):
        return "Comportamiento hija"
```

B) 
```python
class Hija(Padre):
    def metodo(self):
        return "Comportamiento hija"
```

C) 
```python
class Hija(Padre):
    @override
    def metodo(self):
        return "Comportamiento hija"
```

D) 
```python
class Hija(Padre):
    def metodo(self) -> override:
        return "Comportamiento hija"
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** En Python, la sobreescritura de métodos no requiere una palabra clave especial como en otros lenguajes. Simplemente se define en la clase hija un método con el mismo nombre que el método de la clase padre que se desea sobrescribir. Python automáticamente utiliza la implementación de la clase hija cuando se invoca desde una instancia de esta.

</details>

---

## Pregunta 4

**En herencia múltiple en Python, ¿cómo se determina qué método ejecutar cuando una clase hija hereda de dos clases que sobrescriben el mismo método?**

A) Se ejecuta siempre el método de la clase padre que esté más abajo en la jerarquía

B) Se ejecuta según el Method Resolution Order (MRO), priorizando la primera clase heredada de izquierda a derecha

C) Se genera un error de compilación por ambigüedad

D) Se ejecuta el método que tenga la implementación más reciente

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** Python utiliza el Method Resolution Order (MRO) para determinar qué método ejecutar en herencia múltiple. El MRO sigue un orden específico que prioriza las clases según el orden en que se declaran en la herencia (de izquierda a derecha) y la profundidad en la jerarquía. Esto permite resolver conflictos de manera predecible sin errores.

</details>

---

## Pregunta 5

**¿Cuál es la forma correcta de llamar al método de la clase padre desde la clase hija en Python?**

A) `Padre.metodo(self)`

B) `super().metodo()`

C) `self.super().metodo()`

D) `self.Padre.metodo()`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La forma más recomendada y moderna es usar `super().metodo()`, que permite acceder al método de la clase padre de manera genérica. Aunque la opción A también puede funcionar, `super()` es más mantenible y funciona correctamente en herencia múltiple. Las opciones C y D son sintaxis incorrectas.

</details>

---

## Pregunta 6

**¿Qué permite lograr el uso de `super()` en el constructor de una clase hija?**

A) Evitar completamente la ejecución del constructor de la clase padre

B) Ejecutar el constructor de la clase padre y agregar funcionalidad adicional en la clase hija

C) Crear automáticamente todos los atributos sin necesidad de definirlos

D) Hacer que la clase hija herede solo el constructor y no otros métodos

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** `super().__init__()` en el constructor de una clase hija permite ejecutar el constructor de la clase padre, inicializando los atributos heredados, y luego agregar funcionalidad adicional específica de la clase hija. Esto es esencial para mantener la consistencia en la inicialización de objetos en una jerarquía de herencia.

</details>

---

## Pregunta 7

**Dado el siguiente código que implementa un sistema de vehículos, ¿cuál será la salida?**

```python
class Vehiculo:
    def __init__(self, color):
        self.color = color
    
    def describir(self):
        return f"Vehículo de color {self.color}"

class Coche(Vehiculo):
    def __init__(self, color, puertas):
        super().__init__(color)
        self.puertas = puertas
    
    def describir(self):
        return f"Coche con {self.puertas} puertas"

class Moto(Vehiculo):
    def __init__(self, color, cilindrada):
        super().__init__(color)
        self.cilindrada = cilindrada

vehiculos = [
    Coche("Rojo", 4),
    Moto("Azul", 500),
    Vehiculo("Verde")
]

for v in vehiculos:
    print(v.describir())
```

A) 
```
Coche con 4 puertas
Moto Azul con 500cc
Vehículo de color Verde
```

B) 
```
Coche con 4 puertas
Vehículo de color Azul
Vehículo de color Verde
```

C) 
```
Coche con 4 puertas
Vehiculo de color Azul
Vehiculo de color Verde
```

D) 
```
Coche con 4 puertas
Vehículo de color Verde
Vehículo de color Verde
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** 
- Coche: Sobrescribe `describir()` → "Coche con 4 puertas"
- Moto: No sobrescribe `describir()` → usa el método de Vehiculo → "Vehículo de color Azul"
- Vehiculo: Usa su propio método → "Vehículo de color Verde"
La salida muestra que los métodos no sobrescritos mantienen el comportamiento de la clase padre.

</details>

---

## Pregunta 8

**¿Cuál es la forma correcta de sobrescribir un setter de una propiedad en una clase hija?**

A) 
```python
class Hija(Padre):
    @property
    def atributo(self):
        return self.__atributo
    
    @atributo.setter
    def atributo(self, valor):
        self.__atributo = valor
```

B) 
```python
class Hija(Padre):
    def set_atributo(self, valor):
        self.__atributo = valor
```

C) 
```python
class Hija(Padre):
    @property
    def atributo(self):
        return self.__atributo
```

D) 
```python
class Hija(Padre):
    @atributo.setter
    def atributo(self, valor):
        self.__atributo = valor
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** Para sobrescribir un setter en Python, se debe redefinir la propiedad completa en la clase hija (getter y setter). No se puede sobrescribir solo el setter. La opción A muestra la sintaxis correcta para definir una propiedad con getter y setter en la clase hija.

</details>

---

## Pregunta 9

**¿Cuál es la diferencia fundamental entre sobreescritura (override) y sobrecarga (overload) de métodos?**

A) La sobreescritura se aplica en la misma clase, mientras que la sobrecarga requiere herencia

B) La sobreescritura requiere herencia y redefine un método existente, mientras que la sobrecarga permite múltiples métodos con el mismo nombre pero diferentes parámetros

C) Son conceptos idénticos que se refieren a lo mismo

D) La sobreescritura solo funciona con constructores, mientras que la sobrecarga funciona con cualquier método

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** 
- **Sobreescritura (Override)**: Requiere herencia y redefine un método de la clase padre en la clase hija, manteniendo la misma firma.
- **Sobrecarga (Overload)**: Permite definir múltiples métodos con el mismo nombre pero diferentes parámetros en la misma clase. Python no soporta sobrecarga tradicional, aunque se puede simular con parámetros opcionales.

</details>

---

## Pregunta 10

**Se necesita implementar un sistema donde la clase `Animal` tenga un método `sonido()` que las clases hijas sobrescriban. Además, `super()` debe usarse en el constructor. ¿Cuál opción implementa correctamente esta estructura?**

A) 
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def sonido(self):
        return "Guau"
```

B) 
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        Animal.__init__(nombre)
        self.raza = raza
    
    def sonido(self):
        return "Guau"
```

C) 
```python
class Animal:
    def sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def sonido(self):
        return "Guau"
```

D) 
```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def sonido(self):
        return "Guau"
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La opción A implementa correctamente:
- Animal: constructor que recibe nombre y método sonido()
- Perro: hereda de Animal, usa super() en constructor, sobrescribe sonido()
- La estructura permite reutilizar código y polimorfismo

La opción B no usa super() correctamente, C no usa super() en constructor (no inicializa nombre de Animal), y D no define sonido() en Animal.

</details>