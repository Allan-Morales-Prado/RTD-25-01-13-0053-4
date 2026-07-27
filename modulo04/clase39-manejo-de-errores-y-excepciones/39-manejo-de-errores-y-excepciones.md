# Manejo de Errores y Archivos

## ¿Qué entendemos por errores y excepciones?

### Tipos de Errores

| Tipo de Error | Descripción | Características |
|---------------|-------------|-----------------|
| **Errores de Sintaxis** | Código Python que no sigue la gramática del lenguaje | Impiden que el programa se ejecute. Las líneas anteriores a la ubicación del error no son ejecutadas |
| **Errores de Ejecución (Excepciones)** | Error que ocurre durante la ejecución del código | La sintaxis es correcta, pero ocurre un error en tiempo de ejecución. Las líneas anteriores a la instrucción problemática sí se ejecutan |
| **Errores Lógicos** | El programa se ejecuta pero produce resultados incorrectos | Más difíciles de detectar. No impiden la ejecución ni producen excepciones. Detectados por el programador o usuario |

---

## Manejo de Excepciones

### Importancia del Manejo de Excepciones

- **Impide la interrupción** del programa frente a situaciones no controladas
- **Permite crear flujos alternativos** de ejecución

### ¿Qué es una Excepción?

- Es un error de ejecución con un **tipo asociado**
- El tipo corresponde al **nombre de la clase** de la excepción
- **Excepciones built-in:** predefinidas por el intérprete de Python
- **Excepciones personalizadas:** definidas por el usuario
- Todas las excepciones derivan de `BaseException` o de `Exception`

### Jerarquía de Excepciones

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
    ├── StopIteration
    ├── StopAsyncIteration
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    ├── OSError
    ├── RuntimeError
    ├── SyntaxError
    ├── SystemError
    ├── TypeError
    └── ValueError
```

---

## Sentencia try/except

### Estructura Básica

```python
try:
    # Código que puede generar una excepción
    pass
except TipoExcepcion:
    # Código que se ejecuta si ocurre la excepción
    pass
```

### Ejemplo Básico

```python
try:
    edad = int(input("Ingrese su edad:\n"))
    divisor = int(input("Ingrese número para dividir su edad:\n"))
    print(edad / divisor)
except ValueError:
    print("Debe ingresar un número")
except ZeroDivisionError:
    print("El N° por el cual desea dividir no puede ser cero")
```

### Captura de Múltiples Excepciones

```python
consultar = True
while consultar:
    try:
        edad = int(input("Ingrese su edad:\n"))
        divisor = int(input("Ingrese número para dividir su edad:\n"))
        print(edad / divisor)
        consultar = False
    except ValueError:
        print("Debe ingresar un número")
    except ZeroDivisionError:
        print("El N° por el cual desea dividir no puede ser cero")
    except Exception as e:
        print(f"ERROR: {e}")
    except:
        print("ERROR SIN INFORMACIÓN")
```

### Consideraciones Importantes

- El intérprete revisa los `except` en **orden de escritura**
- Se ejecuta el **primer except** que coincide con el tipo de excepción
- Un `except` sin tipo específico captura **cualquier excepción**
- Siempre debe haber al menos **1 declaración except** por cada `try`

---

## Lanzamiento de Excepciones

### Sentencia raise

```python
raise TipoExcepcion
# o
raise TipoExcepcion("mensaje de error")
```

### Ejemplo

```python
if edad < 0:
    raise ValueError("La edad debe ser un número positivo")
```

---

## Excepciones Definidas por el Usuario

### Definición Básica

```python
class Error(Exception):
    """Clase base para excepciones personalizadas"""
    pass

class HoraError(Error):
    """Excepción para errores de formato de hora"""
    pass

class LargoTextoError(Error):
    """Excepción para errores de longitud de texto"""
    def __init__(self, mensaje, texto=None, largo=None):
        self.mensaje = mensaje
        self.texto = texto[:50] if texto else None  # Acortar a 50 caracteres
        self.largo = largo
        super().__init__(mensaje)
    
    def __str__(self):
        if self.texto is None and self.largo is None:
            return super().__str__()
        if self.texto and self.largo:
            return f"'{self.texto}' excede el largo máximo de {self.largo} caracteres"
        return self.mensaje
```

### Buenas Prácticas

- Crear una **clase base** para excepciones personalizadas
- Las clases de excepción suelen terminar en **"Error"**
- Heredar de `Exception` (no directamente de `BaseException`)
- El valor asociado es una lista de argumentos (`*args`)

---

## Acciones de Limpieza

### Cláusula finally

```python
try:
    # Código que puede generar una excepción
    pass
except TipoExcepcion:
    # Manejo de la excepción
    pass
finally:
    # Código que SIEMPRE se ejecuta al final
    pass
```

### Características de finally

- Se ejecuta **siempre**, ocurra o no una excepción
- Útil para acciones de limpieza (cerrar archivos, liberar recursos)
- Se puede usar un bloque `try/finally` sin `except`

### Ejemplo con finally

```python
intentos = 0
while intentos <= 3:
    try:
        edad = int(input("Ingrese su edad:\n"))
        if edad < 0:
            raise EdadError("Debe ser un N° positivo.", edad)
        divisor = int(input("Ingrese número para dividir su edad:\n"))
        print(edad / divisor)
    except ValueError:
        print("Debe ingresar un número")
    except ZeroDivisionError:
        print("El N° por el cual desea dividir no puede ser cero")
    except EdadError as e:
        print(f"La edad '{e.edad}' no es válida. {e.mensaje}")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        intentos += 1
```

### Cláusula else

```python
try:
    # Código que puede generar una excepción
    pass
except TipoExcepcion:
    # Manejo de la excepción
    pass
else:
    # Se ejecuta si NO ocurre ninguna excepción
    pass
finally:
    # Siempre se ejecuta al final
    pass
```

---

## Resumen de Cláusulas en try/except

| Cláusula | Obligatoria | Propósito |
|----------|-------------|-----------|
| `try` | Sí | Contiene el código que puede generar excepciones |
| `except` | Al menos 1 | Captura y maneja excepciones específicas |
| `else` | No | Se ejecuta si no ocurre ninguna excepción |
| `finally` | No | Se ejecuta siempre, ocurra o no una excepción |

---

## Ejercicio Guiado: Validación de Datos

### Contexto

Desarrollo de una aplicación de calendario y agenda. Se debe validar los datos para crear una reunión:

- **Título:** Cadena de texto, máximo 150 caracteres
- **Hora:** Cadena en formato "HH:MM:SS"

### Paso 1: Definir Clase Error (error.py)

```python
class Error(Exception):
    """Clase base para excepciones personalizadas"""
    pass

class HoraError(Error):
    """Excepción para errores de formato de hora"""
    pass
```

### Paso 2: Definir LargoTextoError (error.py)

```python
class LargoTextoError(Error):
    """Excepción para errores de longitud de texto"""
    def __init__(self, mensaje, texto=None, largo=None):
        self.mensaje = mensaje
        self.texto = texto[:50] if texto else None  # Acortar a 50 caracteres
        self.largo = largo
        super().__init__(mensaje)
```

### Paso 3: Sobrecargar __str__ (error.py)

```python
    def __str__(self):
        if self.texto is None and self.largo is None:
            return super().__str__()
        if self.texto and self.largo:
            return f"'{self.texto}' excede el largo máximo de {self.largo} caracteres"
        return self.mensaje
```

### Paso 4: Definir Clase Reunion (reunion.py)

```python
class Reunion:
    def __init__(self, titulo, hora):
        self.titulo = titulo
        self.hora = hora
```

### Paso 5: Importaciones y Variables (demo.py)

```python
from error import HoraError, LargoTextoError
from reunion import Reunion
import re

titulo = None
hora = None
time_re = r"^\d{2}:\d{2}:\d{2}$"
```

### Paso 6: Ciclo While con try/except/else

```python
while True:
    try:
        # Código de entrada de datos
        pass
    except Exception as e:
        print(e)
        continue
    else:
        break
```

### Paso 7: Validación de Título

```python
while True:
    try:
        titulo = input("Ingrese el título de la reunión:\n")
        if not titulo or len(titulo) > 150:
            raise LargoTextoError("Título inválido", titulo, 150)
        break
    except LargoTextoError as e:
        print(e)
```

### Paso 8: Validación de Hora

```python
while True:
    try:
        hora = input("Ingrese la hora (HH:MM:SS):\n")
        if not re.match(time_re, hora):
            raise HoraError(f"Formato de hora inválido: {hora}")
        break
    except HoraError as e:
        print(e)
```

### Paso 9: Crear Instancia de Reunion

```python
reunion = Reunion(titulo, hora)
print(f"Reunión creada: {reunion.titulo} a las {reunion.hora}")
```

---

## Preguntas de Repaso

1. **¿Qué diferencia un error de sintaxis de un error de ejecución?**
   - Error de sintaxis: impide que el programa se ejecute
   - Error de ejecución: el programa comienza pero se interrumpe durante la ejecución

2. **¿Qué error produce una excepción de tipo IndexError?**
   - Se produce al intentar acceder a un índice fuera del rango de una secuencia (lista, tupla, etc.)

3. **¿Qué sentencia en bloque permite el manejo de excepciones en Python?**
   - La sentencia `try/except` (junto con `finally` y `else` opcionales)

---

## Recursos Adicionales

- [Documentación oficial de Python sobre errores y excepciones](https://docs.python.org/3/tutorial/errors.html)
- [Excepciones incorporadas en Python](https://docs.python.org/3/library/exceptions.html)
- [Manejo de excepciones con try/except](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
- [Definición de excepciones personalizadas](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions)
- [Cláusula finally](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)
- [Manejo de archivos con open()](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)