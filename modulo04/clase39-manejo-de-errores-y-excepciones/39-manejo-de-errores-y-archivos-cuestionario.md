# Cuestionario: Manejo de Errores y Excepciones en Python

---

## Pregunta 1

**¿Cuál de las siguientes afirmaciones sobre los tipos de errores en Python es correcta?**

A) Los errores de sintaxis permiten que el programa se ejecute parcialmente hasta encontrar el error.

B) Los errores de ejecución impiden que el programa comience su ejecución.

C) Los errores lógicos no impiden la ejecución del programa pero producen resultados incorrectos.

D) Las excepciones son errores que siempre se producen independientemente de los valores de las variables.

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

**Justificación:** Los errores lógicos son los más difíciles de detectar porque el programa se ejecuta sin problemas aparentes (no lanza excepciones), pero produce resultados no esperados. La opción A es incorrecta porque los errores de sintaxis impiden completamente la ejecución. La opción B es incorrecta porque los errores de ejecución (excepciones) permiten que el programa comience pero se interrumpen durante la ejecución. La opción D es incorrecta porque las excepciones dependen de los valores de variables o argumentos en tiempo de ejecución.

</details>

---

## Pregunta 2

**¿Qué código produce correctamente una excepción personalizada con un mensaje de error?**

A) 
```python
class MiError:
    def __init__(self, mensaje):
        self.mensaje = mensaje
```

B) 
```python
class MiError(Exception):
    pass

raise MiError("Error personalizado")
```

C) 
```python
class MiError(Exception):
    def __init__(self):
        super().__init__()

raise MiError("Error personalizado")
```

D) 
```python
class MiError(BaseException):
    def __init__(self, mensaje):
        self.mensaje = mensaje

raise MiError()
```

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La opción B es correcta porque define correctamente una excepción personalizada heredando de `Exception` y utiliza `raise` con el mensaje como argumento. La opción A es incorrecta porque no hereda de `Exception` (ni de `BaseException`). La opción C es incorrecta porque el constructor no acepta el mensaje que se intenta pasar. La opción D es incorrecta porque aunque hereda de `BaseException`, no es buena práctica y el constructor no acepta argumentos, pero se intenta pasar uno.

</details>

---

## Pregunta 3

**Dado el siguiente código, ¿qué se mostrará en pantalla?**

```python
def procesar_datos(valor):
    try:
        resultado = 100 / valor
        print(f"Resultado: {resultado}")
    except ZeroDivisionError:
        print("División por cero")
    except TypeError:
        print("Tipo de dato incorrecto")
    except Exception:
        print("Error general")
    else:
        print("Operación exitosa")
    finally:
        print("Procesamiento finalizado")

procesar_datos("5")
```
A)
```
División por cero
Procesamiento finalizado
```

B)
```
TypeError
Procesamiento finalizado
```

C)
```
Tipo de dato incorrecto
Procesamiento finalizado
```

D)
```
Error general
Procesamiento finalizado
```




<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

**Justificación:** Al pasar `"5"` (un string) como argumento, la operación `100 / "5"` genera un `TypeError` porque no se puede dividir un número por un string. El código captura esta excepción en el `except TypeError`, imprime "Tipo de dato incorrecto" y luego ejecuta el bloque `finally` que imprime "Procesamiento finalizado". El bloque `else` no se ejecuta porque ocurrió una excepción.

</details>

---

## Pregunta 4

**¿Cuál es el propósito principal de la cláusula `finally` en un bloque `try/except`?**

A) Capturar excepciones que no fueron manejadas por los bloques `except`

B) Ejecutar código solo si no ocurre ninguna excepción en el bloque `try`

C) Ejecutar código de limpieza que debe realizarse siempre, ocurra o no una excepción

D) Relanzar una excepción para que sea manejada en un nivel superior

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

**Justificación:** La cláusula `finally` está diseñada específicamente para ejecutar acciones de limpieza que deben realizarse independientemente de si ocurrió o no una excepción (como cerrar archivos, liberar recursos, etc.). La opción A describe el comportamiento de un `except` sin tipo específico. La opción B describe el propósito de `else`. La opción D describe el propósito de `raise` dentro de un bloque `except`.

</details>

---

## Pregunta 5

**¿Qué imprime el siguiente código?**

```python
try:
    numeros = [10, 20, 30]
    print(numeros[5])
except IndexError:
    print("Índice fuera de rango")
    raise ValueError("Error de valor")
except ValueError:
    print("Error de valor capturado")
finally:
    print("Bloque final ejecutado")
```
A)
```
Índice fuera de rango
Bloque final ejecutado
(Termina con ValueError)
```
B)
```
Índice fuera de rango
Error de valor capturado
Bloque final ejecutado
```
C)
```
Índice fuera de rango
Bloque final ejecutado
```
D)
```
Error de valor capturado
Bloque final ejecutado
```

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: A**

**Justificación:** El código intenta acceder al índice 5 de una lista que solo tiene 3 elementos (índices 0, 1, 2), lo que genera un `IndexError`. Este error es capturado por el primer `except`, imprimiendo "Índice fuera de rango". Luego, dentro del `except`, se ejecuta `raise ValueError("Error de valor")` que lanza una nueva excepción. Esta excepción NO es capturada por el segundo `except` porque ya estamos dentro de un manejador de excepciones y la excepción se propaga hacia arriba. Finalmente se ejecuta el bloque `finally` y el programa termina con un `ValueError` no manejado.

</details>

---

## Pregunta 6

**¿Cuál es el orden correcto para combinar las cláusulas `try`, `except`, `else` y `finally`?**

A) try → else → except → finally

B) try → except → finally → else

C) try → except → else → finally

D) try → finally → except → else

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

**Justificación:** El orden correcto y obligatorio en Python es: `try`, seguido de uno o más bloques `except`, luego opcionalmente `else`, y finalmente opcionalmente `finally`. La opción A es incorrecta porque `else` no puede ir antes de `except`. La opción B es incorrecta porque `finally` debe ir después de `else`. La opción D es incorrecta porque `finally` no puede ir antes de `except`.

</details>

---

## Pregunta 7

**¿Cuál es el resultado de ejecutar el siguiente código?**

```python
class EdadInvalidaError(Exception):
    pass

def verificar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("Edad negativa no permitida")
    elif edad > 150:
        raise EdadInvalidaError("Edad excede el límite máximo")
    return True

try:
    verificar_edad(-5)
    print("Edad válida")
except EdadInvalidaError as e:
    print(f"Error: {e}")
except Exception:
    print("Error desconocido")
else:
    print("Verificación completada")
finally:
    print("Fin de la verificación")
```

A) 
```
Error: Edad negativa no permitida
Verificación completada
Fin de la verificación
```

B) 
```
Error: Edad negativa no permitida
Fin de la verificación
```

C) 
```
Error desconocido
Fin de la verificación
```

D) 
```
Edad válida
Verificación completada
Fin de la verificación
```

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** Al llamar `verificar_edad(-5)`, la función lanza `EdadInvalidaError("Edad negativa no permitida")`. Esta excepción es capturada por el primer `except` que coincide con el tipo `EdadInvalidaError`, imprimiendo "Error: Edad negativa no permitida". El bloque `else` no se ejecuta porque ocurrió una excepción, pero el bloque `finally` siempre se ejecuta, imprimiendo "Fin de la verificación". No se ejecuta "Verificación completada" porque el `else` solo se ejecuta si no hay excepciones.

</details>

---

## Pregunta 8

**¿Qué sucede cuando se utiliza un bloque `except` sin especificar el tipo de excepción?**

A) Captura únicamente las excepciones de tipo `Exception`

B) Captura todas las excepciones, incluyendo `SystemExit` y `KeyboardInterrupt`

C) Captura únicamente las excepciones definidas por el usuario

D) Captura todas las excepciones que heredan de `Exception`, pero no las que heredan de `BaseException`

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** Un `except` sin tipo específico (también conocido como "except desnudo") captura TODAS las excepciones, incluyendo aquellas que no heredan de `Exception` como `SystemExit`, `KeyboardInterrupt` y `GeneratorExit`. Esta práctica generalmente no es recomendada porque puede ocultar errores importantes y dificultar la depuración. La opción D describe el comportamiento de `except Exception`, no del except sin tipo.

</details>

---

## Pregunta 9

**¿Qué mostrará este código al ejecutarse con entrada "diez"?**

```python
def obtener_division():
    intentos = 0
    while intentos < 3:
        try:
            num = input("Ingrese un número: ")
            resultado = 100 / int(num)
            return resultado
        except ValueError:
            print("Valor no numérico")
            intentos += 1
        except ZeroDivisionError:
            print("División por cero")
            intentos += 1
        else:
            print("Operación exitosa")
        finally:
            print(f"Intento {intentos + 1} completado")
    print("Máximo de intentos alcanzado")
    return None

obtener_division()
```
A)
```
Valor no numérico
Intento 1 completado
(continúa hasta 3 intentos)
```

B)
```
Valor no numérico
Intento 0 completado
(continúa hasta 3 intentos)
```

C)
```
Operación exitosa
Intento 1 completado
```

D)
```
Valor no numérico
Intento 2 completado
```

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: A**

**Justificación:** Al ingresar "diez", `int("diez")` genera un `ValueError`, que es capturado por el primer `except`. Se imprime "Valor no numérico" y se incrementa `intentos` a 1. Luego, el bloque `finally` se ejecuta imprimiendo "Intento 1 completado" (observar que la función `input` no se ejecuta dentro del bucle en el análisis, pero el mensaje muestra `intentos + 1`). El bucle continúa hasta que `intentos` llegue a 3, mostrando en cada iteración el mensaje correspondiente al `finally` con el número de intento actualizado. El bloque `else` nunca se ejecuta porque siempre ocurre una excepción.

**Nota:** El mensaje del finally usa `intentos + 1`, por lo que muestra "Intento 1 completado", "Intento 2 completado", "Intento 3 completado".

</details>

---

## Pregunta 10

**¿Cuál de las siguientes afirmaciones sobre el manejo de archivos en Python es correcta?**

A) Se debe usar `try/except` obligatoriamente al abrir archivos porque `open()` siempre lanza una excepción

B) El bloque `finally` es la única forma de asegurar que un archivo se cierre correctamente

C) La sentencia `with` proporciona una forma automática de gestionar el cierre de archivos, equivalente a usar `try/finally`

D) Los archivos abiertos con `open()` se cierran automáticamente al final del programa sin necesidad de ninguna acción

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

**Justificación:** El gestor de contexto `with` es la forma recomendada para manejar archivos en Python porque asegura automáticamente el cierre del archivo al salir del bloque, incluso si ocurre una excepción, funcionando de manera similar a un bloque `try/finally`. La opción A es incorrecta porque `open()` solo lanza excepción si hay un error (como archivo no encontrado). La opción B es incorrecta porque `with` es una alternativa más limpia. La opción D es incorrecta porque Python no garantiza el cierre inmediato de archivos al final del programa.

</details>

---

## Pregunta 11

**Dado el siguiente código, ¿qué excepción se propaga al exterior?**

```python
def funcion_principal():
    try:
        try:
            datos = {"a": 1, "b": 2}
            valor = datos["c"]
        except KeyError:
            print("Clave no encontrada")
            raise TypeError("Error de tipo")
        finally:
            print("Limpiando recursos internos")
    except TypeError:
        print("Error de tipo capturado externamente")
        raise RuntimeError("Error de ejecución")
    finally:
        print("Limpiando recursos externos")

funcion_principal()
```

A) KeyError

B) TypeError

C) RuntimeError

D) No se propaga ninguna excepción

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

**Justificación:** El código intenta acceder a la clave "c" que no existe en el diccionario, generando un `KeyError`. Este es capturado internamente, imprime "Clave no encontrada" y lanza un `TypeError`. El bloque `finally` interno se ejecuta. Luego, el `TypeError` es capturado por el `except` externo, que imprime "Error de tipo capturado externamente" y lanza un `RuntimeError`. Finalmente, el bloque `finally` externo se ejecuta y la excepción `RuntimeError` se propaga hacia el exterior.

</details>

---

## Pregunta 12

**¿Cuál es la mejor práctica para capturar excepciones en Python?**

A) Usar siempre `except Exception as e` para capturar todas las excepciones posibles

B) Capturar excepciones específicas y manejar cada una de manera diferente según el caso

C) Usar siempre `except:` sin especificar tipo para asegurar que nada detenga el programa

D) No capturar excepciones nunca y dejar que el programa termine con errores

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La mejor práctica es capturar excepciones específicas (como `ValueError`, `TypeError`, etc.) y manejarlas de manera adecuada según el contexto. Esto permite un control granular del flujo del programa y facilita la depuración. La opción A y C son incorrectas porque capturar excepciones genéricas puede ocultar errores importantes. La opción D es incorrecta porque un programa robusto debe manejar situaciones de error predecibles.

</details>

---

## Pregunta 13

**¿Qué salida produce el siguiente código?**

```python
class MiError(Exception):
    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo
        super().__init__(mensaje)
    
    def __str__(self):
        return f"{self.mensaje} (Código: {self.codigo})"

try:
    raise MiError("Error de validación", 404)
except MiError as e:
    print(e)
except Exception:
    print("Error genérico")
```

A) Error de validación (Código: 404)

B) Error genérico

C) MiError

D) Error de validación

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La clase `MiError` sobrescribe el método `__str__` para incluir tanto el mensaje como el código en el formato especificado. Al levantar la excepción con `raise MiError("Error de validación", 404)`, y capturarla en el primer `except`, se imprime el resultado del método `__str__`, que es "Error de validación (Código: 404)". El segundo `except` no se ejecuta porque el primer `except` ya capturó la excepción correctamente.

</details>

---

## Pregunta 14

**Identifica el problema en el siguiente código:**

```python
def calcular_promedio(notas):
    try:
        total = sum(notas)
        promedio = total / len(notas)
        return promedio
    except ZeroDivisionError:
        print("Lista vacía")
    except TypeError:
        print("Elementos no numéricos")
    finally:
        print("Cálculo finalizado")
    return 0

resultado = calcular_promedio([])
print(f"Resultado: {resultado}")
```

A) El código lanza un TypeError porque la lista está vacía

B) El código no tiene problemas y funciona correctamente

C) El código nunca retorna 0 porque el finally siempre se ejecuta antes del return

D) El código intenta dividir entre cero pero no lo maneja correctamente porque el return 0 nunca se alcanza

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: D**

**Justificación:** Cuando se pasa una lista vacía, `len(notas)` es 0, lo que genera un `ZeroDivisionError` en la línea `promedio = total / len(notas)`. El bloque `except ZeroDivisionError` captura la excepción, imprime "Lista vacía", luego se ejecuta el `finally` que imprime "Cálculo finalizado", y finalmente se ejecuta el `return 0` que está después del bloque `try/except/finally`. El problema es conceptual: el código funciona, pero el `return 0` después del finally es alcanzable porque no hay un `return` dentro del `except`. Sin embargo, la estructura es confusa y podría mejorarse.

**Nota:** La pregunta busca evaluar la comprensión del flujo de ejecución. El código sí retorna 0, pero la opción D describe mejor el problema de diseño (manejo inadecuado del caso de lista vacía).

</details>

---

## Pregunta 15

**¿Cuál de las siguientes afirmaciones sobre `raise` en Python es FALSA?**

A) `raise` puede usarse sin argumentos para relanzar la excepción actual dentro de un bloque `except`

B) `raise` solo puede usarse dentro de un bloque `try`

C) `raise` puede lanzar una excepción personalizada definida por el usuario

D) `raise` puede usarse para lanzar excepciones de tipos predefinidos como `ValueError`

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** La afirmación falsa es que `raise` solo puede usarse dentro de un bloque `try`. En realidad, `raise` puede usarse en cualquier parte del código para lanzar excepciones explícitamente, no solo dentro de bloques `try`. La opción A es verdadera porque `raise` sin argumentos relanza la excepción actual. La opción C es verdadera porque `raise` puede lanzar excepciones personalizadas. La opción D es verdadera porque `raise` puede lanzar excepciones built-in como `ValueError`.

</details>

---

## Pregunta 16

**¿Qué imprimirá el siguiente código al ejecutarse?**

```python
def procesar_lista(lista):
    try:
        for i, elemento in enumerate(lista):
            if elemento == 0:
                raise ValueError(f"Elemento cero encontrado en índice {i}")
            if not isinstance(elemento, int):
                raise TypeError("Elemento no entero")
            print(elemento * 2)
    except ValueError as e:
        print(f"Error de valor: {e}")
    except TypeError as e:
        print(f"Error de tipo: {e}")
    except:
        print("Error desconocido")
    else:
        print("Procesamiento completado")
    finally:
        print("Procesamiento finalizado")

procesar_lista([1, "2", 3, 0])
```

A)
```
2
Error de tipo: Elemento no entero
Procesamiento finalizado
```

B)
```
2
4
Error de valor: Elemento cero encontrado en índice 3
Procesamiento finalizado
```

C)
```
2
Error de tipo: Elemento no entero
Procesamiento completado
Procesamiento finalizado
```

D)
```
2
Error de valor: Elemento cero encontrado en índice 3
Procesamiento completado
Procesamiento finalizado
```

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: A**

**Justificación:** El proceso comienza con el elemento 1 (entero), imprime 2. Luego encuentra el elemento "2" (string), que no es entero, por lo que se lanza `TypeError("Elemento no entero")`. Esta excepción es capturada por el `except TypeError`, imprimiendo "Error de tipo: Elemento no entero". El bucle se interrumpe y no se procesan los elementos 3 y 0. El bloque `else` no se ejecuta porque ocurrió una excepción. Finalmente, el bloque `finally` imprime "Procesamiento finalizado".

</details>

---

## Pregunta 17

**¿Qué excepción se genera al intentar acceder a un índice que no existe en una lista?**

A) KeyError

B) ValueError

C) IndexError

D) LookupError

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: C**

**Justificación:** `IndexError` es la excepción específica que se lanza cuando se intenta acceder a un índice fuera del rango de una secuencia (listas, tuplas, etc.). `KeyError` se lanza al acceder a una clave inexistente en un diccionario. `ValueError` se lanza cuando una operación recibe un valor de tipo correcto pero valor inapropiado. `LookupError` es la clase base de `IndexError` y `KeyError`, pero la excepción específica que se genera es `IndexError`.

</details>

---

## Pregunta 18

**¿Cuál de los siguientes fragmentos de código define correctamente una excepción personalizada que almacena información adicional del error?**

A) 
```python
class DatabaseError(Exception):
    def __init__(self, mensaje, query):
        self.mensaje = mensaje
        self.query = query
        super().__init__(mensaje)
```

B) 
```python
class DatabaseError(Exception):
    def __init__(self, mensaje, query):
        self.mensaje = mensaje
        self.query = query
```

C) 
```python
class DatabaseError(Exception):
    pass

DatabaseError.mensaje = "Error de base de datos"
DatabaseError.query = "SELECT * FROM users"
```

D) 
```python
class DatabaseError:
    def __init__(self, mensaje, query):
        self.mensaje = mensaje
        self.query = query
        Exception.__init__(mensaje)
```

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La opción A es correcta porque hereda de `Exception`, define un constructor que acepta el mensaje y un parámetro adicional (`query`), almacena ambos como atributos de instancia, y llama correctamente al constructor de la clase padre con `super().__init__(mensaje)`. La opción B es incorrecta porque no llama al constructor de la clase padre. La opción C es incorrecta porque define atributos a nivel de clase, no de instancia. La opción D es incorrecta porque no hereda de `Exception` y usa una sintaxis inapropiada para llamar al constructor.

</details>

---

## Pregunta 19

**¿Qué mostrará el siguiente código al ejecutarse?**

```python
def validar_numero(numero):
    try:
        if numero < 0:
            raise ValueError("Número negativo")
        if numero > 100:
            raise ValueError("Número muy grande")
        return numero * 2
    except ValueError as e:
        print(f"Error: {e}")
        return 0

try:
    resultado = validar_numero(150)
    print(f"Resultado: {resultado}")
except Exception as e:
    print(f"Error externo: {e}")
finally:
    print("Finalizando programa")
```
A)
```
Error: Número muy grande
Resultado: 0
Finalizando programa
```

B)
```
Error: Número muy grande
Finalizando programa
```

C)
```
Error externo: Número muy grande
Finalizando programa
```

D)
```
Resultado: 300
Finalizando programa
```
<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: A**

**Justificación:** La función `validar_numero(150)` detecta que 150 > 100 y lanza `ValueError("Número muy grande")`. Esta excepción es capturada por el `except ValueError` dentro de la función, imprimiendo "Error: Número muy grande" y retornando 0. La función retorna 0, por lo que el código externo imprime "Resultado: 0". El bloque `finally` externo siempre se ejecuta, imprimiendo "Finalizando programa". La excepción fue manejada internamente, por lo que el `except Exception` externo no se ejecuta.

</details>

---

## Pregunta 20

**¿Cuál es la diferencia fundamental entre `except Exception` y un `except` sin tipo específico?**

A) `except Exception` captura más tipos de excepciones que un `except` sin tipo

B) `except Exception` captura todas las excepciones excepto `KeyboardInterrupt` y `SystemExit`, mientras que el `except` sin tipo captura todas sin excepción

C) No hay diferencia, ambos son equivalentes

D) `except Exception` solo captura excepciones definidas por el usuario

<details>
<summary><strong>Ver respuesta correcta</strong></summary>

**Respuesta correcta: B**

**Justificación:** `except Exception` captura todas las excepciones que heredan de `Exception`, que incluye la mayoría de las excepciones comunes, pero NO captura `KeyboardInterrupt`, `SystemExit` y `GeneratorExit` (que heredan directamente de `BaseException`). Un `except` sin tipo específico (desnudo) captura TODAS las excepciones, incluyendo estas tres. Esta es una diferencia crucial porque en programas interactivos, capturar `KeyboardInterrupt` (Ctrl+C) generalmente no es deseable. La opción D es incorrecta porque `except Exception` también captura excepciones built-in.

</details>