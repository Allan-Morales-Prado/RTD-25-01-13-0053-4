# Funciones - Parte I

## Preguntas de Opción Múltiple

---

### Pregunta 1
¿Cuál es la palabra reservada en Python para definir una función?

A) `function`
B) `def`
C) `define`
D) `func`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B) `def`**

`def` es la palabra reservada en Python para definir funciones. Ejemplo: `def mi_funcion():`
</details>

---

### Pregunta 2
¿Qué significa el principio DRY en programación?

A) **D**evelop **R**eusable **Y**ardsticks
B) **D**on't **R**epeat **Y**ourself
C) **D**ata **R**eturn **Y**ield
D) **D**eploy **R**eady **Y**ield

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B) Don't Repeat Yourself**

DRY es un principio que busca evitar la redundancia de código. Si copias y pegas un código más de una vez, probablemente deberías crear una función.
</details>

---

### Pregunta 3
¿Qué sucede si usamos `print()` dentro de una función en lugar de `return`?

A) La función retorna `None` implícitamente y muestra el valor en pantalla
B) La función retorna el valor mostrado
C) La función no se ejecuta
D) La función retorna un string

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A) La función retorna `None` implícitamente y muestra el valor en pantalla**

`print()` muestra el valor en consola pero no lo retorna. Si no hay `return` explícito, la función retorna `None`.
</details>

---

### Pregunta 4
¿Cuál de las siguientes afirmaciones sobre los parámetros es correcta?

A) Los parámetros son los valores concretos que se pasan a una función
B) Los parámetros solo pueden ser números enteros
C) Los parámetros son variables que se definen dentro de la función
D) Los parámetros son elementos que se utilizan dentro de la función para realizar sus cálculos

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: D) Los parámetros son elementos que se utilizan dentro de la función para realizar sus cálculos**

Los parámetros son variables definidas en la declaración de la función. Los argumentos son los valores concretos que se pasan al invocar la función.
</details>

---

### Pregunta 5
¿Qué hace el siguiente código?

```python
def calcular(a, b):
    return a + b
    print("Suma realizada")
```

A) Retorna la suma y luego imprime el mensaje
B) Retorna la suma y no imprime el mensaje
C) Imprime el mensaje y retorna la suma
D) Produce un error

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B) Retorna la suma y no imprime el mensaje**

El `return` termina la ejecución de la función. El `print()` después del `return` nunca se ejecuta.
</details>

---

### Pregunta 6
¿Cómo se invoca (llama) una función llamada `saludar` que no recibe parámetros?

A) `saludar`
B) `saludar()`
C) `call saludar`
D) `invocar saludar`

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: B) `saludar()`**

Para invocar una función en Python se deben usar paréntesis después del nombre de la función.
</details>

---

### Pregunta 7
¿Qué tipo de dato retorna una función que tiene múltiples valores en su `return`?

A) Lista
B) Diccionario
C) Tupla
D) Conjunto

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C) Tupla**

Cuando una función retorna múltiples valores separados por comas, Python los empaqueta automáticamente en una tupla.
</details>

---

### Pregunta 8
¿Cuál de las siguientes es una buena práctica al nombrar funciones en Python?

A) Usar nombres cortos de una sola letra
B) Usar mayúsculas para separar palabras (camelCase)
C) Usar minúsculas con guiones bajos (snake_case)
D) Usar nombres en español

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: C) Usar minúsculas con guiones bajos (snake_case)**

La convención en Python para nombres de funciones es usar `snake_case`, por ejemplo: `calcular_promedio()`.
</details>

---

## Pregunta de Análisis de Código

### Pregunta 9
¿Qué imprime el siguiente código?

```python
def ejemplo(lista):
    resultado = []
    for i in lista:
        resultado.append(i * 2)
    return resultado

numeros = [1, 2, 3, 4]
print(ejemplo(numeros))
```

A) `[2, 4, 6, 8]`
B) `[1, 2, 3, 4]`
C) `[2, 3, 4, 5]`
D) Error

<details>
<summary><strong>Ver respuesta</strong></summary>

**Respuesta correcta: A) `[2, 4, 6, 8]`**

La función recorre la lista y multiplica cada elemento por 2, retornando una nueva lista con los resultados.
</details>

---

## Pregunta de Desarrollo

### Pregunta 10
Escribe una función llamada `es_par` que reciba un número como parámetro y retorne `True` si el número es par y `False` si es impar.

<details>
<summary><strong>Ver solución</strong></summary>

```python
def es_par(numero):
    return numero % 2 == 0

# Pruebas
print(es_par(4))  # True
print(es_par(7))  # False
```
</details>