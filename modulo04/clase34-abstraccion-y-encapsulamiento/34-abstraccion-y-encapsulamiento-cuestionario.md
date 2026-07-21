# Cuestionario: Abstracción y Encapsulamiento en POO con Python

## Pregunta 1

**¿Cuál de las siguientes afirmaciones sobre la abstracción en Python es correcta?**

A) Una clase abstracta puede ser instanciada directamente si todos sus métodos tienen implementación
B) Los métodos abstractos en Python pueden tener implementación parcial y las subclases pueden extenderla usando `super()`
C) Para crear una clase abstracta en Python, solo es necesario usar el decorador `@abstractmethod` en al menos un método
D) Las clases abstractas en Python no pueden tener métodos concretos (con implementación)

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** 
Los métodos abstractos en Python pueden tener implementación parcial. Las subclases están obligadas a implementar el método abstracto, pero pueden (y es buena práctica) usar `super()` para extender la funcionalidad de la clase padre. Las otras opciones son incorrectas porque: (A) las clases abstractas nunca se pueden instanciar directamente, (C) también se necesita heredar de `ABC`, y (D) las clases abstractas pueden tener métodos concretos además de los abstractos.

</details>

---

## Pregunta 2

**¿Cuál será la salida del siguiente código?**

```python
from abc import ABC, abstractmethod

class Instrumento(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self._estado = "apagado"
    
    @abstractmethod
    def tocar(self):
        pass
    
    def encender(self):
        self._estado = "encendido"
        print(f"{self.nombre} está {self._estado}")

class Guitarra(Instrumento):
    def __init__(self):
        super().__init__("Guitarra")
    
    def tocar(self):
        print("¡Rasgueo de cuerdas!")

g = Guitarra()
g.encender()
g.tocar()
```

A) `Guitarra está encendido` seguido de `¡Rasgueo de cuerdas!`
B) `Error: no se puede instanciar la clase abstracta`
C) `Nombre: Guitarra` seguido de `¡Rasgueo de cuerdas!`
D) `Guitarra está apagado` seguido de `¡Rasgueo de cuerdas!`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:**
La clase `Guitarra` implementa correctamente el método abstracto `tocar()`, por lo que puede ser instanciada. Al llamar a `g.encender()`, se ejecuta el método concreto heredado de `Instrumento`, que cambia el estado a "encendido" y muestra el mensaje. Luego, `g.tocar()` imprime el sonido de la guitarra. Las otras opciones son incorrectas porque el código es válido y funciona como se describe.

</details>

---

## Pregunta 3

**¿Cuál de las siguientes implementaciones de una clase abstracta es sintácticamente correcta?**

A)
```python
class Figura:
    @abstractmethod
    def area(self):
        pass
```

B)
```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area():
        pass
```

C)
```python
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area(self):
        return 0
```

D)
```python
from abc import ABC

class Figura(ABC):
    def area(self):
        raise NotImplementedError
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:**
La opción C es correcta porque importa correctamente `ABC` y `@abstractmethod`, hereda de `ABC` para definir una clase abstracta, y usa `@abstractmethod` correctamente. Aunque un método abstracto normalmente solo tiene `pass`, también puede tener una implementación básica que las subclases pueden extender usando `super()`. La opción A falta la importación y herencia de `ABC`. La B falta el parámetro `self`. La D define un método concreto, no abstracto, aunque lanza una excepción.

</details>

---

## Pregunta 4

**¿Cuál será la salida del siguiente código?**

```python
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        self.__velocidad = 0
    
    @property
    def velocidad(self):
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self, valor):
        if valor >= 0:
            self.__velocidad = valor

class Coche(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo

v = Coche("Toyota", "Corolla")
v.velocidad = 120
print(v.velocidad)
print(v._Vehiculo__velocidad)
```

A) `120` seguido de `120`
B) `0` seguido de `0`
C) `120` seguido de un `AttributeError`
D) `Error: no se puede acceder a un atributo privado`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:**
El atributo `__velocidad` tiene name mangling a `_Vehiculo__velocidad`. El setter `velocidad` valida que el valor sea mayor o igual a 0 y asigna 120 correctamente. El getter `velocidad` retorna el valor, y el acceso directo a `_Vehiculo__velocidad` también funciona porque ese es el nombre real del atributo. Las otras opciones son incorrectas porque el código es válido y ambas formas de acceso muestran el valor 120.

</details>

---

## Pregunta 5

**¿Cuál es la principal diferencia entre un atributo con prefijo `_` y uno con prefijo `__` en Python?**

A) `_atributo` es un método mágico, mientras que `__atributo` es un atributo normal
B) `_atributo` es completamente privado e inaccesible, mientras que `__atributo` es protegido
C) `_atributo` es una convención para "protegido", mientras que `__atributo` sufre name mangling
D) Ambos son idénticos en su funcionamiento y solo difieren en la sintaxis

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:**
El prefijo `_atributo` es una convención que indica "no tocar" (protegido) pero es técnicamente accesible y no tiene name mangling. El prefijo `__atributo` sí sufre name mangling, cambiando su nombre internamente a `_Clase__atributo` para evitar colisiones en herencia. La opción A es incorrecta porque los métodos mágicos usan `__atributo__` (doble guión al inicio y final). La B es incorrecta porque ninguno es realmente privado. La D es falsa porque tienen comportamientos diferentes.

</details>

---

## Pregunta 6

**Dado el siguiente código, ¿qué método debe implementar la clase `Cuadrado` para que sea válida?**

```python
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    # ¿Qué falta aquí?
```

A) Solo `def area(self): return self.lado ** 2`
B) Solo `def perimetro(self): return self.lado * 4`
C) `def area(self): return self.lado ** 2` y `def perimetro(self): return self.lado * 4`
D) `@property def area(self): return self.lado ** 2`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:**
La clase `Forma` define dos métodos abstractos: `area` y `perimetro`. Para que la clase `Cuadrado` no sea abstracta y pueda ser instanciada, debe implementar **todos** los métodos abstractos de su clase padre. La opción C es la única que implementa ambos métodos. La opción A y B solo implementan uno de los dos. La opción D implementa `area` como propiedad pero no implementa `perimetro`, y además no es la sintaxis requerida para un método abstracto.

</details>

---

## Pregunta 7

**¿Cuál será la salida del siguiente código?**

```python
class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print("Error: saldo negativo no permitido")
        else:
            self.__saldo = valor
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
cuenta.saldo = -200
print(cuenta.saldo)
```

A) `1500`
B) `-200`
C) `Error: saldo negativo no permitido` seguido de `1500`
D) `Error: saldo negativo no permitido` seguido de `-200`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:**
Primero, `cuenta.depositar(500)` suma 500 al saldo inicial de 1000, resultando en 1500. Luego, `cuenta.saldo = -200` intenta asignar un valor negativo, lo que activa el setter que imprime "Error: saldo negativo no permitido" y **no** modifica el saldo (el setter solo asigna si el valor es >= 0). Finalmente, `print(cuenta.saldo)` muestra el saldo original de 1500. Las otras opciones son incorrectas porque el setter no permite valores negativos.

</details>

---

## Pregunta 8

**¿Qué sucede cuando se intenta instanciar una clase que hereda de `ABC` pero no implementa todos sus métodos abstractos?**

A) El objeto se crea pero los métodos abstractos devuelven `None`
B) El objeto se crea pero los métodos abstractos lanzan una excepción en tiempo de ejecución
C) Se lanza un `TypeError` en tiempo de instanciación
D) Se lanza un `SyntaxError` en tiempo de compilación

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:**
Cuando una clase hereda de `ABC` y tiene métodos abstractos no implementados, Python no permite instanciarla y lanza un `TypeError` con un mensaje indicando qué métodos abstractos faltan. Esto ocurre en tiempo de ejecución (no de compilación). La opción A y B son incorrectas porque no se crea el objeto. La D es incorrecta porque la sintaxis es correcta, es la semántica la que produce el error al intentar instanciar.

</details>

---

## Pregunta 9

**¿Cuál será la salida del siguiente código?**

```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio
        self._descuento = 0
    
    @property
    def precio(self):
        return self.__precio * (1 - self._descuento / 100)
    
    @precio.setter
    def precio(self, valor):
        self.__precio = valor
    
    @property
    def descuento(self):
        return self._descuento
    
    @descuento.setter
    def descuento(self, valor):
        if 0 <= valor <= 50:
            self._descuento = valor

p = Producto("Laptop", 1000)
p.descuento = 20
print(p.precio)
p.precio = 1200
print(p.precio)
```

A) `800` seguido de `960`
B) `1000` seguido de `1200`
C) `800` seguido de `1200`
D) `980` seguido de `1180`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:**
El getter de `precio` devuelve `__precio * (1 - _descuento / 100)`. Inicialmente, `__precio = 1000` y `_descuento = 0`. Con `p.descuento = 20`, el descuento se establece a 20%, por lo que `precio = 1000 * (1 - 0.2) = 800`. Luego, `p.precio = 1200` usa el setter para cambiar `__precio` a 1200, pero el descuento sigue siendo 20%, por lo que `precio = 1200 * (1 - 0.2) = 960`. Las otras opciones no consideran el descuento o el cambio de precio base.

</details>

---

## Pregunta 10

**¿Cuál es el propósito principal del name mangling en Python al usar `__atributo`?**

A) Hacer que el atributo sea completamente inaccesible desde cualquier parte del código
B) Renombrar el atributo para evitar colisiones en contextos de herencia
C) Mejorar el rendimiento del acceso a atributos
D) Convertir el atributo en un método mágico

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:**
El name mangling (alteración de nombre) en Python tiene como propósito principal **evitar colisiones de nombres** en escenarios de herencia. Al renombrar `__atributo` a `_Clase__atributo`, se asegura que una subclase pueda tener su propio `__atributo` sin sobrescribir el de la clase padre. La opción A es incorrecta porque el atributo sigue siendo accesible (aunque con el nombre alterado). La C es incorrecta porque no hay mejora de rendimiento. La D es incorrecta porque los métodos mágicos usan `__atributo__` (doble guión en ambos extremos).

</details>

---

## Pregunta 11

**¿Cuál de las siguientes opciones implementa correctamente una propiedad de solo lectura (sin setter)?**

A)
```python
class Circulo:
    def __init__(self, radio):
        self._radio = radio
    
    @property
    def area(self):
        return 3.14159 * self._radio ** 2
    
    @area.setter
    def area(self, valor):
        raise AttributeError("El área es de solo lectura")
```

B)
```python
class Circulo:
    def __init__(self, radio):
        self._radio = radio
    
    @property
    def area(self):
        return 3.14159 * self._radio ** 2
```

C)
```python
class Circulo:
    def __init__(self, radio):
        self._radio = radio
    
    def area(self):
        return 3.14159 * self._radio ** 2
```

D) B y C son correctas

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** Las propiedades se definen con el decorador `@property`. Si solo se define el getter (sin el decorador `@setter`), la propiedad es de solo lectura. El setter no es obligatorio, y su ausencia impide la asignación. La opción A es válida pero innecesariamente verbosa. La C no es una propiedad, sino un método que debe llamarse con paréntesis.

</details>

---

## Pregunta 12

**Dado el siguiente código, ¿cuál será la salida al ejecutar `print(p._Figura__lados)`?**

```python
class Figura:
    def __init__(self, lados):
        self.__lados = lados
        self._tipo = "figura"

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__(4)
        self.__lados = lado
        self._tipo = "cuadrado"

p = Cuadrado(5)
```

A) `4`
B) `5`
C) `Error: AttributeError`
D) `figura`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:**
El name mangling funciona de forma que el atributo `__lados` en la clase `Figura` se convierte en `_Figura__lados`, mientras que el `__lados` en la clase `Cuadrado` se convierte en `_Cuadrado__lados`. Al usar `p._Figura__lados`, se accede al atributo de la clase `Figura` (el que tiene valor 4), no al de `Cuadrado`. El atributo `_tipo` (con un guión) no sufre name mangling y es sobrescrito por `Cuadrado` a "cuadrado". La opción B sería correcta si se accediera a `_Cuadrado__lados`. La C es incorrecta porque el atributo existe. La D es incorrecta porque se pide el valor de lados, no de tipo.

</details>

---

## Pregunta 13

**¿Qué ventaja proporciona el uso de `@property` sobre los getters y setters tradicionales al estilo Java?**

A) Las propiedades no pueden ser sobrescritas en subclases
B) Las propiedades permiten cambiar la implementación interna sin modificar la interfaz pública
C) Las propiedades son más rápidas que los métodos getter/setter
D) Las propiedades solo funcionan con atributos privados

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:**
La principal ventaja de `@property` es que permite comenzar con atributos públicos simples y luego migrar a métodos con lógica (validación, cálculos, etc.) sin cambiar la interfaz pública. Los usuarios siguen usando `objeto.atributo` en lugar de `objeto.get_atributo()`, manteniendo la compatibilidad con código existente. La opción A es falsa porque las propiedades pueden ser sobrescritas. La C no es necesariamente cierta. La D es falsa porque pueden usarse con cualquier atributo, no solo privados.

</details>

---

## Pregunta 14

**¿Cuál será la salida del siguiente código?**

```python
from abc import ABC, abstractmethod

class Mascota(ABC):
    @abstractmethod
    def sonido(self):
        pass
    
    @abstractmethod
    def dormir(self):
        pass
    
    def comer(self):
        return "Comiendo"

class Perro(Mascota):
    def sonido(self):
        return "Guau"
    
    def dormir(self):
        return super().comer() + " y durmiendo"

class Gato(Mascota):
    def dormir(self):
        return "Durmiendo"
    
    def sonido(self):
        return "Miau"

p = Perro()
g = Gato()
print(p.dormir())
print(g.sonido())
```

A) `Comiendo y durmiendo` seguido de `Miau`
B) `Comiendo` seguido de `Miau`
C) `Error: cannot instantiate abstract class` (en Gato)
D) `Error: cannot instantiate abstract class` (en Perro)

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:**
Ambas clases implementan todos los métodos abstractos de `Mascota` (sonido y dormir), por lo que pueden ser instanciadas. En `Perro.dormir()`, se usa `super().comer()` para llamar al método concreto de la clase padre, que retorna "Comiendo", y se concatenan " y durmiendo", resultando en "Comiendo y durmiendo". `Gato.sonido()` retorna "Miau". La opción B se acerca pero no incluye " y durmiendo". Las opciones C y D son incorrectas porque ambas clases están bien implementadas.

</details>

---

## Pregunta 15

**¿Cuál es la forma correcta de definir un método abstracto en Python?**

A)
```python
@abstractmethod
def calcular():
    pass
```

B)
```python
def calcular(self) -> int:
    raise NotImplementedError
```

C)
```python
from abc import abstractmethod

@abstractmethod
def calcular(self):
    return 0
```

D)
```python
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def calcular(self):
        pass
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:**
Para definir un método abstracto en Python, se necesita: (1) heredar de `ABC`, (2) importar `abstractmethod` del módulo `abc`, y (3) usar el decorador `@abstractmethod` en el método que debe ser implementado por subclases. La opción A falta el contexto de la clase y la herencia de `ABC`. La B define un método concreto que lanza una excepción, no es abstracto. La C importa `abstractmethod` pero falta la herencia de `ABC` y además el método tiene implementación (aunque sea permitido, la estructura mostrada no es completa). La D es la sintaxis correcta y completa.

</details>

---

## Pregunta 16

**Dado el siguiente código, ¿qué se imprimirá al ejecutar el programa completo?**

```python
from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self._salario_base = salario_base
    
    @abstractmethod
    def calcular_salario(self):
        pass
    
    @property
    def salario_base(self):
        return self._salario_base
    
    @salario_base.setter
    def salario_base(self, valor):
        if valor > 0:
            self._salario_base = valor

class EmpleadoPorHora(Empleado):
    def __init__(self, nombre, salario_base, horas):
        super().__init__(nombre, salario_base)
        self.horas = horas
    
    def calcular_salario(self):
        return self.salario_base * self.horas

class EmpleadoFijo(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono
    
    def calcular_salario(self):
        return self.salario_base + self.bono

e1 = EmpleadoPorHora("Ana", 10, 40)
e2 = EmpleadoFijo("Luis", 1000, 200)
print(e1.calcular_salario())
print(e2.calcular_salario())
```

A) `400` seguido de `1200`
B) `400` seguido de `1000`
C) `100` seguido de `1200`
D) `400` seguido de `200`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:**
`EmpleadoPorHora` implementa `calcular_salario()` como `salario_base * horas` (10 * 40 = 400). `EmpleadoFijo` implementa `calcular_salario()` como `salario_base + bono` (1000 + 200 = 1200). Ambos heredan la propiedad `salario_base` que permite acceder al atributo privado `_salario_base`. Las otras opciones son incorrectas porque no reflejan los cálculos correctos: la B ignora el bono, la C usa un cálculo incorrecto para el primer empleado, y la D confunde los resultados.

</details>

---

## Pregunta 17

**¿Qué sucede con un atributo definido como `__atributo` dentro de una clase, cuando esta clase es heredada?**

A) La subclase no puede acceder al atributo bajo ningún nombre
B) La subclase puede acceder al atributo como `_SubClase__atributo`
C) La subclase puede acceder al atributo como `_ClaseBase__atributo`
D) El atributo se convierte automáticamente en público para la subclase

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:**
Cuando un atributo tiene name mangling (`__atributo`), Python lo renombra a `_ClaseBase__atributo`, donde `ClaseBase` es el nombre de la clase donde fue definido. Las subclases pueden acceder a este atributo usando este nombre alterado, pero no directamente. La opción A es incorrecta porque sí se puede acceder con el nombre mangled. La B es incorrecta porque el prefijo es de la clase base, no de la subclase. La D es incorrecta porque el atributo no cambia su nivel de acceso automáticamente.

</details>

---

## Pregunta 18

**¿Cuál será la salida del siguiente código?**

```python
class Banco:
    def __init__(self):
        self.__tasa_interes = 0.05
        self._tasa_extra = 0.01
    
    @property
    def tasa_interes(self):
        return self.__tasa_interes
    
    @tasa_interes.setter
    def tasa_interes(self, valor):
        if 0 <= valor <= 1:
            self.__tasa_interes = valor
    
    def calcular_interes(self, monto):
        return monto * (self.__tasa_interes + self._tasa_extra)

class BancoPremium(Banco):
    def __init__(self):
        super().__init__()
        self.__tasa_interes = 0.15
    
    @property
    def tasa_interes(self):
        return self.__tasa_interes

b = BancoPremium()
print(b.tasa_interes)
```

A) `0.15`
B) `0.05`
C) `0.06`
D) `Error: AttributeError`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:**
En `BancoPremium`, se define un nuevo atributo `__tasa_interes` que sufre name mangling a `_BancoPremium__tasa_interes`. El getter `tasa_interes` en `BancoPremium` está sobrescrito y devuelve este nuevo atributo, no el de la clase base `_Banco__tasa_interes`. Por lo tanto, `b.tasa_interes` devuelve 0.15. La opción B sería el valor de la clase base. La C es la suma de 0.05 + 0.01. La D es incorrecta porque ambos atributos existen (aunque con diferentes nombres mangled).

</details>

---

## Pregunta 19

**¿Cuál de las siguientes implementaciones de una propiedad con setter es correcta?**

A)
```python
@property
def temperatura(self):
    return self.__temperatura

@temperatura.setter
def temperatura(self, valor):
    self.__temperatura = valor
```

B)
```python
def get_temperatura(self):
    return self.__temperatura

def set_temperatura(self, valor):
    self.__temperatura = valor

temperatura = property(get_temperatura, set_temperatura)
```

C)
```python
@property
def temperatura(self):
    return self.__temperatura

def temperatura(self, valor):
    self.__temperatura = valor
```

D)
```python
@property
def temperatura(self):
    return self.__temperatura

@temperatura.getter
def temperatura(self):
    return self.__temperatura
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A (y B es funcionalmente equivalente)**

**Nota:** Tanto A como B son correctas. A usa la sintaxis decoradora moderna y B usa la función `property()` tradicional. La opción C es incorrecta porque la sintaxis para el setter debe usar el decorador `@nombre.setter`. La opción D es incorrecta porque `@temperatura.getter` no existe; el getter se define con `@property`.

**Justificación:** La opción A es la forma más común y pythonica de definir una propiedad con getter y setter. La opción B también es válida y era la forma tradicional antes de los decoradores. Ambas son funcionalmente equivalentes. La C tiene un error de sintaxis porque el setter necesita el decorador específico. La D no tiene sentido porque el getter ya está definido.

</details>

---

## Pregunta 20

**¿Cuál es la relación entre abstracción y encapsulamiento en el contexto de la POO?**

A) La abstracción se enfoca en ocultar la implementación, mientras que el encapsulamiento se enfoca en expo</s>ner la interfaz pública
B) La abstracción simplifica la complejidad exponiendo solo lo esencial, mientras que el encapsulamiento protege los datos internos
C) Ambos conceptos son sinónimos y se refieren a ocultar información
D) La abstracción solo aplica a clases abstractas, mientras que el encapsulamiento solo aplica a atributos privados

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:**
La abstracción se centra en **qué** hace un objeto (interfaz pública, comportamiento esencial), ocultando los detalles internos y mostrando solo lo relevante para el usuario. El encapsulamiento se centra en **cómo** se implementa (datos internos), protegiendo el estado del objeto y controlando el acceso. Son conceptos complementarios: la abstracción define la interfaz pública, y el encapsulamiento protege la implementación interna. La opción A invierte los conceptos. La C es incorrecta porque no son sinónimos. La D limita incorrectamente ambos conceptos.

</details>

---