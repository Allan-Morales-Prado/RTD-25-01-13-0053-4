# Sobrecarga de métodos

## Contenidos
1. [¿Qué entendemos por sobrecarga de métodos?](#qué-entendemos-por-sobrecarga-de-métodos)
2. [Métodos Especiales en Python](#métodos-especiales-en-python)
   - [Ejemplo de Sobrecarga de Método](#ejemplo-de-sobrecarga-de-método---error-inicial)
   - [Ejercicio 1: Método `__sub__`](#-ejercicio-1-método-__sub__)
3. [Sobrescritura de Métodos](#sobrescritura-de-métodos)
4. [¿Por qué se ejecuta el método de la subclase?](#por-qué-se-ejecuta-el-método-de-la-subclase)
   - [Ejercicio 2: Nuevas Subclases](#-ejercicio-2-nuevas-subclases)
   - [Ejercicio Guiado: "Stock de Medicamentos"](#ejercicio-guiado-stock-de-medicamentos)

## ¿Qué entendemos por sobrecarga de métodos?

### Sobrecarga vs Sobrescritura

| **Sobrecarga** | **Sobrescritura** |
|----------------|-------------------|
| Permite definir varios métodos con el mismo nombre pero con diferentes conjuntos de parámetros. | Ocurre cuando una subclase redefine un método heredado de una clase padre. |
| Se basa en la **firma del método**, que incluye el nombre y los tipos de datos de los parámetros. | El método sobrescrito debe tener el **mismo nombre, tipo de retorno y lista de parámetros** que el método de la clase padre. |
| Los métodos sobrecargados se seleccionan en **tiempo de compilación** según los argumentos proporcionados. | La sobrescritura se produce en **tiempo de ejecución** cuando se llama al método desde una instancia de la subclase. |

---

## Métodos Especiales en Python

Python utiliza **métodos especiales** (también llamados "dunder methods" por sus dobles guiones bajos) para implementar la sobrecarga de operadores.

---

## Ejemplo de Sobrecarga de Método - Error Inicial

```python
class Dato:
    def __init__(self, dato1):
        self.dato1 = dato1

dato1 = Dato(10)
dato2 = Dato(30)

print(dato1 + dato2)  # ❌ Error: no podemos sumar instancias de Dato
```
>[!WARNING]
> No podemos realizar operación de suma con el operador `+` en instancias de una clase a menos que definamos el comportamiento.

---

## Ejemplo de Sobrecarga de Método - Solución

### Método especial `__add__` (suma)

Añadimos el método especial `__add__` para definir la lógica de suma de datos. Además, añadimos el método especial `__str__` para formatear la salida de información.

```python
class Dato:
    def __init__(self, dato1):
        self.dato1 = dato1
    
    def __str__(self):
        return f"{self.dato1}"
    
    def __add__(self, suma_datos):
        return Dato(self.dato1 + suma_datos.dato1)

dato1 = Dato(10)
dato2 = Dato(30)

print(dato1 + dato2)  # ✅ Resultado: 40
```

---

## 🧪 Ejercicio 1: Método `__sub__`

**Aplicando los métodos especiales (`__sub__`), utiliza el código anterior y realiza la resta de las instancias de Dato.**

```python
# Tu código aquí
class Dato:
    def __init__(self, dato1):
        self.dato1 = dato1
    
    def __str__(self):
        return f"{self.dato1}"
    
    def __add__(self, suma_datos):
        return Dato(self.dato1 + suma_datos.dato1)
    
    # ✏️ Agrega el método __sub__ aquí
```

---

## Sobrescritura de Métodos

La sobrescritura se ejecuta en métodos de Python bajo el concepto de **herencia**.

### Características:
- Una subclase redefine un método heredado de una clase padre.
- El método debe tener el **mismo nombre** que el método de la clase padre.
- Se produce en **tiempo de ejecución**.

---

## Ejemplo de Sobrescritura

```python
# Clase principal
class Monoplaza:
    color = ""
    
    def aceleracion(self):
        print("El monoplaza acelera")
    
    def frenado(self):
        print("El monoplaza frena")

# Subclase que hereda de la principal
class Redbull(Monoplaza):
    def aceleracion(self):
        print("El monoplaza Redbull acelera hasta los 450km/h")
    
    def frenado(self):
        print("El monoplaza Redbull tiene buena capacidad de frenado")

redbull = Redbull()
redbull.aceleracion()  # ✅ "El monoplaza Redbull acelera hasta los 450km/h"
redbull.frenado()      # ✅ "El monoplaza Redbull tiene buena capacidad de frenado"
```

---

## ¿Por qué se ejecuta el método de la subclase?

```python
redbull = Redbull()        # Instancia de la subclase
redbull.aceleracion()      # ✅ Se ejecuta el método de Redbull
redbull.frenado()          # ✅ Se ejecuta el método de Redbull
```

**📌 Explicación:** Python busca el método dentro de la clase que se está instanciando. Como la instancia se realiza sobre la subclase, ejecuta los métodos de la subclase.

---

## 🧪 Ejercicio 2: Nuevas Subclases

**Genera nuevas subclases en el código de la clase Monoplaza.**

Un monoplaza es un vehículo tipo de competición Fórmula 1.

```python
# Tu código aquí
class Monoplaza:
    color = ""
    
    def aceleracion(self):
        print("El monoplaza acelera")
    
    def frenado(self):
        print("El monoplaza frena")

# ✏️ Crea nuevas subclases (Ferrari, Mercedes, etc.)
```

---

## Ejercicio Guiado: "Stock de Medicamentos"

---

### Contexto del Problema

Desde la cadena farmacéutica para la cual has venido desarrollando un programa para manejar los medicamentos en venta, te solicitan esta vez crear un prototipo que permita manejar el **stock de medicamentos** a medida que son ingresados.

---

### Requisitos del Sistema

| # | Requisito |
|---|-----------|
| 1 | Para ingresar un medicamento se debe solicitar **nombre y stock**, y añadir a un listado de medicamentos ingresados. |
| 2 | Dos medicamentos se consideran **iguales** si tienen el mismo nombre (insensible a mayúsculas). |
| 3 | Solo se debe solicitar (y asignar) el **precio** (considerando IVA, descuento y precio final) en caso de que se ingrese un medicamento que **no existe**. |
| 4 | Si se ingresa un medicamento que **ya existe**, se debe **agregar al stock** del medicamento existente el del medicamento del nuevo ingreso. |
| 5 | Luego de cada ingreso, se debe informar: nombre, precio bruto, descuento (si posee), precio final, stock, y cantidad de medicamentos distintos ingresados. |
| 6 | El programa debe permitir un nuevo ingreso hasta que el usuario indique lo contrario. |

---

## Paso 1: Sobrecarga de `__eq__`

A partir de la clase `Medicamento`, **sobrecarga el método `__eq__`** de forma que dos instancias de `Medicamento` se consideren iguales si sus nombres son iguales (independiente de mayúsculas y minúsculas).

### Código Base (medicamento.py)

```python
class Medicamento():
    IVA = 0.18
    
    def __init__(self, nombre: str, stock: int = 0):
        self.nombre = nombre
        self.stock = stock
        self.precio_bruto = 0
        self.precio_final = 0.0
        self.descuento = 0.0
    
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    
    @property
    def precio(self):
        return self.precio_final
    
    @precio.setter
    def precio(self, precio_bruto: int):
        if self.validar_mayor_a_cero(precio_bruto):
            self.precio_bruto = precio_bruto
            self.precio_final = precio_bruto + precio_bruto * self.IVA
            
            if self.precio_final >= 10000 and self.precio_final < 20000:
                self.descuento = 0.1
            elif self.precio_final >= 20000:
                self.descuento = 0.2
            
            if self.descuento:
                self.precio_final *= 1 - self.descuento
    
    # ✅ Este es el método que se debe agregar
    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()
```

---

## Paso 2: Sobrecarga de `__iadd__`

Sobrecargar el método `__iadd__` (permite sobrecargar operación de asignación `+=`), de forma que, al sumar dos instancias iguales de `Medicamento`, se añada al stock de la instancia actual el stock de la segunda instancia. El método debe retornar la instancia actual.

### Solución

```python
def __iadd__(self, other):
    if self == other:
        self.stock += other.stock
    return self
```

---

## Paso 3: Archivo programa.py

Consultar mediante `input` si el usuario desea ingresar un medicamento y almacenar la opción ingresada en una variable. Iniciar una lista vacía donde se irán almacenando los medicamentos ingresados.

### Solución

```python
# archivo programa.py
from medicamento import Medicamento

opcion_ingreso = int(input("¿Desea agregar un medicamento?\n1. Sí\n2. No\n"))
ingresados = []
```

---

## Paso 4: Ciclo While

Iniciar un ciclo `while` que tenga como condición de ingreso que la opción ingresada en el paso anterior sea `1`. Dentro del ciclo, consultar nombre y stock, y crear una instancia de `Medicamento` con estos datos.

### Solución

```python
while opcion_ingreso == 1:
    nombre = input("\nIngrese nombre del medicamento:\n")
    stock = int(input("\nIngrese stock del medicamento:\n"))
    m = Medicamento(nombre, stock)
```

---

## Paso 5: Verificar Medicamento Existente

Consultar si el nuevo medicamento se encuentra ya ingresado (el operador `in` desencadena un llamado a `__eq__`). De ser así, realizar la suma de stocks y reemplazar el medicamento ingresado por el existente.

### Solución

```python
if m in ingresados:
    indice = ingresados.index(m)
    ingresados[indice] += m
```

---

## Paso 6: Medicamento Nuevo

En caso de que no se cumpla la condición anterior, solicitar el precio, asignar y agregar el medicamento a la lista de ingresados.

### Solución

```python
else:
    ingresados.append(m)
    precio_bruto = int(input("\nIngrese precio bruto del medicamento:\n"))
    m.precio = precio_bruto
```

---

## Paso 7: Mostrar Datos del Medicamento

Luego de finalizar el ingreso, mostrar en pantalla los datos del medicamento ingresado, y la cantidad de medicamentos distintos ingresados.

### Solución

```python
print(f"\n***** DATOS MEDICAMENTO {m.nombre} *****")
print(f"PRECIO BRUTO: ${m.precio_bruto}")
if m.descuento:
    print(f"DESCUENTO: {m.descuento*100}%")
print(f"PRECIO FINAL: ${m.precio_final}")
print(f"STOCK: {m.stock}")
print(f"\nLa farmacia cuenta con {len(ingresados)} medicamento(s)\n")
```

---

## Paso 8: Consultar Nuevo Ingreso

Al final del ciclo, consultar nuevamente si se desea ingresar o no un nuevo medicamento.

### Solución

```python
opcion_ingreso = int(input("¿Desea agregar un medicamento?\n1. Sí\n2. No\n"))
```

---

## Resumen del Código Completo

```python
# medicamento.py
class Medicamento():
    IVA = 0.18
    
    def __init__(self, nombre: str, stock: int = 0):
        self.nombre = nombre
        self.stock = stock
        self.precio_bruto = 0
        self.precio_final = 0.0
        self.descuento = 0.0
    
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    
    @property
    def precio(self):
        return self.precio_final
    
    @precio.setter
    def precio(self, precio_bruto: int):
        if self.validar_mayor_a_cero(precio_bruto):
            self.precio_bruto = precio_bruto
            self.precio_final = precio_bruto + precio_bruto * self.IVA
            
            if self.precio_final >= 10000 and self.precio_final < 20000:
                self.descuento = 0.1
            elif self.precio_final >= 20000:
                self.descuento = 0.2
            
            if self.descuento:
                self.precio_final *= 1 - self.descuento
    
    def __eq__(self, other):
        return self.nombre.lower() == other.nombre.lower()
    
    def __iadd__(self, other):
        if self == other:
            self.stock += other.stock
        return self
```

---

```python
# programa.py
from medicamento import Medicamento

opcion_ingreso = int(input("¿Desea agregar un medicamento?\n1. Sí\n2. No\n"))
ingresados = []

while opcion_ingreso == 1:
    nombre = input("\nIngrese nombre del medicamento:\n")
    stock = int(input("\nIngrese stock del medicamento:\n"))
    m = Medicamento(nombre, stock)
    
    if m in ingresados:
        indice = ingresados.index(m)
        ingresados[indice] += m
    else:
        ingresados.append(m)
        precio_bruto = int(input("\nIngrese precio bruto del medicamento:\n"))
        m.precio = precio_bruto
    
    print(f"\n***** DATOS MEDICAMENTO {m.nombre} *****")
    print(f"PRECIO BRUTO: ${m.precio_bruto}")
    if m.descuento:
        print(f"DESCUENTO: {m.descuento*100}%")
    print(f"PRECIO FINAL: ${m.precio_final}")
    print(f"STOCK: {m.stock}")
    print(f"\nLa farmacia cuenta con {len(ingresados)} medicamento(s)\n")
    
    opcion_ingreso = int(input("¿Desea agregar un medicamento?\n1. Sí\n2. No\n"))
```