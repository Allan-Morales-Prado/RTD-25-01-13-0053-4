# Métodos (Parte II)

### Pregunta 1
**¿Cuál de las siguientes afirmaciones sobre los métodos de instancia es INCORRECTA?**

A) Los métodos de instancia pueden acceder a otros métodos de la clase mediante `self`.
B) Los métodos de instancia requieren el parámetro `self` como primer argumento.
C) Los métodos de instancia pueden ser llamados directamente desde la clase sin necesidad de crear una instancia.
D) Los métodos de instancia pueden modificar los atributos de una instancia específica.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** Los métodos de instancia requieren una instancia de la clase para ser invocados. No pueden ser llamados directamente desde la clase (a diferencia de los métodos estáticos o de clase). La opción C es incorrecta porque afirma lo contrario.

</details>

---

### Pregunta 2
**En el contexto de la programación orientada a objetos en Python, ¿qué representa el parámetro `self` en un método de instancia?**

A) Una variable global que almacena el estado de todos los objetos.
B) Una referencia a la clase en sí misma.
C) Un parámetro opcional que puede omitirse si el método no usa atributos.
D) Una referencia a la instancia específica que está llamando al método.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** `self` es una referencia a la instancia específica de la clase que está ejecutando el método. Permite acceder a los atributos y métodos de esa instancia en particular, distinguiéndola de otras instancias de la misma clase.

</details>

---

### Pregunta 3
**¿Qué diferencia fundamental existe entre un atributo de clase y un atributo de instancia?**

A) Los atributos de instancia son únicos para cada objeto, mientras que los de clase son compartidos por todas las instancias.
B) Los atributos de clase se definen dentro de métodos, mientras que los de instancia se definen a nivel de clase.
C) Los atributos de instancia son compartidos por todas las instancias, mientras que los de clase son únicos para cada objeto.
D) No existe diferencia, ambos términos son sinónimos en Python.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** Los atributos de instancia son específicos de cada objeto y se definen usualmente dentro de métodos usando `self`. Los atributos de clase se definen directamente en la clase y son compartidos por todas las instancias. La opción A describe correctamente esta diferencia.

</details>

---

### Pregunta 4
**Cuando se modifica el valor de un atributo de instancia mediante una asignación directa (ej: `objeto.atributo = valor`), ¿qué método especial de Python se ejecuta implícitamente?**

A) `__init__`
B) `__call__`
C) `__setattr__`
D) `__getattr__`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** Cuando se realiza una asignación a un atributo, Python invoca internamente el método mágico `__setattr__`. Este método está presente en todas las clases por defecto y permite modificar el estado del objeto mediante la sintaxis de punto y el operador "=".

</details>

---

### Pregunta 5
**¿Cuál es la forma correcta de definir un atributo de instancia dentro de una clase?**

A) `color: str` usando anotación de tipo a nivel de clase.
B) `self.color = "rojo"` dentro de un método de instancia.
C) `color = "rojo"` (directamente en el cuerpo de la clase).
D) `color = "rojo"` dentro de un método estático.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** Los atributos de instancia deben definirse dentro de métodos de instancia utilizando `self` (ej: `self.color = "rojo"`). La opción C define un atributo de clase, no de instancia. La opción D usa un método estático que no tiene acceso a `self`. La opción A solo es una anotación sin asignación.

</details>

---

### Pregunta 6
**¿Qué sucede si intentamos acceder a un atributo de instancia desde la clase sin haber creado un objeto?**

A) El atributo se crea automáticamente como atributo de clase.
B) Se crea automáticamente una instancia temporal.
C) El atributo se devuelve con valor `None`.
D) Se genera un error `AttributeError`.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** Los atributos de instancia solo existen cuando se ha creado una instancia y se han inicializado. Intentar acceder a ellos desde la clase (ej: `Pelota.color`) genera un `AttributeError` porque la clase no tiene ese atributo definido directamente.

</details>

---

### Pregunta 7
**Según el contenido, ¿qué representa el "estado" de un objeto en POO?**

A) Los métodos que puede ejecutar el objeto.
B) La definición de la clase a la que pertenece el objeto.
C) El conjunto de valores de todos los atributos del objeto en un momento dado.
D) La memoria que ocupa el objeto en el sistema.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** El estado de un objeto está determinado por los valores de sus atributos en un momento específico. Es la combinación de todos los valores que definen cómo está el objeto en ese instante.

</details>

---

### Pregunta 8
**¿Cuál de las siguientes afirmaciones sobre los objetos sin estado en Python es correcta según el contenido?**

A) La única forma de instanciar un objeto sin estado es creando una instancia de una clase que no posea atributos.
B) Los objetos sin estado pueden tener atributos que se asignen automáticamente al momento de la creación.
C) En Python es posible crear un objeto sin estado simplemente omitiendo la definición de atributos.
D) Un objeto sin estado puede modificarse posteriormente para adquirir atributos mediante asignación directa desde la clase.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** En Python, se debe asignar un valor a cada atributo dentro de la definición de su clase (aunque sea `None`). La única forma de tener un objeto sin estado es creando una instancia de una clase que no posea atributos en absoluto. La opción D es incorrecta porque las asignaciones se hacen desde la instancia, no desde la clase.

</details>

---

### Pregunta 9
**¿Cuál de los siguientes enunciados describe correctamente la relación entre `self` y los atributos de instancia?**

A) `self` no es necesario para definir atributos de instancia si el método es estático.
B) Los atributos de instancia pueden definirse sin usar `self` si se declaran al inicio de la clase.
C) Dentro de un método de instancia, `self` es la única forma de acceder y modificar atributos de instancia.
D) `self` permite acceder a atributos de clase, pero no a atributos de instancia.

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** Dentro de los métodos de instancia, `self` es el mecanismo principal para acceder y modificar atributos de instancia. La opción D es incorrecta porque `self` sí permite acceder a atributos de instancia. La opción B es incorrecta porque los atributos de instancia requieren `self`. La opción A es incorrecta porque los métodos estáticos no tienen acceso a `self`.

</details>

---

### Pregunta 10
**¿Cuál es la salida del siguiente código?**

```python
class Pelota:
    def asigna_color(self, nuevo_color):
        self.color = nuevo_color
    
    def lee_color(self):
        print(f"Color: {self.color}")

pelota1 = Pelota()
pelota1.asigna_color("azul")
pelota2 = Pelota()
pelota2.asigna_color("verde")

pelota1.lee_color()
pelota2.lee_color()
```

A) `Color: azul` / `Color: verde`
B) `Color: verde` / `Color: verde`
C) `Color: azul` / `Error: atributo no definido`
D) `Error: el método asigna_color necesita más argumentos`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** Cada instancia (`pelota1` y `pelota2`) tiene su propio atributo `color`. `pelota1` almacena "azul" y `pelota2` almacena "verde". Al llamar a `lee_color()` en cada una, se imprime el valor de su propio atributo, demostrando que los atributos de instancia son independientes entre objetos.

</details>

---

### Pregunta 11
**Dado el siguiente código, ¿qué ocurre al ejecutarlo?**

```python
class Medicamento:
    descuento = 0.05
    
    def __init__(self):
        self.precio = 0

med1 = Medicamento()
med2 = Medicamento()

med1.precio = 100
med2.precio = 200
Medicamento.descuento = 0.10

print(med1.descuento)
print(med2.descuento)
```

A) `0.05` / `0.05`
B) `0.10` / `0.05`
C) `0.05` / `0.10`
D) `0.10` / `0.10`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** `descuento` es un atributo de clase, no de instancia. Cuando se modifica usando `Medicamento.descuento = 0.10`, el cambio afecta a todas las instancias. Ambas instancias acceden al mismo valor del atributo de clase, por lo que ambas imprimen `0.10`.

</details>

---

### Pregunta 12
**¿Qué imprimirá este código?**

```python
class OrdenCompra:
    def nueva_orden(self):
        self.identificador = 0
        self.monto = 0
        self.codigo_descuento = ""
    
    def asigna_monto(self, nuevo_monto):
        self.monto = nuevo_monto
        self.codigo_descuento = ""
        if self.monto > 20000:
            self.codigo_descuento = "20PORCIENTO"
        elif self.monto > 10000:
            self.codigo_descuento = "10PORCIENTO"

oc = OrdenCompra()
oc.nueva_orden()
oc.asigna_monto(15000)
print(oc.codigo_descuento)
```

A) `"20PORCIENTO"`
B) `"10PORCIENTO"`
C) `""` (cadena vacía)
D) `AttributeError: 'OrdenCompra' object has no attribute 'codigo_descuento'`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** El método `asigna_monto(15000)` evalúa el monto. Como 15000 es mayor que 10000 pero no mayor que 20000, se ejecuta la condición `elif`, asignando `"10PORCIENTO"` al atributo `codigo_descuento`. Por lo tanto, se imprime `"10PORCIENTO"`.

</details>

---

### Pregunta 13
**¿Cuál es el resultado de ejecutar este código?**

```python
class Pelota:
    def inicia_color(self):
        self.color = ""
    
    def cambia_color(self, nuevo_color):
        self.color = nuevo_color

p = Pelota()
p.inicia_color()
print(p.color)
p.cambia_color("rojo")
print(p.color)
```

A) `""` / `"rojo"`
B) `Error: AttributeError` / `"rojo"`
C) `None` / `"rojo"`
D) `""` / `Error: AttributeError`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** `inicia_color()` asigna `""` al atributo `color`, por lo que el primer `print` muestra una cadena vacía. Luego `cambia_color("rojo")` modifica el atributo a `"rojo"`, y el segundo `print` muestra ese valor. Ambas operaciones son válidas y no generan errores.

</details>

---

### Pregunta 14
**¿Qué imprime el siguiente código?**

```python
class Pelota:
    def asigna_color(self, nuevo_color):
        self.color = nuevo_color
    
    def lee_color_local(self, color_local):
        print(f"Color local: {color_local}")
        print(f"Color atributo: {self.color}")

p = Pelota()
p.asigna_color("azul")
color = "verde"
p.lee_color_local(color)
```

A) `Color local: azul` / `Color atributo: azul`
B) `Color local: azul` / `Color atributo: verde`
C) `Color local: verde` / `Color atributo: azul`
D) `Color local: verde` / `Color atributo: verde`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** El parámetro `color_local` recibe el valor `"verde"` de la variable local `color`. El atributo de instancia `self.color` tiene el valor `"azul"` de la asignación anterior. Por lo tanto, se imprime "verde" para el local y "azul" para el atributo, demostrando la diferencia entre variables locales y atributos de instancia.

</details>

---

### Pregunta 15
**¿Qué sucede al ejecutar este código?**

```python
class Pelota:
    forma = "redonda"
    
    def __init__(self):
        self.color = "blanco"

p = Pelota()
print(p.forma)
print(Pelota.forma)
print(Pelota.color)
```

A) `"redonda"` / `"redonda"` / `"blanco"`
B) `"blanco"` / `"redonda"` / `"blanco"`
C) `"redonda"` / `"redonda"` / `AttributeError`
D) `AttributeError` en todos los casos

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** `forma` es un atributo de clase definido directamente en la clase, accesible desde la instancia (`p.forma`) y desde la clase (`Pelota.forma`). `color` es un atributo de instancia definido en `__init__`, solo existe en objetos instanciados. Intentar acceder a `Pelota.color` genera un `AttributeError`.

</details>

---

### Pregunta 16
**Dado el siguiente código, ¿qué se imprimirá al ejecutarlo?**

```python
class Medicamento:
    IVA = 0.18
    
    def __init__(self, precio):
        self.precio = precio
    
    def calcular_precio_final(self):
        return self.precio * (1 + self.IVA)

med = Medicamento(1000)
print(med.calcular_precio_final())
print(Medicamento.IVA)
```

A) `1000.0` / `0.18`
B) `1180.0` / `0.18`
C) `1000.0` / `Error: AttributeError`
D) `1180.0` / `Error: AttributeError`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** El método de instancia `calcular_precio_final` accede al atributo de instancia `self.precio` (1000) y al atributo de clase `self.IVA` (0.18), calculando correctamente 1000 * 1.18 = 1180.0. Luego se imprime el atributo de clase `IVA` directamente desde la clase, mostrando 0.18.

</details>

---

### Pregunta 17
**¿Cuál de los siguientes códigos implementa CORRECTAMENTE un método de instancia que valida un precio antes de asignarlo?**

**Código A:**
```python
class Medicamento:
    @staticmethod
    def validar_mayor_a_cero(numero):
        return numero > 0
    
    def asigna_precio(self, precio):
        if self.validar_mayor_a_cero(precio):
            self.precio = precio
```

**Código B:**
```python
class Medicamento:
    @staticmethod
    def validar_mayor_a_cero(numero):
        return numero > 0
    
    def asigna_precio(self, precio):
        if Medicamento.validar_mayor_a_cero(precio):
            self.precio = precio
```

**Código C:**
```python
class Medicamento:
    def validar_mayor_a_cero(self, numero):
        return numero > 0
    
    def asigna_precio(self, precio):
        if self.validar_mayor_a_cero(precio):
            self.precio = precio
```

**Código D:**
```python
class Medicamento:
    def validar_mayor_a_cero(numero):
        return numero > 0
    
    def asigna_precio(self, precio):
        if validar_mayor_a_cero(precio):
            self.precio = precio
```

A) Solo el Código A
B) Códigos A y C
C) Códigos B y D
D) Códigos A, B y C

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** Los códigos A, B y C son correctos. El A llama al método estático usando `self` (válido), el B lo llama desde la clase `Medicamento` (válido), y el C usa un método de instancia con `self` (válido). El D es incorrecto porque no tiene `self` como parámetro en el método `validar_mayor_a_cero` y tampoco usa la sintaxis correcta para llamarlo desde la clase o instancia.

</details>

---

### Pregunta 18
**¿Cuáles de los siguientes códigos generarán un error al intentar acceder al atributo `color`?**

**Código 1:**
```python
class Pelota:
    pass

p = Pelota()
print(p.color)
```

**Código 2:**
```python
class Pelota:
    def __init__(self):
        self.color = "rojo"

p = Pelota()
print(p.color)
```

**Código 3:**
```python
class Pelota:
    def asigna_color(self):
        self.color = "azul"

p = Pelota()
print(p.color)
```

**Código 4:**
```python
class Pelota:
    color = "verde"

p = Pelota()
print(p.color)
```

A) Códigos 1 y 4
B) Códigos 2 y 3
C) Códigos 1 y 3
D) Códigos 1, 2 y 3

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** 
- **Código 1:** Error porque la clase no tiene el atributo definido ni en clase ni en instancia.
- **Código 2:** Correcto porque `__init__` asigna el atributo de instancia al crear el objeto.
- **Código 3:** Error porque `asigna_color()` nunca se ejecutó, por lo que el atributo `color` no existe en la instancia.
- **Código 4:** Correcto porque `color` es un atributo de clase definido directamente.

</details>

---

### Pregunta 19
**¿Qué código(s) imprimirán la salida correcta del descuento para un medicamento de \$25.000 según la regla de descuento (10% entre \$10.000-\$19.999, 20% entre \$20.000-\$29.999, 30% \$30.000 o más)?**

**Código X:**
```python
class Medicamento:
    def asigna_precio(self, precio):
        self.precio = precio
        self.descuento = 0.0
        if self.precio >= 20000 and self.precio < 30000:
            self.descuento = 0.2

med = Medicamento()
med.asigna_precio(25000)
print(med.descuento)
```

**Código Y:**
```python
class Medicamento:
    def asigna_precio(self, precio):
        self.precio = precio
        if self.precio >= 20000 and self.precio < 30000:
            self.descuento = 0.2

med = Medicamento()
med.asigna_precio(25000)
print(med.descuento)
```

**Código Z:**
```python
class Medicamento:
    def asigna_precio(self, precio):
        self.precio = precio
        self.descuento = 0.0
        if self.precio >= 20000 and self.precio < 30000:
            self.descuento = "20%"

med = Medicamento()
med.asigna_precio(25000)
print(med.descuento)
```

A) X y Y
B) X y Z
C) Solo X
D) Y y Z

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C**

**Justificación:** El Código X es el único que funciona correctamente. Inicializa `descuento` en 0.0 antes de la condición (buena práctica) y asigna el valor numérico correcto (0.2). El Código Y falla porque no inicializa `descuento` antes de la condición, y si no se cumple la condición, el atributo no existe. El Código Z asigna un string `"20%"` en lugar del número decimal `0.2` que se solicita en los requisitos. Solo el Código X cumple completamente con los requisitos.

</details>

---

### Pregunta 20
**¿Cuáles de estos códigos implementan correctamente el concepto de "estado de un objeto" (cada objeto mantiene sus propios valores)?**

**Código P:**
```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

p1 = Perro("Fido")
p2 = Perro("Rex")
print(p1.nombre, p2.nombre)  # Fido Rex
```

**Código Q:**
```python
class Perro:
    nombre = ""
    
    def __init__(self, nombre):
        Perro.nombre = nombre

p1 = Perro("Fido")
p2 = Perro("Rex")
print(p1.nombre, p2.nombre)  # Rex Rex
```

**Código R:**
```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def cambiar_nombre(self, nuevo):
        self.nombre = nuevo

p1 = Perro("Fido")
p2 = Perro("Rex")
p1.cambiar_nombre("Luna")
print(p1.nombre, p2.nombre)  # Luna Rex
```

A) P y Q
B) P y R
C) Solo P
D) P, Q y R

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B**

**Justificación:** Los códigos P y R implementan correctamente el concepto de estado individual porque usan `self` para asignar atributos de instancia, permitiendo que cada objeto mantenga sus propios valores. El código Q es incorrecto porque usa `Perro.nombre` (atributo de clase) en lugar de `self.nombre`, haciendo que todos los objetos compartan el mismo valor (el último asignado).

</details>

---

### Pregunta 21
**¿Qué código(s) NO generarán un error al ejecutarse?**

**Código Alpha:**
```python
class Pelota:
    forma = "redonda"

p = Pelota()
print(Pelota.forma)
print(p.forma)
```

**Código Beta:**
```python
class Pelota:
    def __init__(self):
        self.color = "rojo"

p = Pelota()
print(Pelota.color)
print(p.color)
```

**Código Gamma:**
```python
class Pelota:
    def asigna_color(self, color):
        self.color = color

p = Pelota()
p.asigna_color("azul")
print(p.color)
```

A) Alpha y Gamma
B) Solo Alpha
C) Alpha y Beta
D) Alpha, Beta y Gamma

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A**

**Justificación:** 
- **Alpha:** Correcto. `forma` es atributo de clase accesible tanto desde la clase como desde la instancia.
- **Beta:** Genera error. `color` es atributo de instancia accesible solo desde objetos, `Pelota.color` intenta acceder desde la clase y falla.
- **Gamma:** Correcto. Se asigna `color` mediante el método de instancia y luego se accede correctamente desde la instancia.

</details>

---

### Pregunta 22
**¿Cuáles de los siguientes códigos implementan CORRECTAMENTE el método `asigna_precio` que valida y asigna un descuento adecuadamente?**

**Código I:**
```python
class Medicamento:
    @staticmethod
    def validar_mayor_a_cero(numero):
        return numero > 0
    
    def asigna_precio(self, precio):
        if not self.validar_mayor_a_cero(precio):
            print("Precio no válido")
            return
        self.precio = precio
        self.descuento = 0.0
        if self.precio >= 30000:
            self.descuento = 0.3
        elif self.precio >= 20000:
            self.descuento = 0.2
        elif self.precio >= 10000:
            self.descuento = 0.1
```

**Código II:**
```python
class Medicamento:
    @staticmethod
    def validar_mayor_a_cero(numero):
        return numero > 0
    
    def asigna_precio(self, precio):
        if self.validar_mayor_a_cero(precio):
            self.precio = precio
            self.descuento = 0.0
            if self.precio >= 30000:
                self.descuento = 0.3
            elif self.precio >= 20000:
                self.descuento = 0.2
            elif self.precio >= 10000:
                self.descuento = 0.1
        else:
            print("Precio no válido")
```

**Código III:**
```python
class Medicamento:
    def validar_mayor_a_cero(self, numero):
        return numero > 0
    
    def asigna_precio(self, precio):
        if self.validar_mayor_a_cero(precio):
            self.precio = precio
        self.descuento = 0.0
        if self.precio >= 30000:
            self.descuento = 0.3
        elif self.precio >= 20000:
            self.descuento = 0.2
        elif self.precio >= 10000:
            self.descuento = 0.1
```

A) I y III
B) Solo I
C) II y III
D) I y II

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D**

**Justificación:** Los códigos I y II son correctos. Ambos validan correctamente el precio antes de asignarlo y aplican los descuentos apropiados. El código III es incorrecto porque asigna el descuento incluso si el precio no es válido (el bloque de descuento está fuera del `if` de validación), lo que podría ejecutar el código de descuento con `self.precio` sin valor o con valor previo.

</details>