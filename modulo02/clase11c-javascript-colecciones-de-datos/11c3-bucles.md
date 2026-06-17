# Bucles en JavaScript

## ¿Qué son los bucles?

Los **bucles** (o ciclos) son estructuras que permiten **repetir un bloque de código** varias veces. Son esenciales cuando necesitas realizar una misma operación múltiples veces o recorrer estructuras de datos como arrays.

## El bucle `for`

El bucle `for` es el más común y controlado. Tiene tres partes:

```javascript
for (inicialización; condición; incremento) {
    // Código que se repite
}
```

- **Inicialización:** Se ejecuta una vez al inicio
- **Condición:** Se evalúa antes de cada iteración, si es `true` continúa
- **Incremento:** Se ejecuta después de cada iteración

### Ejemplo básico

```javascript
// Imprimir números del 1 al 5
for (let i = 1; i <= 5; i++) {
    console.log(i);
}
// Resultado: 1, 2, 3, 4, 5
```

### Recorrer un array con `for`

```javascript
let frutas = ["manzana", "pera", "naranja", "uva"];

for (let i = 0; i < frutas.length; i++) {
    console.log(`Fruta ${i+1}: ${frutas[i]}`);
}
// Fruta 1: manzana
// Fruta 2: pera
// Fruta 3: naranja
// Fruta 4: uva
```

## El bucle `while`

El bucle `while` repite el código **mientras** una condición sea verdadera:

```javascript
while (condición) {
    // Código que se repite
}
```

### Ejemplo básico

```javascript
let contador = 1;
while (contador <= 5) {
    console.log(contador);
    contador++;
}
// Resultado: 1, 2, 3, 4, 5
```

### Recorrer array con `while`

```javascript
let numeros = [10, 20, 30, 40, 50];
let i = 0;

while (i < numeros.length) {
    console.log(numeros[i]);
    i++;
}
// Resultado: 10, 20, 30, 40, 50
```

## El bucle `do...while`

El bucle `do...while` ejecuta el código **al menos una vez** antes de verificar la condición:

```javascript
do {
    // Código que se repite
} while (condición);
```

### Ejemplo básico

```javascript
let numero;
do {
    numero = parseInt(prompt("Ingresa un número (0 para salir):"));
    console.log("Ingresaste:", numero);
} while (numero !== 0);
```

## Bucle `for...of` (ES6)

El `for...of` es una forma moderna y más legible de recorrer arrays:

```javascript
let frutas = ["manzana", "pera", "naranja"];

for (let fruta of frutas) {
    console.log(fruta);
}
// manzana
// pera
// naranja
```

## Bucle `for...in` para objetos

El `for...in` recorre las **propiedades** de un objeto:

```javascript
let persona = {
    nombre: "Ana",
    edad: 30,
    ciudad: "Madrid"
};

for (let clave in persona) {
    console.log(`${clave}: ${persona[clave]}`);
}
// nombre: Ana
// edad: 30
// ciudad: Madrid
```

## Combinando bucles con condicionales

```javascript
let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Mostrar solo números pares
for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] % 2 === 0) {
        console.log(`${numeros[i]} es par`);
    }
}
// 2 es par
// 4 es par
// 6 es par
// 8 es par
// 10 es par
```

## Bucles anidados

Los bucles pueden estar dentro de otros bucles:

```javascript
// Tabla de multiplicar del 1 al 3
for (let i = 1; i <= 3; i++) {
    console.log(`Tabla del ${i}:`);
    for (let j = 1; j <= 5; j++) {
        console.log(`${i} × ${j} = ${i * j}`);
    }
    console.log("---");
}
```

## Ejemplos prácticos

### Ejemplo 1: Suma de elementos en array

```javascript
let numeros = [5, 10, 15, 20, 25];
let suma = 0;

for (let i = 0; i < numeros.length; i++) {
    suma += numeros[i];
}

console.log(`La suma es: ${suma}`); // 75
```

### Ejemplo 2: Búsqueda en array

```javascript
let nombres = ["Ana", "Carlos", "María", "Juan", "Pedro"];
let nombreBuscado = prompt("¿Qué nombre buscas?");

let encontrado = false;
for (let i = 0; i < nombres.length; i++) {
    if (nombres[i] === nombreBuscado) {
        console.log(`¡${nombreBuscado} está en la posición ${i}!`);
        encontrado = true;
        break; // Sale del bucle cuando encuentra el nombre
    }
}

if (!encontrado) {
    console.log(`${nombreBuscado} no se encontró`);
}
```

### Ejemplo 3: Procesamiento de notas

```javascript
let notas = [7, 4, 9, 5, 3, 8, 6, 2];
let aprobados = 0;
let reprobados = 0;
let suma = 0;

for (let i = 0; i < notas.length; i++) {
    suma += notas[i];
    
    if (notas[i] >= 5) {
        aprobados++;
    } else {
        reprobados++;
    }
}

let promedio = suma / notas.length;
console.log(`Promedio: ${promedio.toFixed(2)}`);
console.log(`Aprobados: ${aprobados}`);
console.log(`Reprobados: ${reprobados}`);
```

### Ejemplo 4: Array de objetos con bucle

```javascript
let productos = [
    { nombre: "Laptop", precio: 800, stock: 5 },
    { nombre: "Mouse", precio: 25, stock: 20 },
    { nombre: "Monitor", precio: 200, stock: 3 },
    { nombre: "Teclado", precio: 60, stock: 8 }
];

// Mostrar productos con stock bajo
console.log("Productos con stock bajo (menos de 5 unidades):");
for (let i = 0; i < productos.length; i++) {
    if (productos[i].stock < 5) {
        console.log(`- ${productos[i].nombre}: ${productos[i].stock} unidades`);
    }
}

// Calcular valor total del inventario
let total = 0;
for (let i = 0; i < productos.length; i++) {
    total += productos[i].precio * productos[i].stock;
}
console.log(`Valor total del inventario: $${total}`);
```

## Ejercicios propuestos

### Nivel 1: Bucles básicos

**Ejercicio 1: Números del 1 al 100**
> Usa un bucle `for` para mostrar todos los números del 1 al 100 en consola.

**Ejercicio 2: Números pares**
> Muestra todos los números pares del 2 al 50 usando un bucle `for` y el operador `%`.

**Ejercicio 3: Suma acumulativa**
> Usa un bucle `for` para sumar los números del 1 al 100 y muestra el resultado final.

**Ejercicio 4: Tabla de multiplicar**
> Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10.

### Nivel 2: Bucles con arrays

**Ejercicio 5: Recorrer array**
> Dado el array `colores = ["rojo", "azul", "verde", "amarillo", "naranja"]`:
> 1. Muestra todos los colores en consola
> 2. Muestra los colores en orden inverso (sin usar `.reverse()`)
> 3. Muestra los colores que tienen más de 4 letras

**Ejercicio 6: Buscar elemento**
> Dado el array `numeros = [3, 7, 10, 15, 2, 8, 5, 12]`:
> 1. Busca si el número 8 existe y muestra su posición
> 2. Busca si el número 20 existe y muestra un mensaje apropiado
> 3. Encuentra el número más grande del array usando un bucle

**Ejercicio 7: Promedio y estadísticas**
> Dado el array `temperaturas = [22, 25, 19, 23, 21, 24, 20]`:
> 1. Calcula el promedio de temperaturas
> 2. Cuenta cuántas temperaturas son superiores a 22°C
> 3. Cuenta cuántas temperaturas son inferiores o iguales a 22°C

### Nivel 3: Bucles anidados y estructuras complejas

**Ejercicio 8: Matriz numérica**
> Usa bucles anidados para generar una matriz (tabla) como esta:
> ```
> 1 2 3 4 5
> 2 4 6 8 10
> 3 6 9 12 15
> 4 8 12 16 20
> 5 10 15 20 25
> ```

**Ejercicio 9: Procesamiento de calificaciones**
> Dado el array de estudiantes:
> ```javascript
> let estudiantes = [
>     { nombre: "Ana", notas: [7, 8, 9, 6] },
>     { nombre: "Carlos", notas: [5, 6, 4, 7] },
>     { nombre: "María", notas: [9, 9, 10, 8] },
>     { nombre: "Juan", notas: [4, 5, 6, 4] }
> ];
> ```
> Calcula y muestra:
> 1. El promedio de cada estudiante
> 2. El promedio general de la clase
> 3. El estudiante con el promedio más alto
> 4. Los estudiantes aprobados (promedio ≥ 5)

**Ejercicio 10: Filtrado y procesamiento**
> Dado el siguiente array de productos:
> ```javascript
> let inventario = [
>     { nombre: "Laptop", precio: 800, stock: 5, categoria: "electrónica" },
>     { nombre: "Camisa", precio: 30, stock: 12, categoria: "ropa" },
>     { nombre: "Mouse", precio: 25, stock: 20, categoria: "electrónica" },
>     { nombre: "Pantalón", precio: 50, stock: 8, categoria: "ropa" },
>     { nombre: "Monitor", precio: 200, stock: 3, categoria: "electrónica" }
> ];
> ```
> Realiza:
> 1. Muestra todos los productos de la categoría "electrónica"
> 2. Calcula el valor total del inventario (precio × stock)
> 3. Aplica un descuento del 10% a todos los productos de "electrónica" y muestra los precios actualizados
> 4. Encuentra el producto más caro

**Ejercicio 11: Adivina el número**
> Crea un juego donde:
> 1. Genera un número aleatorio entre 1 y 100 usando `Math.floor(Math.random() * 100) + 1`
> 2. El usuario debe adivinar el número
> 3. Por cada intento, muestra "Muy alto" o "Muy bajo"
> 4. Usa un bucle `while` que termine cuando el usuario adivine o ingrese 0 para salir
> 5. Muestra el número de intentos realizados

**Ejercicio 12: Menú interactivo**
> Crea un programa con un menú que tenga las siguientes opciones usando `while` y `switch`:
> 1. Sumar dos números
> 2. Restar dos números
> 3. Multiplicar dos números
> 4. Dividir dos números
> 5. Salir
> 
> El programa debe seguir mostrando el menú hasta que el usuario elija la opción 5. Cada operación debe pedir dos números y mostrar el resultado.