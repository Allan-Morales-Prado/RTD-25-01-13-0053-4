# Sobreescritura de Métodos en Python

---

## Índice

1. [¿Qué es la Sobreescritura?](#qué-es-la-sobreescritura)
2. [Sobreescritura de Métodos](#sobreescritura-de-métodos)
3. [Sobreescritura de Constructor y Propiedades](#sobreescritura-de-constructor-y-propiedades)
4. [Sobreescritura con Llamado a Método de Clase Padre](#sobreescritura-con-llamado-a-método-de-clase-padre)
5. [Herencia Múltiple y Sobreescritura](#herencia-múltiple-y-sobreescritura)
6. [Sobreescritura de Constructor en Herencia Múltiple](#sobreescritura-de-constructor-en-herencia-múltiple)
7. [El Parámetro Especial **kwargs](#el-parámetro-especial-kwargs)
8. [La Función isinstance()](#la-función-isinstance)
9. [Ejercicio Guiado: Polimorfismo y Sobreescritura](#ejercicio-guiado-polimorfismo-y-sobreescritura)
10. [Preguntas Clave](#preguntas-clave)

---

## ¿Qué es la Sobreescritura?

### Definición

La **sobreescritura de métodos** es una forma de aplicar **polimorfismo** que permite dar un comportamiento específico en una clase hija, diferenciándolo del comportamiento de su clase padre.

### Características Principales

| Característica | Descripción |
|----------------|-------------|
| **Requisito** | Requiere una relación de herencia entre dos clases |
| **Mecanismo** | Consiste en volver a definir el método de la clase padre en la clase hija |
| **Identidad** | Se mantiene el mismo nombre del método original |
| **Propósito** | Proporcionar comportamiento específico para la clase hija |

### Ejemplo Conceptual

```python
class Animal:
    def hacer_sonido(self):
        return "Sonido genérico"

class Perro(Animal):
    def hacer_sonido(self):  # Sobreescritura
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):  # Sobreescritura
        return "¡Miau!"

# Uso
animales = [Animal(), Perro(), Gato()]
for animal in animales:
    print(animal.hacer_sonido())
# Salida:
# Sonido genérico
# ¡Guau!
# ¡Miau!
```

---

## Sobreescritura de Métodos

### Aplicación

Para aplicar la sobreescritura, se debe definir dentro de la clase hija el método que se desea sobreescribir de la clase padre, **manteniendo el nombre del método**.

### Comportamiento

- Una vez generada una instancia de la clase hija, al llamar al método sobreescrito se ejecutará el código definido en el **método de la clase hija**
- Los métodos de la clase padre **no sobreescritos** siguen disponibles para las instancias de la clase hija

### Ejemplo

```python
class Vehiculo:
    def arrancar(self):
        return "Motor encendido"
    
    def detener(self):
        return "Motor apagado"

class Coche(Vehiculo):
    def arrancar(self):  # Sobreescrito
        return "Motor encendido con llave"
    
    # detener() no se sobreescribe

coche = Coche()
print(coche.arrancar())  # "Motor encendido con llave" (sobrescrito)
print(coche.detener())   # "Motor apagado" (heredado sin cambios)
```

---

## Sobreescritura de Constructor y Propiedades

### Concepto

La sobreescritura de métodos también se puede aplicar al **constructor** o a las **propiedades**, permitiendo aplicar validaciones específicas para una clase hija.

### Ejemplo

```python
class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        self.__color = color
    
    @property
    def color(self) -> str:
        return self.__color
    
    @color.setter
    def color(self, color) -> None:
        self.__color = color

class PelotaDeTenis(PelotaDeDeporte):
    def __init__(self) -> None:
        self.__color = "Amarillo"
    
    @property
    def color(self) -> str:
        return self.__color
    
    @color.setter
    def color(self, color: str) -> None:
        pass  # No se permite cambiar el color

# Uso
pdt = PelotaDeTenis()
pdt.color = "Rojo"  # Intentar cambiar el color
print(pdt.color)    # "Amarillo" (no se modificó)
```

---

## Sobreescritura con Llamado a Método de Clase Padre

### Concepto

Al sobrescribir un método, también es posible ejecutar el método de la clase padre dentro de la definición del método de la clase hija, combinando ambos comportamientos.

### Uso con super()

Para hacer el llamado al método de la clase padre, se puede usar `super()` sin argumentos.

### Ejemplo con Constructor

```python
class PelotaDeDeporte():
    def __init__(self, color: str):
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

class PelotaDeFutbol(PelotaDeDeporte):
    def __init__(self, color: str, cantidad_hexagonos: int):
        super().__init__(color)  # Ejecuta constructor de la clase padre
        self.__cantidad_hexagonos = cantidad_hexagonos
    
    @property
    def cantidad_hexagonos(self):
        return self.__cantidad_hexagonos

# Uso
pdf = PelotaDeFutbol("Blanco y Negro", 15)
print(pdf.color)              # "Blanco y Negro" (heredado)
print(pdf.cantidad_hexagonos) # 15 (propio)
```

---

## Herencia Múltiple y Sobreescritura

### El Problema del Diamante

Cuando un método es heredado de una clase A y sobrescrito por dos clases B y C, las cuales luego son heredadas por una clase D, no queda claro cuál método se ejecutará.

### Method Resolution Order (MRO)

Python resuelve este problema según el **orden en el cual se heredan las clases**, preservando lo definido en la primera clase heredada (declarada de izquierda a derecha) que posea el método.

### Ejemplo

```python
class A:
    def metodo(self):
        return "Método de A"

class B(A):
    def metodo(self):
        return "Método de B"

class C(A):
    def metodo(self):
        return "Método de C"

class D(B, C):  # Hereda de B primero
    pass

d = D()
print(d.metodo())  # "Método de B" (primera clase heredada)
```

---

## Sobreescritura de Constructor en Herencia Múltiple

### Forma Directa

Una forma de lograr que se ejecute el constructor de más de una clase heredada es haciendo el llamado al constructor directamente desde las clases padres.

### Ejemplo

```python
class PelotaDeDeporte():
    def __init__(self, tamaño: int):
        print("Creando pelota de deporte")
        self.tamaño = tamaño

class PelotaDePlastico():
    def __init__(self, material: str):
        print("Creando pelota de plástico")
        self.material = material

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, tamaño: int, material: str, timbre: str):
        PelotaDeDeporte.__init__(self, tamaño)
        PelotaDePlastico.__init__(self, material)
        print("Creando pelota de ping pong")
        self.timbre = timbre

# Salida:
# Creando pelota de deporte
# Creando pelota de plástico
# Creando pelota de ping pong
pdpp = PelotaDePingPong(4, "celuloide", "POWERTI")
```

---

## El Parámetro Especial **kwargs

### Definición

`**kwargs` es un parámetro especial que permite establecer un número variable de argumentos opcionales con nombre (argumentos de "clave").

### Características

| Característica | Descripción |
|----------------|-------------|
| **Tipo** | Diccionario donde las claves son los nombres de los parámetros y los valores son los argumentos |
| **Diferencia** | A diferencia de `*args` (argumentos posicionales), `**kwargs` son argumentos con nombre |
| **Uso** | Permite pasar argumentos opcionales de manera flexible |

### Ejemplo con super()

```python
class PelotaDeDeporte():
    def __init__(self, tamaño: int, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de deporte")
        self.tamaño = tamaño

class PelotaDePlastico():
    def __init__(self, material: str, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de plástico")
        self.material = material

class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, timbre: str, **kwargs):
        super().__init__(**kwargs)
        print("Creando pelota de ping pong")
        self.timbre = timbre

# El orden de salida cambia debido a la cadena de super()
# Salida:
# Creando pelota de plástico
# Creando pelota de deporte
# Creando pelota de ping pong
pdpp = PelotaDePingPong(tamaño=4, material="celuloide", timbre="POWERTI")
```

---

## La Función isinstance()

### Definición

`isinstance()` es una función que permite verificar si un objeto es de un tipo específico.

### Sintaxis

```python
isinstance(objeto, tipo)
```

### Comportamiento

| Parámetro | Descripción |
|-----------|-------------|
| **Primer argumento** | Un objeto cualquiera |
| **Segundo argumento** | Un tipo (clase) |
| **Retorno** | `True` si el objeto es del tipo especificado, `False` en caso contrario |

### Ejemplo Básico

```python
class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        self.__color = color
    
    @property
    def color(self) -> str:
        return self.__color
    
    @color.setter
    def color(self, color) -> None:
        self.__color = color

class PelotaDeFutbol(PelotaDeDeporte):
    def __init__(self, color: str, cantidad_hexagonos: int) -> None:
        super().__init__(color)
        self.__cantidad_hexagonos = cantidad_hexagonos
    
    def hacer_pase(self, destino: str, fuerza: int) -> tuple:
        return (destino, fuerza * 0.5)

class PelotaDeTenis(PelotaDeDeporte):
    def __init__(self) -> None:
        self.__color = "Amarillo"
    
    def hacer_saque(self, altura: int, fuerza: int) -> tuple:
        return (altura, altura * fuerza)

# Uso
pdf = PelotaDeFutbol("Blanco y Negro", 15)
pdt = PelotaDeTenis()
pelotas = [pdf, pdf, pdt, pdt, pdf]

for p in pelotas:
    if isinstance(p, PelotaDeTenis) == False:
        p.color = "Roja"
    
    if isinstance(p, PelotaDeFutbol):
        p.hacer_pase("jugador 2", 3)
    elif isinstance(p, PelotaDeTenis):
        p.hacer_saque(2, 3)
```

### Uso en Definición de Clase Padre

```python
class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        if isinstance(self, PelotaDeTenis):
            self.__color = "Amarillo"
        else:
            self.__color = color
    
    @property
    def color(self) -> str:
        return self.__color

class PelotaDeTenis(PelotaDeDeporte):
    pass

# Uso
p = PelotaDeTenis("Rojo")
print(p.color)  # "Amarillo" (forzado por isinstance)
```

---

## Ejercicio Guiado: Polimorfismo y Sobreescritura

### Contexto del Problema

Desde la empresa **"Juegos por comida"**, te han solicitado modificar el demo de la batalla entre un jugador y un monstruo.

### Nuevos Requisitos

1. **Diálogo del monstruo**: Antes del enfrentamiento, el monstruo debe mostrar "GRAAAWR"
2. **Mensaje de victoria**: Mostrar mensaje específico según quién gane
3. **Encapsulamiento**: Aplicar atributos privados
4. **Restricción**: No se debe permitir crear monstruos con armas
5. **Uso de **kwargs** y super()**: Para manejar herencia múltiple

### Implementación Paso a Paso

#### Paso 1: Clase NPC

Crear `npc.py`:

```python
# npc.py

class NPC():
    def __init__(self, nombre: str, **kwargs):
        self.__nombre = nombre
        super().__init__(**kwargs)
    
    def mostrar_dialogo(self, texto: str) -> None:
        print(f'{self.__nombre}: "{texto}"')
```

#### Paso 2: Clase Personaje Refactorizada

Crear `personaje.py`:

```python
# personaje.py
from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, hp: int, atk: int, df: int, **kwargs):
        self.__hp = hp
        self.__atk = atk
        self.__df = df
        super().__init__(**kwargs)
    
    @property
    def hp(self) -> int:
        return self.__hp
    
    @hp.setter
    def hp(self, hp: int) -> None:
        self.__hp = hp
    
    @property
    def atk(self) -> int:
        return self.__atk
    
    @property
    def df(self) -> int:
        return self.__df
    
    @abstractmethod
    def ataque(self) -> int:
        pass
    
    @abstractmethod
    def defensa(self, ataque: int) -> None:
        pass
```

#### Paso 3: Clase Jugador Refactorizada

Crear `jugador.py`:

```python
# jugador.py
import random
from personaje import Personaje

class Jugador(Personaje):
    def __init__(self, hp: int, atk: int, df: int, arma: str, **kwargs):
        super().__init__(hp=hp, atk=atk, df=df, **kwargs)
        self.__arma = arma
    
    def ataque(self) -> int:
        if self.__arma:
            return self.atk + random.randint(1, 5)
        return self.atk
    
    def defensa(self, ataque: int) -> None:
        reduccion = random.randint(1, self.df)
        dano = ataque - reduccion
        if dano > 0:
            self.hp = self.hp - dano
```

#### Paso 4: Clase Monstruo Refactorizada

Crear `monstruo.py`:

```python
# monstruo.py
from personaje import Personaje
from npc import NPC

class Monstruo(Personaje, NPC):
    def __init__(self, hp: int, atk: int, df: int, nombre: str, **kwargs):
        super().__init__(hp=hp, atk=atk, df=df, nombre=nombre, **kwargs)
        # Los monstruos no pueden tener armas
    
    def ataque(self) -> int:
        return self.atk + int(self.hp * 0.01)
    
    def defensa(self, ataque: int) -> None:
        reduccion = self.df + int(self.hp * 0.001)
        dano = ataque - reduccion
        if dano > 0:
            self.hp = self.hp - dano
```

#### Paso 5: Demo del Combate

Crear `demo.py`:

```python
# demo.py
from jugador import Jugador
from monstruo import Monstruo

# Crear personajes
jugador = Jugador(hp=500, atk=10, df=5, arma="espada")
monstruo = Monstruo(hp=1000, atk=1, df=8, nombre="Bégimo")

# Mostrar diálogo del monstruo
monstruo.mostrar_dialogo("GRAAAWR")

enfrentados = [jugador, monstruo]
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
            # Mostrar mensaje según quién murió
            from personaje import Personaje
            if isinstance(e, Jugador):
                print("¡Oh no!, haz perdido la batalla :(")
            else:
                print("¡Felicidades!, ¡Haz ganado la batalla!")
            break

print(f"HP restante - Jugador: {jugador.hp}, Monstruo: {monstruo.hp}")
```

---

## Preguntas Clave

### 1. ¿En qué consiste la sobrescritura de métodos?

**Respuesta:** La sobrescritura de métodos es un mecanismo que permite a una clase hija proporcionar una implementación específica de un método que ya está definido en su clase padre, manteniendo el mismo nombre y firma. Esto permite que las clases hijas tengan comportamientos personalizados mientras mantienen la misma interfaz.

### 2. ¿Cómo se aplica la sobrescritura de un método en la clase heredada?

**Respuesta:** Se aplica definiendo en la clase hija un método con el mismo nombre que el método que se desea sobrescribir de la clase padre:

```python
class Padre:
    def metodo(self):
        return "Comportamiento padre"

class Hija(Padre):
    def metodo(self):  # Sobreescritura
        return "Comportamiento hija"
```

### 3. Desde una instancia de una clase hija, ¿cómo se puede ejecutar el método sobrescrito en ella en lugar del definido en su clase padre?

**Respuesta:** Simplemente llamando al método desde la instancia de la clase hija. El método que se ejecutará automáticamente será el de la clase hija (la implementación más específica):

```python
hija = Hija()
hija.metodo()  # Ejecuta el método de Hija
```

### 4. ¿Qué hace la función isinstance()?

**Respuesta:** `isinstance()` es una función que verifica si un objeto es de un tipo específico (clase). Retorna `True` si el objeto es del tipo especificado o de alguna subclase de este, y `False` en caso contrario. Es útil para:
- Validar tipos de objetos antes de realizar operaciones
- Implementar comportamientos condicionales basados en el tipo de objeto
- Mantener el polimorfismo mientras se necesitan verificaciones específicas

```python
isinstance(objeto, Clase)  # Retorna True o False
```

---

## Ejercicios Propuestos

### Ejercicio 1: Sistema de Figuras con Sobreescritura

Crea un sistema de figuras donde:
- Una clase abstracta `Figura` tenga un método `area()` abstracto
- Las clases `Circulo`, `Rectangulo` y `Triangulo` sobreescriban `area()`
- Cada clase tenga un constructor que reciba los parámetros necesarios
- Usa `super()` para inicializar atributos comunes

### Ejercicio 2: Sistema de Empleados con Propiedades

Implementa:
- Una clase `Empleado` con atributos privados y propiedades
- Clases `Gerente` y `Desarrollador` que hereden de `Empleado`
- Sobrescribe el constructor en cada clase hija
- Aplica validaciones específicas en los setters

### Ejercicio 3: Herencia Múltiple con **kwargs**

Desarrolla:
- Clases `Volador`, `Nadador` y `Caminador`
- Una clase `Pato` que herede de las tres
- Usa `**kwargs` y `super()` para manejar la inicialización
- Implementa el método `moverse()` con comportamiento polimórfico

---

## Resumen

### Conceptos Clave

| Concepto | Descripción | Ejemplo |
|----------|-------------|---------|
| **Sobreescritura** | Redefinir métodos de la clase padre en la clase hija | `def metodo(self):` |
| **super()** | Llamar a métodos de la clase padre | `super().__init__()` |
| **isinstance()** | Verificar el tipo de un objeto | `isinstance(obj, Clase)` |
| **kwargs** | Argumentos con nombre variables | `def __init__(self, **kwargs)` |
| **MRO** | Orden de resolución de métodos en herencia múltiple | Orden de herencia |

### Beneficios de la Sobreescritura

1. **Personalización**: Cada clase hija puede tener comportamiento específico
2. **Extensibilidad**: Se pueden añadir nuevas funcionalidades sin modificar código existente
3. **Consistencia**: Se mantiene la misma interfaz para todas las clases
4. **Flexibilidad**: Se puede combinar comportamiento padre e hijo con `super()`