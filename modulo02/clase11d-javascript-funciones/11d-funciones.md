# Funciones en JavaScript

## ¿Qué es una función?

Una función es un **"subprograma"** o bloque de código diseñado para realizar una tarea específica . Piensa en ella como una **receta**: contiene una serie de pasos (instrucciones) que se ejecutan cuando la "invocas" o "llamas" .

Las funciones son fundamentales porque permiten:

- **Reutilizar código**: Escribes la lógica una vez y la usas cuantas veces necesites .
- **Organizar**: Dividen programas complejos en partes más pequeñas y manejables .
- **Mantener**: Facilitan la actualización y corrección de errores.

En JavaScript, las funciones son **objetos de primera clase**, lo que significa que pueden asignarse a variables, pasarse como argumentos y devolverse desde otras funciones .

---

## Sintaxis Básica

### Declaración de función (Function Declaration)

```javascript
function nombreFuncion(parametro1, parametro2) {
    // Código a ejecutar
    return resultado; // Opcional
}
```

**Ejemplo:**
```javascript
function saludar(nombre) {
    return "¡Hola, " + nombre + "!";
}

console.log(saludar("Ana")); // ¡Hola, Ana!
```

### Expresión de función (Function Expression)

```javascript
const nombreFuncion = function(parametro1, parametro2) {
    // Código a ejecutar
    return resultado;
};
```

**Ejemplo:**
```javascript
const sumar = function(a, b) {
    return a + b;
};

console.log(sumar(5, 3)); // 8
```

### Arrow Function (Función flecha) - ES6

```javascript
const nombreFuncion = (parametro1, parametro2) => {
    // Código a ejecutar
    return resultado;
};

// Si solo tiene una línea, puede ser más compacta
const sumar = (a, b) => a + b;
```

**Ejemplo:**
```javascript
const cuadrado = (x) => x * x;
console.log(cuadrado(4)); // 16
```

---

## Parámetros y Argumentos

- **Parámetros**: Son los nombres que se declaran en la definición de la función .
- **Argumentos**: Son los valores reales que se pasan cuando se llama a la función .

```javascript
function sumar(a, b) { // a y b son parámetros
    return a + b;
}

sumar(3, 5); // 3 y 5 son argumentos
```

### Parámetros por defecto

```javascript
function saludar(nombre = "Invitado") {
    console.log("Hola, " + nombre);
}

saludar(); // Hola, Invitado
saludar("María"); // Hola, María
```

### Parámetro Rest (`...`)

Permite representar un número indefinido de argumentos como un array .

```javascript
function sumarTodos(...numeros) {
    let total = 0;
    for (let num of numeros) {
        total += num;
    }
    return total;
}

console.log(sumarTodos(1, 2, 3, 4)); // 10
console.log(sumarTodos(5, 10)); // 15
```

---

## El valor `return`

La sentencia `return` especifica el valor que la función devuelve al código que la llamó .

```javascript
function multiplicar(a, b) {
    return a * b;
}

let resultado = multiplicar(4, 5);
console.log(resultado); // 20
```

**Comportamiento:**

- Cuando se ejecuta `return`, la función **se detiene** inmediatamente .
- Si no hay `return`, la función devuelve `undefined` .
- Una función solo puede devolver **un valor**, pero puedes devolver múltiples usando objetos o arrays .

```javascript
function obtenerDatos() {
    return {
        nombre: "Juan",
        edad: 25,
        ciudad: "Madrid"
    };
}

let datos = obtenerDatos();
console.log(datos.nombre); // Juan
```

---

## Funciones y variables

### Alcance (Scope)

Las variables declaradas dentro de una función son **locales** y solo existen dentro de ella .

```javascript
function miFuncion() {
    let mensaje = "Hola desde dentro";
    console.log(mensaje); // ✅ Funciona
}

console.log(mensaje); // ❌ ReferenceError: mensaje is not defined
```

Las variables declaradas fuera de cualquier función son **globales** y accesibles desde cualquier lugar .

```javascript
let nombreGlobal = "Ana"; // Variable global

function saludar() {
    console.log("Hola, " + nombreGlobal); // ✅ Accede a la variable global
}

saludar(); // Hola, Ana
```

### El objeto `arguments`

Dentro de una función, puedes acceder a todos los argumentos pasados mediante el objeto `arguments` .

```javascript
function listarArgumentos() {
    console.log("Número de argumentos:", arguments.length);
    for (let i = 0; i < arguments.length; i++) {
        console.log("Argumento " + i + ":", arguments[i]);
    }
}

listarArgumentos("a", "b", "c");
// Número de argumentos: 3
// Argumento 0: a
// Argumento 1: b
// Argumento 2: c
```

---

## Propiedades de las funciones

Las funciones, al ser objetos, tienen propiedades útiles .

### Propiedad `name`

Devuelve el nombre de la función .

```javascript
function saludar() {}
console.log(saludar.name); // "saludar"

const despedir = function() {};
console.log(despedir.name); // "despedir"
```

### Propiedad `length`

Devuelve el número de parámetros declarados .

```javascript
function f1(a) {}
function f2(a, b) {}
function f3(a, b, c) {}

console.log(f1.length); // 1
console.log(f2.length); // 2
console.log(f3.length); // 3
```

---

## Buenas prácticas

1. **Nombres descriptivos**: Usa verbos que indiquen qué hace la función (calcularPromedio, obtenerUsuario, validarEmail).

2. **Una sola responsabilidad**: Cada función debe hacer una cosa y hacerla bien.

3. **Evita efectos secundarios**: No modifiques variables fuera de la función si no es necesario.

4. **Usa parámetros por defecto**: Para evitar errores con argumentos no proporcionados.

5. **Declara funciones antes de usarlas**: Aunque el hoisting lo permite, es más legible.

6. **Prefiere `const` para funciones**: Si no necesitas reasignar la función.

7. **Documenta funciones complejas**: Usa comentarios para explicar el propósito y los parámetros.

---

## Ejercicios propuestos

### Nivel 1: Funciones básicas

**Ejercicio 1: Función de saludo**
> Crea una función `saludarUsuario(nombre)` que reciba un nombre y devuelva un saludo personalizado. Si no se proporciona nombre, debe usar "Invitado" por defecto.

**Ejercicio 2: Calculadora simple**
> Crea funciones separadas para sumar, restar, multiplicar y dividir dos números. Luego, crea una función `calcular(a, b, operacion)` que reciba los números y el operador (+, -, *, /) y use las funciones anteriores.

**Ejercicio 3: Convertidor de temperaturas**
> Crea funciones `celsiusAFahrenheit(celsius)` y `fahrenheitACelsius(fahrenheit)` que realicen las conversiones. Usa las fórmulas:
> - °F = (°C × 9/5) + 32
> - °C = (°F - 32) × 5/9

### Nivel 2: Funciones con arrays y objetos

**Ejercicio 4: Promedio de calificaciones**
> Crea una función `calcularPromedio(calificaciones)` que reciba un array de números y devuelva el promedio. Incluye validación para arrays vacíos.

**Ejercicio 5: Filtrar números pares**
> Crea una función `filtrarPares(numeros)` que reciba un array y devuelva un nuevo array solo con los números pares.

**Ejercicio 6: Buscar usuario**
> Dado un array de objetos usuario (con nombre y edad), crea una función `buscarUsuario(nombre, usuarios)` que devuelva el usuario encontrado o `null` si no existe.

### Nivel 3: Funciones con otras funciones

**Ejercicio 7: Calculadora de estadísticas**
> Crea funciones:
> - `sumarArray(numeros)`
> - `promedioArray(numeros)`
> - `maximoArray(numeros)`
> - `minimoArray(numeros)`
> 
> Luego crea una función `estadisticasArray(numeros)` que devuelva un objeto con todas estas estadísticas.

**Ejercicio 8: Generador de secuencias**
> Crea una función `generarSecuencia(inicio, fin, paso)` que devuelva un array con los números desde `inicio` hasta `fin` con el `paso` especificado. Si no se proporciona paso, usa 1.

**Ejercicio 9: Validador de contraseña**
> Crea una función `validarContraseña(contraseña)` que verifique:
> - Longitud mínima de 8 caracteres
> - Al menos una mayúscula
> - Al menos una minúscula
> - Al menos un número
> 
> Devuelve un objeto con `valida` (booleano) y `errores` (array con los incumplimientos).

### Nivel 4: Proyectos integradores

**Ejercicio 10: Sistema de gestión de productos**
> Crea las siguientes funciones:
> - `agregarProducto(inventario, producto)` - Agrega un producto (nombre, precio, stock)
> - `eliminarProducto(inventario, nombre)` - Elimina un producto por nombre
> - `actualizarStock(inventario, nombre, cantidad)` - Actualiza el stock
> - `calcularValorTotal(inventario)` - Calcula el valor total del inventario
> - `buscarPorPrecio(inventario, precioMin, precioMax)` - Busca productos en un rango de precios

**Ejercicio 11: Sistema de votación**
> Crea un sistema de votación con estas funciones:
> - `crearVotacion(pregunta, opciones)` - Crea una votación con una pregunta y array de opciones
> - `votar(votacion, opcion)` - Registra un voto para una opción
> - `mostrarResultados(votacion)` - Muestra los resultados de la votación
> - `calcularPorcentajes(votacion)` - Calcula el porcentaje de cada opción

**Ejercicio 12: Calculadora de interés compuesto**
> Crea una función `calcularInteresCompuesto(capitalInicial, tasaInteres, años, periodos)` que calcule el monto final usando la fórmula:
> `Monto = CapitalInicial × (1 + tasaInteres/periodos)^(periodos × años)`
> 
> También crea una función `simularInversion(capitalInicial, tasaInteres, años)` que muestre año por año cómo crece la inversión.

**Ejercicio 13: Validador de formulario**
> Crea funciones para validar diferentes campos:
> - `validarEmail(email)` - Verifica formato de email
> - `validarTelefono(telefono)` - Verifica formato de teléfono (9 dígitos)
> - `validarFecha(fecha)` - Verifica formato de fecha (DD/MM/AAAA)
> - `validarFormulario(datos)` - Recibe un objeto con todos los campos y devuelve un objeto con validación global y errores por campo

**Ejercicio 14: Sistema de reservas**
> Crea un sistema de reservas para un cine con:
> - `crearSala(filas, columnas)` - Crea una sala con asientos disponibles
> - `reservarAsiento(sala, fila, columna)` - Reserva un asiento
> - `cancelarReserva(sala, fila, columna)` - Cancela una reserva
> - `mostrarSala(sala)` - Muestra el estado de la sala (disponible/reservado)
> - `asientosDisponibles(sala)` - Devuelve el número de asientos disponibles

**Ejercicio 15: Conversor de unidades**
> Crea un sistema de conversión de unidades con funciones para:
> - Longitud: metros a kilómetros, centímetros, milímetros
> - Peso: kilogramos a gramos, libras, onzas
> - Volumen: litros a mililitros, galones
> 
> Crea una función principal `convertir(valor, unidadOrigen, unidadDestino)` que determine automáticamente el tipo de conversión y la realice.