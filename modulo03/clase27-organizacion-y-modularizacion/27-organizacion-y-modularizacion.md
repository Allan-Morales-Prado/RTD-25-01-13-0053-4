# Organización de un Proyecto en Python y Modularización

---

## Contenido

1. [Organización de un Proyecto en Python](#organización-de-un-proyecto-en-python)
   - [Docstrings](#docstrings)
   - [Tipos de Docstrings](#tipos-de-docstrings)
   - [Refactorización](#refactorización)
2. [Modularización y Experiencia de Usuario](#modularización-y-experiencia-de-usuario)
   - [Modularización](#modularización-1)
   - [Experiencia de Usuario](#experiencia-de-usuario-1)

---

# Organización de un Proyecto en Python

## Docstrings

Los **docstrings** son una documentación que podemos implementar dentro de nuestras funciones para recordar, con el tiempo, cuál es la intención de la función, cómo funciona y qué parámetros son necesarios.

Se implementan al inicio de la función utilizando 3 pares de comillas (simples o dobles):

```python
def elevar(base, exponente):
    """Esta función tiene como objetivo elevar una base a un exponente"""
    return base**exponente
```

---

### Tipos de Docstrings

#### Estilo Google

Fomenta generar un pequeño resumen de lo que hace la función, definir los parámetros con el tipo de datos que se espera de ellos, y una descripción y el tipo del retorno.

```python
def elevar(base, exponente):
    """
    Eleva una base a un exponente.
    
    Args:
        base (float): Base de la potencia.
        exponente (float): Exponente de la potencia.
    
    Returns:
        float: Resultado de elevar base a exponente.
    """
    return base**exponente
```

#### Estilo Sphinx

Herramienta especializada en la creación automática de documentación. Similar al de Google, pero define parámetros y tipos en líneas distintas.

```python
def elevar(base, exponente):
    """
    Eleva una base a un exponente.
    
    :param base: Base de la potencia
    :type base: float
    :param exponente: Exponente de la potencia
    :type exponente: float
    :return: Resultado de elevar base a exponente
    :rtype: float
    """
    return base**exponente
```

#### Estilo Docblockr

Casi idéntico al de Google, pero con otro tipo de separadores.

#### Estilo NumPy

Librería de Computación Científica muy popular. El formato utilizado es reconocido como texto enriquecido en editores como VS Code.

```python
def elevar(base, exponente):
    """
    Esta función tiene como objetivo elevar una base a un exponente.
    
    Parameters
    ----------
    base : float
        Base de la Potencia.
    exponente : float
        Exponente de la Potencia.
    
    Returns
    -------
    float
        Retorna el resultado de elevar base a exponente.
    """
    return base**exponente
```

---

## Refactorización

La **refactorización** consiste en abstraer código y generar funciones que se encarguen del cálculo de patrones similares, aplicando el principio **DRY** (Don't Repeat Yourself).

### Ejemplo de Refactorización

**Código inicial:**

```python
valor_entrada = 10
valor_1 = valor_entrada**2 + valor_entrada**3
valor_2 = valor_1*2 + valor_1*3 + valor_1*4
valor_3 = valor_2**2 + valor_2**3
valor_4 = valor_3*2 + valor_3*3 + valor_3*4
valor_5 = valor_4**2 + valor_4**3
valor_6 = valor_5*2 + valor_5*3 + valor_5*4
```

**Primera refactorización:**

```python
def cuadrado_cubo(valor):
    return valor**2 + valor**3

def mult_234(valor):
    return valor*2 + valor*3 + valor*4

valor_entrada = 10
valor_1 = cuadrado_cubo(valor_entrada)
valor_2 = mult_234(valor_1)
valor_3 = cuadrado_cubo(valor_2)
valor_4 = mult_234(valor_3)
valor_5 = cuadrado_cubo(valor_4)
valor_6 = mult_234(valor_5)
```

**Segunda refactorización:**

```python
def cuadrado_cubo(valor):
    return valor**2 + valor**3

def mult_234(valor):
    return valor*2 + valor*3 + valor*4

def op_combinada(valor):
    var_intermedia = cuadrado_cubo(valor)
    return mult_234(var_intermedia)

valor_entrada = 10
valor_2 = op_combinada(valor_entrada)
valor_4 = op_combinada(valor_2)
valor_6 = op_combinada(valor_4)
```

**Tercera refactorización (compose):**

```python
def compose(f, n):
    def fn(x):
        for _ in range(n):
            x = f(x)
        return x
    return fn

valor_entrada = 10
valor_6 = compose(op_combinada, 3)(valor_entrada)
```

>[!IMPORTANT]
>### Consideraciones sobre Refactorización
>La refactorización debe utilizarse con cautela. La idea es siempre introducir funciones que faciliten el entendimiento del código, no que lo compliquen. Es responsabilidad del desarrollador determinar cuántos niveles de refactorización utilizar, pensando siempre en facilitar la estructura del código.

---

# Modularización y Experiencia de Usuario

## Modularización

### Ventajas de la Modularización

1. **Orden del código:** Permite que el código ejecutable no quede mezclado con las funciones.
2. **Reutilización:** El código creado en un proyecto puede ser útil en otro.
3. **Trabajo en equipo:** Permite aislar tareas para que distintos desarrolladores las ejecuten.
4. **Escalabilidad:** Facilita la adición de nuevas funcionalidades en el futuro.

### Estructura de un Proyecto Modular

```
calculadora_basica/
├── main.py
├── suma.py
├── resta.py
└── input.py
```

### Formas de Importar Módulos

```python
# Forma 1: Importar el módulo completo
import suma
suma.sumar(x, y)

# Forma 2: Importar con alias
import resta as r
r.restar(x, y)

# Forma 3: Importar función específica
from input import tomar_datos
tomar_datos()
```

### Ejemplo de main.py

```python
import suma
import resta as r
from input import tomar_datos

opcion = input("""Esto es una calculadora: ¿Qué operación le gustaría realizar?
1. Sumar
2. Restar
0. Salir
> """)

if opcion == '1':
    x, y = tomar_datos()
    suma.sumar(x, y)
elif opcion == '2':
    x, y = tomar_datos()
    r.restar(x, y)
elif opcion == '0':
    print('Nos vemos a la próxima')
else:
    print('No existe esta Operación')
```

### Buenas Prácticas

- Evitar que un módulo y la función al interior tengan el mismo nombre.
- Usar `if __name__ == '__main__':` para impedir salidas inesperadas de los módulos.

#### Sobre `__name__`
`__name__` es una variable especial integrada (a menudo llamada variable "dunder") que indica el nombre del módulo o script que se está ejecutando actualmente.

Su valor es asignado dinámicamente por el intérprete de Python, dependiendo completamente de cómo se esté ejecutando el archivo que la contiene.

La variable `__main__` solo puede tomar los siguientes valores:
- `__main__`: Esta cadena se asigna si el script se ejecuta directamente por el usuario (por ejemplo, al ejecutar `python myscript.py` en la terminal). Marca el punto de entrada del programa.
- **El nombre actual del archivo**: Si el script se importa como un módulo en otro script (por ejemplo, `import myscript`), Python establece `__name__` al nombre del archivo en sí (sin la extensión .py).

**Ejemplo 1: Módulo importado con salidas no controladas**

```python
# funciones.py (sin if __name__ == '__main__')
def es_par(numero: int) -> bool:
  """Función que determina si un número es par"""
  return numero % 2 == 0

def sumar(a, b):
  return a + b

print(es_par(5))
print(es_par(4))
```

```python
# principal.py
import funciones # funciones.py

print(funciones.es_par(10))
print(funciones.sumar(10, 3))
```
**Salida (principal.py)**
```
False
True
True
13
```

**Ejemplo 2: Módulo importado con salidas controladas**

```python
# funciones.py (con if __name__ == '__main__')
def es_par(numero: int) -> bool:
  """Función que determina si un número es par"""
  return numero % 2 == 0

def sumar(a, b):
  return a + b

if __name__ == '__main__':
  print(es_par(5))
  print(es_par(4))
```

```python
# principal.py
import funciones # funciones.py

print(funciones.es_par(10))
print(funciones.sumar(10, 3))
```
**Salida (principal.py)**
```
True
13
``` 
---

## Experiencia de Usuario

### Pausas en el Programa

```python
import time
time.sleep(3)  # Espera 3 segundos
print('Han pasado 3 segundos')
```

### Limpiar la Pantalla

```python
import os
import sys

# Detecta el sistema operativo
clear = 'cls' if sys.platform == 'win32' else 'clear'
os.system(clear)
```

**Valores de sys.platform:**

| Sistema Operativo | Platform Value |
|-------------------|----------------|
| AIX               | 'aix'          |
| Linux             | 'linux'        |
| Windows           | 'win32'        |
| Windows/Cygwin    | 'cygwin'       |
| macOS             | 'darwin'       |

### Terminar el Programa

```python
exit()  # Finaliza la ejecución del programa
```

---

## Resumen de la Unidad

### Objetivos de Aprendizaje

- Utilizar estructuras de datos apropiadas para la elaboración de algoritmos en Python.
- Codificar programas utilizando funciones para la reutilización de código.
- Explicar el sentido de utilizar funciones dentro de un programa.
- Distinguir entre definición y invocación de funciones.
- Utilizar funciones preconstruidas y personalizadas con paso de parámetros y retorno.

---

*Material educativo de (desafío) latam - Academia de talentos digitales*