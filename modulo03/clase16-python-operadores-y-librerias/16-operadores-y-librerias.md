# Introducción a Python - Operadores y Librerías

## Operadores Matemáticos

### Operadores básicos
Python incluye los operadores matemáticos estándar:
- `+` (suma)
- `-` (resta)
- `*` (multiplicación)
- `/` (división)

>[!IMPORTANT]
>**Python vs Javascript - Dividir por cero (`0`)**
>En Javascript, la operación de dividir por cero resulta `'Infinity'` mientras que en Python devuelve un <ins>error</ins> (`ZeroDivisionError`)

### Otros operadores matemáticos
Además de los operadores básicos, Python ofrece:

| Operador | Descripción |
|----------|-------------|
| `**` | Potencia |
| `%` | Módulo (resto de la división) |
| `//` | División entera |

---

## Precedencia de Operadores

"Saber en qué orden se realiza un grupo de operaciones"

### Ejemplo:
```python
10 - 5 * 2
10 - 10
0
```

### Orden de las operaciones
Cuando dos operaciones tienen el mismo nivel de prioridad, se resuelven de **izquierda a derecha**.

### Operaciones y paréntesis
Los paréntesis cambian el orden de precedencia, dando prioridad a las operaciones que están dentro de ellos.

#### Ejemplo:
```python
(10 - 5) * 2
5 * 2
10
```

---

## Librerías

### ¿Qué son las librerías?
Las librerías son extensiones del lenguaje que añaden funcionalidades no disponibles en Python nativo.

### Importar una librería
Normalmente las importaciones se definen al inicio de un código.

#### Sintaxis básica:
```python
import libreria
libreria.metodo()
```

#### Importación específica:
```python
from libreria import funcion
```

### Alias para librerías
Para evitar nombres largos o complicados, es posible importar librerías con un alias:

```python
import libreria as lb
lb.metodo()
```

#### Nombres convencionales comunes:
- `import numpy as np`
- `import pandas as pd`
- `import matplotlib.pyplot as plt`

---

## Instalación de Librerías

### Ventaja de Anaconda
Anaconda ya trae preinstaladas muchas de las librerías más famosas de Python.

### Métodos de instalación

#### 1. Pip
Pip es el instalador por defecto de PyPI (Python Package Index).

```bash
pip install pandas
```

**Ventaja**: Disponibiliza actualizaciones con mayor rapidez.

#### 2. Conda
Conda tiene su propio repositorio de librerías.

```bash
conda install pytorch
```

**Ventaja**: Útil para librerías que prefieren este repositorio.

> **Nota**: Las últimas versiones de Anaconda son compatibles con ambos métodos. Siempre es recomendable revisar la documentación oficial de cada librería para conocer su método preferido de instalación.

---

## Ejercicio Guiado: Contando Calorías

### Contexto
Algunos alimentos consideran un grado alcohólico, donde cada grado alcohólico aporta **7 calorías**.

**Objetivo**: Modificar el programa para ingresar el grado alcohólico de un alimento y calcular el número de calorías que posee.

---

### Paso 1: Solicitar datos para el cálculo

```python
# Solicitar datos al usuario
proteinas = float(input("Ingrese gramos de proteínas: "))
carbohidratos = float(input("Ingrese gramos de carbohidratos: "))
grasas = float(input("Ingrese gramos de grasas: "))
grado_alcoholico = float(input("Ingrese grado alcohólico: "))
```

---

### Paso 2: Calcular la fórmula de calorías

Fórmula:
- 4 calorías por cada gramo de proteína
- 4 calorías por cada gramo de carbohidrato
- 9 calorías por cada gramo de grasa
- 7 calorías por cada grado alcohólico

```python
calorias = (proteinas * 4) + (carbohidratos * 4) + (grasas * 9) + (grado_alcoholico * 7)
```

---

### Paso 3: Entregar el resultado en el formato correcto

Las calorías totales deben redondearse al entero superior. Para ello, se utiliza la librería `math` y la función `ceil`:

```python
import math

calorias_totales = math.ceil(calorias)
print(f"El total de calorías es: {calorias_totales}")
```

---

### Paso 4: Código final

```python
import math

# Solicitar datos
proteinas = float(input("Ingrese gramos de proteínas: "))
carbohidratos = float(input("Ingrese gramos de carbohidratos: "))
grasas = float(input("Ingrese gramos de grasas: "))
grado_alcoholico = float(input("Ingrese grado alcohólico: "))

# Calcular calorías
calorias = (proteinas * 4) + (carbohidratos * 4) + (grasas * 9) + (grado_alcoholico * 7)

# Redondear al entero superior
calorias_totales = math.ceil(calorias)

# Mostrar resultado
print(f"El total de calorías es: {calorias_totales}")
```

---

### Verificación de resultados

- **Por porción** (segunda columna): Los cálculos cuadran a la perfección.
- **Cada 100 gramos** (primera columna): También se obtienen resultados correctos.

---

## Resumen

### Operadores
- Matemáticos básicos: `+`, `-`, `*`, `/`
- Avanzados: `**`, `%`, `//`
- Precedencia: paréntesis > multiplicación/división > suma/resta

### Librerías
- Extienden la funcionalidad de Python
- Se importan con `import`
- Se pueden usar alias para simplificar
- Instalación vía `pip` o `conda`

### Tipos de datos
- Identificar los tipos de datos que utiliza Python
- Formas básicas de manipularlos