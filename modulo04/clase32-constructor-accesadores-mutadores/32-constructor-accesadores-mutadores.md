# Constructor, Accesadores y Mutadores

## Contenido

1. [Constructores](#constructores)
2. [Definición del Constructor en Python](#definición-del-constructor-en-python)
3. [Interfaces de acceso (convención)](#interfaces-de-acceso-convención)
4. [Accesadores (Getters) y Mutadores (Setters)](#accesadores-getters-y-mutadores-setters)
5. [Ejemplo: Clase Pelota](#ejemplo-clase-pelota)
6. [Decorador @property en Python](#decorador-property-en-python)
7. [⚠️ Errores Comunes](#️-errores-comunes)
8. [Ejercicio Guiado: "Ingreso de Medicamentos"](#ejercicio-guiado-ingreso-de-medicamentos)

## Constructores

### ¿Qué son los constructores?

Un **método constructor** es un método que:
- Se ejecuta **automáticamente** al momento de crear una instancia de la clase
- No necesita ser llamado explícitamente
- Su función es dar valores a los atributos de la instancia recién creada

### Formas de asignar valores

Los valores que se dan a los atributos pueden ser:

| Tipo | Descripción |
|------|-------------|
| **Valores por defecto** | Definidos en el constructor |
| **Valores entregados explícitamente** | Especificados al crear la instancia |
| **Combinación** | Valores por defecto que pueden ser sobreescritos |

---

## Definición del Constructor en Python

### Características del método `__init__`

- Se define exclusivamente con el nombre **`__init__`**
- Debe tener como primer parámetro la instancia de la clase: **`self`**
- No puede tener retorno (a menos que sea `None`)
- Por lo general, es el primer método definido dentro de la clase

### Asignación de valores en el constructor

```python
class Ejemplo:
    def __init__(self, parametro="valor_por_defecto"):
        self.atributo1 = "valor_fijo"           # Valor directo en el cuerpo
        self.atributo2 = parametro               # Valor desde parámetro
        self.atributo3 = parametro               # Con valor por defecto
```

**Nota**: La forma de asignar valores está generalmente dada por las reglas del negocio y/o requerimientos.

---

## Interfaces de acceso (convención)

### Atributos Privados y Protegidos en Python

En Python, no existe una verdadera encapsulación como en otros lenguajes (Java, C++ o C#), pero seguimos una **convención**:

| Convención | Significado |
|------------|-------------|
| `_atributo` | Atributo **protegido** (un guion bajo) |
| `__atributo` | Atributo **privado** (doble guion bajo) |

### Importancia de los Atributos Privados

- **Seguridad**: Restringen el acceso directo, protegiendo la integridad de los datos
- **Control**: Permiten controlar cómo se accede y modifica el estado interno del objeto
- **Mantenibilidad**: Facilitan la actualización y mantenimiento del código

---

## Accesadores (Getters) y Mutadores (Setters)

### Accesadores (Getters)
Métodos que permiten **leer** los valores de los atributos privados o protegidos de manera controlada.

### Mutadores (Setters)
Métodos que permiten **modificar** el valor de un atributo en una instancia, aplicando reglas al momento de asignar.

### Ventajas
- Impiden que el valor sea visto o modificado directamente desde la instancia
- Permiten aplicar lógica y validaciones

---

## Ejemplo: Clase Pelota

### Implementación con atributos privados

```python
class Pelota():
    def __init__(self, color="Blanco", tamano=20, material="Plástico"):
        self._color = color
        self._tamano = max(1, tamano)  
        self._material = material

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, valor):
        if not valor:
            raise ValueError("El color no puede estar vacío")
        self._color = valor
```

---

## Decorador @property en Python

### Accesador con @property

```python
@property
def tamano(self):
    return self._tamano
```

### Mutador con @property.setter

```python
@tamano.setter
def tamano(self, valor):
    if valor < 1:
        raise ValueError("El tamaño debe ser al menos 1")
    self._tamano = valor
```

### Uso de la clase

```python
# Creación de instancia
p = Pelota("Amarillo", 25, "plástico")

# Uso del accesador (sin paréntesis)
print(p.descripcion)  # "Pelota Amarillo de plástico, tamaño 25"

# Uso del mutador (con asignación)
p.tamano = 0  # Esto generará ValueError
```

---

## ⚠️ Errores Comunes

### Error de Recursividad
Si un getter o setter utiliza el mismo nombre para el atributo interno (ej., usando `self.tamano` en lugar de `self._tamano`), se producirá un **error de recursividad**.

### AttributeError
Si se intenta acceder a un atributo directamente en el constructor sin haberlo definido correctamente, se lanzará un `AttributeError`.

### Solución
Crear atributos de uso interno o "privados" para que solo puedan ser accedidos o modificados mediante sus getters y setters respectivamente.

---

## Ejercicio Guiado: "Ingreso de Medicamentos"

### Contexto
Desde la cadena farmacéutica, se solicita generar un prototipo de aplicación (script Python) que permita generar medicamentos a partir de datos ingresados por el usuario.

### Requerimientos

1. **Precios por defecto**: Cada medicamento debe tener precio bruto = 0, precio neto = 0 y descuento = 0 (no modificables al crear la instancia).

2. **Nombre obligatorio**: Toda instancia debe tener un nombre entregado al momento de la creación.

3. **Stock opcional**: Si no se entrega stock, se asigna valor de 0.

4. **Asignación de precio bruto**: Al asignar precio bruto > 0, se calcula automáticamente:
   - Precio final (con IVA)
   - Descuento según rango de precio

### Reglas de Descuento

| Rango de Precio | Descuento |
|-----------------|-----------|
| \$10.000 - $19.999 | 10% |
| ≥ $20.000 | 20% |
| < $10.000 | 0% |

---

### Solución Paso a Paso

### Paso 1: Refactorizar la clase Medicamento
Eliminar el atributo `descuento` y el método `asigna_precio`.

### Paso 2: Constructor

```python
class Medicamento:
    def __init__(self, nombre, stock=0):
        self.nombre = nombre
        self.stock = stock
        self.precio_bruto = 0
        self.precio_final = 0
        self.descuento = 0
```

### Paso 3: Accesador de precio_final

```python
@property
def precio_final(self):
    return self._precio_final
```

---

### Paso 4: Mutador de precio (Setter)

```python
@precio.setter
def precio(self, precio_bruto):
    if precio_bruto > 0:
        self.precio_bruto = precio_bruto
        # Cálculo del precio final con IVA
        self.precio_final = self.precio_bruto * 1.19
        # Cálculo del descuento
        if self.precio_final >= 20000:
            self.descuento = 0.20
        elif self.precio_final >= 10000:
            self.descuento = 0.10
        else:
            self.descuento = 0
        # Aplicar descuento
        self.precio_final = self.precio_final * (1 - self.descuento)
```

---

### Paso 8-10: Programa Principal (programa.py)

```python
from medicamento import Medicamento

# Solicitar datos al usuario
nombre = input("Ingrese el nombre del medicamento: ")
stock = int(input("Ingrese el stock: "))
precio_bruto = int(input("Ingrese el precio bruto: "))

# Crear instancia y asignar precio
m1 = Medicamento(nombre, stock)
m1.precio = precio_bruto
```

### Paso 11-13: Mostrar Resultados

```python
# Mostrar nombre y precio bruto
print(f"El precio bruto del medicamento {m1.nombre} es {m1.precio_bruto}")

# Mostrar descuento si corresponde
if m1.descuento > 0:
    print(f"El descuento aplicado es de {m1.descuento * 100}%")

# Mostrar precio final
print(f"El precio final del medicamento es {m1.precio_final}")
```

---

### Ejemplo de Salida

```
Ingrese el nombre del medicamento: Paracetamol
Ingrese el stock: 50
Ingrese el precio bruto: 15000

El precio bruto del medicamento Paracetamol es 15000
El descuento aplicado es de 10.0%
El precio final del medicamento es 16065.0
```