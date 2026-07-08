# Cuestionario - Fundamentos de Programación en Python

### Sub-módulo 1: Introducción a Python y Conceptos Básicos

---

#### Pregunta 1

**¿Cuál de las siguientes afirmaciones describe correctamente una característica de Python?**

A) Python es un lenguaje compilado, lo que significa que todo el código se traduce a lenguaje máquina antes de ejecutarse.

B) Python es un lenguaje de tipado estático, por lo que las variables deben declararse con su tipo antes de usarse.

C) Python es un lenguaje interpretado y dinámicamente tipado, lo que permite ejecutar código línea por línea y cambiar el tipo de una variable en tiempo de ejecución.

D) Python requiere una licencia paga para uso comercial y no permite modificar su código fuente.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

Python es interpretado (ejecuta línea por línea) y dinámicamente tipado (las variables no tienen un tipo fijo). Es de código abierto y gratuito, incluso para uso comercial.

</details>

---

#### Pregunta 2

**¿Qué imprime el siguiente código?**

```python
x = 5
y = "10"
resultado = x + int(y)
print(resultado)
```

A) "510"
B) 15
C) Error de tipo
D) 510

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`int(y)` convierte el string "10" al entero 10, luego se suman 5 + 10 = 15.

</details>

---

#### Pregunta 3

**¿Qué diferencia hay entre un lenguaje compilado y uno interpretado?**

A) Los lenguajes compilados son siempre más lentos que los interpretados.
B) Los lenguajes compilados traducen todo el código antes de ejecutarlo, mientras que los interpretados ejecutan línea por línea.
C) Los lenguajes interpretados no pueden tener errores de sintaxis.
D) No hay diferencia, son términos intercambiables.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Los lenguajes compilados (como C) traducen todo el código a lenguaje máquina antes de la ejecución. Los interpretados (como Python y JavaScript) ejecutan las instrucciones línea por línea mediante un intérprete.

</details>

---

#### Pregunta 4

**¿Cuál de las siguientes es una ventaja del tipado dinámico en Python?**

A) Mayor seguridad de tipos en tiempo de compilación.
B) Las variables ocupan menos espacio en memoria.
C) Mayor flexibilidad al permitir que una variable cambie de tipo durante la ejecución.
D) Mejor rendimiento en operaciones matemáticas.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

El tipado dinámico permite que una misma variable pueda almacenar diferentes tipos de datos en distintos momentos, lo que ofrece flexibilidad. Sin embargo, esto puede llevar a errores en tiempo de ejecución si no se maneja con cuidado.

</details>

---

#### Pregunta 5

**¿Qué es la precedencia de operadores?**

A) El orden en que se ejecutan las funciones en un programa.
B) La prioridad que tienen los operadores al momento de evaluar una expresión.
C) La cantidad de operaciones que puede realizar un procesador.
D) El número de operandos que puede tener un operador.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

La precedencia de operadores determina el orden en que se evalúan las operaciones en una expresión. Por ejemplo, la multiplicación tiene mayor precedencia que la suma.

</details>

---

#### Pregunta 6

**¿Cuál es el resultado de la siguiente expresión?**

```python
8 + 4 * 3 - 2
```

A) 18
B) 34
C) 22
D) 26

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

Por precedencia: 4 * 3 = 12, luego 8 + 12 - 2 = 18.

</details>

---

#### Pregunta 7

**¿Qué hace el siguiente fragmento de código?**

```python
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")
```

A) Solicita un número al usuario y lo imprime.
B) Solicita un texto al usuario y lo imprime con un saludo.
C) Imprime directamente "Hola {nombre}".
D) Genera un error porque no se puede usar f-strings con input().

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`input()` solicita datos al usuario (siempre devuelve string). Luego, el f-string inserta el valor de `nombre` en el mensaje de salida.

</details>

---

#### Pregunta 8

**¿Cuál es el tipo de dato que retorna la función `input()` en Python?**

A) int
B) float
C) str (string)
D) bool

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

La función `input()` siempre retorna un string, incluso si el usuario ingresa números. Para trabajar con números, se debe convertir con `int()` o `float()`.

</details>

---

### Sub-módulo 2: Estructuras de Datos

---

#### Pregunta 9

**Dada la siguiente lista:**

```python
frutas = ["manzana", "banana", "naranja", "uva", "sandía"]
```

**¿Qué elemento se obtiene con `frutas[-2]`?**

A) "uva"
B) "sandía"
C) "naranja"
D) Error

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

Los índices negativos cuentan desde el final: -1 es el último elemento ("sandía"), -2 es el penúltimo ("uva").

</details>

---

#### Pregunta 10

**¿Qué hace el siguiente código?**

```python
mi_lista = [1, 2, 3, 4, 5]
mi_lista.append(6)
print(mi_lista)
```

A) [1, 2, 3, 4, 5, 6]
B) [6, 1, 2, 3, 4, 5]
C) [1, 2, 3, 4, 5]
D) Error

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

`append()` agrega un elemento al final de la lista. La lista queda con los elementos originales más el nuevo al final.

</details>

---

#### Pregunta 11

**¿Cuál es la principal diferencia entre una lista y un diccionario en Python?**

A) Las listas solo almacenan números, los diccionarios almacenan cualquier tipo.
B) Las listas se acceden por índice numérico, los diccionarios se acceden por clave.
C) Las listas son inmutables, los diccionarios son mutables.
D) No hay diferencia, son intercambiables.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Las listas se acceden mediante índices numéricos que se generan automáticamente, mientras que los diccionarios se acceden mediante claves definidas por el usuario.

</details>

---

#### Pregunta 12

**¿Cuál es el resultado del siguiente código?**

```python
diccionario = {"a": 1, "b": 2, "c": 3}
diccionario["b"] = 5
print(diccionario)
```

A) {"a": 1, "b": 2, "c": 3}
B) {"a": 1, "b": 5, "c": 3}
C) Error porque no se puede modificar un diccionario
D) {"a": 1, "b": 2, "c": 3, "b": 5}

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Los diccionarios son mutables. Al asignar un nuevo valor a una clave existente, se sobrescribe el valor anterior.

</details>

---

#### Pregunta 13

**¿Qué imprime el siguiente código?**

```python
tupla = (1, 2, 3)
tupla[1] = 4
print(tupla)
```

A) (1, 4, 3)
B) (1, 2, 3)
C) Error - Las tuplas son inmutables
D) [1, 4, 3]

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

Las tuplas son estructuras inmutables, lo que significa que no se pueden modificar sus elementos una vez creadas. Intentar reasignar un elemento genera un error.

</details>

---

#### Pregunta 14

**Dado el siguiente diccionario:**

```python
persona = {
    "nombre": "María",
    "edad": 30,
    "ciudad": "Santiago"
}
```

**¿Cómo se accede al valor "Santiago"?**

A) `persona[2]`
B) `persona["ciudad"]`
C) `persona.ciudad`
D) `persona[ciudad]`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

En los diccionarios, se accede a los valores usando la clave entre corchetes y comillas (si es string): `persona["ciudad"]`.

</details>

---

#### Pregunta 15

**¿Qué hace el método `keys()` en un diccionario?**

A) Devuelve una lista con todos los valores del diccionario.
B) Devuelve un contenedor de todas las claves del diccionario.
C) Elimina todas las claves del diccionario.
D) Ordena las claves del diccionario.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`keys()` devuelve una vista de las claves del diccionario. Se puede convertir a lista con `list(diccionario.keys())`.

</details>

---

#### Pregunta 16

**¿Cuál es la salida del siguiente código?**

```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```

A) [1, 2, 3]
B) [1, 2, 3, 4]
C) [4, 1, 2, 3]
D) Error

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

En Python, al asignar una lista a otra variable (`b = a`), ambas variables apuntan al mismo objeto en memoria. Modificar `b` también modifica `a`.

</details>

---

### Sub-módulo 3: Algoritmos y Control de Flujo

---

#### Pregunta 17

**¿Qué es un algoritmo según la definición del curso?**

A) Un lenguaje de programación específico.
B) Una serie de pasos finitos y ordenados para resolver un problema.
C) Un tipo de dato complejo en Python.
D) Un programa que solo puede ejecutarse en computadoras.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Un algoritmo es una secuencia finita de pasos ordenados que resuelven un problema. Puede representarse mediante diagramas de flujo, pseudocódigo o código en un lenguaje de programación.

</details>

---

#### Pregunta 18

**¿Cuál de las siguientes NO es una forma de representar un algoritmo?**

A) Diagrama de flujo
B) Pseudocódigo
C) Lenguaje de programación
D) Base de datos relacional

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: D**

Los algoritmos se representan mediante diagramas de flujo (gráfico), pseudocódigo (lenguaje natural estructurado) o directamente en un lenguaje de programación. Una base de datos no es una forma de representar un algoritmo.

</details>

---

#### Pregunta 19

**¿Qué símbolo en un diagrama de flujo representa una decisión?**

A) Rectángulo
B) Rombo
C) Óvalo
D) Círculo

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

En los diagramas de flujo, el rombo (o diamante) representa una decisión, donde el flujo del programa se bifurca según una condición verdadera o falsa.

</details>

---

#### Pregunta 20

**¿Cuál es la salida del siguiente código?**

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

A) 0 0, 0 1, 1 0, 1 1, 2 0, 2 1
B) 0 0, 1 1, 2 2
C) 0 0, 0 1, 0 2, 1 0, 1 1, 1 2
D) Error

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

Es un bucle anidado. Para cada valor de i (0, 1, 2), el bucle interno recorre j (0, 1), imprimiendo todas las combinaciones.

</details>

---

#### Pregunta 21

**¿Qué hace la instrucción `break` en un bucle?**

A) Continúa con la siguiente iteración del bucle.
B) Termina la ejecución del bucle completamente.
C) Reinicia el bucle desde el principio.
D) Pausa la ejecución del bucle.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`break` termina el bucle más cercano en el que se encuentra. El flujo del programa continúa después del bucle.

</details>

---

#### Pregunta 22

**¿Cuál es el resultado de la siguiente expresión booleana?**

```python
(5 > 3) and (10 < 2)
```

A) True
B) False
C) None
D) Error

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`(5 > 3)` es True, `(10 < 2)` es False. Al ser un AND, True AND False = False.

</details>

---

#### Pregunta 23

**¿Qué hace el siguiente código utilizando list comprehension?**

```python
cuadrados = [x**2 for x in range(5)]
print(cuadrados)
```

A) [0, 1, 2, 3, 4]
B) [0, 1, 4, 9, 16]
C) [1, 4, 9, 16, 25]
D) [1, 2, 3, 4, 5]

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

La list comprehension eleva al cuadrado cada número en el rango 0-4: 0²=0, 1²=1, 2²=4, 3²=9, 4²=16.

</details>

---

#### Pregunta 24

**Dado el siguiente diagrama de flujo, ¿qué representan los símbolos?**

A) Inicio: Óvalo, Proceso: Rectángulo, Decisión: Rombo, Entrada/Salida: Paralelogramo
B) Inicio: Rectángulo, Proceso: Óvalo, Decisión: Rombo, Entrada/Salida: Rectángulo
C) Inicio: Círculo, Proceso: Rectángulo, Decisión: Cuadrado, Entrada/Salida: Rombo
D) Inicio: Óvalo, Proceso: Rombo, Decisión: Rectángulo, Entrada/Salida: Círculo

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

En diagramas de flujo: Óvalo = Inicio/Fin, Rectángulo = Proceso, Rombo = Decisión, Paralelogramo = Entrada/Salida de datos.

</details>

---

### Sub-módulo 4: Funciones y Modularización

---

#### Pregunta 25

**¿Cuál es la palabra reservada para definir una función en Python?**

A) function
B) def
C) define
D) func

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`def` es la palabra reservada en Python para definir funciones. Ejemplo: `def mi_funcion():`

</details>

---

#### Pregunta 26

**¿Qué es el principio DRY?**

A) **D**on't **R**epeat **Y**ourself - Evitar duplicar código.
B) **D**ata **R**eturn **Y**ield - Manera de retornar datos.
C) **D**ynamic **R**esponse **Y**ard - Sistema de respuesta dinámica.
D) **D**evelop **R**eusable **Y**ardsticks - Método de desarrollo.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

DRY (Don't Repeat Yourself) es un principio que busca evitar la redundancia de código. Si copias y pegas un código más de una vez, probablemente deberías crear una función.

</details>

---

#### Pregunta 27

**¿Qué imprime el siguiente código?**

```python
def sumar(a, b):
    resultado = a + b
    return resultado
    print("Suma realizada")

print(sumar(3, 4))
```

A) 7
B) 7 y "Suma realizada"
C) "Suma realizada" y 7
D) Error

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

El `return` termina la función antes de que se ejecute el `print("Suma realizada")`. La función retorna 7, que es lo que imprime el `print()` exterior.

</details>

---

#### Pregunta 28

**¿Qué diferencia hay entre un parámetro y un argumento?**

A) Son lo mismo, no hay diferencia.
B) Parámetro es el valor concreto que se pasa, argumento es la variable definida.
C) Parámetro es la variable definida en la función, argumento es el valor que se pasa.
D) Parámetro solo puede ser numérico, argumento puede ser cualquier tipo.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

El parámetro es la variable que se define en la declaración de la función. El argumento es el valor concreto que se pasa al invocar la función.

</details>

---

#### Pregunta 29

**¿Qué hace el siguiente código?**

```python
def operacion(*args):
    return sum(args)

print(operacion(1, 2, 3, 4))
```

A) Error porque *args no recibe múltiples argumentos.
B) 10
C) 24
D) [1, 2, 3, 4]

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`*args` permite pasar un número variable de argumentos posicionales. `sum(args)` suma todos ellos: 1+2+3+4 = 10.

</details>

---

#### Pregunta 30

**¿Cuál es la salida del siguiente código?**

```python
def saludar(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}"

print(saludar("Carlos"))
```

A) "Hola, Carlos"
B) ", Carlos"
C) Error - falta el argumento mensaje
D) "Carlos, Hola"

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

El parámetro `mensaje` tiene un valor por defecto ("Hola"), por lo que es opcional. Si no se proporciona, se usa el valor predeterminado.

</details>

---

#### Pregunta 31

**¿Qué son los docstrings y para qué sirven?**

A) Son comentarios que mejoran el rendimiento del código.
B) Son cadenas de documentación que explican la funcionalidad de funciones, clases y módulos.
C) Son variables especiales que almacenan documentación automática.
D) Son errores que se generan al no documentar el código.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Los docstrings son cadenas de texto que documentan el propósito, parámetros y retorno de funciones y módulos. Se escriben entre tres comillas al inicio de la función o módulo.

</details>

---

#### Pregunta 32

**¿Cuál es la forma correcta de importar una función específica de un módulo?**

A) `import modulo.funcion`
B) `from modulo import funcion`
C) `import funcion from modulo`
D) `import modulo as funcion`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

La sintaxis correcta es `from modulo import funcion`. Esto permite usar la función directamente sin el prefijo del módulo.

</details>

---

#### Pregunta 33

**¿Cuándo se ejecuta el bloque `if __name__ == '__main__':`?**

A) Siempre que se ejecuta el archivo.
B) Solo cuando el archivo se importa como módulo.
C) Solo cuando el archivo se ejecuta directamente, no cuando se importa.
D) Nunca se ejecuta.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

`__name__` es "__main__" cuando el archivo se ejecuta directamente. Cuando se importa, `__name__` toma el nombre del módulo. Esto permite tener código que se ejecute solo cuando el archivo es el programa principal.

</details>

---

#### Pregunta 34

**¿Qué hace el siguiente código de importación?**

```python
import math as m
print(m.sqrt(16))
```

A) Importa todo el módulo math y lo renombra como m, luego calcula la raíz cuadrada de 16.
B) Importa solo la función sqrt del módulo math.
C) Error porque no se pueden usar alias en importaciones.
D) Importa el módulo math pero no permite usar sus funciones.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

`import math as m` importa todo el módulo math y le asigna el alias "m". Luego se puede acceder a sus funciones usando el alias.

</details>

---

### Sub-módulo 5: Variables y Alcance

---

#### Pregunta 35

**¿Qué imprime el siguiente código?**

```python
x = 10

def modificar():
    x = 20
    return x

print(modificar())
print(x)
```

A) 20 y 10
B) 10 y 20
C) 20 y 20
D) Error

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

Dentro de la función, `x = 20` crea una variable local. La función retorna 20. Fuera, la variable global `x` mantiene su valor original (10).

</details>

---

#### Pregunta 36

**¿Cuál es la forma correcta de modificar una variable global dentro de una función?**

A) Usar `global variable` dentro de la función.
B) Usar `global variable` fuera de la función.
C) Modificar directamente la variable sin declaraciones especiales.
D) Usar `extern variable`.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

Para modificar una variable global dentro de una función, se debe usar la palabra clave `global` seguida del nombre de la variable dentro del cuerpo de la función.

</details>

---

#### Pregunta 37

**¿Por qué se considera una mala práctica usar variables globales?**

A) Porque siempre causan errores de sintaxis.
B) Porque pueden generar errores difíciles de depurar al modificar su valor desde diferentes partes del código.
C) Porque son más lentas que las variables locales.
D) Porque no se pueden usar dentro de funciones.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Las variables globales pueden modificar su valor desde cualquier parte del código, lo que dificulta el seguimiento del flujo de datos y puede causar errores difíciles de rastrear.

</details>

---

#### Pregunta 38

**¿Qué hace el siguiente código?**

```python
def multiplicar(factor):
    def interna(numero):
        return numero * factor
    return interna

doble = multiplicar(2)
print(doble(5))
```

A) Error por funciones anidadas.
B) 10
C) 7
D) 25

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Es un ejemplo de función que retorna otra función (cierre o closure). `multiplicar(2)` retorna una función que multiplica por 2. Al llamar `doble(5)`, se obtiene 10.

</details>

---

### Sub-módulo 6: Refactorización y Buenas Prácticas

---

#### Pregunta 39

**¿Qué es la refactorización de código?**

A) Reescribir completamente el código en otro lenguaje.
B) Abstraer código y generar funciones para aplicar el principio DRY.
C) Eliminar todas las funciones del código.
D) Agregar comentarios a todo el código.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

La refactorización consiste en reorganizar el código para mejorar su estructura, aplicando principios como DRY para evitar duplicación y hacer el código más mantenible.

</details>

---

#### Pregunta 40

**¿Qué estilo de docstring es reconocido como texto enriquecido en editores como VS Code y es popular en Ciencia de Datos?**

A) Docblockr Style
B) NumPy Style
C) Sphinx Style
D) Google Style

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

El estilo NumPy es utilizado por la librería de Computación Científica y es reconocido como texto enriquecido en editores como VS Code, lo que permite una documentación más elegante y visual.

</details>

---

#### Pregunta 41

**¿Qué hace el siguiente código?**

```python
import sys
import os

clear = 'cls' if sys.platform == 'win32' else 'clear'
os.system(clear)
```

A) Crea una nueva ventana de terminal.
B) Limpia la pantalla de la terminal de forma multiplataforma.
C) Muestra información del sistema operativo.
D) Error porque os.system no recibe strings.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

El código detecta el sistema operativo usando `sys.platform` y ejecuta el comando apropiado para limpiar la pantalla: 'cls' en Windows, 'clear' en macOS/Linux.

</details>


### Preguntas Adicionales (del Plan Formativo)

---

#### Pregunta 43

**¿Qué representa el símbolo de paralelogramo en un diagrama de flujo?**

A) Inicio del programa.
B) Decisión.
C) Entrada o salida de datos.
D) Proceso.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

El paralelogramo representa operaciones de entrada (lectura de datos) o salida (presentación de resultados) en un diagrama de flujo.

</details>

---

#### Pregunta 44

**¿Qué es PSEINT según el material del curso?**

A) Un lenguaje de programación compilado.
B) Una herramienta para escribir y ejecutar pseudocódigo.
C) Un entorno de desarrollo para Python.
D) Un framework para desarrollo web.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

PSEINT es una herramienta educativa que permite escribir pseudocódigo y ejecutarlo, facilitando el aprendizaje de algoritmos sin preocuparse por la sintaxis de un lenguaje específico.

</details>

---

#### Pregunta 45

**¿Cuál es la salida del siguiente código?**

```python
def es_par(numero):
    return numero % 2 == 0

numeros = [1, 2, 3, 4, 5]
pares = [n for n in numeros if es_par(n)]
print(pares)
```

A) [1, 3, 5]
B) [2, 4]
C) [1, 2, 3, 4, 5]
D) Error

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

La list comprehension filtra los números pares usando la función `es_par()`. Solo los números que cumplen la condición (2 y 4) se incluyen en la nueva lista.

</details>

---

#### Pregunta 46

**¿Qué hace la función `time.sleep()` en Python?**

A) Detiene completamente la ejecución del programa.
B) Pausa la ejecución del programa durante el número de segundos especificado.
C) Acelera la ejecución del programa.
D) Mide el tiempo de ejecución del programa.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`time.sleep(segundos)` pausa la ejecución del programa durante la cantidad de segundos especificada, mejorando la experiencia de usuario en aplicaciones de consola.

</details>

---

#### Pregunta 47

**¿Qué tipo de datos se utiliza para almacenar valores lógicos (verdadero/falso) en Python?**

A) int
B) str
C) bool
D) float

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

El tipo `bool` en Python representa valores booleanos: `True` (Verdadero) y `False` (Falso). Son utilizados en expresiones lógicas y control de flujo.

</details>

---

#### Pregunta 48

**¿Qué imprime el siguiente código?**

```python
texto = "Hola Mundo"
print(texto.count('o'))
print(texto.upper())
```

A) 2 y "HOLA MUNDO"
B) 2 y "hola mundo"
C) 1 y "HOLA MUNDO"
D) Error

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

`count('o')` cuenta las veces que aparece 'o' en el string (2 veces). `upper()` convierte todo el string a mayúsculas.

</details>

---

#### Pregunta 49

**¿Cuál es la diferencia entre `=` y `==` en Python?**

A) `=` es comparación, `==` es asignación.
B) `=` es asignación, `==` es comparación.
C) Ambos son para comparación.
D) Ambos son para asignación.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`=` es el operador de asignación (asigna un valor a una variable). `==` es el operador de comparación (verifica si dos valores son iguales).

</details>

---

#### Pregunta 50

**¿Qué hace el siguiente código?**

```python
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000
}

def filtrar(diccionario, umbral):
    return {k: v for k, v in diccionario.items() if v > umbral}

resultado = filtrar(precios, 50000)
print(resultado)
```

A) {'Notebook': 700000, 'Monitor': 250000}
B) {'Notebook': 700000, 'Teclado': 25000, 'Mouse': 12000, 'Monitor': 250000}
C) {'Teclado': 25000, 'Mouse': 12000}
D) Error

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

La función filtra los elementos del diccionario cuyo valor es mayor al umbral (50000). Solo 'Notebook' (700000) y 'Monitor' (250000) superan el umbral.

</details>

---

#### Pregunta 51

**¿Cuál es el propósito de la modularización en Python?**

A) Hacer el código más rápido.
B) Organizar el código en módulos separados para mejorar la reutilización y el trabajo en equipo.
C) Eliminar todos los comentarios del código.
D) Convertir el código a otro lenguaje de programación.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

La modularización permite organizar el código en módulos independientes, facilitando la reutilización, el trabajo en equipo, la escalabilidad y el mantenimiento del proyecto.

</details>

---

#### Pregunta 52

**¿Qué hace la función `exit()` en Python?**

A) Pausa la ejecución del programa.
B) Finaliza la ejecución del programa.
C) Reinicia el programa.
D) Muestra un mensaje de error.

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`exit()` termina la ejecución del programa de forma inmediata, útil para salir de un programa cuando se ha cumplido una condición.

</details>

---

#### Pregunta 53

**¿Cuál es el orden correcto de los parámetros en la definición de una función?**

A) Opcionales → Obligatorios → *args → **kwargs
B) Obligatorios → Opcionales → *args → **kwargs
C) *args → Obligatorios → Opcionales → **kwargs
D) Obligatorios → *args → Opcionales → **kwargs

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

El orden correcto es: parámetros obligatorios, luego parámetros opcionales (con valor por defecto), luego *args y finalmente **kwargs.

</details>

---

#### Pregunta 54

**¿Qué imprime el siguiente código?**

```python
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)
```

A) [1, 2, 3, 4, 5]
B) [5, 4, 3, 2, 1]
C) Error
D) [5, 4, 3, 2, 1, 0]

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`reverse()` invierte el orden de los elementos de la lista in-place, es decir, modifica la lista original.

</details>

---

#### Pregunta 55

**¿Cuál es el resultado de la siguiente operación?**

```python
15 // 4
```

A) 3.75
B) 3
C) 4
D) 15

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`//` es el operador de división entera. 15 dividido por 4 es 3 con resto 3, por lo que el resultado es 3 (la parte entera de la división).

</details>
