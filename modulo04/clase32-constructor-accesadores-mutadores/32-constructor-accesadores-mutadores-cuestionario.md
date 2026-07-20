# Constructor, Accesadores y Mutadores

---

### Pregunta 1

**¿Cuál es la función principal del método constructor `__init__` en Python?**

A) Ejecutar código automáticamente al momento de crear una instancia para inicializar sus atributos
B) Eliminar los atributos de una instancia cuando ya no se necesitan
C) Modificar los valores de los atributos privados después de creada la instancia
D) Mostrar información de la instancia en formato de texto

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** El método `__init__` es el constructor en Python y se ejecuta automáticamente al instanciar una clase. Su propósito es inicializar los atributos del objeto recién creado, estableciendo su estado inicial con valores predeterminados o proporcionados por el usuario. Las otras opciones describen funcionalidades que no corresponden al constructor.
</details>

---

### Pregunta 2

**Dado el siguiente código:**

```python
class Vehiculo:
    def __init__(self, velocidad=0):
        self._velocidad = velocidad
    
    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, valor):
        if valor >= 0:
            self._velocidad = valor

v = Vehiculo(50)
v.velocidad = -10
print(v.velocidad)
```

**¿Cuál es la salida del código?**

A) -10
B) 50
C) Error de recursividad
D) 0

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** El setter de `velocidad` incluye una validación que solo permite valores positivos o cero. Al intentar asignar -10, la validación `if valor >= 0` falla y el atributo `_velocidad` no se modifica, manteniendo su valor inicial de 50. Por lo tanto, la salida es 50.
</details>

---

### Pregunta 3

**Según la convención de Python, ¿cómo se indica que un atributo debe ser tratado como "protegido"?**

A) Usando el prefijo `protected_` antes del nombre del atributo
B) Usando un solo guion bajo al inicio del nombre (`_atributo`)
C) Usando la palabra clave `protected` antes del atributo
D) Usando doble guion bajo al inicio del nombre (`__atributo`)

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** En Python, la convención para atributos protegidos es el uso de un solo guion bajo al inicio del nombre (`_atributo`). El doble guion bajo (`__atributo`) se usa para atributos privados. Las opciones A y C corresponden a otros lenguajes de programación que sí tienen palabras clave para control de acceso.
</details>

---

### Pregunta 4

**¿Qué hace el siguiente código en la clase Estudiante?**

```python
@property
def promedio(self):
    if self._notas:
        return sum(self._notas) / len(self._notas)
    return 0
```

A) Define un mutador para el atributo `promedio`
B) Define un getter que calcula el promedio dinámicamente
C) Define un atributo fijo llamado `promedio`
D) Define un método para eliminar todas las notas

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** El decorador `@property` convierte el método en un getter, permitiendo acceder al promedio como si fuera un atributo (`estudiante.promedio`). El método calcula el promedio de manera dinámica cada vez que se accede a él, dividiendo la suma de las notas entre la cantidad de notas. Si no hay notas, retorna 0. No es un mutador porque no modifica atributos, solo los lee.
</details>

---

### Pregunta 5

**¿Cuál de las siguientes afirmaciones sobre los accesadores (getters) es correcta?**

A) Los getters permiten leer valores de atributos de manera controlada
B) Los getters se ejecutan automáticamente al crear una instancia
C) Los getters pueden modificar directamente los atributos
D) Los getters solo pueden retornar valores sin lógica adicional

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La función principal de los getters es proporcionar acceso controlado a los atributos, permitiendo aplicar lógica adicional (como transformaciones, validaciones o cálculos) antes de retornar el valor. No se ejecutan al crear la instancia (eso es función del constructor), no modifican atributos (esa es función de los setters), y sí pueden incluir lógica adicional.
</details>

---

### Pregunta 6

**¿Cuál es la salida del siguiente código?**

```python
class Libro:
    def __init__(self, titulo, paginas=0):
        self._titulo = titulo
        self._paginas = max(1, paginas)
    
    @property
    def paginas(self):
        return self._paginas

l = Libro("Python 101", -5)
print(l.paginas)
```

A) -5
B) 0
C) 1
D) Error de recursividad

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** En el constructor, la función `max(1, paginas)` garantiza que el número de páginas sea al menos 1, sin importar el valor ingresado. Al pasar -5, `max(1, -5)` retorna 1, por lo que el atributo `_paginas` se inicializa en 1. Esta es una técnica común para asegurar valores mínimos en atributos.
</details>

---

### Pregunta 7

**En el ejercicio de "Ingreso de Medicamentos", ¿por qué el descuento se calcula en el setter del precio?**

A) Para que el código sea más difícil de entender
B) Para garantizar que el descuento siempre se calcule automáticamente al asignar un precio
C) Para evitar el uso de métodos en la clase
D) Para que el descuento solo se calcule una vez al final

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** Calcular el descuento en el setter del precio asegura que cada vez que se asigne un nuevo precio, se aplique automáticamente la lógica de negocio correspondiente (cálculo de IVA y descuento según el rango de precio). Esto encapsula la regla de negocio dentro de la clase y evita que el usuario deba recordar llamar a un método separado, garantizando la consistencia de los datos.
</details>

---

### Pregunta 8

**¿Cuál código implementa correctamente un getter y setter para `temperatura` validando el cero absoluto?**

A) Usando `get_temperatura` y `set_temperatura` sin decoradores
B) Usando `@property` con recursividad en el getter
C) Usando `@property` y `@temperatura.setter` con validación
D) Usando `@property` sin validación en el setter

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** La implementación correcta debe usar los decoradores `@property` para el getter y `@temperatura.setter` para el setter, con la validación correspondiente en el setter. La opción A usa un estilo antiguo sin decoradores, la B causaría recursividad al usar `self.temperatura` en lugar de `self._temperatura`, y la D no incluye la validación requerida.
</details>

---

### Pregunta 9

**¿Qué sucede si un getter utiliza el mismo nombre que el atributo interno sin el guion bajo?**

A) El atributo se vuelve automáticamente público
B) El código funciona correctamente pero con menor rendimiento
C) Se produce un error de recursividad infinita
D) Python ignora el getter y usa el atributo directamente

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** Si dentro del getter se usa `self.tamano` en lugar de `self._tamano`, se está llamando al mismo getter recursivamente, ya que `self.tamano` invoca al getter. Esto crea un bucle infinito que eventualmente produce un error de recursividad. La solución es usar el atributo interno con guion bajo (`self._tamano`) en la implementación.
</details>

---

### Pregunta 10

**El siguiente código implementa la regla de descuento de medicamentos:**

```python
if self.precio_final >= 20000:
    self.descuento = 0.20
elif self.precio_final >= 10000:
    self.descuento = 0.10
else:
    self.descuento = 0
```

**¿Qué descuento aplica para un medicamento con precio final de $15.000?**

A) 0%
B) 20%
C) 15%
D) 10%

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** El precio de \$15.000 no es mayor o igual a \$20.000, por lo que no entra en la primera condición. Sin embargo, sí es mayor o igual a \$10.000, por lo que entra en la segunda condición (`elif self.precio_final >= 10000`) y se asigna un descuento del 10% (0.10). La estructura evalúa las condiciones en orden jerárquico.
</details>

---

### Pregunta 11

**En POO en Python, ¿qué es un "mutador"?**

A) Un método que permite modificar el valor de un atributo de manera controlada
B) Un método que destruye una instancia
C) Un método que permite leer el valor de un atributo
D) Un método que convierte una clase en otra

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** Un mutador (también llamado setter) es un método diseñado específicamente para modificar el valor de un atributo de manera controlada. Su propósito es aplicar validaciones, reglas de negocio o transformaciones antes de asignar el nuevo valor. La opción C describe un accesador (getter), mientras que B y D describen conceptos que no existen en POO con este nombre.
</details>

---

### Pregunta 12

**¿Cuál código calcula correctamente el precio final con IVA (19%) y descuento?**

A) `self.precio_final = self.precio_bruto * 1.19 * (1 - self.descuento)`
B) `self.precio_final = self.precio_bruto * (1 + 0.19 - self.descuento)`
C) `self.precio_final = self.precio_bruto / 1.19 / (1 - self.descuento)`
D) `self.precio_final = self.precio_bruto * 1.19 * self.descuento`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** Para calcular correctamente el precio final, primero se debe aplicar el IVA (multiplicar por 1.19) y luego restar el descuento (multiplicar por 1 - descuento). La opción A hace exactamente esto. La B aplica el descuento de forma incorrecta al restarlo directamente del IVA. La C usa división en lugar de multiplicación. La D multiplica por el descuento en lugar de restarlo.
</details>

---

### Pregunta 13

**¿Qué problema resuelve el uso de atributos privados con getters y setters?**

A) El problema de que los atributos sean modificados de manera inválida
B) El problema de que el código sea demasiado rápido
C) El problema de que los atributos ocupen mucho espacio
D) El problema de que la clase tenga demasiados métodos

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** El principal problema que resuelven los atributos privados con getters y setters es la protección de la integridad de los datos. Al impedir el acceso directo a los atributos y canalizar toda modificación a través de setters, se pueden aplicar validaciones que eviten que los atributos tomen valores inválidos o inconsistentes. Esto es fundamental para mantener la consistencia del objeto.
</details>

---

### Pregunta 14

**¿Cuál es la salida del siguiente código?**

```python
class Pelicula:
    def __init__(self, titulo, anio=2000):
        self._titulo = titulo
        self._anio = anio
    
    @property
    def anio(self):
        return self._anio
    
    @anio.setter
    def anio(self, valor):
        if valor > 1800:
            self._anio = valor

p = Pelicula("Inception", 2010)
p.anio = 1899
print(p.anio)
```

A) 2010
B) 2000
C) 1899
D) 1800

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** El setter de `anio` valida que el año sea mayor a 1800. Como 1899 cumple con esta condición (`1899 > 1800` es verdadero), el atributo `_anio` se actualiza correctamente de 2010 a 1899. Por lo tanto, al imprimir `p.anio`, la salida es 1899. La validación permite años históricos pero excluye años anteriores a 1801.
</details>

---

### Pregunta 15

**¿Por qué es recomendable que el constructor (`__init__`) sea el primer método de una clase?**

A) Porque establece el estado inicial y facilita la comprensión
B) Porque es obligatorio por el lenguaje
C) Porque si no es el primero, Python genera error
D) Porque debe ejecutarse antes que cualquier otro método

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** Aunque Python no exige que `__init__` sea el primer método, es una buena práctica colocarlo al inicio porque es el método que se ejecuta primero al instanciar un objeto. Definirlo primero establece claramente cómo se inicializa la clase, qué atributos tiene y qué parámetros espera, facilitando la comprensión del código a otros desarrolladores. No es obligatorio ni genera error si no es el primero.
</details>