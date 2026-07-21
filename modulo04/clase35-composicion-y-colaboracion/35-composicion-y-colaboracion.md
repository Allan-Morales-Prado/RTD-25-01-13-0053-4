# Colaboración y Composición en POO con Python

## Índice
1. [Colaboración entre objetos](#colaboración-entre-objetos)
2. [Composición de objetos](#composición-de-objetos)
3. [Agregación vs Composición](#agregación-vs-composición)
4. [Uso conjunto de colaboración y composición](#uso-conjunto-de-colaboración-y-composición)
5. [Ejercicio guiado: Módulo de venta de productos](#ejercicio-guiado-módulo-de-venta-de-productos)
6. [Resumen](#resumen)

---

## Colaboración entre objetos

### Concepto

La **colaboración** en programación orientada a objetos se refiere a la interacción entre diferentes objetos de distintas clases para lograr un objetivo común. Cada objeto contribuye con sus responsabilidades específicas, trabajando juntos para resolver un problema complejo.

### Características principales

- **Independencia**: Los objetos que colaboran no dependen el uno del otro para existir
- **Interacción**: Se comunican mediante el paso de mensajes (llamadas a métodos)
- **Coordinación**: Un objeto puede actuar como mediador entre otros objetos

### Ejemplo práctico: Sistema de Biblioteca

```python
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False

    def devolver(self):
        if self.prestado:
            self.prestado = False
            return True
        return False

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro.devolver():
            self.libros_prestados.remove(libro)
            return True
        return False

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def prestar_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(isbn)
        if usuario and libro:
            return usuario.tomar_prestado(libro)
        return False

    def devolver_libro(self, id_usuario, isbn):
        usuario = self.buscar_usuario(id_usuario)
        libro = self.buscar_libro(isbn)
        if usuario and libro:
            return usuario.devolver_libro(libro)
        return False

# Uso del sistema
biblioteca = Biblioteca()

# Crear objetos
libro1 = Libro("1984", "George Orwell", "123456789")
libro2 = Libro("Brave New World", "Aldous Huxley", "987654321")
usuario1 = Usuario("Alice", 1)
usuario2 = Usuario("Bob", 2)

# Registrar en la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Operaciones
print(biblioteca.prestar_libro(1, "123456789"))  # True
print(biblioteca.prestar_libro(2, "123456789"))  # False (ya prestado)
print(biblioteca.devolver_libro(1, "123456789")) # True
print(biblioteca.prestar_libro(2, "123456789"))  # True (ahora disponible)
```

### Características de la colaboración en el ejemplo

| Clase | Rol | Colaboración |
|-------|-----|--------------|
| **Libro** | Recurso | Proporciona métodos para prestar/devolver |
| **Usuario** | Actor | Gestiona los libros que toma prestados |
| **Biblioteca** | Mediador | Coordina la interacción entre Usuario y Libro |

---

## Composición de objetos

### Concepto

La **composición** es una relación donde una clase (clase compuesta) tiene un atributo que es una instancia de otra clase (clase componente). Es una forma de **agregación fuerte** donde:

- La clase compuesta **contiene** a la clase componente
- La clase componente **no puede existir** independientemente de la clase compuesta
- El ciclo de vida de ambos está ligado

### Características

| Aspecto | Descripción |
|---------|-------------|
| **Relación** | "Tiene un" (Has-a) |
| **Dependencia** | El componente depende del compuesto para existir |
| **Ciclo de vida** | Ligado: cuando muere el compuesto, muere el componente |
| **Implementación** | El componente se crea dentro del constructor del compuesto |

### Ejemplo de composición

```python
from abc import ABC, abstractmethod

class Material(ABC):
    @abstractmethod
    def romper(self):
        pass

class MaterialPlastico(Material):
    nombre = "Plástico"
    duracion = "Corta"
    
    def __init__(self, textura: str):
        self.textura = textura
    
    def romper(self):
        pass

class Pelota():
    def __init__(self, tamanio: int, color: str, textura: str):
        self.tamanio = tamanio
        self.color = color
        self.textura = textura
        # La pelota está compuesta por un componente material
        self.material = MaterialPlastico(self.textura)

# Uso
p = Pelota(16, "Amarillo", "Lisa")
print(p.material.nombre)  # "Plástico"
```

---

## Agregación vs Composición

| Característica | Agregación ("Agregación normal") | Composición ("Agregación fuerte") |
|----------------|----------------------------------|-----------------------------------|
| **Relación** | "Tiene un" (Has-a) | "Tiene un" (Has-a) |
| **Dependencia** | El componente puede existir independientemente | El componente depende del compuesto |
| **Ciclo de vida** | Independiente | Ligado al compuesto |
| **Creación** | El componente se crea **fuera** y se pasa al constructor | El componente se crea **dentro** del constructor |
| **Ejemplo** | Una Pelota tiene un Material preexistente | Una Venta tiene un DetalleVenta creado internamente |

### Comparación en código

**Agregación** (existencia independiente):
```python
class Material:
    def __init__(self, nombre: str, duracion: str, textura: str):
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura

class Pelota:
    def __init__(self, tamanio: int, color: str, material: Material):
        self.tamanio = tamanio
        self.color = color
        self.material = material  # Material se crea fuera y se pasa como argumento

# El material existe independientemente
m = Material("Plástico", "Corta", "Lisa")
p = Pelota(16, "Amarillo", m)
```

**Composición** (existencia ligada):
```python
class Material:
    def __init__(self, nombre: str, duracion: str, textura: str):
        self.nombre = nombre
        self.duracion = duracion
        self.textura = textura

class Pelota:
    def __init__(self, tamanio: int, color: str, textura: str):
        self.tamanio = tamanio
        self.color = color
        # El material se crea dentro del constructor de Pelota
        self.material = Material("Plástico", "Corta", textura)

# El material no existe fuera de la pelota
p = Pelota(16, "Amarillo", "Lisa")
```

---

## Uso conjunto de colaboración y composición

Las relaciones entre objetos no son mutuamente excluyentes. En un sistema complejo, se pueden usar **simultáneamente**:

### Ventajas de combinarlos

1. **Estructura modular**: Cada clase tiene responsabilidades bien definidas
2. **Escalabilidad**: Fácil de extender sin modificar código existente
3. **Mantenibilidad**: Cambios aislados en componentes específicos
4. **Reutilización**: Los componentes pueden reutilizarse en diferentes contextos

### Elementos complementarios

- **Clases abstractas (ABC)**: Sirven como plantillas para tipos similares de objetos
- **Encapsulamiento**: Cada clase protege su estado interno
- **Propiedades (@property)**: Controlan el acceso y modificación de atributos

---

## Ejercicio guiado: Módulo de venta de productos

### Contexto del problema

La tienda **"Mis Mascotas"** (venta de productos para perros, gatos y exóticos) necesita un prototipo para el backend del módulo de venta de su sitio web de e-commerce.

**Requerimientos:**
- Aplicación de consola en Python
- Ingreso de productos y cantidades mediante `input()`
- Mostrar el detalle completo de la venta al finalizar

**Estructura:**
- **Venta**: Contiene un detalle de venta (composición)
- **DetalleVenta**: Lista de ítems (agregación)
- **DetalleVentaItem**: Cada producto con su cantidad (colaboración)

### Diagrama de relaciones

```
Venta (Compuesto)
   └── DetalleVenta (Componente) - Composición
           └── DetalleVentaItem (Lista) - Agregación
           
Venta --- colabora con ---> DetalleVentaItem
```

### Implementación paso a paso

#### Paso 1-4: Clase DetalleVentaItem

```python
# archivo venta.py

class DetalleVentaItem():
    def __init__(self, producto: str, cantidad: int):
        self.__producto = producto
        self.__cantidad = cantidad
    
    @property
    def producto(self):
        return self.__producto
    
    @property
    def cantidad(self):
        return self.__cantidad
```

#### Paso 5-7: Clase DetalleVenta

```python
class DetalleVenta():
    def __init__(self):
        self.__items = []
    
    def agregar_item(self, item: DetalleVentaItem):
        self.__items.append(item)
    
    def __str__(self):
        retorno = ":::::::: DETALLE DE ESTA VENTA :::::::::\n"
        retorno += "PRODUCTO\tCANTIDAD\n"
        items = [f"{i.producto}\t\t{i.cantidad}\n" for i in self.__items]
        return f"{retorno}{''.join(items)}"
```

#### Paso 8-11: Clase Venta

```python
class Venta():
    def __init__(self):
        self.__detalle = DetalleVenta()
    
    def modificar_detalle(self, producto: str, cantidad: int):
        detalle_venta_item = DetalleVentaItem(producto, cantidad)
        self.__detalle.agregar_item(detalle_venta_item)
    
    @property
    def detalle(self):
        return self.__detalle
```

#### Paso 12-17: Programa principal

```python
# archivo programa.py
from venta import Venta

# Crear instancia de venta
venta = Venta()

# Ingresar ítems
opcion = int(input("¿Desea ingresar un ítem a la venta?\n1. Sí\n2. No\n"))

while opcion == 1:
    producto = input("\nIngrese nombre del producto vendido:\n")
    cantidad = int(input("\nIngrese cantidad vendida del producto:\n"))
    
    venta.modificar_detalle(producto, cantidad)
    
    opcion = int(input("\n¿Desea ingresar un ítem a la venta?\n1. Sí\n2. No\n"))

# Mostrar detalle
print(venta.detalle)
```

### Ejemplo de ejecución

```
¿Desea ingresar un ítem a la venta?
1. Sí
2. No
1

Ingrese nombre del producto vendido:
spikes

Ingrese cantidad vendida del producto:
1

¿Desea ingresar un ítem a la venta?
1. Sí
2. No
1

Ingrese nombre del producto vendido:
k/d

Ingrese cantidad vendida del producto:
2

¿Desea ingresar un ítem a la venta?
1. Sí
2. No
2

:::::::: DETALLE DE ESTA VENTA :::::::::
PRODUCTO        CANTIDAD
spikes          1
k/d             2
```

### Análisis de relaciones en el ejercicio

| Relación | Clases involucradas | Tipo | Justificación |
|----------|-------------------|------|---------------|
| **Composición** | Venta → DetalleVenta | Composición | El DetalleVenta se crea dentro del constructor de Venta y no existe sin ella |
| **Agregación** | DetalleVenta → DetalleVentaItem | Agregación | Los ítems se crean externamente y se agregan a la lista |
| **Colaboración** | Venta ↔ DetalleVentaItem | Colaboración | Venta usa DetalleVentaItem para agregar ítems, pero no depende de ellos |

---

## Resumen

### Colaboración
- **Definición**: Interacción entre objetos de distintas clases
- **Característica**: Los objetos son independientes
- **Implementación**: Paso de mensajes (llamadas a métodos)
- **Ejemplo**: Biblioteca, Usuario y Libro

### Composición
- **Definición**: Una clase contiene a otra como atributo
- **Característica**: El componente no existe sin el compuesto
- **Implementación**: El componente se crea dentro del constructor del compuesto
- **Ejemplo**: Venta contiene DetalleVenta

### Agregación vs Composición
- **Agregación**: El componente existe independientemente
- **Composición**: El componente depende del compuesto
- **Diferencia clave**: Ciclo de vida y creación

### Uso conjunto
- Complementar colaboración y composición resuelve problemas complejos
- Mejora la estructura, escalabilidad y mantenibilidad del código
- Se puede combinar con clases abstractas y encapsulamiento

---

## Preguntas clave del módulo

1. **¿Cómo se genera colaboración a nivel de código?**
   - Mediante la interacción entre objetos a través de métodos
   - Un objeto llama a métodos de otro objeto
   - Se pasan instancias como argumentos

2. **¿A qué se refiere la composición en POO?**
   - Relación "tiene un" fuerte
   - El componente no puede existir sin el compuesto
   - El compuesto crea y gestiona al componente

3. **Diferencia entre colaboración y composición**
   - **Colaboración**: Interacción temporal, objetos independientes
   - **Composición**: Relación estructural, dependencia de existencia