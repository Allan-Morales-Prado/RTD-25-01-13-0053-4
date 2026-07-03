# Funciones y variables (parte II)

## Preguntas de Opción Múltiple

---

### Pregunta 1

**¿Cuál es la diferencia principal entre `*args` y `**kwargs` en Python?**

A) `*args` se usa para argumentos con nombre y `**kwargs` para argumentos posicionales
B) `*args` recibe una tupla de argumentos posicionales y `**kwargs` recibe un diccionario de argumentos con nombre
C) `*args` solo funciona con números y `**kwargs` solo con strings
D) No hay diferencia, son intercambiables

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

`*args` recibe una tupla de argumentos posicionales variables, mientras que `**kwargs` recibe un diccionario de argumentos con nombre (clave-valor). Esto permite flexibilidad al definir funciones que aceptan un número variable de argumentos.
</details>

---

### Pregunta 2

**¿Qué sucede si se pasa una función como argumento sin paréntesis?**

```python
def saludar():
    return "Hola"

def ejecutar(funcion):
    return funcion()

resultado = ejecutar(saludar)
```

A) Se ejecuta la función inmediatamente al pasarla como argumento
B) Se pasa la referencia a la función, permitiendo ejecutarla dentro de la otra función
C) Se produce un error de sintaxis
D) Se pasa el resultado de ejecutar la función

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Al pasar `saludar` sin paréntesis, se pasa la **referencia** a la función, no su resultado. Esto permite que la función receptora (en este caso `ejecutar`) decida cuándo llamarla, añadiendo flexibilidad al código.
</details>

---

### Pregunta 3

**¿Qué imprime el siguiente código?**

```python
x = 10

def modificar():
    x = 20
    print(x)

modificar()
print(x)
```

A) 10 y 20
B) 20 y 10
C) 20 y 20
D) Error, no se puede modificar una variable global

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Dentro de la función, `x = 20` crea una **variable local** que solo existe dentro de la función (imprime 20). Fuera de la función, la variable global `x` mantiene su valor original (10). Esto demuestra el alcance local de las variables dentro de funciones.
</details>

---

### Pregunta 4

**¿Cuál es la forma correcta de modificar una variable global dentro de una función?**

A) `global nombre_variable` dentro de la función
B) `global nombre_variable` fuera de la función
C) `nombre_variable = nuevo_valor` directamente
D) `return nombre_variable` y asignar fuera

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

Para modificar una variable global dentro de una función, se debe usar la palabra clave `global` seguida del nombre de la variable dentro del cuerpo de la función. Sin `global`, Python crea una nueva variable local.

**Nota**: Aunque es posible, esta práctica no es recomendada ya que puede llevar a errores difíciles de depurar.
</details>

---

### Pregunta 5

**¿Qué caracteriza a un parámetro opcional o por defecto?**

A) Siempre debe ser el primer parámetro en la definición
B) Tiene un valor predeterminado que se usa si no se proporciona un argumento
C) Solo puede ser de tipo booleano
D) No se puede modificar su valor después de definido

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Los parámetros opcionales tienen un valor por defecto definido en la firma de la función (`redondear=False` en el ejemplo). Si el usuario no proporciona un valor para ese parámetro al llamar la función, se usará el valor predeterminado.

**Tip**: Los parámetros opcionales siempre deben definirse **después** de los parámetros obligatorios.
</details>

---

### Pregunta 6

**¿Qué resultado produce la siguiente función?**

```python
def crear_diccionario(**datos):
    return datos

resultado = crear_diccionario(nombre="Ana", ciudad="Madrid", edad=30)
print(resultado)
```

A) `{'nombre': 'Ana', 'ciudad': 'Madrid', 'edad': 30}`
B) `['Ana', 'Madrid', 30]`
C) `('Ana', 'Madrid', 30)`
D) Error, la función no puede recibir parámetros con nombre

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

`**kwargs` (en este caso renombrado a `**datos`) captura todos los argumentos con nombre y los convierte en un diccionario. En el ejemplo, los tres argumentos con nombre se transforman en un diccionario con sus respectivas claves y valores.
</details>

---

### Pregunta 7

**En el ejercicio de Loto, ¿por qué es necesario usar `global pool` dentro de la función `sacar_numero`?**

```python
pool = [1, 2, 3, ..., 41]

def sacar_numero(posicion):
    global pool
    elegido = random.choice(pool)
    pool.remove(elegido)
```

A) Para que la variable `pool` sea accesible dentro de la función
B) Para modificar la lista `pool` que está definida fuera de la función
C) Para crear una nueva lista local con el mismo nombre
D) No es necesario; se puede modificar sin `global`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Aunque las listas son mutables y se pueden modificar sin `global` usando métodos como `.remove()`, se usa `global` para **reasignar** la variable. Sin `global`, Python interpretaría `pool =` como una nueva variable local. En este caso particular, el código usa `pool.remove()` que no reasigna, por lo que técnicamente no necesitaría `global`; sin embargo, se incluye para claridad y consistencia.
</details>

---

### Pregunta 8

**¿Qué sucede si se llama a esta función sin el segundo argumento?**

```python
def saludar(nombre, mensaje="Hola"):
    return f"{mensaje}, {nombre}"

print(saludar("Carlos"))
```

A) Error, faltan argumentos
B) Imprime `"Hola, Carlos"`
C) Imprime `", Carlos"`
D) Error de sintaxis

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

El parámetro `mensaje` tiene un valor por defecto (`"Hola"`), por lo que es opcional. Cuando se llama con un solo argumento, se usa el valor predeterminado, resultando en `"Hola, Carlos"`.
</details>

---

### Pregunta 9

**¿Cuál es el orden correcto de los parámetros en la definición de una función?**

A) Opcionales → Obligatorios → `*args` → `**kwargs`
B) Obligatorios → Opcionales → `*args` → `**kwargs`
C) `*args` → Obligatorios → Opcionales → `**kwargs`
D) Obligatorios → `*args` → Opcionales → `**kwargs`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

El orden correcto es:
1. Parámetros obligatorios
2. Parámetros opcionales (con valor por defecto)
3. `*args` (argumentos posicionales variables)
4. `**kwargs` (argumentos con nombre variables)

Este orden es obligatorio para que Python pueda interpretar correctamente los argumentos.
</details>

---

### Pregunta 10

**¿Cuál(es) invocaciones son válidas e inválidas en el siguiente código?**

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# Siguientes líneas de código:
parrot()                                    # 1
parrot(1000)                                # 2
parrot(voltage=1000)                        # 3
parrot(110, voltage=220)                    # 4
parrot(actor='John Cleese')                 # 5
parrot(voltage=5.0, 'dead')                 # 6
parrot(voltage=1000000, action='VOOOOOM')   # 7
parrot(action='VOOOOOM', voltage=1000000)   # 8
parrot('a million', 'bereft of life', 'jump') # 9
parrot('a thousand', state='pushing up the daisies') # 10
```

**Alternativas:**

A) Válidas: 2, 3, 7, 8, 9, 10 — Inválidas: 1, 4, 5, 6
B) Válidas: 2, 3, 7, 8, 9 — Inválidas: 1, 4, 5, 6, 10
C) Válidas: 1, 2, 3, 7, 8, 9, 10 — Inválidas: 4, 5, 6
D) Válidas: 2, 3, 7, 8, 10 — Inválidas: 1, 4, 5, 6, 9

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

- **Llamada 1** ❌: Falta `voltage` (obligatorio)
- **Llamada 2** ✅: `1000` → `voltage` por posición
- **Llamada 3** ✅: `voltage=1000` por nombre
- **Llamada 4** ❌: `voltage` recibe dos valores (`110` y `voltage=220`)
- **Llamada 5** ❌: `actor` no es parámetro válido + falta `voltage`
- **Llamada 6** ❌: Argumento posicional (`'dead'`) después de uno con nombre (`voltage=5.0`)
- **Llamada 7** ✅: Argumentos con nombre válidos
- **Llamada 8** ✅: Orden de argumentos con nombre no importa
- **Llamada 9** ✅: Tres argumentos posicionales (`voltage`, `state`, `action`)
- **Llamada 10** ✅: Posicional + con nombre (`state`)
</details>

---
### Pregunta 11

**¿Por qué se consideran las variables globales una mala práctica en programación?**

A) Porque siempre causan errores de sintaxis
B) Porque pueden generar errores difíciles de depurar al modificar su valor desde diferentes partes del código
C) Porque son más lentas que las variables locales
D) Porque no se pueden usar dentro de funciones

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Las variables globales pueden llevar a errores difíciles de rastrear porque:
- Su valor puede modificarse desde cualquier parte del código
- Pueden causar conflictos de nombres con librerías externas
- Dificultan el seguimiento del flujo de datos

La alternativa recomendada es usar `return` para devolver valores de las funciones y mantener un flujo de datos controlado.
</details>

---

### Pregunta 12

**¿Qué imprimirá el siguiente código al ser ejecutado?**

```python
def agregar_elemento(elemento, lista=[]):
    lista.append(elemento)
    return lista

def agregar_elemento_seguro(elemento, lista=None):
    if lista is None:
        lista = []
    lista.append(elemento)
    return lista

# Bloque 1
print(agregar_elemento(1))
print(agregar_elemento(2))
print(agregar_elemento(3))

# Bloque 2
print(agregar_elemento_seguro(1))
print(agregar_elemento_seguro(2))
print(agregar_elemento_seguro(3))
```

**Alternativas:**

A) Bloque 1: `[1]` `[2]` `[3]` — Bloque 2: `[1]` `[2]` `[3]`
B) Bloque 1: `[1]` `[1, 2]` `[1, 2, 3]` — Bloque 2: `[1]` `[2]` `[3]`
C) Bloque 1: `[1]` `[1, 2]` `[1, 2, 3]` — Bloque 2: `[1]` `[1, 2]` `[1, 2, 3]`
D) Bloque 1: `[1]` `[2]` `[3]` — Bloque 2: `[1]` `[1, 2]` `[1, 2, 3]`

<details> 
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

**Bloque 1 (`agregar_elemento`):**
- El valor por defecto `[]` se evalúa una sola vez al definir la función.
- Todas las llamadas comparten la misma lista.
- Resultado: `[1]` → `[1, 2]` → `[1, 2, 3]`

**Bloque 2 (`agregar_elemento_seguro`):**
- None es inmutable; cada llamada sin argumento crea una nueva lista.
- Resultado: `[1]` → `[2]` → `[3]`

Conclusión: Usar None como valor por defecto y crear una nueva lista dentro de la función evita el problema de compartir objetos mutables.

</details>

---

### Pregunta 13 (Reflexión)

**¿Qué ventaja tiene pasar una función como argumento en lugar de llamarla directamente?**

A) No hay ventaja, es solo una cuestión de estilo
B) Permite crear funciones más flexibles y reutilizables (programación funcional)
C) Hace el código más rápido
D) Permite usar funciones sin importarlas

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Pasar funciones como argumentos permite crear **funciones de orden superior** que pueden adaptar su comportamiento según la función que reciban. Esto es un pilar de la programación funcional y permite escribir código más flexible, reusable y modular.

**Ejemplo de uso**: Funciones como `map()`, `filter()` y `sorted()` en Python, que aceptan funciones como argumentos para personalizar su comportamiento.
</details>

---

### Pregunta 14
**Dada la siguiente definición de función, ¿cuál(es) de las llamadas son válidas?**

```python
def procesar_datos(nombre, /, edad, *, ciudad, pais="Chile"):
    print(f"{nombre}, {edad} años, de {ciudad}, {pais}")
```

**Llamadas:**
```python
procesar_datos("Ana", 30, ciudad="Santiago")
procesar_datos(nombre="Luis", edad=25, ciudad="Valparaíso")
procesar_datos("Carlos", edad=40, ciudad="Concepción", pais="Argentina")
procesar_datos("María", 35, "Viña del Mar")
procesar_datos("Pedro", 28, ciudad="Antofagasta", pais="Chile", extra="dato")
procesar_datos(edad=22, nombre="Sofía", ciudad="Temuco")
```

**Alternativas:**

A) Válidas: 1, 3 — Inválidas: 2, 4, 5, 6
B) Válidas: 1, 2, 3 — Inválidas: 4, 5, 6
C) Válidas: 1, 3, 6 — Inválidas: 2, 4, 5
D) Válidas: 1, 3, 4 — Inválidas: 2, 5, 6

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

**Desglose de parámetros:**
- `nombre`: **Solo posicional** (`/`) → debe pasarse por posición
- `edad`: Posicional o con nombre
- `ciudad`: **Solo con nombre** (`*`) → debe pasarse con `ciudad=valor`
- `pais`: **Solo con nombre** (`*`) → debe pasarse con `pais=valor` (opcional)

**Análisis:**
- **Llamada 1** ✅: `"Ana"` → `nombre` (posicional), `30` → `edad`, `ciudad="Santiago"` (con nombre)
- **Llamada 2** ❌: `nombre="Luis"` (con nombre) pero `nombre` es solo posicional
- **Llamada 3** ✅: `"Carlos"` → `nombre`, `edad=40`, `ciudad="Concepción"`, `pais="Argentina"`
- **Llamada 4** ❌: `"Viña del Mar"` intenta asignarse a `ciudad` por posición, pero `ciudad` es solo con nombre
- **Llamada 5** ❌: `extra="dato"` no es un parámetro válido
- **Llamada 6** ❌: `nombre="Sofía"` (con nombre) pero `nombre` es solo posicional

**Regla clave:** Los parámetros antes de `/` son **solo posicionales**; los parámetros después de `*` son **solo con nombre**.
</details>