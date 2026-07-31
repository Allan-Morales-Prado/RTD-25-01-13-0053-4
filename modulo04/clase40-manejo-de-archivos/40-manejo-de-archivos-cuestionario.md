# Cuestionario: Manejo de archivos y excepciones en Python

## Pregunta 1

**¿Qué ocurre cuando se intenta escribir en un archivo abierto en modo `'r'` (lectura) en Python?**

A) El archivo se convierte automáticamente al modo escritura
B) Se genera una excepción de tipo `UnsupportedOperation`
C) El contenido se escribe al final del archivo sin sobrescribir
D) Se genera una excepción de tipo `FileNotFoundError`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

**Justificación:** El modo `'r'` (lectura) solo permite acceder al contenido de un archivo existente sin posibilidad de modificarlo. Al intentar utilizar métodos de escritura, Python lanza una excepción `UnsupportedOperation` indicando que la operación no está soportada para ese modo de apertura.
</details>

---

## Pregunta 2

**¿Cuál es la salida del siguiente código?**

```python
with open("datos.txt", "w") as archivo:
    archivo.write("Hola\nMundo\nPython\n")

with open("datos.txt", "r") as archivo:
    linea = archivo.readline()
    print(linea, end="")
    archivo.seek(0)
    print(archivo.read(8))
```

Considerando que el archivo "datos.txt" no existía previamente.

A) `HolaMundo` (sin salto de línea)
B) `Hola` y luego `Hola\nMun`
C) `Hola` y luego `Hola\nMun`
D) `Hola\nMundo\nPython` (completo)

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

**Justificación:** 
1. Primero, `readline()` lee la primera línea "Hola\n" y se imprime como "Hola" (sin salto adicional por `end=""`)
2. Luego, `seek(0)` reposiciona el puntero al inicio del archivo
3. Finalmente, `read(8)` lee los primeros 8 bytes: "Hola\nMun"
4. Por lo tanto, la salida es: `Hola` y luego `Hola\nMun` (con el \n mostrado como salto de línea)
</details>

---

## Pregunta 3

**Se desea leer un archivo CSV que contiene datos de estudiantes y almacenarlos en una lista de diccionarios. ¿Cuál de los siguientes bloques de código logra correctamente este objetivo?**

Archivo `estudiantes.csv`:
```
nombre,edad,curso
Ana,20,Matemáticas
Luis,22,Física
```

A) 
```python
lista_estudiantes = []
with open("estudiantes.csv", "r") as file:
    for linea in file.readlines():
        datos = linea.strip().split(",")
        lista_estudiantes.append({
            "nombre": datos[0],
            "edad": int(datos[1]) if datos[1] != "edad" else datos[1],
            "curso": datos[2]
        })
```

B) 
```python
lista_estudiantes = []
with open("estudiantes.csv", "r") as file:
    for linea in file:
        if not linea.startswith("nombre"):
            datos = linea.strip().split(",")
            lista_estudiantes.append({
                "nombre": datos[0],
                "edad": int(datos[1]),
                "curso": datos[2]
            })
```

C) 
```python
lista_estudiantes = []
with open("estudiantes.csv", "r") as file:
    for linea in file.read().splitlines():
        datos = linea.split(",")
        if datos[0] != "nombre":
            lista_estudiantes.append(dict(zip(["nombre","edad","curso"], datos)))
```

D) Todas las anteriores

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: D**

**Justificación:** Todos los bloques de código logran el objetivo correctamente:
- A: Omite correctamente la cabecera al comparar si el primer dato es "edad", y convierte edad a int
- B: Omite correctamente la cabecera verificando que la línea no comience con "nombre"
- C: Omite correctamente la cabecera y usa `zip` para crear los diccionarios
</details>

---

## Pregunta 4

**¿Qué método permite reposicionar el puntero de lectura/escritura dentro de un archivo abierto en Python?**

A) `reposition()`
B) `move()`
C) `seek()`
D) `set_position()`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

**Justificación:** El método `seek()` es el método incorporado de Python que permite reposicionar el puntero dentro de un archivo abierto. Recibe como argumento la posición (en bytes) donde se desea posicionar. Por ejemplo, `seek(0)` reposiciona al inicio del archivo, mientras que `seek(0, 2)` mueve al final.
</details>

---

## Pregunta 5

**¿Cuál es la forma correcta de abrir un archivo en modo binario para lectura y escritura, asegurando que se cree si no existe?**

A) `archivo = open("datos.bin", "r+b")`
B) `archivo = open("datos.bin", "w+b")`
C) `archivo = open("datos.bin", "a+b")`
D) `archivo = open("datos.bin", "x+b")`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

**Justificación:** El modo `'w+b'` abre el archivo en modo binario para lectura y escritura. Si el archivo no existe, lo crea. Si existe, trunca (borra) su contenido. La opción `'r+b'` no lo crea si no existe, y `'a+b'` solo permite escritura al final del archivo aunque también permita lectura.
</details>

---

## Pregunta 6

**¿Cuál será la salida del siguiente programa?**

```python
import os

ruta = os.path.join("carpeta", "archivo.txt")
if not os.path.exists(os.path.dirname(ruta)):
    print("A", end="")
else:
    print("B", end="")

try:
    with open(ruta, "r") as f:
        print("C", end="")
except FileNotFoundError:
    print("D", end="")
```

Asumiendo que la carpeta "carpeta" NO existe en el sistema.

A) A D
B) B D
C) A C
D) B C

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

**Justificación:** 
1. `os.path.dirname(ruta)` devuelve "carpeta"
2. Como "carpeta" no existe, `os.path.exists()` es `False`, por lo que se imprime "A"
3. Al intentar abrir el archivo para lectura, como la carpeta no existe, se lanza `FileNotFoundError`
4. El bloque `except` captura la excepción e imprime "D"
5. Salida final: "A D"
</details>

---

## Pregunta 7

**¿Cuál de las siguientes afirmaciones sobre el context manager `with` en el manejo de archivos es FALSA?**

A) El archivo se cierra automáticamente al salir del bloque `with`
B) Puede manejar múltiples archivos en una sola línea `with open('a.txt') as f1, open('b.txt') as f2:`
C) La excepción `UnsupportedOperation` no ocurre si usamos `with`
D) El archivo se cierra aunque ocurra una excepción dentro del bloque `with`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

**Justificación:** El uso de `with` no previene excepciones como `UnsupportedOperation`. Si se intenta una operación no soportada (como escribir en modo lectura) dentro de un bloque `with`, se lanzará la excepción igualmente. La ventaja del context manager es asegurar que el archivo se cierre correctamente, no que se eviten excepciones de operaciones inválidas.
</details>

---

## Pregunta 8

**Se necesita un programa que procese un archivo de logs y extraiga solo las líneas que contienen la palabra "ERROR". ¿Cuál de los siguientes códigos logra este objetivo de manera eficiente para archivos grandes?**

A) 
```python
with open("logs.txt", "r") as f:
    contenido = f.read()
lineas_error = [linea for linea in contenido.split("\n") if "ERROR" in linea]
```

B) 
```python
with open("logs.txt", "r") as f:
    lineas_error = []
    for linea in f:
        if "ERROR" in linea:
            lineas_error.append(linea)
```

C) 
```python
lineas_error = []
with open("logs.txt", "r") as f:
    while True:
        linea = f.readline()
        if not linea:
            break
        if "ERROR" in linea:
            lineas_error.append(linea)
```

D) B y C son correctas

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: D**

**Justificación:** Tanto B como C son correctas y eficientes para archivos grandes porque:
- Ambos leen línea por línea, evitando cargar todo el archivo en memoria
- La opción A carga todo el archivo en memoria con `read()`, lo cual es ineficiente para archivos grandes
- B usa iteración directa sobre el objeto archivo, que es la forma más idiomática en Python
- C también es correcta pero más verbosa, usando `readline()` en un bucle
</details>

---

## Pregunta 9

**Dado el siguiente código incompleto, ¿qué línea completa correctamente el programa para escribir un registro con timestamp?**

```python
from datetime import datetime

def registrar_error(mensaje_error):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Línea para completar aquí
```

Archivo: "errores.log", debe mantener el historial (agregar al final).

A) `with open("errores.log", "w") as f: f.write(f"[{timestamp}] {mensaje_error}\n")`
B) `with open("errores.log", "a") as f: f.write(f"[{timestamp}] {mensaje_error}\n")`
C) `with open("errores.log", "r+") as f: f.write(f"[{timestamp}] {mensaje_error}\n")`
D) `with open("errores.log", "x") as f: f.write(f"[{timestamp}] {mensaje_error}\n")`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

**Justificación:** Para mantener el historial (agregar al final sin borrar contenido previo), se debe usar el modo `'a'` (append). Este modo abre el archivo para escritura posicionando el puntero al final, creando el archivo si no existe. El modo `'w'` sobrescribiría todo el contenido previo, `'r+'` requiere que el archivo exista y sobrescribe desde el inicio, y `'x'` falla si el archivo ya existe.
</details>

---

## Pregunta 10

**¿Cuál es la diferencia entre los métodos `read()` y `readlines()` al leer archivos en Python?**

A) `read()` retorna un string, `readlines()` retorna una lista de strings
B) `read()` lee todo el archivo, `readlines()` solo lee la primera línea
C) `read()` solo funciona con archivos binarios, `readlines()` solo con archivos de texto
D) `read()` retorna bytes, `readlines()` retorna strings

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: A**

**Justificación:** `read()` retorna todo el contenido del archivo como un único string (o bytes si está en modo binario), mientras que `readlines()` retorna una lista de strings donde cada elemento es una línea del archivo. Ambos métodos pueden leer archivos de texto, y `read()` también puede leer archivos binarios.
</details>

---

## Pregunta 11

**¿Cuál será la salida del siguiente código?**

```python
with open("test.txt", "w") as f:
    f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

with open("test.txt", "r") as f:
    print(f.read(5))
    print(f.tell())
```

A) `ABCDE` seguido de `10`
B) `ABCDE` seguido de `5`
C) `ABCDEFGHIJ` seguido de `10`
D) `ABC` seguido de `3`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

**Justificación:** 
1. `read(5)` lee los primeros 5 caracteres del archivo: "ABCDE"
2. `tell()` devuelve la posición actual del puntero en el archivo, que después de leer 5 bytes está en la posición 5
3. Por lo tanto, la salida es: "ABCDE" seguido de 5 en la siguiente línea
</details>

---

## Pregunta 12

**¿Cuál es la mejor práctica para manejar archivos cuando se necesita realizar múltiples operaciones de lectura y escritura que podrían generar excepciones?**

A) Usar un solo bloque try-except alrededor de todas las operaciones
B) Abrir el archivo en modo `'r+'` y usar finally para cerrarlo
C) Usar el context manager `with` en el bloque que contiene todas las operaciones
D) No es necesario manejar excepciones, Python las maneja automáticamente

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

**Justificación:** La mejor práctica es usar el context manager `with` que encapsula todas las operaciones en un bloque. Esto garantiza que:
- El archivo se cierre automáticamente al salir del bloque (sea por éxito o por excepción)
- El código es más legible y conciso
- Se pueden usar múltiples archivos en el mismo bloque si es necesario
- Las excepciones específicas pueden manejarse dentro o fuera del bloque según se requiera
</details>