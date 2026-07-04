# Organización de Proyectos en Python y Modularización

---

### Pregunta 1

**¿Cuál es el propósito principal de los docstrings en Python?**

A) Mejorar el rendimiento del código
B) Documentar la funcionalidad de funciones, clases y módulos
C) Evitar errores de sintaxis
D) Optimizar el uso de memoria

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: B**

Los docstrings sirven para documentar la funcionalidad del código, explicando qué hace una función, qué parámetros recibe y qué retorna. Esto facilita el mantenimiento y la comprensión del código, especialmente en proyectos grandes.

</details>

---

### Pregunta 2

**¿Qué estilo de docstring es reconocido como texto enriquecido en editores como VS Code y es popular en Ciencia de Datos?**

A) Google Style
B) Sphinx Style
C) NumPy Style
D) Docblockr Style

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

El estilo NumPy es utilizado por la librería de Computación Científica y es reconocido como texto enriquecido en editores como VS Code, lo que permite una documentación más elegante y visual.

</details>

---

### Pregunta 3

**¿Cuál es la principal advertencia sobre la refactorización?**

A) Siempre debe aplicarse hasta el nivel más profundo posible
B) Debe evitarse por completo en proyectos grandes
C) Debe utilizarse con cautela, priorizando la claridad del código sobre la complejidad innecesaria
D) Solo debe aplicarse al inicio del desarrollo

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

El material enfatiza que la refactorización debe usarse con cautela. El objetivo es facilitar el entendimiento del código, no complicarlo. Es responsabilidad del desarrollador determinar el nivel apropiado de refactorización.

</details>

---

### Pregunta 4

**¿Cuál de las siguientes NO es una ventaja de la modularización?**

A) Permite el trabajo en equipo al aislar tareas
B) Facilita la reutilización de código entre proyectos
C) Aumenta automáticamente la velocidad de ejecución del programa
D) Permite estructuras ordenadas y escalables

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

La modularización no aumenta automáticamente la velocidad de ejecución. Sus ventajas son organizativas: facilita el trabajo en equipo, la reutilización de código y la escalabilidad del proyecto.

</details>

---

### Pregunta 5

**Dado el siguiente código:**

```python
# archivo: operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

if __name__ == '__main__':
    print(sumar(5, 3))
```

**¿Qué sucede cuando se ejecuta `python operaciones.py` y qué sucede cuando se importa en otro script?**

A) En ambos casos se imprime `8`
B) No se imprime nada en ningún caso
C) Se imprime `8` al ejecutar directamente; no se imprime nada al importar
D) No se imprime nada al ejecutar directamente; se imprime `8` al importar

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

Cuando se ejecuta directamente, `__name__` es `'__main__'`, por lo que se ejecuta el bloque y se imprime `8`. Cuando se importa, `__name__` toma el nombre del módulo (`'operaciones'`), por lo que el bloque condicional no se ejecuta.

</details>

---

### Pregunta 6

**¿Qué función de Python permite agregar una pausa en la ejecución del programa?**

A) `pause()`
B) `stop()`
C) `time.sleep()`
D) `wait()`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

La función `time.sleep(n)` de la librería `time` permite pausar la ejecución del programa durante `n` segundos.

</details>

---

### Pregunta 7

**¿Cuál es la forma correcta de limpiar la pantalla en Python de manera multiplataforma?**

A) Usar siempre `os.system('cls')`
B) Usar siempre `os.system('clear')`
C) Detectar el sistema operativo con `sys.platform` y ejecutar el comando apropiado
D) Usar `print('\n' * 100)`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

La forma multiplataforma correcta es detectar el sistema operativo usando `sys.platform` y ejecutar `cls` en Windows o `clear` en macOS/Linux, ya que los comandos son diferentes.

</details>

---

### Pregunta 8

**Dado el siguiente código de importación:**

```python
import resta as r
```

**¿Cómo se debe llamar a la función `restar` que está dentro del módulo?**

A) `resta.restar()`
B) `restar()`
C) `r.restar()`
D) `import.restar()`

<details>
<summary>Ver respuesta</summary>

**Respuesta correcta: C**

Cuando se usa `import ... as`, se crea un alias para el módulo. En este caso, el alias es `r`, por lo que se debe llamar a la función como `r.restar()`.

</details>
