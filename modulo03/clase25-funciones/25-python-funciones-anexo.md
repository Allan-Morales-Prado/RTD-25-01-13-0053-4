# Funciones - Parte I

## Explicación teórico-práctica del *Ejercicio Guiado: Estandarización*

>[!IMPORTANT]
>Las computadoras tienen la capacidad de realizar operaciones matemáticas de gran complejidad en un parpadear. Son muy utilizadas en áreas como la estadística, probabilidad, álgebra, cálculo, métodos numéricos, entre otras áreas de la matemática al igual que en otras áreas donde se trabajan con muchos datos, especialmente numéricos.

A continuación se presenta el enunciado del PPT, seguido de una explicación rigurosa de cada fómula y su implementación paso a paso en codigo Python.

### Enunciado
Calcular la versión estandarizada para el vector `[1, 2, 3, 4, 5, 6]`
La función tiene que retornar la media, la desviación estándar y la versión estandarizada.

La estandarización es un proceso en el cual un vector (una lista de números) de datos es transformado y llevado a un rango de datos más acotado. Para ello es necesario el cálculo de dos estadísticos que  permitirán llevarlo a este estado:

- La media aritmética se calcula como $\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} $
- La desviación estándar muestral se define como:

$$
s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1} }
$$
- El vector estandarizado se define como: 
```math
\mathbf{z} = \left[ z_1, z_2, \dots, z_n \right] = \left[ \frac{x_1 - \bar{x}}{s}, \frac{x_2 - \bar{x}}{s}, \dots, \frac{x_n - \bar{x}}{s} \right]
```
>[!IMPORTANT]
>Las fórmulas mostradas en la PPT se ven diferentes.
>Sin embargo, estas fórmulas son equivalentes, sobretodo la tercera fórmula, donde te ofrezco una versión más parecida a una lista de python.

## Explicación de la media aritmética

$$\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n} $$

- $\bar{x}$, es como se simboliza la media aritmética, más conocida como **Promedio Simple** o **Promedio**.
- $n$, es la cantidad de datos numéricos.
- $\sum_{i=1}^{n} x_i$, es la sumatoria (o suma total) comprendida desde el i-ésimo término, hasta el n-ésimo término.

**EJEMPLO**

Tengo la siguiente lista de números: 2, 3, 1, 8 y 6

La analogía es clave:

| Estadística (Matemáticas)  | Lenguaje Python  |
|---|---|
| $$2, 3, 1, 8, 6$$  | `[2, 3, 1, 8, 6]` |
| $$n = 5$$  | `len([2, 3, 1, 8, 6])` |
| $$x_i = \begin{cases} 2, & \text{si } i = 1 \\ 3, & \text{si } i = 2 \\ 1, & \text{si } i = 3 \\ 8, & \text{si } i = 4 \\ 6, & \text{si } i = 5 \\  \end{cases}$$  | <code># si x = [2, 3, 1, 8, 6]</code><br><code># Entonces:</code><br><code># x[0] == 2</code><br><code># x[1] == 3</code><br><code># x[2] == 1</code><br><code># x[3] == 8</code><br><code># x[4] == 6</code> |
| $$\sum_{i=1}^{n} x_i = x_1 + x_2 +x_3 +... +x_n$$  | `sum([2, 3, 1, 8, 6])` |
| $$\frac{\sum_{i=1}^{n} x_i}{n} $$  | `sum([2, 3, 1, 8, 6]) / len([2, 3, 1, 8, 6])` |

## Explicación de la desviación estándar

$$
s = \sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1} }
$$

- $s$, es como se simboliza la desviación estándar. En ocasiones se utiliza la letra griega "sigma" minúscula ($ \sigma $).
- $n$, es la cantidad de datos numéricos.
- $\sum_{i=1}^{n} (x_i - \bar{x})^2$, es la sumatoria (o suma total) de los cuadrados de las diferencias entre cada término y la media (calculada anteriormente).

Analogía:
| Estadística (Matemáticas)  | Lenguaje Python  |
|---|---|
| $$2, 3, 1, 8, 6$$  | `[2, 3, 1, 8, 6]` |
| $$n = 5$$  | `len([2, 3, 1, 8, 6])` |
| $$(x_i - \bar{x})^2 = \begin{cases} (2 - \bar{x})^2, & \text{si } i = 1 \\ (3 - \bar{x})^2, & \text{si } i = 2 \\ (1 - \bar{x})^2, & \text{si } i = 3 \\ (8 - \bar{x})^2, & \text{si } i = 4 \\ (6 - \bar{x})^2, & \text{si } i = 5 \\  \end{cases}$$  | <code># si x = [2, 3, 1, 8, 6]</code><br><code># y 'm' la media Entonces:</code><br><code># (x[0] - m)**2</code><br><code># (x[1] - m)**2</code><br><code># (x[2] - m)**2</code><br><code># (x[3] - m)**2</code><br><code># (x[4] - m)**2</code> |
| $$\sum_{i=1}^{n} (x_i - \bar{x})^2 = (x_1 - \bar{x})^2+...+(x_n - \bar{x})^2$$  | `sum([(i - m)**2 for i in x])` |
| $$\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1}$$  | `sum([(i - m)**2 for i in x]) / (len(x) - 1)` |
| $$\sqrt{\frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n-1} }$$  | `math.sqrt(sum([(i - m)**2 for i in x]) / (len(x) - 1))` |

## Explicación del vector estandarizado

$$\bar{V} = \frac{v - \bar{x}}{s}$$

- $\bar{V}$ en realidad se utiliza más el símbolo $\mathbf{z}$ y simboliza al vector estandarizado
- $\bar{x}$, es la media
- $s$, es la desviación estándar
- $v$ aquí es un vector (lista de i números)

A por la analogía:

| Estadística (Matemáticas)  | Lenguaje Python  |
|---|---|
| $$2, 3, 1, 8, 6$$  | `[2, 3, 1, 8, 6]` |
| $$\bar{x}$$  | `sum(2, 3, 1, 8, 6) / len([2, 3, 1, 8, 6])` |
| $$s$$  | `math.sqrt(sum([(i - m)**2 for i in x]) / (len(x) - 1))` |
| $$\frac{v - \bar{x}}{s} = \left[ \frac{x_1 - \bar{x}}{s}, \frac{x_2 - \bar{x}}{s}, \dots, \frac{x_n - \bar{x}}{s} \right]$$  | <code># si x = [2, 3, 1, 8, 6]</code><br><code># 'm' la media</code><br><code># y 's' la desviación estándar</code><br><code>v = [(i - m) / s for i in x]</code> |

## Código sin Python Comprehension
```python
import math

def media(lista : list[int | float]) -> float:
  return sum(lista) / len(lista)

def sdd(lista : list[int | float], media : int | float):
  # diff = [(elemento - media) ** 2 for elemento in lista]
  suma = 0
  for elemento in lista:
    suma += (elemento - media)**2
  return math.sqrt(suma /(len(lista) - 1))

def resultado(lista : list[int | float]):
  m = media(lista)
  sd = sdd(lista, m)
  # lista_estandarizada = [(valor - m) / sd for valor in lista]
  lista_estandarizada = []
  for valor in lista:
    lista_estandarizada.append((valor - m) / sd)
  return m, sd, lista_estandarizada

lista = [1, 2, 3, 4, 5, 6]

m, desv_st, l_e = resultado(lista)
print("La media es: ", m)
print("La desviación estandard es: ", desv_st)
print("La lista estandarizada es: ", l_e)
```