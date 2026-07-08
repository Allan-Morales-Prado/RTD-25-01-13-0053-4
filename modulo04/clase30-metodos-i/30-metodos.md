# Métodos (Parte I)

## Contenido

1. [Los Métodos](#los-métodos)
2. [Métodos de una clase y diferencia con funciones](#métodos-de-una-clase-y-diferencia-con-funciones)
3. [Definir un método estático](#definir-un-método-estático)
4. [Decoradores](#decoradores)
5. [¿Cómo hacer el llamado a un método estático?](#cómo-hacer-el-llamado-a-un-método-estático)
6. [Objetos](#objetos)
7. [Métodos y comportamiento](#métodos-y-comportamiento)

---

## Los Métodos

Corresponden a un **bloque de código** que permite realizar una tarea específica, los que pueden tener o no un retorno y pueden ser con o sin parámetros.

### Tipos de métodos

- **Estático**
- **No estático**

>[!NOTE]
> Un método por definición, pertenece a una clase, por lo que hablar de "método de una clase" puede ser redundante y, por eso, simplemente se habla de "métodos".

---

## Ejemplo: Clase Pelota

- El método **no estático** no altera los valores de los atributos de la clase Pelota.
- El método **estático** sí afecta el atributo posiciones.

### Clase: Pelota

**Atributos:**
- `posiciones`: Lista de números

**Método estático:**
- `crear_rebote()`: Genera lista de posiciones (números) que permiten generar un rebote válido (el primer número debe ser mayor a 0, y luego intercala 0 con números mayores a 0, cada vez menores, hasta llegar a 0).

**Método no estático:**
- `rebotar()`: Asigna lista de posiciones válidas (que generan un rebote), a una pelota específica en su atributo posiciones.

---

## Métodos de una clase y diferencia con funciones

Los métodos se definen igual que las funciones, haciendo uso de la palabra reservada `def`, dando un nombre en **snake_case**, y definiendo los parámetros en caso de ser necesario.

La diferencia con las funciones está dada porque:
- Las funciones **no** se definen dentro de una clase y, por ende, no están asociadas a una clase ni a un objeto específico.
- En el caso de los métodos, a diferencia de las funciones, se debe hacer uso del decorador `@staticmethod` cuando se define un método estático, y se debe incluir el parámetro `self` para métodos no estáticos.

---

## Comparativa: Funciones vs Métodos

| Característica | Funciones | Métodos |
|----------------|-----------|---------|
| Se definen con la palabra reservada `def` | ✓ | ✓ |
| Su nombre por convención es en snake_case | ✓ | ✓ |
| Pueden o no tener parámetros | ✓ | ✓ |
| Pueden o no tener retorno | ✓ | ✓ |
| Se definen dentro de una clase | ✗ | ✓ |

---

## Definir un método estático

- Un método estático es aquel que se puede llamar **directamente desde la clase**, sin que se requiera crear una instancia de ella para hacer uso de él.
- Para definir un método estático, se requiere hacer uso del decorador `@staticmethod`.

### Ejemplo:

```python
# archivo pelota.py
class Pelota():
    posiciones = [3, 0, 2, 1, 0]
    
    @staticmethod
    def crear_rebote():
        return [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
```

---

## Decoradores

- Un decorador corresponde a un texto que comienza por el símbolo **"@"** y se escribe en la línea anterior a la definición de un método o una función.
- El texto que acompaña al símbolo "@" corresponde al nombre del decorador y lo que desencadena es el llamado a una función, que toma como argumento la función definida a continuación del decorador.
- Para que un método sea estático, además de tener el decorador `@staticmethod`, dentro de su lógica **no puede modificar los valores de los atributos de la clase**.

---

## ¿Cómo hacer el llamado a un método estático?

Hacer uso de la sintaxis de punto `.` directamente desde el nombre de la clase.

### Ejemplo:

```python
# desde otro archivo, se importa la clase
from pelota import Pelota

# Se llama al método directamente desde la clase, sin haber creado un objeto o instancia de pelota
print(Pelota.crear_rebote())

# La salida del print anterior será:
# [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
```

### Ejemplo adicional:

```python
# archivo pelota.py
class Pelota():
    posiciones = [3, 0, 2, 1, 0]
    
    @staticmethod
    def crear_rebote():
        posiciones = [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
        return posiciones
    
    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote()
        print(Pelota.posiciones)

# La salida será [3, 0, 2, 1, 0]
Pelota.imprimir_posiciones()
```

---

## Ejercicio Guiado: Uso de la clase del Medicamento

### Contexto

Desde la cadena farmacéutica donde se está desarrollando el software que permite manejar el stock de medicamentos, te informan que se requiere agregar una nueva funcionalidad al programa: cada medicamento creado no puede tener un precio igual o menor a cero.

### Requerimientos

1. Agregar dentro de la clase `Medicamento` un método estático que permita hacer la validación de que un argumento ingresado sea mayor a 0 o no, devolviendo `True` de cumplir con esta condición, y `False` en caso contrario.

2. Crear un script que al ejecutarse solicite al usuario ingresar un precio, y mediante el método solicitado se informe en pantalla si es o no un precio válido.

3. El script debe validar que todos los medicamentos tengan el mismo IVA y descuento. Crear dos instancias de la clase y corroborar que ambas instancias tienen los mismos valores en estos atributos. De ser así, mostrar en pantalla los valores de descuento e IVA, haciendo referencia directamente a la clase.

---

## Solución del Ejercicio Guiado

### Paso 1: Definir clase Medicamento

```python
# archivo medicamento.py
class Medicamento():
    descuento = 0.05
    IVA = 0.18
```

### Paso 2: Definir método estático `validar_mayor_a_cero`

```python
# archivo medicamento.py
class Medicamento():
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_mayor_a_cero(numero: int):
        # Implementación en el siguiente paso
        pass
```

### Paso 3: Implementar lógica del método

```python
# archivo medicamento.py
class Medicamento():
    descuento = 0.05
    IVA = 0.18
    
    @staticmethod
    def validar_mayor_a_cero(number: int):
        return numero > 0
```

### Paso 4: Importar la clase en programa.py

```python
# archivo programa.py
from medicamento import Medicamento
```

---

### Paso 5: Solicitar precio al usuario

```python
# archivo programa.py
from medicamento import Medicamento

precio = int(input("Ingrese un precio a validar:\n"))
```

### Paso 6: Llamar al método y almacenar retorno

```python
# archivo programa.py
from medicamento import Medicamento

precio = int(input("Ingrese un precio a validar:\n"))
es_valido = Medicamento.validar_mayor_a_cero(precio)
```

### Paso 7: Mostrar resultado

```python
# archivo programa.py
from medicamento import Medicamento

precio = int(input("Ingrese un precio a validar:\n"))
es_valido = Medicamento.validar_mayor_a_cero(precio)

if es_valido:
    print("El precio ingresado es válido")
else:
    print("El precio ingresado no es válido")
```

---

### Paso 8: Crear dos instancias de la clase

```python
m1 = Medicamento()
m2 = Medicamento()
```

### Paso 9: Validar que ambos atributos son iguales

```python
m1 = Medicamento()
m2 = Medicamento()

if m1.IVA == m2.IVA and m1.descuento == m2.descuento:
    # Continuar en el siguiente paso
```

### Paso 10: Mostrar valores de los atributos

```python
m1 = Medicamento()
m2 = Medicamento()

if m1.IVA == m2.IVA and m1.descuento == m2.descuento:
    print("Todas las instancias tienen igual descuento e IVA")
    print("El valor del IVA es: ", Medicamento.IVA)
    print("El valor del descuento es:", Medicamento.descuento)
```

---

### Salida esperada

Al ejecutar el script `programa.py` e ingresando un precio de 1000:

```
Ingrese un precio a validar: 1000
El precio ingresado es válido
Todas las instancias tienen igual descuento e IVA
El valor del IVA es: 0.18
El valor del descuento es: 0.05
```

---

## Objetos

En Programación Orientada a Objetos, un objeto tiene **características** y **acciones** que realiza:

- Las **características** se denominan **atributos**, los cuales se definen dentro de la clase.
- Las **acciones** que realiza el objeto se definen en los **métodos**.

Los métodos pueden o no alterar el estado de un objeto, es decir, modificar los valores de los atributos en una instancia específica de la clase, en un momento dado.

En general, la capacidad que tiene el objeto de realizar una acción determinada es lo que se conoce como **comportamiento**.

---

## Métodos y Comportamiento

- **Acciones** que pueden ocurrir dentro de un objeto; estas acciones son comunes a todos los objetos de un mismo tipo, por lo que se definen dentro de una clase como métodos.
- Puede o no modificar el estado del objeto, pero siempre estará relacionado con acciones características del objeto, por ello, se definen en el "molde" de un objeto que corresponde a la clase.

---

## Método vs Comportamiento

| Característica | Método | Comportamiento |
|----------------|--------|----------------|
| Se relaciona con las acciones que realizan todos los objetos de una clase específica | ✓ | ✓ |
| Ejecución de la acción definida para un objeto | ✗ | ✓ |
| Define una acción que realiza un objeto | ✓ | ✓ |

---

## Conceptos Clave

- **Método:** Corresponden a los bloques de código definidos dentro de una clase que permiten realizar un comportamiento una vez que son llamados.

- **Comportamiento:** Es la acción en sí que realiza el objeto, mientras que el método es el código que define dicha acción. Se puede decir además que un comportamiento corresponde también cuando se realiza uno o más llamados de métodos, dando así un resultado.

### Ejemplo:

```python
class Pelota:
    @staticmethod
    def crear_rebote():
        return [2, 0, 1, 0]
    
    def rebotar(self):
        self.posiciones = self.crear_rebote()
```

> El comportamiento del objeto, mediante métodos no estáticos, permite también modificar los valores de los atributos de una instancia, es decir, modificar el estado de un objeto.