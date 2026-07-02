# Funciones - Parte I

## Contenido del Curso

1. [Introducción a las Funciones](#introducción-a-las-funciones)
2. [Sintaxis Básica de una Función](#sintaxis-básica-de-una-función)
3. [Principio DRY](#principio-dry)
4. [Anatomía de una Función](#anatomía-de-una-función)
5. [Retorno de Funciones](#retorno-de-funciones)
6. [Ejercicio Guiado: Mini encuesta](#ejercicio-guiado-mini-encuesta)
7. [Ejercicio Guiado: Estandarización](#ejercicio-guiado-estandarización)
8. [Resumen](#resumen-de-la-sesión)
---

### Objetivo general
- Define funciones que utilizan parámetros de entrada y que producen un retorno para resolver un problema

---

## Introducción a las Funciones

### Funciones Built-in vs User Defined

Hasta ahora hemos utilizado funciones propias de Python (**built-in functions**) tales como:
- `print()`
- `len()`
- `input()`
- `sorted()`
- `zip()`

Estas funciones ya vienen creadas en el lenguaje. Ahora nos enfocaremos en **funciones definidas por el usuario** (user defined functions), que el programador crea según sus necesidades.

---

## Sintaxis Básica de una Función

```python
def nombre_de_la_funcion():
    pass
```

**Elementos clave:**
- `def` - Palabra reservada para definir la función
- **Nombre** - Por convención se usa `snake_case`
- **Buena práctica** - Utilizar nombres representativos de la operación
- `pass` - Palabra reservada que indica que la función no hace nada

---

### Ejemplo uso de una función
¿Cuál es la utilidad de crear nuestras propias funciones?

**Versión SIN función**

```python
# Código repetitivo - Mala práctica
print('Opciones: ')
print('1) De acuerdo')
print('2) En desacuerdo')
print('3) No me interesa')

# ... más código ...

print('Opciones: ')
print('1) De acuerdo')
print('2) En desacuerdo')
print('3) No me interesa')

# ... más código ...

print('Opciones: ')
print('1) De acuerdo')
print('2) En desacuerdo')
print('3) No me interesa')
```
<span><em>Código #1: Código repetido, utilizado para mostrar por pantalla el mismo texto varias veces.</em></span>

**Problemas:**
- Código extenso y repetitivo
- Difícil de mantener
- Si se quiere cambiar el menú, hay que modificar múltiples lugares

---

**Versión CON función**

```python
# Definición de la función
def imprimir_menu():
    print('Opciones: ')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')

# Invocaciones de la función
imprimir_menu()  # Primera vez
# ... más código ...
imprimir_menu()  # Segunda vez
# ... más código ...
imprimir_menu()  # Tercera vez
```
<span><em>Código #2: Código reutilizado (definido en una función), para mostrar por pantalla el mismo texto varias veces.</em></span>

**Ventajas:**
- Código más corto
- Fácil mantenimiento (un solo punto de modificación)
- Reutilización de código

---

## Principio DRY

**DRY** = **D**on't **R**epeat **Y**ourself

> "Si tengo que copiar y pegar un trozo de código 2 o más veces, es muy probable que necesite crear una función."

Este es un principio básico en el diseño de software que busca evitar la redundancia de código.

---

## Anatomía de una Función

### Parámetros y Argumentos

| Concepto | Definición |
|----------|------------|
| **Parámetro** | Elemento que podrá ser utilizado dentro de la función para realizar sus cálculos. Permite crear funciones reutilizables. |
| **Argumento** | Valores que tomará el parámetro para ser utilizado dentro de la función. |

Los parámetros pueden ser **cualquier tipo de dato**, incluyendo estructuras de datos.

---

## Retorno de Funciones

### ¿Qué es el retorno?

- Las funciones pueden devolver un valor que se pueda utilizar posteriormente
- El retorno implica el **término de la función**
- Cualquier código después de `return` no se ejecuta

### Ejemplo de Retorno

```python
def prueba_return():
    a = "Esta línea se va a imprimir"
    b = "Esta línea no se va a imprimir"
    return a  # Punto de salida
    print(b)  # ¡Nunca se ejecuta!

print(prueba_return())  # Imprime: "Esta línea se va a imprimir"
```

`print()` muestra en pantalla pero no es un valor utilizable.
`return` devuelve un valor que puede ser utilizado en cálculos posteriores.

---

### Múltiples Retornos

Python permite retornar múltiples valores usando tuplas:

```python
def cuadrado_y_cubo(numero):
    cuadrado = numero ** 2
    cubo = numero ** 3
    return cuadrado, cubo  # Retorna una tupla

# Desempaquetado
cuadrado, cubo = cuadrado_y_cubo(3)
print(cuadrado)  # 9
print(cubo)      # 27
```

---

## Ejercicio Guiado: Mini Encuesta

### Enunciado
- Una empresa de encuestas necesita generar una mini encuesta de 3 preguntas
- Las respuestas deben ser:
  - Almacenadas en una lista
  - Mostradas al final del programa

### Solución Paso a Paso

#### Paso 1: Definir preguntas
```python
preguntas = [
    'Enunciado Pregunta 1',
    'Enunciado Pregunta 2',
    'Enunciado Pregunta 3'
]
```

#### Paso 2: Definir menú y recolectar respuestas
```python
def imprimir_menu():
    print('Opciones: ')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')

respuestas = []

for p in preguntas:
    print(p)
    imprimir_menu()
    respuestas.append(input('> '))
```
>[!TIP]
>**Pregunta rápida**: ¿La función `input` devuelve un valor?

#### Paso 3: Mostrar resultados
```python
for i in range(3):
    print(f'La respuesta a la pregunta {i+1} fue {respuestas[i]}')
print('Muchas gracias por responder la encuesta')
```

### Código Completo
```python
def imprimir_menu():
    print('Opciones: ')
    print('1) De acuerdo')
    print('2) En desacuerdo')
    print('3) No me interesa')

preguntas = [
    'Enunciado Pregunta 1',
    'Enunciado Pregunta 2',
    'Enunciado Pregunta 3'
]
respuestas = []

for p in preguntas:
    print(p)
    imprimir_menu()
    respuestas.append(input('> '))

for i in range(3):
    print(f'La respuesta a la pregunta {i+1} fue {respuestas[i]}')
print('Muchas gracias por responder la encuesta')
```
<span><em>Código #3: Uso combinado de funciones y bucles para elaborar una mini-encuesta</em></span>

## Ejercicio Guiado: Estandarización

### Enunciado
Crear un script que calcule:
- Media
- Desviación estándar
- Valores estandarizados (z-scores)

### Solución Paso a Paso

#### Paso 1: Definir la función para la media
```python
def media(lista):
    return sum(lista) / len(lista)
```

#### Paso 2: Definir la función para la desviación estándar
```python
import math

def sdd(lista, media):
    diff = [(elemento - media) ** 2 for elemento in lista]
    return math.sqrt(sum(diff) / (len(lista) - 1))
```

#### Paso 3: Función que calcula los tres resultados
```python
def resultado(lista):
    m = media(lista)
    sd = sdd(lista, m)
    lista_estandarizada = [(valor - m) / sd for valor in lista]
    return m, sd, lista_estandarizada
```

### Código Completo
```python
import math

def media(lista):
    return sum(lista) / len(lista)

def sdd(lista, media):
    diff = [(elemento - media) ** 2 for elemento in lista]
    return math.sqrt(sum(diff) / (len(lista) - 1))

def resultado(lista):
    m = media(lista)
    sd = sdd(lista, m)
    lista_estandarizada = [(valor - m) / sd for valor in lista]
    return m, sd, lista_estandarizada
```
<span><em>Código #4: Problema resuelto con funciones - Estandarización de vectores</em></span>

>[!TIP]
>Media, desviación estándar y vectores, con conceptos matemáticos muy utilizados en **ciencias de datos**, donde se trabaja codo a codo con los lenguajes **Python** y **R**. Revisa el Anexo para una explicación e implementación más detallada de este ejercicio.

## Resumen de la Sesión

### Conceptos Clave
- ✅ **Funciones definidas por el usuario** (`def`)
- ✅ **Principio DRY** - Evitar redundancia de código
- ✅ **Parámetros** - Entradas de una función
- ✅ **Retorno** (`return`) - Salidas de una función
- ✅ **Múltiples retornos** - Usando tuplas y desempaquetado

### Buenas Prácticas
- Usar nombres representativos en `snake_case`
- Definir funciones al inicio del código
- Mantener las funciones enfocadas en una sola tarea
- Utilizar `return` en lugar de `print()` dentro de funciones

---

## Próxima Sesión

**Temas a tratar:**
- Tipos de argumentos
- Variables locales y globales
- Funciones como argumentos de otras funciones

---

Adaptado del material del curso elaborado por *Desafío Latam - Academia de Talentos Digitales*