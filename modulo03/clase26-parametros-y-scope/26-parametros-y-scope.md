# Funciones y variables (parte II)

## Contenido del Curso

1. [Tipos de argumentos](#tipos-de-argumentos)
2. [Tipos de parámetros](#tipos-de-parámetros)
3. [Ejercicio guiado: Expandiendo diccionarios](#ejercicio-guiado-expandiendo-diccionarios)
4. [Variables: Locales vs Globales](#variables-locales-vs-globales)
5. [Alcance de variables (Scope)](#alcance-de-variables-scope)
6. [Ejercicio guiado: Loto](#ejercicio-guiado-loto)
7. [Resumen](#resumen-de-la-sesión)

---

### Objetivos Generales

- Comprender el contexto de las declaraciones de variables
- Crear funciones en conocimiento de los tipos de parámetros disponibles

---

## Tipos de argumentos

Los **argumentos** son valores que toman los parámetros de una función. Pueden ser:
- Cualquier tipo de dato
- Estructuras de datos (listas, diccionarios, etc.)
- **Otras funciones**

### Ejemplo con diccionario

```python
precios = {
    'Notebook': 700000, 
    'Teclado': 25000, 
    'Mouse': 12000, 
    'Monitor': 250000, 
    'Escritorio': 135000, 
    'Tarjeta de Video': 1500000
}

def filtrar(diccionario, umbral):
    filtro = {k: v for k, v in diccionario.items() if v > umbral}
    return filtro

filtrar(precios, 12000)
# {'Notebook': 700000, 'Teclado': 25000, 'Monitor': 250000, 
#  'Escritorio': 135000, 'Tarjeta de Video': 1500000}
```

---

### Funciones como argumentos

En Python podemos pasar funciones como argumentos. **Solo se debe utilizar el nombre de la función, sin paréntesis.**

```python
lista_numeros = [1, 2, 3, 4, 5]
lista_string = ['a', 'b', 'c', 'd', 'e']

def sumar_contar_tipos(lista, funcion):
    tipos = [type(elemento) for elemento in lista]
    opcion = funcion(lista)
    return tipos, opcion

# Usando len como argumento
tipo, conteo = sumar_contar_tipos(lista_string, len)
print(tipo)   # [<class 'str'>, ...]
print(conteo) # 5

# Usando sum como argumento
tipo, suma = sumar_contar_tipos(lista_numeros, sum)
print(tipo)   # [<class 'int'>, ...]
print(suma)   # 15
```

---

## Tipos de parámetros
### Parámetros obligatorios

Son aquellos que **deben** recibir un argumento; de lo contrario, la función fallará.

```python
def extremo_multiplicado(lista, factor):
    minimo = min(lista)
    maximo = max(lista)
    return factor * minimo, factor * maximo

# ✅ Correcto - orden correcto
print(extremo_multiplicado([1, 2, 3, 4], 4))  # (4, 16)

# ✅ Correcto - usando nombres de parámetros
print(extremo_multiplicado(factor=4, lista=[1, 2, 3, 4]))  # (4, 16)

# ❌ Incorrecto - orden equivocado
# print(extremo_multiplicado(4, [1, 2, 3, 4]))  # Error
```

---

### Parámetros opcionales o por defecto

Permiten definir un valor predeterminado cuando no se proporciona el argumento.

```python
def elevar(base, exponente, redondear=False):
    if redondear:
        valor = round(base ** exponente, 2)
    else:
        valor = base ** exponente
    return valor

print(elevar(2, 3))                    # 19.241905543136184
print(elevar(2, 3, redondear=True))    # 19.24
```

>[!IMPORTANT]
>El valor por defecto se evalúa **una sola vez** en el punto de definición de la función. Esto es relevante cuando el valor por defecto es un objeto mutable, como una lista o un diccionario.

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]
```

Para evitar que el valor por defecto sea compartido entre llamadas, se puede escribir la función así:

```python
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
```
---

### Parámetros especiales

Por defecto, los argumentos pueden pasarse a una función por posición o explícitamente por nombre. Para legibilidad y rendimiento, es posible restringir cómo se pasan los argumentos usando los símbolos `/` y `*` en la definición de la función.

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    #        |          Posicional o con nombre   |
    #        |                                    - Solo con nombre
    #         -- Solo posicionales
```

- `/`: Marca los parámetros anteriores como **solo posicionales**. Su orden importa y no pueden pasarse con nombre.

- `*`: Marca los parámetros siguientes como **solo con nombre**. Deben pasarse usando la sintaxis nombre=valor.

**Ejemplos:**
```python
def standard_arg(arg):
    print(arg)  # Puede llamarse por posición o con nombre

def pos_only_arg(arg, /):
    print(arg)  # Solo por posición

def kwd_only_arg(*, arg):
    print(arg)  # Solo con nombre

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)
```

**Recapitulación:**

- **Solo posicionales:** Usar cuando los nombres de los parámetros no tienen significado real o para forzar el orden.

- **Solo con nombre:** Usar cuando los nombres tienen significado y la función es más comprensible siendo explícita.

- Para una API, usar parámetros solo posicionales para evitar que cambios en el nombre del parámetro rompan la compatibilidad.

---

### Argumentos variables (*args)

Permite pasar un número **variable de argumentos posicionales** sin definirlos a priori.

```python
def sumar_numeros(*args):
    suma = 0
    for num in args:
        suma += num
    return suma

print(sumar_numeros(1, 2, 3))          # 6
print(sumar_numeros(1, 2, 3, 4, 5))    # 15
print(sumar_numeros(1, 2))             # 3
print(sumar_numeros())                 # 0
```

---

### Argumentos con nombre variables (**kwargs)

Permite un número indeterminado de **argumentos con nombre**.

```python
def crear_perfil(**kwargs):
    perfil = {}
    for key, value in kwargs.items():
        perfil[key] = value
    return perfil

perfil1 = crear_perfil(nombre='Alice', edad=25, ciudad='Barcelona')
perfil2 = crear_perfil(nombre='Bob', edad=30, ocupacion='Ingeniero')

print(perfil1)  # {'nombre': 'Alice', 'edad': 25, 'ciudad': 'Barcelona'}
print(perfil2)  # {'nombre': 'Bob', 'edad': 30, 'ocupacion': 'Ingeniero'}
```


## Ejercicio guiado: Expandiendo diccionarios

Crear una función `get_multiple()` que permita extraer valores de un diccionario usando un número variable de claves.

### Paso 1: Crear el script `get_multiple.py`

### Paso 2: Definir la función con *args

```python
def get_multiple(diccionario, *claves):
    pass
```

### Paso 3: Iterar y verificar claves

```python
def get_multiple(diccionario, *claves):
    return {clave: diccionario[clave] for clave in claves}
```

### Paso 4: Probar la función

```python
diccionario_prueba = {
    'manzana': 'verde', 
    'platano': 'amarillo', 
    'frutilla': 'roja'
}

resultado = get_multiple(diccionario_prueba, 'manzana', 'platano')
print(resultado)  # {'manzana': 'verde', 'platano': 'amarillo'}
```

---

## Variables: Locales vs Globales

### Variables Locales
- Definidas **dentro de un contexto específico** (como una función)
- Solo disponibles dentro de ese bloque (scope local)

### Variables Globales
- Definidas **fuera de cualquier función**
- Accesibles desde cualquier parte del código

---

## Alcance de variables (Scope)

Python busca variables en el siguiente orden:
1. **Scope local** (dentro de la función)
2. **Scope global** (fuera de la función)

```python
continent = "Sudamérica"  # Variable global

def get_continent():
    # No hay variable local 'continent'
    # Python busca en el scope global
    print(continent)  # Imprime: Sudamérica

get_continent()
```

---

### Modificando variables globales

Para modificar una variable global dentro de una función, se usa la palabra clave `global`.

> ⚠️ **Precaución**: Esta práctica es **poco recomendada** y puede generar errores difíciles de depurar.

```python
contador = 0  # Variable global

def incrementar():
    global contador
    contador += 1

incrementar()
print(contador)  # 1
```

---

### Precauciones con variables globales

### ¿Por qué son consideradas una mala práctica?

- **Código difícil de entender**: Es complejo rastrear dónde y cuándo se modifica una variable global.
- **Errores inesperados**: En programas grandes (miles de líneas + librerías externas), dos partes del código pueden usar el mismo nombre de variable global sin saberlo.
- **Problemas de depuración**: Los cambios en variables globales pueden afectar el comportamiento de funciones que no esperaban ese cambio.

### Alternativa recomendada
Usar **`return`** para devolver valores desde las funciones, manteniendo el flujo de datos controlado.

---

## Ejercicio guiado: Loto

Crear un programa que simule un sorteo de Loto.

### Reglas
- Pool de números del 1 al 41
- Se extraen 6 números al azar
- Un séptimo número es el comodín

### Paso 1: Crear el archivo `loto.py`

### Paso 2: Crear el pool de números

```python
pool = [n for n in range(1, 42)]
```

### Paso 3: Seleccionar un número al azar

```python
import random

elegido = random.choice(pool)
print("El primer número es", elegido)
```

### Paso 4: Remover el número seleccionado

```python
pool.remove(elegido)
elegido = random.choice(pool)
print("El segundo número es", elegido)
```

### Paso 5: El séptimo número es el comodín

```python
pool.remove(elegido)
elegido = random.choice(pool)
print("El Comodín número es", elegido)
```

### Paso 6: Condensar en una función

```python
def sacar_numero(posicion):
    global pool
    elegido = random.choice(pool)
    pool.remove(elegido)
    print(f'El {posicion} es {elegido}')
```

### Paso 7: Ejecutar el programa

Al ejecutar, se observan los números extraídos y cómo el pool disminuye en cada iteración.

---

## Resumen de la sesión

- **Argumentos**: Obligatorios, opcionales, variables (*args) y con nombre (**kwargs)
- **Funciones como argumentos**: Se pasan solo por nombre, sin paréntesis
- **Variables locales**: Definidas dentro de una función
- **Variables globales**: Definidas fuera de funciones
- **Scope**: Orden de búsqueda de variables (local → global)
- **Precaución con globales**: Pueden causar errores difíciles de depurar

---

Adaptado del material del curso elaborado por *Desafío Latam - Academia de Talentos Digitales*