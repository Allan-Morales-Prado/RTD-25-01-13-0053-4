# Arrays en JavaScript

## ¿Qué es un Array?

Un **array** (arreglo o lista) es una estructura de datos que permite almacenar **múltiples valores** en una sola variable. Cada valor dentro de un array tiene una **posición numérica** llamada **índice**, que comienza en 0.

### Sintaxis básica

```javascript
// Array vacío
let miArray = [];

// Array con valores
let frutas = ["manzana", "pera", "naranja"];
let numeros = [1, 2, 3, 4, 5];
let mixto = ["texto", 42, true, null];
```

## Accediendo a elementos

Los elementos de un array se acceden mediante su **índice** entre corchetes `[]`:

```javascript
let frutas = ["manzana", "pera", "naranja"];

console.log(frutas[0]); // "manzana"
console.log(frutas[1]); // "pera"
console.log(frutas[2]); // "naranja"
console.log(frutas[3]); // undefined (no existe)
```

## Propiedad `.length`

La propiedad `.length` devuelve el número de elementos en un array:

```javascript
let frutas = ["manzana", "pera", "naranja"];
console.log(frutas.length); // 3

// Útil para acceder al último elemento
console.log(frutas[frutas.length - 1]); // "naranja"
```

## Modificando Arrays

### Cambiar un elemento existente

```javascript
let frutas = ["manzana", "pera", "naranja"];
frutas[1] = "uva";
console.log(frutas); // ["manzana", "uva", "naranja"]
```

### Agregar elementos al final con `.push()`

```javascript
let frutas = ["manzana", "pera"];
frutas.push("naranja");
console.log(frutas); // ["manzana", "pera", "naranja"]
```

### Eliminar el último elemento con `.pop()`

```javascript
let frutas = ["manzana", "pera", "naranja"];
let ultimaFruta = frutas.pop();
console.log(ultimaFruta); // "naranja"
console.log(frutas); // ["manzana", "pera"]
```

### Agregar elementos al inicio con `.unshift()`

```javascript
let frutas = ["pera", "naranja"];
frutas.unshift("manzana");
console.log(frutas); // ["manzana", "pera", "naranja"]
```

### Eliminar el primer elemento con `.shift()`

```javascript
let frutas = ["manzana", "pera", "naranja"];
let primeraFruta = frutas.shift();
console.log(primeraFruta); // "manzana"
console.log(frutas); // ["pera", "naranja"]
```

## Combinando Arrays

### Concatenar con `.concat()`

```javascript
let frutas1 = ["manzana", "pera"];
let frutas2 = ["naranja", "uva"];
let todas = frutas1.concat(frutas2);
console.log(todas); // ["manzana", "pera", "naranja", "uva"]
```

### Unir con `...` (spread operator)

```javascript
let frutas1 = ["manzana", "pera"];
let frutas2 = ["naranja", "uva"];
let todas = [...frutas1, ...frutas2];
console.log(todas); // ["manzana", "pera", "naranja", "uva"]
```

## Buscar en Arrays

### `.indexOf()` - encontrar posición

```javascript
let frutas = ["manzana", "pera", "naranja", "pera"];
console.log(frutas.indexOf("pera")); // 1
console.log(frutas.indexOf("uva")); // -1 (no existe)
```

### `.includes()` - verificar existencia

```javascript
let frutas = ["manzana", "pera", "naranja"];
console.log(frutas.includes("pera")); // true
console.log(frutas.includes("uva")); // false
```

## Arrays de números - operaciones comunes

```javascript
let numeros = [10, 20, 30, 40, 50];

// Sumar todos los elementos
let suma = 0;
for (let i = 0; i < numeros.length; i++) {
    suma += numeros[i];
}
console.log(suma); // 150

// Encontrar el máximo
let maximo = numeros[0];
for (let i = 1; i < numeros.length; i++) {
    if (numeros[i] > maximo) {
        maximo = numeros[i];
    }
}
console.log(maximo); // 50
```

## Arrays y condicionales

```javascript
let numeros = [5, 12, 8, 3, 15, 7];

// Encontrar números mayores a 10
let mayores = [];
for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] > 10) {
        mayores.push(numeros[i]);
    }
}
console.log(mayores); // [12, 15]
```

## Ejemplos prácticos

### Ejemplo 1: Lista de tareas

```javascript
let tareas = ["Estudiar", "Hacer ejercicio", "Leer"];

// Mostrar tareas
console.log("Tareas pendientes:");
console.log(tareas[0]);
console.log(tareas[1]);
console.log(tareas[2]);

// Agregar nueva tarea
tareas.push("Dormir temprano");
console.log("Tareas actualizadas:", tareas);
```

### Ejemplo 2: Promedio de calificaciones

```javascript
let calificaciones = [8.5, 7.0, 9.0, 6.5, 9.5];

let suma = 0;
for (let i = 0; i < calificaciones.length; i++) {
    suma += calificaciones[i];
}

let promedio = suma / calificaciones.length;
console.log("Promedio:", promedio.toFixed(2));
```

## Ejercicios propuestos

### Nivel 1: Operaciones básicas

**Ejercicio 1: Lista de compras**
> Crea un array llamado `compras` con 5 productos. Muestra en consola:
> 1. El primer producto
> 2. El último producto
> 3. El número total de productos

**Ejercicio 2: Agregar y eliminar**
> Parte con un array `colores = ["rojo", "verde", "azul"]` y realiza:
> 1. Agrega "amarillo" al final
> 2. Agrega "negro" al inicio
> 3. Elimina el último elemento
> 4. Elimina el primer elemento
> 5. Muestra el array final

### Nivel 2: Recorrido con condicionales

**Ejercicio 3: Filtrar números**
> Dado el array `numeros = [3, 7, 10, 15, 2, 8, 5]`, crea un nuevo array que contenga solo los números pares (usa `%` para verificar).

**Ejercicio 4: Mayor y menor**
> Dado el array `notas = [8, 5, 9, 3, 7, 6]`, encuentra:
> 1. La nota más alta
> 2. La nota más baja
> 3. El promedio

**Ejercicio 5: Aprobados y reprobados**
> Dado el array `calificaciones = [7, 4, 9, 5, 3, 8, 6, 2]`, crea dos arrays:
> 1. `aprobados` con las notas mayores o iguales a 5
> 2. `reprobados` con las notas menores a 5
> 3. Muestra cuántos aprobados y cuántos reprobados hay

### Nivel 3: Problemas más complejos

**Ejercicio 6: Invertir array**
> Dado el array `palabras = ["hola", "mundo", "javascript"]`, crea un nuevo array que contenga los elementos en orden inverso SIN usar `.reverse()`.

**Ejercicio 7: Eliminar duplicados**
> Dado el array `numeros = [1, 2, 2, 3, 4, 4, 5]`, crea un nuevo array sin elementos duplicados.

**Ejercicio 8: Calculadora de estadísticas**
> Pide al usuario 5 números usando `prompt()` y guárdalos en un array. Luego calcula y muestra:
> 1. La suma total
> 2. El promedio
> 3. El número más grande
> 4. El número más pequeño