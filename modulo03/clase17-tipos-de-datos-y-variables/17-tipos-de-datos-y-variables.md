# Tipos de datos y variables

## Índice de Contenidos

1. **Tipos de Datos Nativos en Python**
   - Valores Numéricos
   - Strings
   - Valores Booleanos
2. **Variables**
   - Definición y Características
   - Manipulación
   - Transformación de Datos
3. **Entrada de Datos**
   - Función `input()`
4. **Ejercicio Guiado**
   - Presentándome con Python

---

## Unidades del Curso

| Unidad | Tema |
|--------|------|
| **Unidad 1** | Introducción a Python |
| **Unidad 2** | Sentencias condicionales e iterativas |
| **Unidad 3** | Estructuras de datos y funciones |

---

## Tipos de Datos Nativos en Python

Son distintas formas de representar información en el lenguaje:

- **Valores numéricos**
- **Strings**
- **Valores booleanos**

---

## Valores Numéricos

### Integer (Enteros)
```python
print(27)      # 27
print(-5)      # -5
print(0)       # 0
print(3 + 7)   # 10
print(31 - 7)  # 24
print(4 * 8)   # 32
```

### Float (Decimales)
```python
print(27.6)          # 27.6
print(-5.9)          # -5.9
print(0.0)           # 0.0
print(3.2 + 7.456)   # 10.656
print(31.5 - 7.0)    # 24.5
print(4.190 * 8.12)  # 34.0228
print(9.0 / 8.1)     # 1.1111111111111112
```
>[!IMPORTANT]
> El separador decimal en Python es el punto (`.`).

>[!IMPORTANT]
> **División en Python:** Cualquier operación de división entre integers devuelve un `float`. Ejemplo: `5 // 2` → `2.0`

### Operaciones Mixtas
```python
print(3.5 + 12)   # 15.5
print(20 * 45.6)  # 912.0
```

---

## Strings (Cadenas de Texto)

Son elementos encerrados entre **comilla simple** (`'`) o **comilla doble** (`"`).

### Características:
- La comilla de apertura y cierre debe ser la misma
- Pueden contener caracteres numéricos, pero no permiten operaciones matemáticas

```python
print('hola')                     # hola
print("150")                      # 150 (como texto)
print('este es un texto más largo')  # este es un texto más largo
```

### Operaciones con Strings

#### Concatenación
```python
print("Carlos" + "Santana")   # CarlosSantana
print("Carlos " + "Santana")  # Carlos Santana
print("15" + "23")            # 1523 (no es una suma numérica)
```

#### Duplicación
```python
print(3 * "Carlos")   # CarlosCarlosCarlos
print(5 * "12")       # 1212121212
```

> **❌ Restricción:** Las operaciones matemáticas entre un valor numérico y un string **no son válidas**.

---

## Métodos de Strings

### `.count()`
Cuenta el número de veces que aparece un carácter o subcadena.
```python
texto = "Hola mundo"
print(texto.count('o'))  # 2
```

### `.upper()`
Transforma el string a mayúsculas.
```python
print("hola".upper())  # HOLA
```

### `.lower()`
Transforma el string a minúsculas.
```python
print("HOLA".lower())  # hola
```

### `.title()`
Coloca mayúscula solo a la primera letra de cada palabra.
```python
print("hola mundo".title())  # Hola Mundo
```

### `.join()`
Permite unir elementos separados por un string.
```python
separador = ", "
print(separador.join(['a', 'b', 'c']))  # a, b, c
```

### `len()`
**Nota:** No es un método, es una función.
Cuenta el número de caracteres en un string.
```python
print(len("Hola"))  # 4
```

---

## Carácter Especial: Salto de Línea

`\n` - Permite agregar un salto de línea dentro de un string.

```python
print("hola\na\ntodos")
# Resultado:
# hola
# a
# todos
```

---

## Valores Booleanos

Son valores lógicos que pueden tomar solo dos valores:

- `True` (Verdadero)
- `False` (Falso)

Son el resultado de pruebas lógicas o asignaciones directas.
Se utilizan principalmente en **Control de Flujo**.

```python
es_mayor = True
es_menor = False
```

---

## Variables

### ¿Qué es una Variable?

Es un **contenedor** que permite:
- Guardar el resultado de operaciones
- Almacenar valores para ser reutilizados

Una variable se compone de:
- **Un nombre**
- **Un valor**

### Ejemplo:
```python
nombre = "Carlos"
edad = 25
```

---

### Consideraciones para Nombrar Variables

| Regla | Ejemplo |
|-------|---------|
| Comienza con minúscula | `nombre` |
| Múltiples palabras: `snake_case` | `cant_alumnos` |
| Sin espacios | ❌ `nombre persona` |
| No comenzar con número | ❌ `1nombre` |
| Usar nombres representativos | ✅ `edad_usuario` |

### Tipos de Datos de una Variable

Python asigna el tipo según el valor que se le asigne:
- `int`
- `float`
- `str`
- `bool`

### Función `type()`
Permite identificar el tipo de dato de una variable.

```python
entero = 2
decimal = -6.5
texto = "Hola Mundo"

print(type(entero))  # <class 'int'>
print(type(decimal)) # <class 'float'>
print(type(texto))   # <class 'str'>
```

> **📌 Importante:** La función `type()` se aplica a la variable, no al `print()`.

---

## Manipulando Variables

Las variables pueden ser reutilizadas y reasignadas.

```python
a = 2           # se asigna el valor 2
a = a + 1       # se suma 1 y se reasigna
print(a)        # 3

nombre = "Carlos"
apellido = "Santana"
print(nombre + " " + apellido)  # Carlos Santana
```

---

## Transformación de Datos

### Interpolación
Permite insertar variables dentro de un string.

**Método `.format()`:**
```python
nombre = 'Carlos'
apellido = 'Santana'
print("Mi nombre es {} {}".format(nombre, apellido))
# Mi nombre es Carlos Santana
```

**F-strings (Python 3.6+):**
```python
nombre = 'Carlos'
apellido = 'Santana'
print(f"Mi nombre es {nombre} {apellido}")
# Mi nombre es Carlos Santana
```

### Precisión de Datos
Permite controlar la cantidad de decimales mostrados.

```python
# Sin control de precisión
print(f'El resultado es {1/9}')
# El resultado es 0.1111111111111111

# Con 2 decimales
print(f'El resultado es {1/9:.2f}')
# El resultado es 0.11
```

---

## Ingresando Datos: `input()`

La función `input()` permite al usuario ingresar texto.

### Características:
- Abre un prompt o cuadro de diálogo
- El texto dentro de `input()` se muestra como mensaje
- **Siempre devuelve un string**
- La consola se bloquea hasta que el usuario presione Enter

```python
# Ejemplo básico
nombre = input("Ingrese su nombre: ")
print(f"Su nombre es {nombre}")

# Siempre es string
edad = input("Ingrese su edad: ")
print(type(edad))  # <class 'str'>
```

---

## Ejercicio Guiado: "Presentándome con Python"

### Planteamiento del Problema

Un conferencista necesita automatizar la presentación personal que realiza en cada conferencia. Debe crear un programa que genere una presentación con información variable.

### Plantilla Original:
```
Mi nombre es Bill, tengo 52 años y me desempeño como CEO en Microsoft.
Soy Creativo, Apasionado y Visionario.
Mi pasatiempo es jugar Golf y me gustaría poder jubilarme pronto.
```

### Variables Identificadas:
- Nombre
- Edad
- Ocupación
- Lugar de Trabajo
- Características (3)
- Pasatiempos
- Algo que hacer

---

### Solución - Paso 1: Solicitar Datos

```python
# presentador.py

nombre = input('Ingrese su Nombre: ')
edad = input('Ingrese Edad: ')
ocupacion = input('Ingrese Ocupación: ')
lugar = input('En dónde?: ')

caracteristica_1 = input('Ingrese 3 características:\n1. > ')
caracteristica_2 = input('2. > ')
caracteristica_3 = input('3. > ')

pasatiempo = input('Cuál es tu pasatiempo: ')
hacer = input('¿Qué quieres hacer? ')
```

---

### Solución - Paso 2: Generar el Texto con Interpolación

```python
print(f'''

Mi nombre es {nombre}, tengo {edad} años y me desempeño como {ocupacion} en {lugar}.
Soy una persona {caracteristica_1}, {caracteristica_2} y {caracteristica_3}.

Mi pasatiempo es {pasatiempo} y me gustaría poder {hacer}.
''')
```
>[!NOTE]
>Se utiliza **string multilínea** (tres comillas) para organizar mejor el texto.

---

### Solución - Paso 3: Ejecución

Al ejecutar el programa, se solicitan los datos y se genera la presentación personalizada de manera rápida y sencilla.

```
Ingrese su Nombre: Carlos
Ingrese Edad: 30
Ingrese Ocupación: desarrollador
En dónde?: una startup
Ingrese 3 características:
1. > creativo
2. > dedicado
3. > curioso
Cuál es tu pasatiempo: programar
¿Qué quieres hacer? viajar

Mi nombre es Carlos, tengo 30 años y me desempeño como desarrollador en una startup.
Soy una persona creativo, dedicado y curioso.

Mi pasatiempo es programar y me gustaría poder viajar.
```

---

## Preguntas Clave

1. **¿Cuáles son los tipos de datos nativos en Python?**
   - Integer (int)
   - Float
   - String (str)
   - Boolean (bool)

2. **¿De qué manera se permite al usuario ingresar datos en Python de manera interactiva?**
   - Mediante la función `input()`

3. **¿Cómo se crean y utilizan aspectos básicos de estructuras de datos en Python?**
   - Mediante variables que almacenan diferentes tipos de datos
   - Manipulando strings con métodos como `.upper()`, `.lower()`, etc.
   - Utilizando interpolación para construir mensajes dinámicos

---

## Resumen de Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| **Tipos de datos** | int, float, str, bool |
| **Variables** | Contenedores con nombre y valor |
| **Strings** | Texto entre comillas, con métodos específicos |
| **Interpolación** | Insertar variables en strings con f-strings o `.format()` |
| **Input** | Entrada de datos por consola con `input()` |
| **Snake_case** | Convención de nombres con guiones bajos |