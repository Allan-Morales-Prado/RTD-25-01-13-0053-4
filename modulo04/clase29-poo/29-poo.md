# Introducción a la programación orientada a objetos con Python

## Contenido

1. [Qué entendemos por *paradigma*](#qué-entendemos-por-paradigma)
   - [Programación estructurada](#programación-estructurada)
   - [Programación Orientada a Objetos](#programación-orientada-a-objetos)
2. [Clases, atributos estáticos y objetos](#clases-atributos-estáticos-y-objetos)
   - [Clases](#clases)
   - [Tipos de clases](#tipos-de-clases)
   - [Objetos](#objetos)
   - [Atributos](#atributos)
3. [Definiendo una clase](#definiendo-una-clase)
4. [Instanciar un objeto](#instanciar-un-objeto)

## ¿Qué entendemos por paradigma?
Un paradigma de programación es un estilo o enfoque que define cómo abordar el diseño y la escritura de un programa de software.

Cada paradigma tiene sus propias características, reglas, técnicas y principios que lo hacen más o menos adecuado para resolver diferentes tipos de problemas. La elección de un paradigma influye en aspectos como la legibilidad, el mantenimiento y la escalabilidad del código.

---

### Programación estructurada

#### Formas de programar

Habitualmente, cuando aprendemos a programar, lo hacemos utilizando instrucciones y comandos que construyen funciones. Así, nos enfocamos en resolver tareas, a partir de acciones específicas.

#### ¿En qué consiste?

Es un paradigma de programación, que se centra principalmente en la construcción de un programa mediante bloques de subrutinas, las cuales son básicamente funciones que realizan tareas específicas.

>[!TIP]
>Básicamente, aprendimos a programar con el paradigma estructural de programación en el módulo 3:
>_Programa = Algoritmos + Estructuras de Datos_


---

### Programación orientada a objetos

#### ¿Qué es?
- Forma de estructurar un programa, que se basa en empaquetar comportamientos y propiedades similares en objetos individuales.

#### Beneficios de la POO

- Abstracción y modelado del mundo real
- Reutilización de código
- Mantenibilidad y escalabilidad
- Facilidad de colaboración
- Encapsulación y ocultamiento de la información

#### Ventajas

- Permite resolver problemas.
- Hace un nexo entre una problemática real y su resolución, mediante una codificación sencilla y fácil de entender.
- No solamente permite resolver un problema mediante un objeto aislado, sino que también establece relaciones entre distintos objetos.

---

### POO vs PE

| Característica                 | Orientada a objetos                                                                                                 | Estructurada                                                                                                   |
| :----------------------------- | :----------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **¿Cómo se organiza el programa?** | En torno a objetos que representan entidades del mundo real.                                                         | En una secuencia de procedimientos o funciones.                                                                |
| **¿En qué se enfoca?**         | En la encapsulación, la herencia y el polimorfismo.                                                                 | En la claridad, la simplicidad y la modularidad del código.                                                    |
| **¿Qué utiliza?**              | Clases y objetos como las unidades fundamentales de diseño y abstracción.                                           | Estructuras de control como secuenciales, condicionales y bucles para controlar el flujo del programa.         |
| **¿Cómo se manipulan los objetos?** | Los objetos encapsulan datos (atributos) y comportamiento (métodos) relacionados, lo que permite un diseño más modular y mantenible. | Las variables y los procedimientos son entidades independientes y se manipulan por separado.                       |

---

#### Orientación a objetos aplicada en la vida cotidiana: El objeto “pelota”

Una pelota es un objeto en el mundo real… pero puede haber muchos tipos de pelotas.

- Cada una de ellas puede estar confeccionada con distinto material, tener diferentes colores, etc.
- Podemos jugar diferentes deportes, pueden rodar, dar bote, etc.
- Andrea y Luis compran pelotas iguales… ¿tienen la misma pelota?

---

**Conceptos clave:**

- Las características de la pelota se asocian con los **atributos** de un objeto.
- Las acciones que se pueden realizar, se asocian con los **métodos** del objeto.
- Ciertamente, y pese a que puedan ser idénticas, la pelota de Andrea es distinta a la pelota de Luis. Cada una es un objeto diferente.

Ahora bien, ¿cómo construimos cada pelota?

---

## Clases, atributos estáticos y objetos

### Clases

- Código que define qué contiene y qué hace un objeto de un tipo de dato, el cual corresponde al nombre de la clase.
- Por esta razón, muchas veces se hace la analogía diciendo que la clase corresponde a un **“plano”** o **“molde”** que permite fabricar objetos de un tipo específico.
- Si quieres profundizar más sobre qué son las clases y cómo trabajar con ellas en Python, puedes revisar la [documentación oficial](https://docs.python.org/3/tutorial/classes.html) en este enlace.

#### Ejemplo: Clase Pelota

En la siguiente imagen, puedes ver que la clase `Pelota` constituye el molde para crear tres objetos diferentes. Cada objeto, o instancia de la clase `Pelota`, tiene sus propios valores para los atributos, donde todos tienen la capacidad de rebotar, dado por el método “rebotar” definido en la clase.

---

### Ejemplo: Clase Automóvil

Imagina que quieres crear un programa para gestionar información sobre automóviles. Necesitarás definir las características comunes a todos los automóviles, como marca, modelo y consumo de combustible, así como las acciones que pueden realizar, como calcular el consumo de combustible con base en una distancia recorrida.

#### Atributos

- `marca`: La marca del automóvil (e.g., "Toyota").
- `modelo`: El modelo del automóvil (e.g., "Corolla").
- `consumo_por_km`: El consumo de combustible en litros por kilómetro (e.g., 0.05 litros/km).

#### Métodos

- `__init__(self, marca, modelo, consumo_por_km)`: Constructor que inicializa los atributos del automóvil.
- `calcularConsumo(self, distancia)`: Método que calcula el consumo de combustible en función de la distancia recorrida.

---

### Tipos de clases

**En Python, todas las clases son públicas por defecto**. Es decir, no hay un mecanismo del lenguaje que impida que importes o heredes de cualquier clase definida en cualquier módulo.

Sin embargo, en el ecosistema de Python, "clase pública" se refiere a una _convención de diseño_:

- **Convención de nomenclatura:** Si una clase está diseñada para ser usada desde fuera del módulo, se documenta como "pública".

- **El prefijo guion bajo (`_`):** Si una clase comienza con un guion bajo (ej: `_MiClaseInterna`), es una convención que indica "esta clase es privada o interna". Los desarrolladores entienden que no deben usarla fuera de ese módulo, pero el lenguaje no les impedirá hacerlo.

**Ejemplo**

```python
# Esto es una clase pública por convención (sin guion bajo)
class Calculadora:
    def sumar(self, a, b):
        return a + b

# Esto es una clase "privada" por convención (con guion bajo)
class _LoggerInterno:
    def log(self, msg):
        print(msg)
```

---

### Objetos

Un objeto se define como la **instancia de una clase**, es decir, una estructura de datos construida a partir de una clase y que tiene valores iniciales y métodos invocables <ins>en las diferentes interfaces de acceso definidas</ins>[^1].
[^1]: En Python esto no funciona así. Como se comentó en [Tipos de Clases](#tipos-de-clases) clases, Python no tiene interfaces de acceso estricta como en Java, C++ y C#. En Python todo es accesible desde cualquier parte del código, pero las convenciones en el código cumplen solamente con informar a los desarrolladores sobre el uso adecuado de las clases.

En Python, **todo es un objeto** y todo objeto tiene un tipo asociado, dado por la clase a la cual pertenece. Algunas de estas clases son nativas de Python y corresponden principalmente a:

- Tipos de datos básicos (`bool`, `float`, `str`, `int`)
- Estructuras de datos (`list`, `dict`, `tuple`)
- Funciones (`function`)
- ¡Y muchos más! (`class`)

#### Ejemplos en Python

```python
variable = "hola"

def suma(num1, num2):
    return num1 + num2

class Gato():
    hace = "miau"
    colores = ["rojo", "verde"]
```

Si quieres profundizar más sobre qué son y cómo trabajar con objetos en Python, puedes revisar la [documentación oficial](https://docs.python.org/3/reference/datamodel.html) en este enlace.

>[!TIP]
>**Ahora tiene sentido**
>Se abordó el uso de `type()` como una <ins>función</ins>. Pero ¿Qué nos dice *VSCode* sobre lo que es en realidad?
>
>También se dijo que `type()` nos indica el <ins>tipo de dato</ins> al que corresponde un valor, pero la salida que entrega tiene lo siguiente: `<class 'nombre_de_clase'>`
>
>Otra forma de conocer el tipo de un valor u objeto es mediante el atributo especial `__class__`

---

### Atributos

Contenedor de un valor o de un conjunto de valores, definido dentro de una clase que adquiere un tipo de dato según el valor que se le asigne.

Es decir, un atributo es análogo a una variable de Python, pero que en este caso se define dentro de una clase, a diferencia de una variable cualquiera de Python que no necesita definirse dentro de una clase. Por lo tanto, para acceder al atributo o modificar su valor, se debe hacer por medio de la clase.

#### Tipos de atributos

| Características                                   | Atributos de clase | Atributos de instancia |
| :------------------------------------------------ | :----------------: | :--------------------: |
| Puede contener un dato o conjunto de datos        |         ✓          |           ✓            |
| Su tipo de dato está dado por el valor asignado   |         ✓          |           ✓            |
| Se define dentro de una clase                     |         ✓          |           ✓            |
| Se puede leer su valor sin crear una instancia    |         ✓          |           ✗            |

- **Estáticos o de clase:** Pertenecen a la definición de la clase como tal, por lo que es posible acceder a ellos o asignarles un valor, directamente desde la clase, sin necesidad de generar un objeto o instancia.
- **No estáticos o de instancia:** No pertenecen a la definición de la clase como tal, por lo que para acceder a ellos o asignarles un valor se requiere primero crear un objeto (o instancia) de la clase.

---

### Resumen: Clase vs Objeto

- **Clase:** Corresponde al conjunto de atributos y métodos que permiten definir un objeto.
- **Objeto:** Corresponde al conjunto de datos y métodos definidos por la clase a la cual pertenece, en una instancia específica de ella. Por ello, normalmente se tratan los términos objeto e instancia como sinónimos.

---

## Definiendo una clase

El código que pertenece a la clase se escribe en la línea siguiente, por lo general con una indentación de 4 espacios.

Si se quiere definir una clase sin atributos ni métodos, simplemente se debe escribir la palabra reservada `pass`.

---

### Ejercicio guiado: "Definir la clase medicamento"

#### Enunciado

Trabajas como programador para una cadena de farmacias que desea desarrollar un software para manejar su stock de medicamentos.

Como primera entrega, debes definir la clase que permite crear objetos de tipo `Medicamento`, los que tienen un descuento de 5% y un IVA de 18%.

#### Solución

**Paso 1:** Definir la clase `Medicamento`.

```python
class Medicamento():
```

**Paso 2:** Agregar atributo `descuento` con valor `0.05`.

```python
class Medicamento():
    descuento = 0.05
```

**Paso 3:** Agregar atributo `IVA` con valor `0.18`.

```python
class Medicamento():
    descuento = 0.05
    IVA = 0.18
```

---

## Instanciar un objeto

### ¿Cómo instanciar objetos a partir de una clase?

Para instanciar o crear un objeto en Python a partir de una clase, se debe escribir el nombre de esta, seguido de paréntesis redondos de apertura y cierre `()` y hacer la asignación en una variable.

#### Ejemplo 1: Creación básica

**archivo pelota.py**
```python
class Pelota():
    forma = "redondeada"
```

**archivo objetos.py**
```python
from pelota import Pelota

pelota_de_andy = Pelota()

# Salida: "redondeada" (valor del atributo forma)
print(pelota_de_andy.forma)
```

#### Consideraciones importantes

1.  La instancia se crea al momento de escribir el nombre de la clase seguido de los paréntesis (`Pelota()`), pero si no se hace la asignación en una variable, no se podrá hacer uso de esa instancia.
2.  El objeto o instancia de la clase, tiene la capacidad de hacer referencia a atributos de la clase, utilizando la sintaxis de **“punto”** (`.`): `instancia.atributo`.

#### Ejemplo 2: Uso de módulos

Si la clase que se desea utilizar está definida en un módulo, también es posible hacer uso de ella, para lo cual primero se debe importar la clase desde este módulo (en este caso, en el archivo `pelota.py`) al espacio principal de trabajo (archivo `objetos.py`).

---

### Ejercicio guiado: "Crear una instancia de Medicamento"

#### Enunciado

Continuemos con el ejercicio guiado anterior.

Desde la cadena farmacéutica, ahora solicitan que cada vez que se inicie el programa se debe generar una nueva instancia de un `Medicamento`.

Considera que el programa principal se ejecuta desde un archivo diferente a donde se ha definido la clase.

#### Solución

**Paso 1:** Importar la clase `Medicamento` desde el módulo `medicamento` (archivo `medicamento.py`), en el archivo actual (`programa.py`).

```python
# archivo programa.py
from medicamento import Medicamento
```

**Paso 2:** Instanciar clase `Medicamento` y almacenar la instancia en una variable.

```python
# archivo programa.py
from medicamento import Medicamento

mi_medicamento = Medicamento()
```
---

## Próxima sesión…

- Explica el concepto de método de una clase haciendo la distinción con el concepto de comportamiento de un objeto.
- Identifica los principios de abstracción y encapsulamiento de acuerdo al paradigma de orientación a objetos.


**Academia de talentos digitales**