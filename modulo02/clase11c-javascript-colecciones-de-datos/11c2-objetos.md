
# Objetos en JavaScript

## ¿Qué es un Objeto?

Un **objeto** es una estructura de datos que permite almacenar **información estructurada** mediante pares de **clave: valor**. A diferencia de los arrays que usan índices numéricos, los objetos usan nombres (claves) para acceder a sus valores.

## Sintaxis básica

```javascript
// Objeto vacío
let persona = {};

// Objeto con propiedades
let persona = {
    nombre: "Ana",
    edad: 30,
    ciudad: "Madrid"
};
```

## Propiedades de un objeto

Las propiedades son las características del objeto, definidas como `clave: valor`:

```javascript
let producto = {
    nombre: "Laptop",
    precio: 800,
    disponible: true,
    categorias: ["electrónica", "computación"],
    especificaciones: {
        procesador: "Intel i7",
        ram: "16GB"
    }
};
```

## Accediendo a propiedades

### Notación de punto (`.`)

```javascript
let persona = {
    nombre: "Ana",
    edad: 30
};

console.log(persona.nombre); // "Ana"
console.log(persona.edad); // 30
```

### Notación de corchetes (`[]`)

```javascript
let persona = {
    nombre: "Ana",
    edad: 30
};

console.log(persona["nombre"]); // "Ana"
console.log(persona["edad"]); // 30

// Útil cuando la clave es dinámica
let clave = "nombre";
console.log(persona[clave]); // "Ana"
```

## Modificando objetos

### Agregar nuevas propiedades

```javascript
let persona = {
    nombre: "Ana",
    edad: 30
};

persona.ciudad = "Madrid";
persona["profesion"] = "Ingeniera";

console.log(persona);
// {nombre: "Ana", edad: 30, ciudad: "Madrid", profesion: "Ingeniera"}
```

### Modificar propiedades existentes

```javascript
let persona = {
    nombre: "Ana",
    edad: 30
};

persona.edad = 31;
persona["nombre"] = "Ana María";

console.log(persona);
// {nombre: "Ana María", edad: 31}
```

### Eliminar propiedades con `delete`

```javascript
let persona = {
    nombre: "Ana",
    edad: 30,
    ciudad: "Madrid"
};

delete persona.ciudad;
console.log(persona);
// {nombre: "Ana", edad: 30}
```

## Verificando propiedades

### `.hasOwnProperty()`

```javascript
let persona = {
    nombre: "Ana",
    edad: 30
};

console.log(persona.hasOwnProperty("nombre")); // true
console.log(persona.hasOwnProperty("ciudad")); // false
```

### Operador `in`

```javascript
let persona = {
    nombre: "Ana",
    edad: 30
};

console.log("nombre" in persona); // true
console.log("ciudad" in persona); // false
```

## Objetos anidados

Los objetos pueden contener otros objetos o arrays:

```javascript
let estudiante = {
    nombre: "Carlos",
    edad: 22,
    direccion: {
        calle: "Calle Mayor",
        numero: 10,
        ciudad: "Barcelona"
    },
    asignaturas: ["Matemáticas", "Física", "Programación"],
    calificaciones: {
        matematicas: 8.5,
        fisica: 7.0,
        programacion: 9.0
    }
};

// Acceso a propiedades anidadas
console.log(estudiante.direccion.ciudad); // "Barcelona"
console.log(estudiante.asignaturas[1]); // "Física"
console.log(estudiante.calificaciones.programacion); // 9.0
```

## Arrays de objetos

Combinación muy común en programación:

```javascript
let productos = [
    {
        id: 1,
        nombre: "Laptop",
        precio: 800,
        stock: 10
    },
    {
        id: 2,
        nombre: "Mouse",
        precio: 25,
        stock: 50
    },
    {
        id: 3,
        nombre: "Teclado",
        precio: 60,
        stock: 30
    }
];

// Acceder a un producto específico
console.log(productos[0].nombre); // "Laptop"

// Recorrer todos los productos
for (let i = 0; i < productos.length; i++) {
    console.log(`${productos[i].nombre}: $${productos[i].precio}`);
}
```

## Ejemplos prácticos

### Ejemplo 1: Registro de usuario

```javascript
let usuario = {
    nombre: "",
    email: "",
    edad: 0,
    esAdmin: false
};

// Completar datos
usuario.nombre = prompt("Ingresa tu nombre:");
usuario.email = prompt("Ingresa tu email:");
usuario.edad = parseInt(prompt("Ingresa tu edad:"));

// Verificar si es mayor de edad
if (usuario.edad >= 18) {
    console.log(`${usuario.nombre} es mayor de edad`);
} else {
    console.log(`${usuario.nombre} es menor de edad`);
}
```

### Ejemplo 2: Catálogo de productos

```javascript
let productos = [
    { nombre: "Laptop", precio: 800, stock: 5 },
    { nombre: "Mouse", precio: 25, stock: 20 },
    { nombre: "Monitor", precio: 200, stock: 3 }
];

// Mostrar productos disponibles
console.log("Productos disponibles:");

for (let i = 0; i < productos.length; i++) {
    if (productos[i].stock > 0) {
        console.log(`${productos[i].nombre}: $${productos[i].precio} (${productos[i].stock} unidades)`);
    }
}

// Calcular valor total del inventario
let valorTotal = 0;
for (let i = 0; i < productos.length; i++) {
    valorTotal += productos[i].precio * productos[i].stock;
}
console.log(`Valor total del inventario: $${valorTotal}`);
```

## Ejercicios propuestos

### Nivel 1: Creación y acceso

**Ejercicio 1: Datos personales**
> Crea un objeto llamado `persona` con las propiedades: `nombre`, `apellido`, `edad` y `ciudad`. Luego:
> 1. Muestra cada propiedad en consola
> 2. Modifica la edad sumándole 1 año
> 3. Agrega una nueva propiedad `profesion`
> 4. Elimina la propiedad `ciudad`

**Ejercicio 2: Libro**
> Crea un objeto `libro` con propiedades: `titulo`, `autor`, `año` y `genero`. Muestra un mensaje como: "El libro 'Cien años de soledad' fue escrito por Gabriel García Márquez en 1967".

### Nivel 2: Objetos anidados

**Ejercicio 3: Estudiante**
> Crea un objeto `estudiante` con:
> - nombre, edad, curso
> - direccion (calle, numero, ciudad)
> - calificaciones (matematicas, lenguaje, ciencias, historia)
> 
> Luego calcula y muestra el promedio de sus calificaciones.

**Ejercicio 4: Inventario de tienda**
> Crea un array de 5 objetos `producto`. Cada producto debe tener: `id`, `nombre`, `precio` y `stock`. Luego:
> 1. Muestra todos los productos en consola
> 2. Calcula el valor total del inventario (precio × stock)
> 3. Encuentra el producto más caro

### Nivel 3: Operaciones con arrays de objetos

**Ejercicio 5: Filtro de usuarios**
> Crea un array de 5 usuarios con: `nombre`, `edad` y `activo` (booleano). Luego:
> 1. Muestra solo los usuarios activos
> 2. Muestra solo los usuarios mayores de 18 años
> 3. Muestra el nombre del usuario más joven

**Ejercicio 6: Sistema de calificaciones**
> Crea un objeto `curso` con:
> - `nombre`: "Programación"
> - `estudiantes`: un array de objetos con `nombre` y `nota`
> 
> Luego calcula y muestra:
> 1. El promedio de todas las notas
> 2. Los estudiantes aprobados (nota ≥ 5)
> 3. Los estudiantes reprobados (nota < 5)
> 4. La nota más alta y la más baja

**Ejercicio 7: Tienda con descuentos**
> Crea un array de 5 productos en una tienda. Cada producto tiene: `nombre`, `precio` y `categoria`. Aplica:
> - Descuento del 10% a todos los productos de la categoría "electrónica"
> - Descuento del 5% a todos los productos de la categoría "ropa"
> - Muestra los productos con sus precios actualizados