# Métodos (Parte II)

## Contenidos
- [¿Cuáles son los tipos de métodos?](#cuáles-son-los-tipos-de-métodos)
- [¿Cómo definir un método no estático en Python?](#cómo-definir-un-método-no-estático-en-python)
  - [Ejercicio: Crear método que asigna un precio válido](#ejercicio-crear-método-que-asigna-un-precio-válido)
- [Atributos de instancia o no estáticos](#atributos-de-instancia-o-no-estáticos)
- [Definir un atributo que pertenezca a cada instancia](#definir-un-atributo-que-pertenezca-a-cada-instancia)
  - [Ejercicio: Crear método que asigna descuento a un medicamento](#ejercicio-crear-método-que-asigna-descuento-a-un-medicamento)
- [Modificar el estado de un objeto mediante `__setattr__`](#modificar-el-estado-de-un-objeto-mediante-__setattr__)
  - [Ejercicio guiado: "Tienda de artículos para mascotas"](#ejercicio-guiado-tienda-de-artículos-para-mascotas)
  - [Refactorización de clase OrdenCompra](#refactorización-de-clase-ordencompra)
  - [Refactorización de script `generar_orden.py`](#refactorización-de-script-generar_ordenpy)

## ¿Cuáles son los tipos de métodos?

### Métodos no estáticos o método de instancia

#### Características:
- Puede ser llamado sólo desde una instancia de una clase.
- También se les llama **métodos de instancia**.
- Son capaces de modificar el valor de los atributos de una instancia de la clase.
- Son capaces de acceder a los valores de estos atributos en cada instancia específica.
- Sus retornos pueden variar entre distintas instancias de la clase, ya que cada instancia puede tener distintos estados (valores en sus atributos).

#### Definición en el código:
- Se debe definir el método al igual que se define cualquier función, pero dentro de una clase.
- Puede o no tener retorno, sin embargo, en cuanto a los parámetros se requiere que como mínimo tenga el parámetro `self`.
- `self` hace referencia a una instancia específica de la clase y permite acceder a otros métodos de la clase o a los atributos.

---

## ¿Cómo definir un método no estático en Python? 

**Ejemplo**

```python
class Pelota():
    # Método de instancia que asigna color
    def asigna_color(self, nuevo_color: str):
        self.color = nuevo_color
    
    # Método de instancia que lee color de la instancia
    def lee_color(self):
        print("El color de esta pelota es {}".format(self.color))
    
    def lee_color_local_y_atributo(self, color_local: str):
        # Esta variable "color" sólo existe en el alcance del método
        color = color_local
        # Un método de instancia puede llamar a otros métodos
        self.lee_color()
        print("El color {} NO es el color de ESTA pelota".format(color))
```

### Uso de métodos de instancia

```python
# Se crea instancia
pelota_multicolor = Pelota()

# Se asigna color a la instancia
pelota_multicolor.asigna_color("rojo")

# Se lee color. La salida será "El color de esta pelota es rojo"
pelota_multicolor.lee_color()

pelota_multicolor.asigna_color("verde")

# Las salidas serán:
# El color de esta pelota es verde
# El color amarillo NO es el color de ESTA pelota
pelota_multicolor.lee_color_local_y_atributo("amarillo")
```

> **Nota:** Cuando se llama a un método de instancia, solo se debe pasar como argumento los parámetros definidos en el método que sean distintos a `self`, es decir, el argumento correspondiente a `self` se asigna implícitamente.

---

## Ejercicio: Crear método que asigna un precio válido

**Contexto:** Desde la cadena farmacéutica donde se está desarrollando el software que permite manejar el stock de medicamentos, se te solicita que el programa permita asignar un precio ingresado por el usuario a cada instancia creada. Sin embargo, no es posible usar una asignación simple de valor al atributo, ya que antes de asignar un precio a cualquier medicamento se debe validar que este sea un precio válido (mayor a 0).

### Requisitos:
1. Agregar un método de instancia al código existente que dentro de su lógica llame al método que valida un precio positivo.
2. Si el retorno del llamado es `True`, se asigna el valor ingresado por parámetro al valor de precio de la instancia de la clase.
3. Si el retorno es `False`, no se asigna el valor y se muestra un mensaje en pantalla.

### Solución paso a paso:

#### Paso 1: Definir clase Medicamento
```python
class Medicamento():
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
```

#### Paso 2: Definir método de instancia
```python
def asigna_precio(self, precio_entregado: int):
```

#### Paso 3: Validar el precio
```python
def asigna_precio(self, precio_entregado: int):
    es_valido = self.validar_mayor_a_cero(precio_entregado)
```

#### Paso 4: Asignar el precio si es válido
```python
def asigna_precio(self, precio_entregado: int):
    es_valido = self.validar_mayor_a_cero(precio_entregado)
    if es_valido:
        self.precio = precio_entregado
```

#### Paso 5: Manejar caso de precio no válido
```python
def asigna_precio(self, precio_entregado: int):
    es_valido = self.validar_mayor_a_cero(precio_entregado)
    if es_valido:
        self.precio = precio_entregado
    else:
        print("El precio '{}' no es un precio válido".format(precio_entregado))
```

#### Paso 6: Crear script de ejecución
```python
# archivo ejecucion.py
from medicamento import Medicamento
```

#### Paso 7: Crear instancia
```python
medicamento_nuevo = Medicamento()
```

#### Paso 8: Solicitar precio al usuario
```python
precio = int(input("Ingrese precio del medicamento\n"))
```

#### Paso 9: Hacer la asignación
```python
medicamento_nuevo.asigna_precio(precio)
```

---

## Atributos de instancia o no estáticos

### Características:
- Son aquellos que requieren necesariamente de una instancia de la clase u objeto, para poder acceder a ellos o asignarles un valor.
- Los atributos de instancia (o no estáticos) son **únicos para cada instancia**.

### Estado de un objeto:
- Se determina por los valores que poseen sus atributos en un momento específico.
- Al crear un objeto, éste se encuentra en su estado inicial.
- Si se modifican los valores de los atributos del objeto instanciado, entonces se está modificando su estado.

### Conceptos clave:
- **Atributo:** Característica específica de un objeto que contiene un valor.
- **Estado:** Conjunto de valores que tienen los atributos de un objeto en un momento dado.

### Objetos sin estado en Python:
- En Python se le debe asignar un valor a un atributo dentro de la definición de su clase (aunque sea `None`).
- La única forma de instanciar un objeto sin estado sería creando una instancia de una clase que no posea atributos.

---

## Definir un atributo que pertenezca a cada instancia

### Uso de `self` para atributos de instancia

```python
class Pelota():
    def asigna_color(self, nuevo_color: str):
        self.color = nuevo_color
```

### Acceso a atributos de instancia desde la clase

```python
class Pelota():
    forma = "redondeada"
    
    def asigna_color(self, nuevo_color: str):
        self.color = nuevo_color
    
    def lee_color_y_forma(self):
        print("El color de esta pelota es {}".format(self.color))
        print("La forma de esta pelota es {}".format(self.forma))
```

### Error al acceder a atributo de instancia desde la clase

```python
from pelota import Pelota
Pelota.color
# AttributeError: type object 'Pelota' has no attribute 'color'
```

### Uso correcto

```python
from pelota import Pelota

p = Pelota()
p.asigna_color("rojo")

# Salida: El color de esta pelota es rojo
p.lee_color()
```

---

## Ejercicio: Crear método que asigna descuento a un medicamento

**Contexto:** Continuando con el desarrollo de la farmacéutica, se pide esta vez que en el método que asigna el precio válido, se asigne un descuento siguiendo las siguientes reglas:

- **10%** de descuento si el medicamento cuesta entre $10.000 y $19.999
- **20%** de descuento si el medicamento cuesta entre $20.000 y $29.999
- **30%** de descuento si el medicamento cuesta $30.000 o más

El descuento se debe definir como un número decimal (0.1 = 10%, 0.2 = 20%, 0.3 = 30%).

### Solución paso a paso:

#### Paso 1: Definir clase Medicamento existente
```python
# archivo medicamento.py
class Medicamento():
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        return numero > 0
    
    def asigna_precio(self, precio_entregado: int):
        es_valido = self.validar_mayor_a_cero(precio_entregado)
        if es_valido:
            self.precio = precio_entregado
        else:
            print("El precio '{}' no es un precio válido".format(precio_entregado))
```

#### Paso 2: Definir atributo descuento con valor por defecto
```python
if es_valido:
    self.precio = precio_entregado
    self.descuento = 0.0
```

#### Paso 3: Aplicar reglas de negocio
```python
if es_valido:
    self.precio = precio_entregado
    self.descuento = 0.0
    
    if self.precio >= 10000 and self.precio < 20000:
        self.descuento = 0.1
    elif self.precio >= 20000 and self.precio < 30000:
        self.descuento = 0.2
    elif self.precio >= 30000:
        self.descuento = 0.3
```

---

## Modificar el estado de un objeto mediante `__setattr__`

### Métodos mágicos o especiales en Python

Al modificar el valor mediante una asignación:
```python
pelota_de_andy.color = "Amarillo"
```

Se está haciendo uso de un **método mágico** o **método especial** de Python llamado `__setattr__`.

Estos métodos pertenecen a todas las clases que se creen en Python, y tienen un funcionamiento por defecto.

### Ejemplo completo:

```python
class Pelota():
    def inicia_color(self):
        self.color = ""

# Se crea objeto y se asigna valor por defecto a atributo color
pelota_de_andy = Pelota()
pelota_de_andy.inicia_color()

# Se modifica estado asignando un nuevo color
pelota_de_andy.color = "Amarillo"
```

---

## Ejercicio guiado: "Tienda de artículos para mascotas"

### Contexto
La tienda **"Nuestras mascotas"** se dedica a la venta de productos para perros, gatos y mascotas exóticas. Actualmente, se está evaluando la idea de realizar una tienda virtual, para lo cual se requiere primero realizar un prototipo en Python que permita ingresar una orden de compra.

### Características de la orden de compra:
- Identificador (código numérico)
- Total de productos
- Monto
- Código de descuento (por defecto cadena vacía)
  - "10PORCIENTO" si el monto es superior a 10.000
  - "20PORCIENTO" si el monto es mayor a 20.000

### Solución paso a paso:

#### Paso 1: Crear archivo orden_compra.py
```python
# archivo orden_compra.py
class OrdenCompra():
    
    # Se crea un método de instancia para definir atributos
    def nueva_orden(self):
        # Se define los atributos de instancia
        self.identificador = 0
        self.total_productos = 0
        self.monto = 0
        self.codigo_descuento = ""
```

#### Paso 2: Crear archivo generar_orden.py
```python
# archivo generar_orden.py
from orden_compra import OrdenCompra
```

#### Paso 3: Crear objeto y llamar al método nueva_orden
```python
oc = OrdenCompra()
oc.nueva_orden()
```

#### Paso 4: Solicitar identificador al usuario
```python
oc.identificador = int(input("Ingrese identificador de la OC:\n"))
```

#### Paso 5: Solicitar total de productos y monto
```python
oc.total_productos = int(input("Ingrese total de productos:\n"))
oc.monto = int(input("Ingrese monto:\n"))
```

#### Paso 6: Determinar código de descuento según el monto
```python
if oc.monto > 20000:
    oc.codigo_descuento = "20PORCIENTO"
elif oc.monto > 10000:
    oc.codigo_descuento = "10PORCIENTO"
```

---

## Refactorización de clase OrdenCompra

### Nuevos requisitos:
- La lógica que aplica un código de descuento se debe ejecutar cada vez que se asigne un monto.
- Esto se debe realizar mediante un método propio, en lugar del operador "=".
- Solo las instancias que tengan un monto asignado mediante este método deben contar con el atributo `codigo_descuento`.

### Solución paso a paso:

#### Paso 1: Eliminar atributo codigo_descuento y crear método asigna_monto
```python
class OrdenCompra():
    
    def nueva_orden(self):
        self.identificador = 0
        self.total_productos = 0
        self.monto = 0
    
    def asigna_monto(self, nuevo_monto: int):
```

#### Paso 2: Asignar monto y definir código de descuento como cadena vacía
```python
def asigna_monto(self, nuevo_monto: int):
    self.monto = nuevo_monto
    self.codigo_descuento = ""
```

#### Paso 3: Incluir lógica que asigna descuento
```python
def asigna_monto(self, nuevo_monto: int):
    self.monto = nuevo_monto
    self.codigo_descuento = ""
    
    if self.monto > 20000:
        self.codigo_descuento = "20PORCIENTO"
    elif self.monto > 10000:
        self.codigo_descuento = "10PORCIENTO"
```

---

## Refactorización de script generar_orden.py

### Nuevos requisitos:
- Modificar el valor del monto mediante el método `asigna_monto`.
- El identificador y el total de productos deben mantener su forma de asignación.
- Una vez asignado el monto, mostrar en pantalla el código de descuento.

### Solución paso a paso:

#### Paso 1: Eliminar asignación directa del monto y código de descuento
```python
# archivo generar_orden.py
from orden_compra import OrdenCompra

oc = OrdenCompra()
oc.nueva_orden()
oc.identificador = int(input("Ingrese identificador de la OC:\n"))
oc.total_productos = int(input("Ingrese total de productos:\n"))
```

#### Paso 2: Almacenar el valor del monto ingresado por el usuario
```python
monto = int(input("Ingrese monto:\n"))
```

#### Paso 3: Llamar al método asigna_monto
```python
oc.asigna_monto(monto)
```

#### Paso 4: Mostrar el código de descuento en pantalla
```python
print(oc.codigo_descuento)
```