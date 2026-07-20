# Sobrecarga y Sobrescritura de Métodos en Python

### Pregunta 1
¿Cuál es la principal diferencia entre la sobrecarga y la sobrescritura de métodos en Python?

A) La sobrecarga ocurre en tiempo de ejecución, mientras que la sobrescritura ocurre en tiempo de compilación.
B) La sobrecarga permite múltiples métodos con el mismo nombre pero diferentes parámetros, mientras que la sobrescritura redefine un método heredado en una subclase.
C) La sobrecarga solo funciona con operadores matemáticos, mientras que la sobrescritura funciona con cualquier método.
D) La sobrecarga y la sobrescritura son conceptos idénticos en Python.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La sobrecarga (implementada mediante métodos especiales como `__add__`) permite definir comportamientos específicos para operadores, mientras que la sobrescritura ocurre cuando una subclase redefine un método heredado de su clase padre. La opción A es incorrecta porque invierte los tiempos de ejecución. La opción C es falsa porque la sobrecarga no se limita solo a operadores matemáticos. La opción D es incorrecta porque son conceptos fundamentalmente diferentes.
</details>

---

### Pregunta 2
¿Qué son los "dunder methods" (métodos especiales) en Python?

A) Son métodos que deben ser definidos obligatoriamente en todas las clases.
B) Son métodos que comienzan y terminan con doble guión bajo, como `__init__` o `__add__`, y permiten sobrecargar operadores y comportamientos incorporados.
C) Son métodos que solo funcionan en Python 3 y superiores.
D) Son métodos que solo pueden ser utilizados dentro de clases abstractas.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** Los "dunder methods" (contracción de "double underscore") son métodos especiales en Python que permiten sobrecargar operadores y comportamientos incorporados. Ejemplos incluyen `__init__` para inicialización, `__add__` para suma, `__eq__` para igualdad, entre otros. La opción A es incorrecta porque no son obligatorios. La opción C es falsa porque existen desde versiones anteriores. La opción D es incorrecta porque no están limitados a clases abstractas.
</details>

---

### Pregunta 3
¿Cuándo se selecciona el método a ejecutar en una sobrescritura versus una sobrecarga?

A) La sobrecarga se selecciona en tiempo de compilación y la sobrescritura en tiempo de ejecución.
B) Ambas se seleccionan en tiempo de compilación.
C) Ambas se seleccionan en tiempo de ejecución.
D) La sobrecarga se selecciona en tiempo de ejecución y la sobrescritura en tiempo de compilación.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La sobrecarga (métodos especiales como `__add__`) se determina en tiempo de compilación basándose en los tipos de argumentos proporcionados. La sobrescritura ocurre en tiempo de ejecución cuando Python busca el método en la cadena de herencia comenzando desde la clase de la instancia. La opción B es incorrecta porque la sobrescritura no se determina en compilación. La opción C es incorrecta porque la sobrecarga no se determina en tiempo de ejecución. La opción D invierte correctamente los conceptos.
</details>

---

### Pregunta 4
¿Cuál es el propósito del método especial `__eq__` en Python?

A) Definir cómo se comporta la conversión a string de un objeto.
B) Definir cómo se comporta el operador de asignación `=` en una clase.
C) Definir cómo se comporta el operador de igualdad `==` entre dos objetos de una clase.
D) Definir cómo se comporta el operador `+` entre dos objetos de una clase.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** El método `__eq__` se utiliza para sobrecargar el operador de igualdad `==`. Permite definir qué significa que dos objetos de una clase sean considerados "iguales". La opción A corresponde al método `__str__` o `__repr__`. La opción B corresponde al método `__setattr__` o `__setitem__`. La opción D corresponde al método `__add__`.
</details>

---

### Pregunta 5
En el contexto de la sobrescritura, ¿qué ocurre cuando una subclase redefine un método de la clase padre?

A) El método de la clase padre se elimina permanentemente.
B) Python lanza un error de compilación.
C) Ambos métodos se ejecutan simultáneamente.
D) El método de la subclase reemplaza completamente al de la clase padre para las instancias de la subclase.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** Cuando una subclase sobrescribe un método de la clase padre, el método de la subclase reemplaza completamente al de la clase padre para las instancias de la subclase. El método de la clase padre aún existe y puede ser accedido mediante `super()`. La opción A es incorrecta porque el método padre no se elimina. La opción B es incorrecta porque la sobrescritura es una característica válida y común en POO. La opción C es incorrecta porque no se ejecutan simultáneamente (a menos que se llame explícitamente a `super()`).
</details>

---

### Pregunta 6
¿Qué salida produce el siguiente código?

```python
class Dato:
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):
        return f"Dato: {self.valor}"
    
    def __add__(self, otro):
        return Dato(self.valor + otro.valor)

d1 = Dato(5)
d2 = Dato(3)
resultado = d1 + d2
print(resultado)
```

A) Error de tipo
B) `8`
C) `5 + 3`
D) `Dato: 8`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** El método `__add__` devuelve una nueva instancia de `Dato` con la suma de los valores. Luego, `print(resultado)` llama automáticamente al método `__str__` de la clase `Dato`, que devuelve `"Dato: 8"`. La opción A es incorrecta porque el código está correctamente implementado y funciona. La opción B sería correcta si el método `__str__` no existiera o devolviera solo el valor. La opción C no tiene relación con el código.
</details>

---

### Pregunta 7
Dado el siguiente código, ¿qué se imprime en pantalla?

```python
class Vehiculo:
    def mover(self):
        print("El vehículo se mueve")

class Coche(Vehiculo):
    def mover(self):
        print("El coche acelera")

class Moto(Vehiculo):
    pass

vehiculo = Vehiculo()
coche = Coche()
moto = Moto()

vehiculo.mover()
coche.mover()
moto.mover()
```

A) 
```
El vehículo se mueve
El coche acelera
El vehículo se mueve
```

B) 
```
El vehículo se mueve
El coche acelera
El coche acelera
```

C) 
```
El vehículo se mueve
El vehículo se mueve
El vehículo se mueve
```

D) Error de tipo

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La clase `Vehiculo` tiene el método `mover()`. La clase `Coche` sobrescribe este método con su propia implementación. La clase `Moto` hereda de `Vehiculo` pero no sobrescribe el método, por lo que utiliza el método de la clase padre. Por lo tanto: `vehiculo.mover()` usa el método de `Vehiculo`, `coche.mover()` usa el método sobrescrito de `Coche`, y `moto.mover()` usa el método heredado de `Vehiculo`. La opción B es incorrecta porque `moto` no tiene el método sobrescrito. La opción C es incorrecta porque ignora la sobrescritura en `Coche`. La opción D es incorrecta porque el código es válido.
</details>

---

### Pregunta 8
¿Cuál es la salida del siguiente código que utiliza el método `__iadd__`?

```python
class Inventario:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
    
    def __iadd__(self, otro):
        if self.producto == otro.producto:
            self.cantidad += otro.cantidad
        return self

prod1 = Inventario("Laptop", 5)
prod2 = Inventario("Laptop", 3)
prod1 += prod2
print(prod1.cantidad)
```

A) `3`
B) `15`
C) `8`
D) `5`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** El método `__iadd__` sobrecarga el operador `+=`. Cuando se ejecuta `prod1 += prod2`, verifica que los productos sean iguales (ambos son "Laptop") y suma la cantidad de `prod2` a `prod1`. La cantidad inicial de `prod1` es 5, se le suman 3 de `prod2`, resultando en 8. La opción A es incorrecta porque muestra solo la cantidad del segundo objeto. La opción B es incorrecta porque multiplica en lugar de sumar. La opción D es incorrecta porque no considera la suma.
</details>

---

### Pregunta 9
¿Qué sucede al ejecutar el siguiente código?

```python
class Medicamento:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __eq__(self, otro):
        return self.nombre.lower() == otro.nombre.lower()

m1 = Medicamento("Paracetamol")
m2 = Medicamento("paracetamol")
m3 = Medicamento("Ibuprofeno")

print(m1 == m2)
print(m1 == m3)
```

A) 
```
False
False
```

B) 
```
False
True
```

C) 
```
True
True
```

D) 
```
True
False
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** El método `__eq__` está sobrecargado para comparar los nombres de los medicamentos sin considerar mayúsculas/minúsculas (`lower()`). `m1` y `m2` tienen nombres que son iguales después de aplicar `lower()` ("paracetamol" == "paracetamol"), por lo que el primer print muestra `True`. `m1` y `m3` tienen nombres diferentes ("paracetamol" vs "ibuprofeno"), por lo que el segundo print muestra `False`. La opción A es incorrecta porque el primero es `True`. La opción B es incorrecta porque el primero es `True` y el segundo `False`. La opción C es incorrecta porque el segundo es `False`.
</details>

---

### Pregunta 10
¿Cuál es la salida del siguiente código?

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f"Persona: {self.nombre}"
    
    def __repr__(self):
        return f"Persona('{self.nombre}')"

p = Persona("Ana")
print(str(p))
print(repr(p))
```

A) 
```
Persona: Ana
Persona('Ana')
```

B) 
```
Persona('Ana')
Persona('Ana')
```

C) 
```
Persona('Ana')
Persona: Ana
```

D) 
```
'Ana'
Persona('Ana')
```

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** `print(str(p))` llama al método `__str__`, que devuelve una representación amigable para el usuario `"Persona: Ana"`. `print(repr(p))` llama al método `__repr__`, que devuelve una representación más técnica y unívoca `"Persona('Ana')"`. La opción B es incorrecta porque `str` y `repr` son diferentes en este caso. La opción C invierte el orden de salida. La opción D no coincide con la implementación de los métodos especiales.
</details>

---

### Pregunta 11
¿Cuál de los siguientes fragmentos de código implementa correctamente la sobrecarga del operador de resta (`-`) para la clase `Numero`?

**Código A:**
```python
class Numero:
    def __init__(self, val):
        self.val = val
    def sub(self, otro):
        return Numero(self.val - otro.val)
```

**Código B:**
```python
class Numero:
    def __init__(self, val):
        self.val = val
    def __resta__(self, otro):
        return Numero(self.val - otro.val)
```

**Código C:**
```python
class Numero:
    def __init__(self, val):
        self.val = val
    def __sub__(self, otro):
        return Numero(self.val - otro.val)
```

**Código D:**
```python
class Numero:
    def __init__(self, val):
        self.val = val
    def __sub__(self, otro, extra):
        return Numero(self.val - otro.val - extra)
```

A) Código A
B) Código B
C) Código C
D) Código D

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** Solo el Código C implementa correctamente el método especial `__sub__`, que es el nombre correcto para sobrecargar el operador de resta (`-`). El Código A usa un nombre de método convencional `sub` que no sobrecarga ningún operador. El Código B usa el nombre incorrecto `__resta__`. El Código D tiene un error porque `__sub__` solo debe aceptar dos parámetros (`self` y `otro`), no tres. La opción A es incorrecta porque D tiene un error de parámetros. La opción C es incorrecta porque B no es un método especial válido. La opción D es incorrecta porque A no sobrecarga ningún operador.
</details>

---

### Pregunta 12
¿Cuáles de los siguientes fragmentos de código generan una salida de "El vehículo acelera" cuando se ejecuta `mi_vehiculo.acelerar()`?

**Código A:**
```python
class Vehiculo:
    def acelerar(self):
        print("El vehículo acelera")

class Coche(Vehiculo):
    pass

mi_vehiculo = Coche()
```

**Código B:**
```python
class Vehiculo:
    def acelerar(self):
        print("El vehículo acelera")

class Coche(Vehiculo):
    def acelerar(self):
        print("El coche acelera")

mi_vehiculo = Coche()
```

**Código C:**
```python
class Vehiculo:
    def acelerar(self):
        print("El vehículo acelera")

class Coche(Vehiculo):
    def Acelerar(self):
        print("El coche acelera")

mi_vehiculo = Coche()
```

**Código D:**
```python
class Vehiculo:
    def acelerar(self):
        print("El vehículo acelera")

class Coche(Vehiculo):
    def acelerar(self, velocidad):
        print(f"El coche acelera a {velocidad} km/h")

mi_vehiculo = Coche()
```

A) Códigos A y B
B) Código A solamente
C) Códigos A, B y C
D) Códigos C y D

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** El Código A genera "El vehículo acelera" porque no sobrescribe el método, por lo que usa el método de la clase padre. El Código B NO genera "El vehículo acelera" porque sobrescribe el método con "El coche acelera". El Código C NO genera "El vehículo acelera" porque `Acelerar()` con mayúscula es un método diferente, pero `acelerar()` no está definido en la subclase, por lo que usaría el método de la clase padre. Espera... ¡Código C SÍ generaría "El vehículo acelera"! El Código D causaría un error porque el método sobrescrito requiere parámetros adicionales. Por lo tanto, los códigos A y C generan la salida deseada. La opción A es la correcta. La opción B omite al Código C. La opción C incluye al Código B que no genera la salida. La opción D es incorrecta porque D causa error.
</details>

---

### Pregunta 13
¿Cuáles de los siguientes códigos implementan correctamente la lógica de igualdad entre medicamentos basada en el nombre (insensible a mayúsculas)?

**Código A:**
```python
class Medicamento:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre
```

**Código B:**
```python
class Medicamento:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
    
    def equals(self, otro):
        return self.nombre.lower() == otro.nombre.lower()
```

**Código C:**
```python
class Medicamento:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
    
    def __eq__(self, otro, ignorar_case=True):
        if ignorar_case:
            return self.nombre.lower() == otro.nombre.lower()
        return self.nombre == otro.nombre
```

**Código D:**
```python
class Medicamento:
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
    
    def __eq__(self, otro):
        return self.nombre.lower() == otro.nombre.lower()
```

A) Códigos A y D
B) Código A solamente
C) Código D solamente
D) Códigos B y D

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** Solo el Código D implementa correctamente la lógica requerida. El método `__eq__` es el método especial correcto para sobrecargar `==`, y usa `lower()` para hacer la comparación insensible a mayúsculas. El Código A es incorrecto porque no maneja mayúsculas/minúsculas. El Código B no usa un método especial, por lo que no sobrecarga el operador `==`. El Código C tiene un error porque `__eq__` solo debe aceptar `self` y `other`, no acepta parámetros adicionales como `ignorar_case`. La opción A es incorrecta porque A no maneja el case insensitive. La opción B es incorrecta porque A no maneja el case insensitive. La opción D es incorrecta porque B no es un método especial.
</details>

---

### Pregunta 14
¿Cuáles de los siguientes códigos implementan correctamente la sobrecarga del operador `+` para concatenar dos objetos de tipo `Texto`?

**Código A:**
```python
class Texto:
    def __init__(self, contenido):
        self.contenido = contenido
    
    def __add__(self, otro):
        return Texto(self.contenido + " " + otro.contenido)
```

**Código B:**
```python
class Texto:
    def __init__(self, contenido):
        self.contenido = contenido
    
    def __add__(self, otro):
        return self.contenido + " " + otro.contenido
```

**Código C:**
```python
class Texto:
    def __init__(self, contenido):
        self.contenido = contenido
    
    def __concat__(self, otro):
        return Texto(self.contenido + " " + otro.contenido)
```

**Código D:**
```python
class Texto:
    def __init__(self, contenido):
        self.contenido = contenido
    
    def __add__(self, otro):
        return Texto(self.contenido + otro.contenido)
```

A) Códigos A y C
B) Códigos A y D
C) Código A solamente
D) Todos los códigos

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** Los códigos A y D usan correctamente el método especial `__add__` para sobrecargar el operador `+`. Ambos retornan un objeto de tipo `Texto`, aunque con diferentes estrategias de concatenación (A agrega espacio, D no). El Código B usa `__add__` pero retorna un string en lugar de un objeto `Texto`, lo que podría causar problemas de tipo si se encadenan operaciones. El Código C usa un nombre de método incorrecto (`__concat__`). La opción A incluye al Código C que es incorrecto. La opción C omite al Código D que también es correcto. La opción D incluye códigos incorrectos.
</details>

---

### Pregunta 15
¿Cuáles de los siguientes códigos NO generan un error al ser ejecutados?

**Código A:**
```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __lt__(self, otro):
        return self.precio < otro.precio

p1 = Producto("A", 100)
p2 = Producto("B", 200)
print(p1 < p2)
```

**Código B:**
```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def menor_que(self, otro):
        return self.precio < otro.precio

p1 = Producto("A", 100)
p2 = Producto("B", 200)
print(p1 < p2)
```

**Código C:**
```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __lt__(self, otro):
        return self.precio < otro.precio

p1 = Producto("A", 100)
p2 = Producto("B", 200)
print(p1.menor_que(p2))
```

**Código D:**
```python
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __lt__(self, otro, extra):
        return self.precio < otro.precio

p1 = Producto("A", 100)
p2 = Producto("B", 200)
print(p1 < p2)
```

A) Código A
B) Códigos A y C
C) Códigos A, B y C
D) Código C

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** Solo el Código A se ejecuta sin errores porque implementa correctamente el método especial `__lt__` para sobrecargar el operador `<` y lo usa correctamente. El Código B no tiene `__lt__`, por lo que `p1 < p2` intenta usar una operación no definida y lanza error. El Código C implementa `__lt__` pero luego intenta llamar a `p1.menor_que(p2)`, método que no existe. El Código D tiene un error porque `__lt__` solo debe aceptar dos parámetros (`self` y `otro`), no tres. La opción B es incorrecta porque C tiene un error de método inexistente. La opción C es incorrecta porque B y C tienen errores. La opción D es incorrecta porque omite al Código A y C tiene error de método.
</details>