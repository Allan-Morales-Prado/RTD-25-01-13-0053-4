# Estructuras básicas de datos

## Listas

### Introducción a listas

Son **contenedores** que permiten almacenar múltiples datos.

**Características:**
- Los elementos de la lista se pueden modificar
- Se pueden cambiar los valores, agregar o eliminar elementos
- Las listas son **mutables**

### Definir una lista

Sintaxis básica:
```python
mi_lista = [elemento1, elemento2, elemento3, ...]
```

### Elementos de la lista

Todo lo que esté dentro de los corchetes `[]`, separados por coma.

### Mostrar una lista

Se puede utilizar `print()` o llamar al objeto contenedor directamente.

### Índices

Cada elemento en la lista tiene una posición específica llamada **índice**.

**Características de los índices:**
- En Python, los índices parten en **cero**
- Van hasta **n - 1**, donde n es la cantidad de elementos

**Ejemplo:** En una lista con 4 elementos:
- Primer elemento: posición 0
- Último elemento: posición 3

### Acceder a elementos

```python
nombre_lista[indice]
```

### Error común: IndexError

Si el índice es mayor o igual a la cantidad de elementos:

```python
colores[8]  # Si la lista tiene menos de 9 elementos
# IndexError: list index out of range
```

### Índices negativos

Los índices negativos permiten acceder desde el último al primer elemento:

| Índice negativo | Posición |
|-----------------|----------|
| -1 | Último elemento |
| -2 | Penúltimo elemento |
| -n | Primer elemento |

**Ejemplo:**
```python
a = [1, 2, 3, 4, 5]
a[-1]  # Devuelve: 5
```

### Documentación oficial

La información oficial sobre listas se encuentra en: **docs.python.org**

>[!IMPORTANT]
>Verificar que la versión consultada coincida con la que se está trabajando.

---

## Otras estructuras de datos

### Tuplas

**Características:**
- Par ordenado **inmutable**
- No se pueden modificar partes de ella
- Para actualizarla, se debe modificar la tupla completa

**Unpacking (desempaquetamiento):**
```python
# Ejemplo de unpacking
a, b, c = (1, 2, 3)
# a = 1, b = 2, c = 3
```

### Sets

**Características:**
- Útil en **análisis de texto** para palabras únicas
- Permite trabajar con teoría de conjuntos
- **No permite valores duplicados**
- Ideal para conocer valores únicos

---

## Diccionarios

### ¿Qué son?

Estructura de datos compuesta por pares de **clave:valor**

**Analogía:**
- La **clave** equivale a la **palabra** en un diccionario real
- El **valor** equivale a su **definición**

**Características:**
- Cada clave se asocia con un elemento
- Permiten almacenar gran cantidad de datos en una sola variable

### Listas vs Diccionarios

| Característica | Lista | Diccionario |
|----------------|-------|-------------|
| Acceso | Por índice/posición | Por clave |
| Índices/Claves | Se generan automáticamente | Se definen explícitamente |
| Orden | Ordenado (por índice) | No ordenado |
| Tipo de clave | Solo números (índices) | String, número o booleano |

### Crear un diccionario

**Diccionario vacío:**
```python
mi_diccionario = {}
```

**Diccionario con elementos:**
```python
diccionario = {
    "clave1": "valor1",
    "clave2": "valor2",
    "clave3": "valor3"
}
```

**Formato:** `clave: valor`

**Múltiples líneas:** Se puede definir en varias líneas para mejor legibilidad.

### Acceder a un elemento

Se accede utilizando la **clave** del valor:

```python
diccionario["clave"]
```

### Clave única

**Regla:** Solo puede haber un valor asociado a una clave.

```python
diccionario = {
    "nombre": "Ana",
    "edad": 25,
    "nombre": "María"  # Sobrescribe el valor anterior
}
# "nombre" será "María"
```

Si se usa dos veces la misma clave, Python se queda con la última definición.

---

## Pregunta de reflexión

**¿Qué ventajas tienen las listas frente a los diccionarios? ¿Y los diccionarios frente a las listas?**