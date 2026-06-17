# Algoritmos y Condicionales: La lógica de la programación

## ¿Qué es un algoritmo?

Un **algoritmo** es un conjunto de instrucciones definidas, ordenadas y finitas que permiten resolver un problema o realizar una tarea. En la vida cotidiana usamos algoritmos constantemente: una receta de cocina, un manual de instrucciones o los pasos para atarte los zapatos son ejemplos de algoritmos.

En programación, un algoritmo es el **paso previo** a escribir el código. Primero defines la solución al problema (el algoritmo) y luego lo codificas en un lenguaje que la computadora pueda entender.

---

## Partes de un algoritmo

Todo algoritmo consta de tres partes fundamentales:

1. **Entrada (Input):** La información inicial con la que trabajará el algoritmo.
2. **Proceso:** La secuencia de pasos ordenados que transforman la entrada para obtener una solución.
3. **Salida (Output):** El resultado final del algoritmo.

---

## Características de un algoritmo

Para que un algoritmo sea válido debe cumplir con estas características:

- **Preciso:** Cada paso debe estar claramente definido, sin ambigüedades.
- **Ordenado:** Los pasos deben seguir una secuencia clara y lógica.
- **Finito:** Debe tener un número determinado de pasos; no puede ser infinito.
- **Definido:** Dado un mismo conjunto de datos de entrada, siempre debe producir el mismo resultado.
- **Concreto:** Debe ofrecer una solución determinada para el problema planteado.

---

## Diseño básico de resolución de problemas

### 1. Descomposición del problema

El primer paso para resolver un problema es **dividirlo en problemas más pequeños**. Esta técnica permite abordar cada subproblema de forma independiente y simplifica la solución global.

**Ejemplo:** Calcular el promedio de calificaciones de un alumno.

- Subproblema 1: Sumar todas las calificaciones.
- Subproblema 2: Contar cuántas calificaciones hay.
- Subproblema 3: Dividir la suma entre el total.

### 2. Identificación de la entrada y salida

Antes de escribir cualquier código, define claramente qué datos necesitas (entrada) y qué resultado esperas obtener (salida).

**Ejemplo:** Calcular el área de un rectángulo.

- Entrada: base y altura.
- Salida: área (base × altura).

### 3. Diseño de la secuencia de pasos

Una vez que tienes clara la entrada y la salida, diseña los pasos intermedios. Generalmente esto implica:

- Declarar variables para almacenar datos.
- Realizar operaciones aritméticas o lógicas.
- Tomar decisiones (condicionales).
- Repetir acciones (bucles).

### 4. Verificación del algoritmo

Prueba tu algoritmo con diferentes valores de entrada para asegurarte de que siempre produce el resultado correcto.

**Ejemplo de verificación:** Si tu algoritmo calcula el promedio, pruébalo con valores donde conozcas el resultado esperado (ej: calificaciones: 10, 10, 10 → promedio 10).

---

## Estructuras de decisión (Condicionales)

Hasta ahora, todos los programas que has escrito se ejecutan en **orden lineal**: una instrucción después de otra sin importar lo que pase. Pero en programación, muchas veces necesitamos que el código **tome decisiones** basadas en ciertas condiciones.

### ¿Qué son las estructuras condicionales?

Las estructuras condicionales permiten que un programa ejecute diferentes bloques de código dependiendo de si una condición se cumple o no. Es como tomar decisiones en la vida real: "Si llueve, llevo paraguas; si no, no lo llevo".

### La estructura `if` (si)

La forma más básica de condicional en JavaScript es `if`:

```javascript
if (condición) {
    // Código que se ejecuta si la condición es verdadera
}
```

**Ejemplo en contexto:**
```javascript
let edad = parseInt(prompt("¿Cuántos años tienes?"));

if (edad >= 18) {
    console.log("Eres mayor de edad");
}
```

### La estructura `if...else` (si...sino)

Cuando queremos ejecutar un código si la condición se cumple y otro diferente si no se cumple, usamos `else`:

```javascript
if (condición) {
    // Código si la condición es verdadera
} else {
    // Código si la condición es falsa
}
```

**Ejemplo:**
```javascript
let edad = parseInt(prompt("¿Cuántos años tienes?"));

if (edad >= 18) {
    console.log("Eres mayor de edad");
} else {
    console.log("Eres menor de edad");
}
```

### La estructura `if...else if...else` (múltiples condiciones)

Para evaluar varias condiciones posibles, encadenamos `else if`:

```javascript
if (condición1) {
    // Código si condición1 es verdadera
} else if (condición2) {
    // Código si condición2 es verdadera
} else {
    // Código si ninguna condición se cumple
}
```

**Ejemplo:**
```javascript
let nota = parseFloat(prompt("Ingresa tu nota (0-10):"));

if (nota >= 9) {
    console.log("Sobresaliente");
} else if (nota >= 7) {
    console.log("Notable");
} else if (nota >= 5) {
    console.log("Aprobado");
} else {
    console.log("Suspenso");
}
```

---

## Operadores lógicos

Los operadores lógicos nos permiten **combinar múltiples condiciones** en una sola expresión.

### Operador AND (`&&`) - "Y"

El operador `&&` devuelve `true` **solo si todas** las condiciones son verdaderas.

**Tabla de verdad:**
| Condición 1 | Condición 2 | Resultado |
|-------------|-------------|-----------|
| true        | true        | true      |
| true        | false       | false     |
| false       | true        | false     |
| false       | false       | false     |

**Ejemplo:**
```javascript
let edad = parseInt(prompt("Ingresa tu edad:"));
let tieneCarnet = prompt("¿Tienes carnet de conducir? (si/no)") === "si";

if (edad >= 18 && tieneCarnet) {
    console.log("Puedes conducir legalmente");
} else {
    console.log("No puedes conducir");
}
```

### Operador OR (`||`) - "O"

El operador `||` devuelve `true` si **al menos una** de las condiciones es verdadera.

**Tabla de verdad:**
| Condición 1 | Condición 2 | Resultado |
|-------------|-------------|-----------|
| true        | true        | true      |
| true        | false       | true      |
| false       | true        | true      |
| false       | false       | false     |

**Ejemplo:**
```javascript
let esEstudiante = prompt("¿Eres estudiante? (si/no)") === "si";
let esJubilado = prompt("¿Eres jubilado? (si/no)") === "si";

if (esEstudiante || esJubilado) {
    console.log("Tienes derecho a descuento");
} else {
    console.log("No tienes descuento");
}
```

### Operador NOT (`!`) - "No"

El operador `!` invierte el valor de una condición. Lo que era `true` se convierte en `false` y viceversa.

**Tabla de verdad:**
| Condición | !Condición |
|-----------|------------|
| true      | false      |
| false     | true       |

**Ejemplo:**
```javascript
let usuarioLogeado = false;

if (!usuarioLogeado) {
    console.log("Por favor, inicia sesión");
} else {
    console.log("Bienvenido usuario");
}
```

---

## Jerarquía de operadores (orden de evaluación)

Cuando combinamos operadores aritméticos, de comparación y lógicos, JavaScript los evalúa en este orden:

1. **Operadores aritméticos** (`*`, `/`, `%`, `+`, `-`)
2. **Operadores de comparación** (`>`, `<`, `>=`, `<=`, `==`, `===`, `!=`, `!==`)
3. **Operadores lógicos** (`!`, `&&`, `||`)

**Ejemplo de evaluación:**
```javascript
let edad = 25;
let tieneLicencia = true;

// Esta expresión se evalúa así:
// 1. Primero: edad >= 18 → true
// 2. Luego: true && tieneLicencia → true (porque tieneLicencia es true)
if (edad >= 18 && tieneLicencia) {
    console.log("Puedes conducir");
}
```

---

## Ejemplo completo: Algoritmo con condicionales

**Problema:** Determinar si un número es positivo, negativo o cero.

**Algoritmo:**
1. Solicitar un número al usuario.
2. Si el número es mayor que 0, mostrar "Positivo".
3. Si el número es menor que 0, mostrar "Negativo".
4. Si el número es igual a 0, mostrar "Cero".

**Implementación:**
```javascript
// 1. Entrada de datos
let numero = parseFloat(prompt("Ingresa un número:"));

// 2. Proceso y salida
if (numero > 0) {
    console.log("El número es positivo");
} else if (numero < 0) {
    console.log("El número es negativo");
} else {
    console.log("El número es cero");
}
```

---

## Ejercicios propuestos

### Nivel 1: Condicionales básicos (`if` y `if...else`)

**Ejercicio 1: Mayor de edad**
> Solicita la edad del usuario y determina si es mayor de edad (18 años o más). Si lo es, muestra "Eres mayor de edad"; si no, muestra "Eres menor de edad".

**Ejercicio 2: Número positivo o negativo**
> Pide un número al usuario y determina si es positivo o negativo. Si es cero, muéstralo también.

**Ejercicio 3: Par o impar**
> Pide un número al usuario y determina si es par o impar utilizando el operador módulo (`%`). Muestra el resultado.

**Ejercicio 4: Aprobado o reprobado**
> Solicita al usuario una calificación (0-10). Si es mayor o igual a 5, muestra "Aprobado"; de lo contrario, muestra "Reprobado".

### Nivel 2: Condicionales múltiples (`if...else if...else`)

**Ejercicio 5: Rango de edad**
> Pide la edad del usuario y clasifícala en:
- "Niño" (0-12 años)
- "Adolescente" (13-17 años)
- "Adulto" (18-64 años)
- "Jubilado" (65 años o más)

**Ejercicio 6: Calculadora de IMC con diagnóstico**
> Calcula el IMC (peso / altura²) y muestra:
- "Bajo peso" si IMC < 18.5
- "Normal" si IMC entre 18.5 y 24.9
- "Sobrepeso" si IMC entre 25 y 29.9
- "Obesidad" si IMC ≥ 30

**Ejercicio 7: Nota con texto**
> Pide una nota (0-10) y muestra la calificación textual:
- 9-10: "Sobresaliente"
- 7-8.9: "Notable"
- 5-6.9: "Aprobado"
- 0-4.9: "Suspenso"

**Ejercicio 8: Calculadora de descuento por edad**
> Pide la edad del usuario y aplica un descuento:
- Menores de 12 años: 50% de descuento
- De 12 a 17 años: 25% de descuento
- De 18 a 64 años: sin descuento
- 65 años o más: 30% de descuento
> Pide el precio original y muestra el precio final con descuento.

### Nivel 3: Operadores lógicos (`&&`, `||`, `!`)

**Ejercicio 9: Verificador de acceso**
> Pide la edad del usuario y si tiene carnet de conducir (respuesta "si" o "no"). Usa el operador `&&` para determinar si puede conducir. Si tiene 18 años o más Y tiene carnet, muestra "Puede conducir", en caso contrario "No puede conducir".

**Ejercicio 10: Descuento especial**
> Pide al usuario si es estudiante y si es jubilado (responde "si" o "no"). Usa el operador `||` para dar un 20% de descuento si es estudiante O jubilado. Pide el precio original y muestra el precio final.

**Ejercicio 11: Rango de temperatura**
> Pide la temperatura actual. Usa `&&` para verificar si está en el rango confortable (entre 18°C y 25°C). Muestra "Temperatura confortable" o "Temperatura incómoda".

**Ejercicio 12: Validación de usuario**
> Crea un programa que pida usuario y contraseña. Usa `&&` para verificar si el usuario es "admin" Y la contraseña es "1234". Si se cumple, muestra "Acceso concedido"; si no, "Acceso denegado".

### Nivel 4: Combinando condiciones complejas

**Ejercicio 13: Calculadora de envío**
> Pide el total de la compra y la distancia del envío en km. Aplica estas reglas:
- Si el total es mayor a $100, el envío es gratuito (sin importar la distancia).
- Si el total es entre $50 y $100, el envío es gratuito solo si la distancia es menor a 10km.
- Si el total es menor a $50, el envío cuesta $5 sin importar la distancia.
> Muestra el costo final (total + envío).

**Ejercicio 14: Clasificador de triángulos**
> Pide tres números que representan los lados de un triángulo y determina:
- Si es equilátero (todos los lados iguales)
- Si es isósceles (dos lados iguales)
- Si es escaleno (todos los lados diferentes)
> Usa `===` y `&&` para comparar los lados.

**Ejercicio 15: Verificador de vacaciones**
> Pide el día de la semana (1-7, donde 1=lunes) y el mes (1-12). Determina si es fin de semana (sábado o domingo) o si es agosto (mes de vacaciones). Usa `||` para mostrar "Es día de vacaciones" si es fin de semana O es agosto; en caso contrario, "Día laboral".
