# Manejo de errores y archivos en Python

## Índice de contenidos
1. [¿Por qué manejar archivos?](#por-qué-manejar-archivos)
2. [FileDescriptor](#filedescriptor)
3. [Función open](#función-open)
4. [Modos de apertura](#modos-de-apertura)
5. [Buenas prácticas](#buenas-prácticas)
6. [Ejercicio guiado](#ejercicio-guiado)
7. [Preguntas de repaso](#preguntas-de-repaso)

---

## ¿Por qué manejar archivos?

Los archivos constituyen una **fuente importante de entrada de datos**, para resolver distintos problemas y algoritmos.

### Ejemplos de uso:

- **Ciencia de datos:** Lectura de archivos CSV como fuente de datos de análisis.
- **Desarrollo web:** Manejo de archivos multimedia (fotos, videos, documentos, etc.) que requieren ser manejados como bytes en lugar de texto.
- **Registro de logs:** Salida de datos a un archivo para el historial de una aplicación.

---

## FileDescriptor

Recurso que permite manipular archivos, resolviendo operaciones de bajo nivel en el sistema operativo que permiten acciones de entrada y salida.

### Características:

- Se representa por un número entero positivo.
- En Python normalmente se instancia como una variable de nombre `fd`.
- Se requiere hacer uso del método `open` del módulo `os`.
- La instancia `fd` es utilizada como argumento de los distintos métodos dentro del módulo `os` que permiten la manipulación del archivo (lectura, escritura y cierre).

>[!NOTE]
> El uso de un descriptor de archivo está sugerido para acciones de bajo nivel de entrada y salida. Para uso normal, se sugiere utilizar la función nativa de Python `open`, que retorna un objeto de tipo `file`.

---

## Función `open`

El primer paso para manipular un archivo en Python (leer, crear o modificar) es **abrirlo**.

### Sintaxis básica:

```python
import os
log_file = open(os.path.abspath("logs/error.log"))
```

### Argumentos:

| Argumento | Descripción |
|-----------|-------------|
| **Primer argumento** | Ruta donde se encuentra (o donde se desea crear) el archivo, o un int correspondiente a un descriptor de archivo. Puede ser absoluta o relativa. |
| **Segundo argumento** | Modo de apertura (opcional). Por defecto: solo lectura (`'r'`). |

### Retorno:

La función `open` retorna un objeto de tipo `file`, por defecto como archivo de texto.

>[!IMPORTANT]
> En caso de que el archivo no se haya podido abrir, se lanzará una **excepción**.

---

## Modos de apertura

### Modo de solo lectura (`'r'`)

Solo se puede acceder al contenido de un archivo existente, sin posibilidad de modificarlo.

```python
# modo lectura (por defecto)
archivo = open("ejemplo.txt")

# modo lectura, especificado por el segundo argumento 'r'
historial = open("log.txt", 'r')
```

**Comportamiento:**
- Si la ruta no existe → `FileNotFoundError`
- Si se intenta escribir → `UnsupportedOperation`

#### Leer archivo completo:

```python
pagina = open("index.html")
contenido = pagina.read()
```

#### Leer línea por línea:

```python
pagina = open("index.html")
lineas = pagina.readlines()
```

#### Iterar sobre líneas:

```python
with open("index.html", "r") as archivo:
    for linea in archivo:
        print(linea.strip())
```

#### Cerrar un archivo:

```python
archivo = open("index.html")
archivo.close()
```

---

### Modo de solo escritura (`'w'`)

Permite escribir datos en el archivo.

```python
# Si el archivo no existe, será creado sin contenido
# Si el archivo existe, se eliminará su contenido
archivo = open("nuevo_log.log", 'w')
```

**Comportamiento:**
- Si el archivo no existe → se crea
- Si el archivo existe → su contenido se elimina
- No se puede leer → `UnsupportedOperation`

#### Escribir en un archivo:

```python
import time

try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open(f"{round(time.time())}.log", "w") as log:
        log.write(f"ERROR: {e}")
```

#### Renombrar un archivo:

```python
import os
antiguo = os.path.join("logs", "error.txt")
nuevo = os.path.join("logs", "error.log")
os.rename(antiguo, nuevo)
```

---

### Modo de escritura y lectura (`'r+'`)

Permite tanto lectura como escritura, eliminando primero el contenido del archivo abierto.

```python
try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open("ultimo_error.log", "r+") as log:
        log.write(f"ERROR: {e}")
```

**Comportamiento:**
- Permite lectura y escritura
- Si el archivo no existe → `FileNotFoundError`

---

### Modo Append (`'a'` y `'a+'`)

Permite abrir un archivo en modo de escritura donde el nuevo contenido se agrega al final.

```python
from datetime import datetime

try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open("error.log", "a+") as log:
        log.seek(0)
        print(log.read())
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log.seek(0)
        print(log.read())
```

**Características:**
- `'a'`: Solo escritura al final
- `'a+'`: Lectura y escritura al final
- Si el archivo no existe → se crea
- Al abrir, apunta "al final del documento"

---

### Lectura de bytes

```python
with open("error.log") as log:
    log.seek(10)
    print(log.read(10))
```

#### Leer por chunks:

```python
chunk_size = 70
with open("comprobante_de_pago.pdf", "rb") as archivo:
    chunk = archivo.read(chunk_size)
    while chunk:
        print(chunk)
        chunk = archivo.read(chunk_size)
```

**Características:**
- `'b'`: Modo binario
- `read(n)`: Lee `n` bytes
- La posición de lectura avanza automáticamente

---

## Resumen de modos de apertura

| Modo | Descripción | Crear si no existe | Trunca contenido |
|------|-------------|-------------------|------------------|
| `'r'` | Lectura | ❌ | ❌ |
| `'w'` | Escritura | ✅ | ✅ |
| `'a'` | Append | ✅ | ❌ |
| `'r+'` | Lectura/Escritura | ❌ | ✅ |
| `'a+'` | Append/Lectura | ✅ | ❌ |
| `'rb'` | Lectura binaria | ❌ | ❌ |

---

## Buenas prácticas en el manejo de archivos

### Recomendaciones:

1. **Siempre abrir archivos utilizando el context manager `with`**

   ```python
   with open("archivo.txt", "r") as archivo:
       contenido = archivo.read()
   # El archivo se cierra automáticamente al salir del bloque
   ```

2. **Alternativa: usar `try/finally`**

   ```python
   archivo = open("archivo.txt", "r")
   try:
       contenido = archivo.read()
   finally:
       archivo.close()  # Siempre se cierra
   ```

---

## Ejercicio guiado

### Generación de objetos a partir de un archivo

**Descripción:** Crear instancias de `Producto` a partir de los datos contenidos en un archivo de texto. Cada línea del archivo corresponde a un texto en estructura JSON.

#### Estructura del archivo (`productos.txt`):

```json
{"nombre": "Producto A", "precio": 100}
{"nombre": "Producto B", "precio": 200}
{"nombre": "Producto C", "precio": 300}
```

#### Solución paso a paso:

**Paso 1:** Crear la clase `Producto` en `productos.py`

```python
class Producto():
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio
```

**Paso 2:** Importar `json` y crear lista contenedora

```python
import json
instancias = []
```

**Paso 3-4:** Abrir archivo y leer primera línea

```python
with open("productos.txt") as productos:
    linea = productos.readline()
```

**Paso 5-8:** Iterar sobre líneas y crear instancias

```python
with open("productos.txt") as productos:
    linea = productos.readline()
    while linea:
        producto = json.loads(linea)
        instancias.append(
            Producto(producto.get("nombre"), producto.get("precio"))
        )
        linea = productos.readline()
```

---

## Preguntas de repaso

1. **¿Por qué es importante el manejo de archivos en la resolución de un algoritmo?**

2. **¿Qué función nativa de Python permite la apertura de archivos?**
   - Respuesta: La función `open()`

3. **¿Qué retorna el método `readlines()`?**
   - Respuesta: Una lista de cadenas, donde cada elemento corresponde a una línea del archivo.
