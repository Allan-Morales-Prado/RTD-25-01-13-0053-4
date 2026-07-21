# Herencia y Polimorfismo en Python

---

## Índice

1. [¿Qué es la Herencia?](#qué-es-la-herencia)
2. [Herencia Simple](#herencia-simple)
3. [Herencia Múltiple](#herencia-múltiple)
4. [Ejercicio Guiado: Herencia Simple y Múltiple](#ejercicio-guiado-herencia-simple-y-múltiple)
5. [¿Qué es el Polimorfismo?](#qué-es-el-polimorfismo)
6. [Heredar una Clase y Aplicar Polimorfismo](#heredar-una-clase-y-aplicar-polimorfismo)
7. [Uso de super()](#uso-de-super)
8. [Ejercicio Guiado: Polimorfismo en Subclases](#ejercicio-guiado-polimorfismo-en-subclases)
9. [Preguntas Clave](#preguntas-clave)

---

## ¿Qué es la Herencia?

### Definición

La herencia es un **mecanismo** que permite derivar una clase para crear una **jerarquía de clases** que comparten los mismos atributos y métodos.

### Características Principales

| Característica | Descripción |
|----------------|-------------|
| **Clase Padre** | Define un conjunto de atributos y métodos que describen un comportamiento común del conjunto de clases hijas |
| **Clase Hija** | Hereda tanto los atributos como el comportamiento de la clase padre |
| **Extensibilidad** | Las clases hijas pueden añadir otros atributos y comportamientos adicionales |
| **Modificabilidad** | Los comportamientos heredados pueden ser reescritos (sobrescritos) para modificar la lógica según se requiera |

### Ejemplo Conceptual

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Uso
perro = Perro("Firulais")
gato = Gato("Misi")

print(perro.hacer_sonido())  # ¡Guau!
print(gato.hacer_sonido())   # ¡Miau!
```

---

## Herencia Simple

### Definición

La **herencia simple** consiste en que una clase hija hereda solamente desde una **clase padre**, por lo que solamente hay dos clases involucradas en la relación.

### Características

- Se define una clase cualquiera, la cual será la clase padre
- La herencia se crea en el momento en que otra clase la use como argumento en su definición
- Las instancias de la clase hija poseen tanto los atributos como los métodos de la clase padre

### Ejemplo

```python
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def arrancar(self):
        return "Motor encendido"

class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
    
    def abrir_maletero(self):
        return "Maletero abierto"

# Uso
coche = Coche("Toyota", "Corolla", 4)
print(coche.arrancar())      # Heredado de Vehiculo
print(coche.abrir_maletero()) # Método propio de Coche
```

---

## Herencia Múltiple

### Definición

La **herencia múltiple** consiste en que una clase hija hereda **más de una clase padre**, es decir, la clase hija poseerá todos los atributos y métodos de todas las clases heredadas.

### Características

- Para heredar de más de una clase padre, se deben incluir todas las clases como argumentos en la definición
- Si un atributo o método se encuentra en más de una clase, se considerarán los definidos en la **primera clase heredada de izquierda a derecha**

### Ejemplo

```python
class PelotaDeDeporte():
    tipo = "Deporte"

class PelotaDePlastico():
    tipo = "Plástico"

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    pass

# Salida: "Deporte" (primera clase heredada)
print(PelotaDePingPong.tipo)
```

### Consideraciones Importantes

1. **Herencia Híbrida**: Cuando se utilizan varios tipos de herencia a la vez
2. **Disponibilidad**: La herencia múltiple no está disponible en todos los lenguajes POO, pero Python sí la permite
3. **Constructores**: Si se heredan varias clases con constructores, al crear una instancia se ejecutará solamente el constructor de la **primera clase heredada** que tenga un constructor

---

## Ejercicio Guiado: Herencia Simple y Múltiple

### Contexto del Problema

Desde un emprendimiento, se te ha solicitado comenzar el diseño de la estructura de clases para sus productos. Por ahora, se considera solamente el caso de los **chocolates**, donde existen, por el momento, solo los **chocolates amargos** (en el futuro habrá más tipos específicos).

**Requisitos:**
- Todos los chocolates deben tener un porcentaje de cacao específico
- Los chocolates amargos deben tener entre 75% y 85% de cacao
- También existe una variedad de **chocolate amargo sin gluten**
- En el futuro existirán otros productos sin gluten

**Nota:** Una clase abstracta puede implementar, además de al menos 1 método abstracto, métodos no abstractos.

### Implementación Paso a Paso

#### Paso 1: Clase SinGluten

Crear el archivo `sin_gluten.py`:

```python
# sin_gluten.py

class SinGluten():
    tipo_producto = "Sin Gluten"
```

#### Paso 2: Clase Abstracta Chocolate

Crear el archivo `chocolate.py`:

```python
# chocolate.py
from abc import ABC, abstractmethod
from sin_gluten import SinGluten

class Chocolate(ABC):
    def __init__(self, porc_cacao: float):
        self.porc_cacao = self.validar_porc_cacao(porc_cacao)
    
    @abstractmethod
    def validar_porc_cacao(self, porc_cacao: float) -> float:
        pass
```

#### Paso 3: Clase ChocolateAmargo

```python
class ChocolateAmargo(Chocolate):
    def validar_porc_cacao(self, porc_cacao: float) -> float:
        if porc_cacao < 0.75:
            return 0.75
        elif porc_cacao > 0.85:
            return 0.85
        else:
            return porc_cacao
```

#### Paso 4: Clase ChocolateAmargoSinGluten

```python
class ChocolateAmargoSinGluten(ChocolateAmargo, SinGluten):
    pass
```

#### Ejemplo de Uso

```python
# Ejemplo de instanciación
chocolate_amargo = ChocolateAmargo(0.80)
print(chocolate_amargo.porc_cacao)  # 0.8

chocolate_sin_gluten = ChocolateAmargoSinGluten(0.78)
print(chocolate_sin_gluten.porc_cacao)      # 0.78
print(chocolate_sin_gluten.tipo_producto)   # "Sin Gluten"
```

---

## ¿Qué es el Polimorfismo?

### Definición

En la vida real, el polimorfismo se refiere a la capacidad de **"tener varias formas"**. En programación orientada a objetos, el polimorfismo se refiere a este mismo concepto, considerando que la "forma" corresponde al **comportamiento de un objeto**.

**El polimorfismo se refiere a que el comportamiento del objeto cambia según la clase de origen del objeto desde el cual se está llevando a cabo.**

### Características

- Un mismo método puede tener diferentes implementaciones en diferentes clases
- Permite escribir código más genérico y reutilizable
- Facilita la extensión del sistema sin modificar código existente

### Ejemplo Conceptual

```python
class Figura:
    def area(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio ** 2

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto

# Polimorfismo en acción
figuras = [Circulo(5), Rectangulo(4, 6)]
for figura in figuras:
    print(f"Área: {figura.area()}")
```

---

## Heredar una Clase y Aplicar Polimorfismo

### Concepto

El polimorfismo también es posible de implementar en una **jerarquía de clases**. En ella, la clase padre actúa como **interfaz** de un conjunto de clases, donde cada **clase hija** define una forma específica de un método definido previamente en su clase padre.

### Funcionamiento

- Cuando una clase hija sobrescribe un método de la clase padre
- Al crearse una instancia de la clase hija y llamar al método
- **El método que se ejecutará será el definido en la clase hija**

### Ejemplo

```python
class PelotaDePlastico():
    def __init__(self):
        self.rebotes = []
    
    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [int(altura), 0]
            altura //= 1.1

class PelotaDeJuguete(PelotaDePlastico):
    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [altura, 0]
            altura //= 2

# Uso
pdj = PelotaDeJuguete()
pdj.rebotar(5)
print(pdj.rebotes)  # [5, 0, 1, 0]
```

---

## Uso de super()

### Definición

En Python, para hacer uso del comportamiento de la clase padre desde una clase hija, se debe hacer uso del método **built-in `super()`**.

### Sintaxis

```python
super(tipo_clase_hija, instancia_clase_hija).metodo_padre()
```

### Uso Práctico

```python
class PelotaDePlastico():
    def __init__(self):
        self.rebotes = []
    
    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [int(altura), 0]
            altura //= 1.1

class PelotaDeJuguete(PelotaDePlastico):
    def rebotar(self, altura):
        self.rebotes = []
        while altura > 0:
            self.rebotes += [altura, 0]
            altura //= 2

# Uso
pdj = PelotaDeJuguete()
pdj.rebotar(5)
print(pdj.rebotes)  # [5, 0, 1, 0]

# Se hace llamado al método del padre
super(type(pdj), pdj).rebotar(5)
print(pdj.rebotes)  # [5, 0, 2, 0, 1, 0]
```

---

## Ejercicio Guiado: Polimorfismo en Subclases

### Contexto del Problema

Desde la empresa **"Juegos por comida"**, te han solicitado programar el prototipo de una batalla entre un jugador y un monstruo.

### Requisitos del Sistema

**Características de los personajes:**
- Puntos de vida (HP)
- Puntos de ataque (ATK)
- Puntos de defensa (DF)
- Opcionalmente un arma (solo jugadores)

**Mecánicas de combate:**
1. Los ataques generan un puntaje de ataque (número entero)
2. La defensa recibe un ataque y disminuye el HP
3. El combate es por turnos hasta que alguien muera

### Implementación Paso a Paso

#### Paso 1: Clase Abstracta Personaje

Crear `personaje.py`:

```python
# personaje.py
from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, hp: int, atk: int, df: int, arma: str = None):
        self.hp = hp
        self.atk = atk
        self.df = df
        self.arma = arma
    
    @abstractmethod
    def ataque(self) -> int:
        pass
    
    @abstractmethod
    def defensa(self, ataque: int) -> None:
        pass
```

#### Paso 2: Clase Jugador

Crear `jugador.py`:

```python
# jugador.py
import random
from personaje import Personaje

class Jugador(Personaje):
    def ataque(self) -> int:
        if self.arma:
            return self.atk + random.randint(1, 5)
        return self.atk
    
    def defensa(self, ataque: int) -> None:
        reduccion = random.randint(1, self.df)
        dano = ataque - reduccion
        if dano > 0:
            self.hp -= dano
        # Si dano <= 0, no se reduce HP
```

#### Paso 3: Clase Monstruo

Crear `monstruo.py`:

```python
# monstruo.py
from personaje import Personaje

class Monstruo(Personaje):
    def ataque(self) -> int:
        return self.atk + int(self.hp * 0.01)
    
    def defensa(self, ataque: int) -> None:
        reduccion = self.df + int(self.hp * 0.001)
        dano = ataque - reduccion
        if dano > 0:
            self.hp -= dano
        # Si dano <= 0, no se reduce HP
```

#### Paso 4: Demo del Combate

Crear `demo.py`:

```python
# demo.py
from jugador import Jugador
from monstruo import Monstruo

# Crear personajes
enfrentados = [
    Jugador(500, 10, 5, "espada"),
    Monstruo(1000, 1, 8)
]

atk = 0

# Ciclo de combate
while all(e.hp > 0 for e in enfrentados):
    for e in enfrentados:
        # Defenderse si hay un ataque pendiente
        if atk:
            e.defensa(atk)
        
        # Atacar si aún tiene vida
        if e.hp > 0:
            atk = e.ataque()
            print(f"{e.__class__.__name__} ataca con {atk} de daño")
        else:
            print(f"¡Oh no!, el {e.__class__.__name__} ha muerto :(")

print(f"¡Batalla terminada!")
for e in enfrentados:
    print(f"{e.__class__.__name__}: {e.hp} HP")
```

### Ejemplo de Ejecución

```
Jugador ataca con 12 de daño
Monstruo ataca con 11 de daño
Jugador ataca con 14 de daño
Monstruo ataca con 10 de daño
...
¡Oh no!, el Monstruo ha muerto :(
¡Batalla terminada!
Jugador: 350 HP
Monstruo: 0 HP
```

---

## Preguntas Clave

### 1. ¿Qué es la herencia?

**Respuesta:** La herencia es un mecanismo que permite crear una nueva clase (clase hija) a partir de una clase existente (clase padre), heredando sus atributos y métodos, permitiendo además añadir nuevos o modificar los existentes.

### 2. ¿Cómo se debe heredar una clase en Python?

**Respuesta:** Se debe incluir la clase padre entre paréntesis en la definición de la clase hija:
```python
class ClaseHija(ClasePadre):
    pass
```

### 3. ¿Cuál es la ventaja del Polimorfismo en la programación orientada a objetos?

**Respuesta:** Permite que objetos de diferentes clases respondan al mismo mensaje (método) de manera específica según su tipo, facilitando la creación de código más flexible, extensible y mantenible.

### 4. En Python, si una clase hija ha sobrescrito un método de una clase padre, ¿cómo puede una instancia de la clase hija hacer uso del método original de su clase padre?

**Respuesta:** Utilizando la función `super()`:
```python
super(ClaseHija, instancia).metodo_padre()
```
O simplemente:
```python
super().metodo_padre()
```

### 5. Codifica un programa utilizando herencia y sobreescritura de métodos

**Ejemplo de solución:**

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        return "Sonido genérico"
    
    def moverse(self):
        return "Se mueve de manera genérica"

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"
    
    def moverse(self):
        return "Corre y salta"

class Pajaro(Animal):
    def hacer_sonido(self):
        return "¡Pío!"
    
    def moverse(self):
        return "Vuela"

# Uso
animales = [
    Perro("Firulais"),
    Pajaro("Piolín")
]

for animal in animales:
    print(f"{animal.nombre}: {animal.hacer_sonido()}, {animal.moverse()}")
```

---

## Resumen

### Conceptos Clave

| Concepto | Definición | Ejemplo |
|----------|------------|---------|
| **Herencia** | Mecanismo para derivar clases y crear jerarquías | `class Perro(Animal):` |
| **Herencia Simple** | Una clase hija hereda de una clase padre | `class Coche(Vehiculo):` |
| **Herencia Múltiple** | Una clase hija hereda de múltiples clases padre | `class A(B, C):` |
| **Polimorfismo** | Capacidad de objetos de diferentes clases de responder al mismo mensaje de manera específica | `objeto.hacer_sonido()` |
| **Sobrescritura** | Redefinir un método de la clase padre en la clase hija | `def hacer_sonido(self):` |
| **super()** | Función para acceder a métodos de la clase padre | `super().metodo()` |

### Beneficios

1. **Reutilización de código**: Los atributos y métodos se definen una vez en la clase padre
2. **Extensibilidad**: Se pueden añadir nuevas funcionalidades sin modificar código existente
3. **Mantenibilidad**: Cambios en la clase padre se propagan automáticamente
4. **Polimorfismo**: Permite escribir código más genérico y flexible

---

## Ejercicios Propuestos

### Ejercicio 1: Sistema de Figuras

Crea un sistema de figuras geométricas con una clase abstracta `Figura` y clases concretas como `Circulo`, `Rectangulo` y `Triangulo`.

### Ejercicio 2: Sistema de Empleados

Diseña un sistema de empleados con una clase base `Empleado` y clases derivadas como `Gerente`, `Desarrollador` y `Diseñador`, cada una con su propio cálculo de salario.

### Ejercicio 3: Sistema de Vehículos

Implementa un sistema de vehículos con clases como `Vehiculo`, `Coche`, `Moto` y `Camion`, incluyendo métodos específicos para cada tipo.