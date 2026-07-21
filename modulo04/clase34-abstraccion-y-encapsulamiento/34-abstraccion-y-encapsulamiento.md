# Abstracción y Encapsulamiento en POO con Python

## Los Cuatro Pilares de la POO

- **Abstracción**
- **Encapsulamiento**
- **Herencia**
- **Polimorfismo**

---

## Principios Básicos

En programación orientada a objetos, se busca:
- **Abstraer** la lógica de los métodos de una clase, dejando expuesto solamente los nombres de los métodos y sus parámetros.
- **Encapsular** el estado de los objetos, ocultando sus atributos.

>[!TIP]
>**Sobre la abstracción**
>Recuerden la *analogía del punto de vista y necesidades* de dos personas diferentes sobre un objeto o algo tratado como tal entre un veterinario y el dueño de una mascota:
> - ¿Cuánto sabe cada uno sobre ese animal?
> - ¿Qué información es relevante o **necesaria** para cada individuo?

>[!IMPORTANT]
>Recordar que en Python los atributos y métodos son **públicos** y lo que se hace en realidad con la notación de nombres de atributos y métodos (prefijos `__` y `_`) además de el uso de los decoradores `@property` y `@property.setter` es forzar el encapsulamiento.

---

## Abstracción

### Concepto

La abstracción en POO busca **disponibilizar solamente la información esencial** que permite definir un objeto.

En Python, pueden existir tanto clases abstractas como métodos abstractos:
- Una clase abstracta posee al menos 1 método abstracto
- Un método abstracto es aquel que solo posee firma (sin implementación)

### Sintaxis

```python
from abc import ABC, abstractmethod

class PelotaAbstracta(ABC):
    @abstractmethod
    def rebotar(self, altura: int):
        pass

class PelotasDeJuguete(PelotaAbstracta):
    def rebotar(self, altura: float):
        self.rebotes = []
        while altura > 0:
            self.rebotes.append(altura)
            self.rebotes.append(0)
            altura //= 2

# Uso
pelota_andy = PelotasDeJuguete()
pelota_andy.rebotar(10)
```

### Características

- Se debe importar `ABC` y `abstractmethod` del módulo `abc`
- La clase abstracta se define heredando de `ABC`
- Los métodos abstractos usan el decorador `@abstractmethod`
- Los métodos abstractos solo contienen `pass`
- **No se puede instanciar una clase abstracta** (produce error)

### Función de la Clase Base

La clase abstracta funciona como un **"molde"** que contiene aspectos comunes de un conjunto de subclases. Las subclases:
- Implementan los métodos definidos en la clase base
- Pueden definir otros métodos propios de la subclase específica

---

## Encapsulamiento

### Concepto

El encapsulamiento **delimita un conjunto de datos y los métodos** que afectan esos datos dentro de una misma unidad, restringiendo el acceso y uso de los datos y métodos "encapsulados".

Un ejemplo clásico corresponde a una **Clase**, ya que dentro de su estructura encierra todos los métodos y atributos que permiten definir un objeto.

### Particularidad de Python

A diferencia de otros lenguajes, **todos los métodos y atributos de la clase son públicos** en Python. Sin embargo, es posible indicar que un atributo o método es **privado** anteponiendo dos underscores (`__`) al nombre.

### Atributos Privados

```python
class PelotaDeJuguete(Pelota):
    def __init__(self, color):
        self.__color = color
    
    def rebotar(self, altura: float):
        pass

p = PelotaDeJuguete("amarilla")
# AttributeError: 'PelotaDeJuguete' object has no attribute '__color'
print(p.__color)
```

### Getters y Setters con Propiedades

```python
class PelotaDeJuguete(Pelota):
    def __init__(self, color: str):
        self.__color = color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, nuevo_color: str):
        self.__color = nuevo_color
    
    def rebotar(self, altura: float):
        pass

p = PelotaDeJuguete("amarilla")
print(p.color)  # Salida: amarilla
p.color = "roja"  # Cambia el color
```

### Acceso a Atributos Privados (Name Mangling)

Python permite acceder a atributos privados usando la sintaxis:

```python
p = PelotaDeJuguete("amarilla")
print(p._PelotaDeJuguete__color)  # Salida: amarilla
```

**¿Por qué?**
Al definir un atributo con la notación de interfaces de acceso (privado/protegido), Python automáticamente cambia su nombre internamente para evitar conflictos de *herencia*.

En el ejemplo, cuando se define `self.__atributo`, Python <ins>internamente</ins    > lo nombra `_Clase__atributo`. 

>[!TIP]
>Ejecuta `python -i <ruta_archivo.py>`, luego ejecuta `dir(p)` para observar el nombramiento interno del atributo.

>[!CAUTION]
>***Se puede, PERO NO SE DEBE***
>Acceder a los atributos privados fuera de esa interfaz de acceso **ROMPE EL ENCAPSULAMIENTO:**
>```python
>p._PelotaDeJuguete__color ## Ud, NO LO HAGA
>p.__color ## Debería devolver un error
>p.color ## Forma correcta (si se implementa bien)
>```

---

## Abstraer y Encapsular un Algoritmo

**Mediante la abstracción**:
- Se establece la pauta a seguir para todas las subclases que comparten comportamientos en común
- La clase base define el contrato que las subclases deben cumplir

**Mediante el encapsulamiento**:
- Se delimita dentro de una clase todo el comportamiento y estado de cada objeto
- Se protegen los datos internos de accesos no deseados

### Elementos para Establecer Reglas

- **Tipos de métodos**: constructor, getters, setters, métodos de instancia, métodos estáticos
- **Atributos**: de clase, de instancia
- **Niveles de acceso**: privado o público
- **Propiedades**: para controlar acceso a atributos

---

## Ejercicio Guiado: "Solicitudes en Créditos"

### Descripción del Problema

Una institución bancaria solicita un prototipo de programa que permita a un usuario ingresar una solicitud de crédito. El prototipo debe ser una aplicación de consola en Python que solicite:

1. **Tipo de crédito**: Consumo, Comercial o Hipotecario
2. **Monto del crédito**
3. **Correo de contacto**

### Reglas de Negocio

#### Rangos de Monto
| Tipo de Crédito | Monto Mínimo | Monto Máximo |
|-----------------|--------------|--------------|
| Consumo | $1.000.000 | $5.000.000 |
| Comercial | $1.000.000 | $5.000.000 |
| Hipotecario | $20.000.000 | $100.000.000 |

- Si se solicita un crédito fuera del rango, se fuerza al valor posible más cercano.

#### Validación de Correo

**Consumo e Hipotecario**:
- Terminaciones: `.cl` o `.com`
- Debe tener 1 símbolo `@`

**Comercial**:
- Terminaciones: `.cl`, `.com` o `.org`
- Debe tener 1 símbolo `@`
- No puede contener: `gmail`, `outlook` ni `hotmail`

- Si el correo no es válido, se fuerza a un texto vacío.

---

### Implementación Paso a Paso

#### Paso 1: Importar ABC y definir clase base

```python
# archivo solicitud_credito.py
from abc import ABC, abstractmethod

class SolicitudCredito(ABC):
    pass
```

#### Paso 2 y 3: Definir métodos abstractos

```python
class SolicitudCredito(ABC):
    @abstractmethod
    def validar_monto(self, monto: str):
        pass
    
    @abstractmethod
    def validar_correo(self, correo: str):
        pass
```

#### Paso 4: Definir subclase Consumo

```python
class SolicitudCreditoDeConsumo(SolicitudCredito):
    __terminaciones = (".cl", ".com")
```

#### Paso 5: Implementar validar_monto

```python
def validar_monto(self, monto: int):
    if monto < 1000000:
        monto = 1000000
    elif monto > 5000000:
        monto = 5000000
    return monto
```

#### Paso 6: Implementar validar_correo

```python
def validar_correo(self, correo: str):
    return (correo if correo.count("@") == 1 
            and correo.endswith(SolicitudCreditoDeConsumo.__terminaciones)
            else "")
```

#### Paso 7: Definir constructor

```python
def __init__(self, monto: int, correo: str):
    self.__monto = self.validar_monto(monto)
    self.__correo = self.validar_correo(correo)
```

#### Paso 8: Agregar propiedades con getter y setter

```python
@property
def monto(self):
    return self.__monto

@monto.setter
def monto(self, monto: int):
    self.__monto = self.validar_monto(monto)

@property
def correo(self):
    return self.__correo

@correo.setter
def correo(self, correo: str):
    self.__correo = self.validar_correo(correo)
```

#### Paso 9: Definir subclase Comercial

```python
class SolicitudCreditoComercial(SolicitudCredito):
    __prohibidos = ("gmail", "outlook", "hotmail")
    __terminaciones = (".cl", ".com", ".org")
    
    def __init__(self, monto: int, correo: str):
        self.__monto = self.validar_monto(monto)
        self.__correo = self.validar_correo(correo)
    
    @property
    def monto(self):
        return self.__monto
    
    @monto.setter
    def monto(self, monto: int):
        self.__monto = self.validar_monto(monto)
    
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, correo: str):
        self.__correo = self.validar_correo(correo)
    
    def validar_monto(self, monto: int):
        if monto < 1000000:
            monto = 1000000
        elif monto > 5000000:
            monto = 5000000
        return monto
    
    def validar_correo(self, correo: str):
        return (correo if not any(p in correo.lower() 
                for p in SolicitudCreditoComercial.__prohibidos)
                and correo.count("@") == 1
                and correo.endswith(SolicitudCreditoComercial.__terminaciones)
                else "")
```

#### Paso 10: Definir subclase Hipotecario

```python
class SolicitudCreditoHipotecario(SolicitudCredito):
    __terminaciones = (".cl", ".com")
    
    def __init__(self, monto, correo: str):
        self.__monto = self.validar_monto(monto)
        self.__correo = self.validar_correo(correo)
    
    @property
    def monto(self):
        return self.__monto
    
    @monto.setter
    def monto(self, monto: int):
        self.__monto = self.validar_monto(monto)
    
    @property
    def correo(self):
        return self.__correo
    
    @correo.setter
    def correo(self, correo: str):
        self.__correo = self.validar_correo(correo)
    
    def validar_monto(self, monto: int):
        if monto < 20000000:
            monto = 20000000
        elif monto > 100000000:
            monto = 100000000
        return monto
    
    def validar_correo(self, correo: str):
        return (correo if correo.count("@") == 1
                and correo.endswith(SolicitudCreditoHipotecario.__terminaciones)
                else "")
```

#### Paso 11: Crear programa principal

```python
# archivo programa.py
from solicitud_credito import (
    SolicitudCreditoDeConsumo,
    SolicitudCreditoComercial,
    SolicitudCreditoHipotecario
)
```

#### Paso 12: Solicitar datos al usuario

```python
print("¡Gracias por solicitar un crédito con nuestro Banco!")
tipo = int(input("\nIngrese el Tipo de Crédito a solicitar:\n"
                "1. Crédito de consumo\n"
                "2. Crédito Comercial\n"
                "3. Crédito Hipotecario\n"))
monto = int(input("\nIngrese el monto que desea solicitar:\n"))
correo = input("\nIngrese su correo de contacto:\n")
```

#### Paso 13: Crear instancia según tipo

```python
credito = None
if tipo == 1:
    credito = SolicitudCreditoDeConsumo(monto, correo)
elif tipo == 2:
    credito = SolicitudCreditoComercial(monto, correo)
elif tipo == 3:
    credito = SolicitudCreditoHipotecario(monto, correo)
```

#### Ejemplo de Ejecución

```
¡Gracias por solicitar un crédito con nuestro Banco!

Ingrese el Tipo de Crédito a solicitar:
1. Crédito de consumo
2. Crédito Comercial
3. Crédito Hipotecario
3

Ingrese el monto que desea solicitar:
50000000

Ingrese su correo de contacto:
miau@gmail.com
```

---

## Resumen

### Abstracción en Python
- Se usa `ABC` y `@abstractmethod`
- Las clases abstractas no se pueden instanciar
- Definen un contrato que las subclases deben cumplir

### Encapsulamiento en Python
- Todo es público por defecto
- Se usa `__atributo` para indicar privacidad
- Se usan propiedades (`@property`) para controlar acceso
- Python permite acceso mediante name mangling (`_Clase__atributo`)