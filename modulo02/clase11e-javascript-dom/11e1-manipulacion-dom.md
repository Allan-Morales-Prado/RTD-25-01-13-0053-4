# Manipulación del DOM con JavaScript

## Introducción al DOM

El **Document Object Model (DOM)** es una representación en forma de árbol que el navegador crea a partir del HTML de tu página . Piensa en él como un mapa que organiza todos los elementos de tu web (etiquetas, textos, atributos) en una estructura jerárquica que JavaScript puede leer y modificar .

Cada elemento en el DOM es un **nodo**. Los nodos se organizan en el árbol según sus relaciones :

- **Nodo raíz**: El nodo superior, en HTML es el elemento `<html>`.
- **Nodo padre**: Un nodo que contiene a otro.
- **Nodo hijo**: Un nodo que está contenido dentro de otro.
- **Nodos hermanos**: Nodos que comparten el mismo padre.
- **Nodo descendiente**: Un nodo en cualquier nivel dentro de otro.

Entender esta estructura es fundamental porque la mayoría de los métodos para manipular el DOM se basan en estas relaciones de parentesco .

---

## Seleccionando elementos

Antes de manipular un elemento, necesitas encontrarlo en el DOM.

### `querySelector()` y `querySelectorAll()`

Estos son los métodos modernos y más recomendados porque usan selectores CSS .

```javascript
// Selecciona el primer elemento que coincida con el selector
const elemento = document.querySelector('.mi-clase');

// Selecciona TODOS los elementos que coincidan (devuelve una NodeList)
const elementos = document.querySelectorAll('p');
```

### Otros métodos para seleccionar elementos

```javascript
// Por ID (muy rápido)
const porId = document.getElementById('miId');

// Por nombre de etiqueta
const parrafos = document.getElementsByTagName('p');

// Por clase
const porClase = document.getElementsByClassName('mi-clase');
```

---

## Leyendo y modificando contenido

### `textContent`

Para leer o cambiar el texto de un elemento (ignora etiquetas HTML):

```javascript
const parrafo = document.querySelector('p');
console.log(parrafo.textContent); // Lee el texto
parrafo.textContent = 'Nuevo texto'; // Cambia el texto
```

**Nota importante:** `textContent` es más rápido que `innerText`, porque no verifica estilos del elemento .

### `innerHTML`

Para leer o cambiar el contenido HTML completo de un elemento:

```javascript
const contenedor = document.querySelector('.contenedor');
contenedor.innerHTML = '<h2>Nuevo título</h2><p>Nuevo párrafo</p>';
```

Usar `innerHTML` es muy rápido para construir grandes bloques de HTML, ya que el navegador utiliza su optimizado parser interno .

---

## Creando y añadiendo elementos

### `createElement()` y `appendChild()`

Para crear elementos de forma dinámica:

```javascript
// 1. Crear el elemento
const nuevoParrafo = document.createElement('p');

// 2. Darle contenido
nuevoParrafo.textContent = 'Este párrafo fue creado con JavaScript';

// 3. Añadirlo al final del contenedor padre
const contenedor = document.querySelector('.contenedor');
contenedor.appendChild(nuevoParrafo);
```

### `insertAdjacentHTML()` (más rápido que `innerHTML`)

Para insertar HTML sin destruir el contenido existente :

```javascript
const contenedor = document.querySelector('.contenedor');

// Inserta al final del elemento
contenedor.insertAdjacentHTML('beforeend', '<p>Nuevo párrafo al final</p>');

// Inserta al principio del elemento
contenedor.insertAdjacentHTML('afterbegin', '<p>Nuevo párrafo al inicio</p>');
```

### Creando texto con `createTextNode()`

A veces necesitas crear nodos de texto de forma explícita :

```javascript
const texto = document.createTextNode('Este texto es un nodo separado');
const contenedor = document.querySelector('.contenedor');
contenedor.appendChild(texto);
```

---

## Modificando atributos y estilos

### Atributos HTML vs Propiedades DOM

Es importante distinguir entre atributos HTML (lo que ves en el código) y propiedades DOM (el objeto JavaScript) :

```javascript
// Atributos (lo que está en el HTML)
elemento.getAttribute('id');
elemento.setAttribute('class', 'nueva-clase');

// Propiedades DOM (más recomendadas para uso general)
elemento.id = 'nuevoId';
elemento.className = 'nueva-clase';
```

**Nota:** Cuando un atributo estándar cambia, la propiedad correspondiente se actualiza automáticamente, y viceversa .

### `dataset` para atributos `data-*`

Los atributos `data-*` son una forma segura de almacenar datos personalizados en HTML :

```html
<div id="usuario" data-usuario-id="123" data-rol="admin"></div>
```

```javascript
const usuario = document.getElementById('usuario');
console.log(usuario.dataset.usuarioId); // "123"
console.log(usuario.dataset.rol); // "admin"
```

### Modificando estilos CSS

**Opción 1: Estilos inline (para cambios puntuales)**

```javascript
const elemento = document.querySelector('.mi-elemento');
elemento.style.backgroundColor = 'blue';
elemento.style.padding = '20px';
```

**Opción 2: Clases CSS (más eficiente y recomendada)** 

```css
/* En tu archivo CSS */
.activo {
    background-color: blue;
    padding: 20px;
    border-radius: 5px;
}
```

```javascript
// En JavaScript
const elemento = document.querySelector('.mi-elemento');
elemento.classList.add('activo');
elemento.classList.remove('inactivo');
elemento.classList.toggle('visible'); // Agrega o quita según estado actual
```

Usar clases CSS es más eficiente porque el navegador aplica todos los estilos de una sola vez, evitando múltiples repintados .

---

## Eliminando elementos

```javascript
// Si tienes el elemento y su padre
const elemento = document.querySelector('.eliminar');
elemento.parentNode.removeChild(elemento);

// Método moderno (elimina el elemento directamente)
elemento.remove();
```

`remove()` no está soportado en navegadores muy antiguos, pero es el método más limpio .

---

## Eventos

### `addEventListener()`

La forma moderna y recomendada de escuchar eventos :

```javascript
const boton = document.querySelector('#miBoton');

boton.addEventListener('click', function() {
    console.log('¡Botón clickeado!');
});
```

**Opción `once: true`:** El listener se ejecuta una sola vez y se elimina automáticamente :

```javascript
boton.addEventListener('click', function() {
    console.log('Esto solo ocurrirá una vez');
}, { once: true });
```

### Event Delegation (Delegación de eventos)

En lugar de añadir listeners a múltiples elementos, aprovecha la burbuja de eventos y añade un único listener al contenedor padre :

```javascript
// ❌ Ineficiente: listener por cada botón
document.querySelectorAll('.btn').forEach(btn => {
    btn.addEventListener('click', function() {
        console.log('Clic en:', this.textContent);
    });
});

// ✅ Eficiente: un único listener en el padre
document.querySelector('.contenedor-botones').addEventListener('click', function(e) {
    // Verifica si el elemento clickeado es un botón
    if (e.target.classList.contains('btn')) {
        console.log('Clic en:', e.target.textContent);
    }
});
```

**Ventajas:** Mejor rendimiento y funciona con elementos añadidos dinámicamente .

---

## Buenas prácticas para un DOM eficiente

### 1. Caché de referencias

Guardar referencias a elementos que usarás varias veces :

```javascript
// ❌ Ineficiente: busca en el DOM cada vez
for (let i = 0; i < 100; i++) {
    document.getElementById('contador').textContent = i;
}

// ✅ Eficiente: referencia en caché
const contador = document.getElementById('contador');
for (let i = 0; i < 100; i++) {
    contador.textContent = i;
}
```

### 2. Usa `DocumentFragment` para múltiples inserciones

Cuando vayas a añadir muchos elementos, agrúpalos en un fragmento para hacer una sola inserción :

```javascript
// ❌ Ineficiente: causa un reflow por cada inserción
const lista = document.getElementById('miLista');
for (let i = 0; i < 1000; i++) {
    const item = document.createElement('li');
    item.textContent = `Elemento ${i}`;
    lista.appendChild(item);
}

// ✅ Eficiente: solo un reflow al final
const lista = document.getElementById('miLista');
const fragment = document.createDocumentFragment();

for (let i = 0; i < 1000; i++) {
    const item = document.createElement('li');
    item.textContent = `Elemento ${i}`;
    fragment.appendChild(item);
}

lista.appendChild(fragment); // Solo una operación de DOM
```

### 3. Separa lectura y escritura (evita "layout thrashing")

Agrupa todas las lecturas de propiedades de layout antes de hacer cualquier escritura :

```javascript
// ❌ Ineficiente: alterna lectura y escritura
elementos.forEach(el => {
    const altura = el.offsetHeight; // Lectura (fuerza layout)
    el.style.height = altura + 10 + 'px'; // Escritura
});

// ✅ Eficiente: lee todo, luego escribe todo
const alturas = elementos.map(el => el.offsetHeight); // Todas las lecturas
elementos.forEach((el, i) => {
    el.style.height = alturas[i] + 10 + 'px'; // Todas las escrituras
});
```

### 4. Prefiere `textContent` sobre `innerText`

`textContent` es más rápido porque no verifica estilos .

### 5. Prefiere `insertAdjacentHTML` sobre `innerHTML` para añadir contenido

`insertAdjacentHTML` no destruye el DOM existente antes de insertar :

```javascript
// ❌ Destruye y recrea todo el contenido interno
contenedor.innerHTML += '<p>Nuevo texto</p>';

// ✅ Añade sin destruir
contenedor.insertAdjacentHTML('beforeend', '<p>Nuevo texto</p>');
```

---

## Ejemplos resueltos

### Ejemplo 1: Lista dinámica con eventos

```javascript
const input = document.getElementById('nuevoItem');
const botonAgregar = document.getElementById('agregar');
const lista = document.getElementById('lista');

// Agregar elemento
botonAgregar.addEventListener('click', function() {
    const texto = input.value.trim();
    if (texto === '') return;
    
    // Crear nuevo elemento de lista
    const li = document.createElement('li');
    li.textContent = texto;
    
    // Añadir botón de eliminar
    const btnEliminar = document.createElement('button');
    btnEliminar.textContent = '✕';
    btnEliminar.addEventListener('click', function(e) {
        e.stopPropagation();
        li.remove();
    });
    
    li.appendChild(btnEliminar);
    lista.appendChild(li);
    
    input.value = '';
});

// Marcar como completado (event delegation)
lista.addEventListener('click', function(e) {
    if (e.target.tagName === 'LI') {
        e.target.classList.toggle('completado');
    }
});
```

### Ejemplo 2: Validación de formulario con mensajes de error

Basado en técnicas de validación con DOM :

```javascript
const formulario = document.getElementById('miFormulario');

formulario.addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Eliminar mensajes de error anteriores
    const erroresExistentes = document.querySelector('.errores');
    if (erroresExistentes) erroresExistentes.remove();
    
    // Validar campos
    const nombre = document.getElementById('nombre');
    const email = document.getElementById('email');
    const errores = [];
    
    if (nombre.value.trim().length < 3) {
        errores.push('El nombre debe tener al menos 3 caracteres');
        nombre.style.borderColor = 'red';
    }
    
    if (!email.value.includes('@')) {
        errores.push('El email debe ser válido');
        email.style.borderColor = 'red';
    }
    
    // Mostrar errores si existen
    if (errores.length > 0) {
        const divErrores = document.createElement('div');
        divErrores.className = 'errores';
        divErrores.style.color = 'red';
        divErrores.style.padding = '10px';
        divErrores.style.border = '1px solid red';
        
        const titulo = document.createElement('h3');
        titulo.textContent = 'Errores en el formulario:';
        divErrores.appendChild(titulo);
        
        const listaErrores = document.createElement('ul');
        errores.forEach(error => {
            const li = document.createElement('li');
            li.textContent = error;
            listaErrores.appendChild(li);
        });
        divErrores.appendChild(listaErrores);
        
        formulario.prepend(divErrores);
    } else {
        alert('Formulario enviado correctamente');
        formulario.reset();
    }
});

// Limpiar estilos de error al escribir
document.querySelectorAll('input').forEach(input => {
    input.addEventListener('input', function() {
        this.style.borderColor = '';
    });
});
```

---

## Ejercicios propuestos

### Nivel 1: Selección y modificación básica

**Ejercicio 1: Cambiar título**
> Crea una página con un `<h1>` que diga "Título original" y un botón. Al hacer clic en el botón, cambia el texto del `<h1>` a "Título cambiado".

**Ejercicio 2: Lista de colores**
> Crea una lista `<ul>` con 3 colores. Añade un botón que permita agregar un nuevo color al final de la lista. Cada nuevo color debe ser un `<li>` con el nombre del color.

**Ejercicio 3: Mostrar/ocultar**
> Crea un párrafo y un botón. El botón debe alternar (mostrar/ocultar) el párrafo cada vez que se hace clic.

### Nivel 2: Manipulación de estilos y clases

**Ejercicio 4: Fondo aleatorio**
> Crea un botón que, al hacer clic, cambie el color de fondo de la página a un color aleatorio.

**Ejercicio 5: Contador con estilo**
> Crea un contador con botones "+" y "-". Cuando el contador llegue a 10, cambia el color del número a verde. Cuando llegue a 0, cambia a rojo.

**Ejercicio 6: Toggle de clase**
> Crea un `<div>` que al hacer clic alterne entre dos clases CSS (por ejemplo, `.activo` e `.inactivo`). Cada clase debe tener estilos visualmente diferentes.

### Nivel 3: Creación dinámica y eventos

**Ejercicio 7: Tabla dinámica**
> Crea un formulario que pida número de filas y columnas. Al enviarlo, genera una tabla con esas dimensiones, con celdas que digan "Fila X, Columna Y".

**Ejercicio 8: Cronómetro simple**
> Crea un cronómetro con botones "Iniciar", "Pausar" y "Reiniciar". Muestra el tiempo en minutos:segundos. Usa `setInterval()` y actualiza el DOM cada segundo.

**Ejercicio 9: Galería de imágenes**
> Crea una galería con miniaturas (pueden ser textos o emojis). Al hacer clic en una miniatura, se muestra una versión ampliada en un contenedor principal. La imagen ampliada debe cambiar al hacer clic en diferentes miniaturas.

**Ejercicio 10: Formulario con validación en tiempo real**
> Crea un formulario de registro con: nombre, email y contraseña. Valida en tiempo real mientras el usuario escribe:
> - Nombre: mínimo 3 caracteres
> - Email: debe contener "@"
> - Contraseña: mínimo 6 caracteres
> 
> Muestra un mensaje de error o éxito debajo de cada campo. El botón de envío solo debe habilitarse cuando todos los campos son válidos.

### Nivel 4: DOM avanzado y rendimiento

**Ejercicio 11: Lista infinita (rendimiento)**
> Crea una lista de 10,000 elementos. Usa `DocumentFragment` para hacer una sola inserción. Añade un campo de búsqueda que filtre la lista en tiempo real mostrando solo los elementos que coinciden.

**Ejercicio 12: To-do list con drag and drop**
> Crea una lista de tareas donde se puedan agregar y eliminar tareas. Implementa que las tareas se puedan reordenar usando drag and drop (investiga los eventos `dragstart`, `dragover`, `drop`).

**Ejercicio 13: Validación de formulario con errores en el DOM**
> Crea un formulario con los campos: nombre, teléfono, fecha de nacimiento y dirección. Al enviar, valida todo y muestra un bloque de errores al inicio del formulario (como en el ejemplo resuelto). Cada error debe ser un enlace que, al hacer clic, enfoque el campo correspondiente.

**Ejercicio 14: Sistema de pestañas (tabs)**
> Crea un sistema de pestañas con 3 secciones. Las pestañas deben alternar mostrando la sección correspondiente. Usa clases CSS para mostrar/ocultar y `dataset` para identificar qué pestaña está activa.

**Ejercicio 15: Chat simple**
> Crea una interfaz de chat donde:
> - El usuario escribe un mensaje y lo envía
> - El mensaje se añade a una lista de mensajes
> - Usa `createElement` y `appendChild` para cada mensaje
> - Los mensajes deben tener un timestamp (hora actual)
> - Añade un botón para limpiar todos los mensajes

---

## Resumen de métodos clave

| Acción | Método recomendado |
|--------|-------------------|
| Seleccionar elemento | `querySelector()` |
| Seleccionar múltiples | `querySelectorAll()` |
| Cambiar texto | `textContent` |
| Cambiar HTML | `innerHTML` o `insertAdjacentHTML()` |
| Crear elemento | `createElement()` |
| Añadir al DOM | `appendChild()` o `append()` |
| Eliminar del DOM | `remove()` |
| Modificar clases | `classList.add()`, `.remove()`, `.toggle()` |
| Escuchar eventos | `addEventListener()` |
| Batching | `DocumentFragment` |