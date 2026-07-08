# Métodos (Parte I)

#### Pregunta 1

**¿Qué diferencia fundamental existe entre una función y un método en Python?**

A) Las funciones siempre tienen retorno, los métodos no.
B) Los métodos se definen con `def` y las funciones con `method`.
C) Los métodos se definen dentro de una clase, mientras que las funciones se definen fuera de ella.
D) No hay diferencia, son términos intercambiables.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

Los métodos son bloques de código definidos dentro de una clase y están asociados a ella. Las funciones se definen fuera de cualquier clase y no están asociadas a un objeto específico.

</details>

---

#### Pregunta 2

**¿Cuál de las siguientes NO es una característica de un método estático en Python?**

A) Se puede llamar sin crear una instancia de la clase.
B) Puede modificar el estado de una instancia usando `self`.
C) Se define usando el decorador `@staticmethod`.
D) Puede acceder a atributos de clase usando el nombre de la clase.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Los métodos estáticos no tienen acceso al parámetro `self` ni pueden modificar el estado de una instancia específica. Esta es precisamente la característica que los diferencia de los métodos de instancia.

</details>

---

#### Pregunta 3

**¿Qué decorador se utiliza para definir un método estático en Python?**

A) `@staticmethod`
B) `@classmethod`
C) `@abstractmethod`
D) `@property`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

El decorador `@staticmethod` se utiliza para definir métodos estáticos en Python. Se coloca en la línea anterior a la definición del método.

</details>

---

#### Pregunta 5

**Dado el siguiente código:**

```python
class Calculadora:
    PI = 3.14159
    
    @staticmethod
    def sumar(a, b):
        return a + b
    
    @staticmethod
    def area_circulo(radio):
        return Calculadora.PI * radio ** 2

print(Calculadora.sumar(3, 4))
print(Calculadora.area_circulo(2))
```

**¿Cuál es la salida del código?**

A) 7 y 12.56636
B) Error - Los métodos estáticos no pueden tener parámetros
C) Error - No se puede acceder a PI desde un método estático
D) 7 y 12.0

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

El método `sumar()` retorna 7 (3+4). El método `area_circulo()` calcula π * r² = 3.14159 * 4 = 12.56636. Ambos métodos estáticos funcionan correctamente y pueden acceder a atributos de clase usando `Clase.atributo`.

</details>

---

#### Pregunta 6

**¿Qué sucede al ejecutar el siguiente código?**

```python
class Pelota:
    posiciones = [3, 0, 2, 1, 0]
    
    @staticmethod
    def crear_rebote():
        posiciones = [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
        return posiciones
    
    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote()
        print(Pelota.posiciones)

Pelota.imprimir_posiciones()
```

A) [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
B) Error - No se puede llamar a un método estático desde otro método estático
C) [3, 0, 2, 1, 0]
D) None

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

`crear_rebote()` retorna una nueva lista, pero no modifica el atributo de clase `posiciones`. La variable `posiciones` dentro del método es local y no afecta al atributo de clase. Por lo tanto, `Pelota.posiciones` sigue siendo [3, 0, 2, 1, 0].

</details>

---

#### Pregunta 7

**¿Qué imprime el siguiente código?**

```python
class Medicamento:
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_precio(precio):
        return precio > 0

med1 = Medicamento()
med2 = Medicamento()

print(med1.descuento == med2.descuento)
print(Medicamento.validar_precio(-5))
```

A) True y False
B) False y True
C) False y False
D) True y True

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

`med1.descuento == med2.descuento` es True porque ambos comparten el mismo atributo de clase (0.05). `Medicamento.validar_precio(-5)` retorna False porque -5 no es mayor que 0.

</details>

---

#### Pregunta 8

**¿Cuál es la salida del siguiente código?**

```python
class Configuracion:
    version = "1.0"
    
    @staticmethod
    def mostrar_version():
        print(Configuracion.version)
    
    @staticmethod
    def actualizar_version(nueva):
        version = nueva
        Configuracion.mostrar_version()

Configuracion.actualizar_version("2.0")
```

A) "2.0"
B) Error - No se puede modificar `version` desde un método estático
C) "1.0"
D) None

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

La línea `version = nueva` crea una variable local llamada `version`, no modifica el atributo de clase `Configuracion.version`. Por lo tanto, `mostrar_version()` imprime "1.0".

</details>

---

#### Pregunta 10

**Dado el siguiente código incompleto:**

```python
class Temperatura:
    UNIDAD = "Celsius"
    
    @staticmethod
    def celsius_a_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_a_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# ¿Qué línea de código es válida para llamar a estos métodos?
```

**¿Cuál de las siguientes líneas de código es CORRECTA?**
  i. `Temperatura.celsius_a_fahrenheit(0)`
  ii. 
  ```python
  temp = Temperatura()
  temp.celsius_a_fahrenheit(0)
  ```
  iii. `Temperatura().celsius_a_fahrenheit(0)`

A) Sólo i.
B) Sólo iii.
C) i. y ii.
D) i. ii. y iii.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: D**

Todas las opciones son válidas:
- i. Llama al método directamente desde la clase.
- ii. Crea una instancia y llama al método desde ella.
- iii. Crea una instancia temporal y llama al método.

Los métodos estáticos pueden ser llamados tanto desde la clase como desde sus instancias.

</details>

---

#### Pregunta 11

**¿Cuál es la salida del siguiente código?**

```python
class Contador:
    cuenta = 0
    
    @staticmethod
    def incrementar():
        Contador.cuenta += 1
        return Contador.cuenta

print(Contador.incrementar())
print(Contador.incrementar())
```

A) 1 y 1
B) Error - Los métodos estáticos no pueden modificar atributos de clase
C) 1 y 2
D) 0 y 0

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

Aunque se recomienda no modificar atributos de clase en métodos estáticos, Python no lo impide. `Contador.cuenta` es un atributo de clase que se incrementa correctamente en cada llamada.

</details>

---

#### Pregunta 12

**¿Cuál es la diferencia entre un método estático y una función normal que está dentro de un módulo?**

A) Los métodos estáticos siempre son más rápidos que las funciones.
B) Los métodos estáticos se definen dentro de una clase; las funciones se definen fuera de ella.
C) Los métodos estáticos pueden acceder a atributos de clase; las funciones no.
D) No hay diferencia, son exactamente lo mismo.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

La principal diferencia es el contexto: los métodos estáticos pertenecen a una clase, mientras que las funciones son independientes. Los métodos estáticos tienen acceso al espacio de nombres de la clase.

</details>

---

#### Pregunta 13

**¿Qué relación existe entre un método y un comportamiento en POO?**

A) El comportamiento define el método, no al revés.
B) Son conceptos idénticos y sinónimos.
C) Los métodos solo existen en teoría, los comportamientos en la práctica.
D) Un método es el código que define una acción, mientras que el comportamiento es la ejecución de esa acción.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: D**

El método es el bloque de código que define una acción posible. El comportamiento es la acción en sí que realiza el objeto cuando se invoca el método. Un comportamiento puede involucrar uno o más llamados a métodos.

</details>

---

#### Pregunta 14

**¿Qué representa el estado de un objeto en POO?**

A) La cantidad de memoria que ocupa.
B) Los valores actuales de sus atributos en un momento dado.
C) Los métodos que puede ejecutar.
D) El nombre de la clase a la que pertenece.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

El estado de un objeto está determinado por los valores actuales de sus atributos. Los métodos pueden modificar este estado al cambiar los valores de los atributos.

</details>

---

#### Pregunta 15

**¿Cuándo un método puede modificar el estado de un objeto?**

A) Solo cuando es un método estático.
B) Cuando es un método no estático que modifica atributos de la instancia usando `self`.
C) Siempre, todos los métodos modifican el estado.
D) Nunca, los objetos son inmutables.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Los métodos no estáticos (métodos de instancia) pueden modificar el estado del objeto al cambiar los valores de sus atributos usando `self.atributo = nuevo_valor`. Los métodos estáticos no pueden modificar el estado de una instancia.

</details>

---

#### Pregunta 16

**Dado el siguiente código:**

```python
class Validador:
    @staticmethod
    def es_email_valido(email):
        return '@' in email and '.' in email
    
    @staticmethod
    def es_telefono_valido(telefono):
        return len(telefono) >= 8 and telefono.isdigit()

# ¿Qué línea de código retornará True?
```

**¿Cuál de las siguientes llamadas retorna True?**

A) `Validador.es_telefono_valido("12a45678")`
B) `Validador.es_email_valido("usuariodominio.com")`
C) `Validador.es_telefono_valido("1234567")`
D) `Validador.es_email_valido("usuario@dominio")`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: D**

- A: Contiene letra "a" → False (isdigit() retorna False)
- B: No tiene "@" → False
- C: "1234567" tiene 7 caracteres → False
- D: "@" y "." están presentes → True

</details>

---

#### Pregunta 17

**¿Cuál es la mejor práctica para acceder a atributos de clase desde un método estático?**

A) Usar `atributo` directamente
B) Usar `self.atributo`
C) Usar `cls.atributo`
D) Usar `NombreClase.atributo`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: D**

La forma más clara y explícita de acceder a atributos de clase desde un método estático es usando el nombre de la clase: `NombreClase.atributo`. Esto hace evidente que se está accediendo a un atributo de clase y no a una variable local.

</details>

---

#### Pregunta 18

**¿Qué imprime el siguiente código?**

```python
class Convertidor:
    FACTOR = 1.8
    OFFSET = 32
    
    @staticmethod
    def celsius_a_fahrenheit(c):
        return c * Convertidor.FACTOR + Convertidor.OFFSET
    
    @staticmethod
    def fahrenheit_a_celsius(f):
        return (f - Convertidor.OFFSET) / Convertidor.FACTOR

temp = 100
print(Convertidor.celsius_a_fahrenheit(temp))
print(Convertidor.fahrenheit_a_celsius(Convertidor.celsius_a_fahrenheit(temp)))
```

A) 212.0 y 212.0
B) 180.0 y 100.0
C) 212.0 y 100.0
D) 100.0 y 100.0

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

- `celsius_a_fahrenheit(100)` = 100 * 1.8 + 32 = 212.0
- `fahrenheit_a_celsius(212)` = (212 - 32) / 1.8 = 100.0

</details>

---

#### Pregunta 19

**¿Cuál es la salida del siguiente código?**

```python
class Config:
    nivel = "produccion"
    
    @staticmethod
    def get_nivel():
        return Config.nivel
    
    @staticmethod
    def set_nivel(nuevo):
        Config.nivel = nuevo

print(Config.get_nivel())
Config.set_nivel("desarrollo")
print(Config.get_nivel())
```

A) Error - No se puede modificar un atributo de clase desde un método estático
B) `produccion` y `produccion`
C) `desarrollo` y `desarrollo`
D) `produccion` y `desarrollo`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: D**

Aunque no es la práctica más recomendada, es posible modificar atributos de clase desde métodos estáticos usando `Clase.atributo = nuevo_valor`. El código funciona correctamente.

</details>

---

#### Pregunta 20
¿Cuál de las siguientes afirmaciones sobre atributos y estado es CORRECTA?

A) Los atributos y el estado son exactamente lo mismo.

B) Los atributos son los valores actuales de un objeto, mientras que el estado es la definición de características.

C) Los atributos son características definidas en la clase, mientras que el estado son los valores actuales de esas características en un objeto específico.

D) Solo los objetos tienen atributos, pero no estado.

<details> 
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

Los atributos son las características que se definen en la clase (como un "molde"). El estado son los valores concretos que tienen esos atributos en una instancia específica en un momento dado.

</details>

---

#### Pregunta 21
Si dos objetos son instancias de la misma clase, ¿qué podemos afirmar?

A) Siempre tienen exactamente el mismo estado.
B) Siempre tienen los mismos atributos (definidos), pero pueden tener diferente estado.
C) Siempre tienen diferentes atributos y diferente estado.
D) No tienen relación entre sí.

<details> <summary>Ver respuesta</summary>

**Respuesta correcta: B**

Dos objetos de la misma clase comparten la misma definición de atributos, pero pueden tener diferentes valores (estado). Por ejemplo, dos personas pueden tener nombres diferentes, edades diferentes, etc.

</details>

---

#### Pregunta 22
¿Qué ocurre con el estado de un objeto cuando se ejecuta un método no estático?

A) Siempre permanece igual.
B) Puede cambiar si el método modifica atributos usando `self`.
C) Siempre cambia.
D) Solo cambia si el método retorna un valor.

<details> <summary>Ver respuesta</summary>

**Respuesta correcta: B**

El estado de un objeto puede cambiar cuando un método no estático modifica uno o más atributos usando `self.atributo = nuevo_valor`. No todos los métodos modifican el estado; algunos solo consultan valores.

</details>