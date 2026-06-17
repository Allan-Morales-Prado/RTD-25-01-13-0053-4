# jQuery para Frontend: Uso Básico y Común

## ¿Qué es jQuery?

jQuery es una biblioteca de JavaScript ligera y rápida que simplifica la interacción con el DOM, el manejo de eventos, las animaciones y las peticiones AJAX . Fue diseñada para hacer que tareas comunes en JavaScript sean mucho más sencillas con menos líneas de código.

Aunque hoy existen frameworks modernos como React o Vue, jQuery sigue siendo una herramienta valiosa porque:

- Es **fácil de aprender** para principiantes 
- Simplifica el manejo de **diferencias entre navegadores** 
- Es **perfecto para prototipos rápidos** y mejoras en páginas estáticas 
- Sigue siendo muy utilizado en **proyectos legacy** 

## Instalación y Configuración

### Cargar jQuery desde CDN

La forma más común y rápida de incluir jQuery es mediante un CDN :

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi proyecto con jQuery</title>
    <!-- Cargar jQuery desde CDN -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <!-- Tu contenido HTML -->
    <script src="app.js"></script>
</body>
</html>
```

### Descarga local

También puedes descargar jQuery desde [jquery.com](https://jquery.com) e incluirlo localmente:

```html
<script src="js/jquery-3.6.0.min.js"></script>
```

## Sintaxis Básica

La sintaxis de jQuery gira en torno al símbolo `$` (dólar), que es un alias de `jQuery` :

```javascript
$(selector).acción();
```

- **`$`** : Indica que estamos usando jQuery
- **`selector`** : Cómo encontrar elementos en el DOM
- **`acción()`** : Qué hacer con esos elementos

### El evento `$(document).ready()`

**Siempre** debes envolver tu código jQuery en `$(document).ready()` para asegurarte de que el DOM esté completamente cargado antes de ejecutar el código :

```javascript
$(document).ready(function() {
    // Tu código jQuery aquí
    console.log("El DOM está listo");
});

// Versión abreviada (muy común)
$(function() {
    // Tu código jQuery aquí
});
```

## Selectores en jQuery

jQuery usa selectores CSS para encontrar elementos, lo que lo hace muy intuitivo :

| Tipo | Sintaxis | Ejemplo |
|------|----------|---------|
| Por ID | `$("#id")` | `$("#miBoton")` |
| Por clase | `$(".clase")` | `$(".mensaje")` |
| Por etiqueta | `$("etiqueta")` | `$("p")` |
| Por atributo | `$("[atributo='valor']")` | `$("[data-id='123']")` |

```javascript
// Seleccionar un elemento por ID
$("#titulo").text("Nuevo título");

// Seleccionar todos los elementos con una clase
$(".item").css("color", "blue");

// Seleccionar todos los párrafos
$("p").addClass("destacado");
```

## Manipulación del DOM

jQuery facilita enormemente la manipulación del DOM con métodos intuitivos .

### Leer y modificar contenido

```javascript
// .html() - Obtener o establecer HTML
let contenido = $("#miDiv").html();  // Leer
$("#miDiv").html("<h2>Nuevo HTML</h2>");  // Escribir

// .text() - Obtener o establecer texto (ignora etiquetas)
$("#miDiv").text("Texto plano");

// .val() - Obtener o establecer valor de inputs
let valor = $("#miInput").val();
$("#miInput").val("Nuevo valor");
```

### Modificar atributos y estilos

```javascript
// .attr() - Atributos HTML
$("#miImagen").attr("src", "nueva-imagen.jpg");

// .css() - Estilos CSS
$(".item").css("background-color", "yellow");
$(".item").css({
    "background-color": "yellow",
    "font-size": "18px"
});

// .addClass(), .removeClass(), .toggleClass()
$("#elemento").addClass("activo");
$("#elemento").removeClass("inactivo");
$("#elemento").toggleClass("visible");
```

### Crear y añadir elementos

```javascript
// Crear elementos con HTML
let nuevoParrafo = $("<p>Este párrafo es nuevo</p>");

// Añadir al final del elemento
$("#contenedor").append(nuevoParrafo);

// Añadir al principio
$("#contenedor").prepend(nuevoParrafo);

// Insertar antes o después
$("#elemento").before("<div>Antes</div>");
$("#elemento").after("<div>Después</div>");
```

### Eliminar elementos

```javascript
// .remove() - Elimina el elemento
$("#elemento").remove();

// .empty() - Elimina todo el contenido interno
$("#contenedor").empty();
```

## Eventos

jQuery simplifica el manejo de eventos con métodos cortos y la poderosa función `.on()` .

### Eventos comunes

```javascript
// Click
$("#miBoton").click(function() {
    alert("¡Click!");
});

// Hover (entrada y salida)
$("#miElemento").hover(
    function() { $(this).css("background", "yellow"); },  // Entrada
    function() { $(this).css("background", "white"); }     // Salida
);

// Submit de formulario
$("#miFormulario").submit(function(e) {
    e.preventDefault();  // Evita el envío tradicional
    console.log("Formulario enviado");
});

// Keyup (tecla levantada)
$("#miInput").keyup(function() {
    console.log("Valor actual:", $(this).val());
});
```

### Event Delegation (Delegación de eventos)

En lugar de asignar eventos a cada elemento, se asigna a un elemento padre :

```javascript
// En lugar de esto (ineficiente con muchos elementos)
$(".item").click(function() { /* ... */ });

// Mejor: delegación de eventos
$("#lista").on("click", ".item", function() {
    console.log("Click en item:", $(this).text());
});
```

**Ventajas de la delegación:**
- Menos event listeners = mejor rendimiento
- Funciona con elementos añadidos dinámicamente

## Efectos y Animaciones

jQuery proporciona efectos simples para dar vida a las páginas .

### Mostrar y ocultar

```javascript
// Ocultar y mostrar
$("#elemento").hide();      // Oculta inmediatamente
$("#elemento").show();      // Muestra inmediatamente
$("#elemento").toggle();    // Alterna visible/oculto

// Con animación (duración en milisegundos o "slow"/"fast")
$("#elemento").hide(400);
$("#elemento").show(600);
$("#elemento").toggle("slow");
```

### Desvanecimiento (Fade)

```javascript
$("#elemento").fadeIn(400);     // Aparece gradualmente
$("#elemento").fadeOut(300);    // Desaparece gradualmente
$("#elemento").fadeToggle(500); // Alterna con fade
```

### Deslizamiento (Slide)

```javascript
$("#elemento").slideUp(400);    // Se desliza hacia arriba
$("#elemento").slideDown(300);  // Se desliza hacia abajo
$("#elemento").slideToggle(500); // Alterna con slide
```

### Encadenamiento (Chaining)

Una de las características más potentes de jQuery es el encadenamiento de métodos :

```javascript
$("#mensaje")
    .slideUp(400)
    .delay(200)
    .slideDown(400)
    .fadeOut(300)
    .fadeIn(300);
```

### Animación personalizada con `.animate()`

```javascript
$("#elemento").animate({
    left: "50px",
    opacity: 0.5,
    height: "200px"
}, 500);  // Duración en milisegundos
```

## Traversing (Navegación por el DOM)

jQuery facilita moverse entre elementos relacionados .

```javascript
// Subir en el árbol
$("#elemento").parent();        // Padre directo
$("#elemento").parents();       // Todos los ancestros
$("#elemento").closest(".contenedor"); // Ancestro más cercano con esa clase

// Bajar en el árbol
$("#lista").children();         // Hijos directos
$("#lista").find("li");         // Todos los descendientes que sean li

// Lado a lado
$("#elemento").siblings();      // Todos los hermanos
$("#elemento").next();          // Siguiente hermano
$("#elemento").prev();          // Hermano anterior
```

## AJAX con jQuery

jQuery simplifica las peticiones AJAX .

### `$.ajax()` - Método completo

```javascript
$.ajax({
    url: "https://api.ejemplo.com/datos",
    method: "GET",
    dataType: "json",
    success: function(response) {
        console.log("Respuesta:", response);
        $("#resultados").html(JSON.stringify(response));
    },
    error: function(xhr, status, error) {
        console.error("Error:", error);
    }
});
```

### Métodos abreviados

```javascript
// GET
$.get("https://api.ejemplo.com/datos", function(data) {
    console.log(data);
});

// POST
$.post("https://api.ejemplo.com/guardar", 
    { nombre: "Juan", email: "juan@email.com" },
    function(response) {
        console.log("Guardado:", response);
    }
);

// GET JSON
$.getJSON("https://api.ejemplo.com/datos.json", function(data) {
    console.log(data);
});
```

### Enviar formulario con AJAX

```javascript
$("#miFormulario").submit(function(e) {
    e.preventDefault();
    
    $.post({
        url: "https://api.ejemplo.com/enviar",
        data: $(this).serialize(),  // Serializa los datos del formulario
        success: function(response) {
            $("#mensaje").text("¡Enviado correctamente!");
        },
        error: function() {
            $("#mensaje").text("Error al enviar");
        }
    });
});
```

## Buenas Prácticas

### 1. Optimizar selectores

El rendimiento de jQuery depende en gran medida de cómo escribas los selectores :

```javascript
// ❌ Ineficiente: selector de jQuery extension (usa Sizzle)
$("#tabla tr:even");

// ✅ Eficiente: selector estándar CSS
$("#tabla tr:nth-child(odd)");

// ❌ Selector muy específico y lento
$(".data table.attendees td.gonzalez");

// ✅ Más simple y rápido
$(".data td.gonzalez");
```

### 2. Cachear selecciones

Guarda los elementos seleccionados para reutilizarlos :

```javascript
// ❌ Ineficiente: busca en el DOM cada vez
$("#elemento").css("color", "red");
$("#elemento").addClass("destacado");
$("#elemento").text("Nuevo texto");

// ✅ Eficiente: una sola búsqueda
const $elemento = $("#elemento");
$elemento.css("color", "red");
$elemento.addClass("destacado");
$elemento.text("Nuevo texto");
```

### 3. Usar event delegation para elementos dinámicos

```javascript
// ❌ Solo funciona para elementos existentes al momento
$(".item").click(function() { /* ... */ });

// ✅ Funciona con elementos creados después
$("#lista").on("click", ".item", function() { /* ... */ });
```

### 4. Preferir `textContent` vs `innerHTML` cuando no necesites HTML

```javascript
// ✅ Más eficiente si no necesitas HTML
$("#elemento").text("Texto plano");

// ❌ Más lento si solo necesitas texto
$("#elemento").html("Texto plano");
```

### 5. Minimizar operaciones del DOM

Agrupa las manipulaciones para evitar múltiples reflows :

```javascript
// ❌ Múltiples operaciones
$("#lista").append("<li>Item 1</li>");
$("#lista").append("<li>Item 2</li>");
$("#lista").append("<li>Item 3</li>");

// ✅ Una sola operación
$("#lista").append("<li>Item 1</li><li>Item 2</li><li>Item 3</li>");
```

### 6. Usar versión CDN para mejorar velocidad de carga

Usar un CDN permite que los usuarios se beneficien del cache del navegador si ya han visitado otro sitio que usa jQuery desde el mismo CDN .

## Ejemplos Resueltos

### Ejemplo 1: Toggle de mensaje con animación

```html
<!DOCTYPE html>
<html>
<head>
    <title>jQuery Demo</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        #mensaje { 
            padding: 20px; 
            background: #4CAF50; 
            color: white; 
            display: none;
        }
    </style>
</head>
<body>
    <h1>Bienvenido</h1>
    <button id="toggleBtn">Mostrar mensaje</button>
    <div id="mensaje">¡Hola! jQuery está funcionando 🎉</div>

    <script>
        $(document).ready(function() {
            $("#toggleBtn").click(function() {
                $("#mensaje").fadeToggle(600);
                
                // Cambiar texto del botón
                let $btn = $(this);
                if ($("#mensaje").is(":visible")) {
                    $btn.text("Ocultar mensaje");
                } else {
                    $btn.text("Mostrar mensaje");
                }
            });
        });
    </script>
</body>
</html>
```

### Ejemplo 2: Lista de tareas interactiva

```html
<!DOCTYPE html>
<html>
<head>
    <title>Lista de tareas con jQuery</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <style>
        .completada { text-decoration: line-through; color: gray; }
        .tarea-item { cursor: pointer; padding: 5px; }
        .tarea-item:hover { background: #f0f0f0; }
        .eliminar-btn { margin-left: 10px; color: red; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Lista de tareas</h1>
    <input type="text" id="nuevaTarea" placeholder="Escribe una tarea">
    <button id="agregarBtn">Agregar</button>
    <ul id="listaTareas"></ul>

    <script>
        $(document).ready(function() {
            // Agregar tarea
            $("#agregarBtn").click(function() {
                let texto = $("#nuevaTarea").val().trim();
                if (texto === "") return;
                
                let $item = $("<li>")
                    .addClass("tarea-item")
                    .text(texto)
                    .append($("<span>")
                        .addClass("eliminar-btn")
                        .text("✕")
                    );
                
                $("#listaTareas").append($item);
                $("#nuevaTarea").val("");
            });

            // Marcar como completada (click en el li)
            $("#listaTareas").on("click", ".tarea-item", function(e) {
                // Evitar que el click en el botón eliminar también marque completada
                if ($(e.target).hasClass("eliminar-btn")) return;
                $(this).toggleClass("completada");
            });

            // Eliminar tarea (click en ✕)
            $("#listaTareas").on("click", ".eliminar-btn", function(e) {
                e.stopPropagation();
                $(this).parent().fadeOut(300, function() {
                    $(this).remove();
                });
            });

            // Enter para agregar
            $("#nuevaTarea").keyup(function(e) {
                if (e.key === "Enter") {
                    $("#agregarBtn").click();
                }
            });
        });
    </script>
</body>
</html>
```

### Ejemplo 3: Carga de datos con AJAX

```javascript
$(document).ready(function() {
    // Cargar usuarios desde una API
    function cargarUsuarios() {
        $("#loading").show();
        $("#listaUsuarios").empty();
        
        $.ajax({
            url: "https://jsonplaceholder.typicode.com/users",
            method: "GET",
            dataType: "json",
            success: function(usuarios) {
                $.each(usuarios, function(index, usuario) {
                    $("#listaUsuarios").append(
                        $("<div>")
                            .addClass("usuario-card")
                            .html(`
                                <h3>${usuario.name}</h3>
                                <p>Email: ${usuario.email}</p>
                                <p>Teléfono: ${usuario.phone}</p>
                            `)
                    );
                });
            },
            error: function() {
                $("#mensajeError").text("Error al cargar los datos").show();
            },
            complete: function() {
                $("#loading").hide();
            }
        });
    }
    
    $("#cargarBtn").click(cargarUsuarios);
});
```

## Ejercicios Propuestos

### Nivel 1: Selectores y manipulación básica

**Ejercicio 1: Cambiar título con animación**
> Crea una página con un `<h1>` y un botón. Al hacer clic, cambia el texto del título y agrega una animación de fade.

**Ejercicio 2: Lista de colores interactiva**
> Crea una lista `<ul>` con colores. Añade un input y un botón para agregar nuevos colores. Cada nuevo color debe aparecer con una animación de slideDown.

**Ejercicio 3: Modo oscuro**
> Crea un botón que alterne entre modo claro y oscuro en la página. Usa `.toggleClass()` para cambiar estilos.

### Nivel 2: Eventos y efectos

**Ejercicio 4: Carrusel simple**
> Crea un carrusel con 3 imágenes que cambien cada 3 segundos. Añade botones "Anterior" y "Siguiente".

**Ejercicio 5: Acordeón**
> Crea un acordeón donde al hacer clic en un título se despliegue el contenido correspondiente y se oculten los demás.

**Ejercicio 6: Contador con efectos**
> Crea un contador con botones "+" y "-". Cuando el contador cambie, aplica un efecto de fade rápido.

### Nivel 3: Formularios y validación

**Ejercicio 7: Validación de formulario en tiempo real**
> Crea un formulario con nombre, email y contraseña. Valida en tiempo real:
> - Nombre: mínimo 3 caracteres
> - Email: debe contener "@"
> - Contraseña: mínimo 6 caracteres
> 
> Muestra mensajes de error debajo de cada campo y deshabilita el botón de envío hasta que todo esté válido.

**Ejercicio 8: Selector de país dinámico**
> Crea dos selects: "País" y "Ciudad". Al seleccionar un país, carga dinámicamente las ciudades correspondientes usando un objeto con los datos.

**Ejercicio 9: Subida de archivo con vista previa**
> Crea un input de tipo file que al seleccionar una imagen muestre una vista previa de la misma.

### Nivel 4: AJAX y proyectos integradores

**Ejercicio 10: Buscador de usuarios**
> Usa la API de `jsonplaceholder.typicode.com/users` para mostrar una lista de usuarios. Añade un campo de búsqueda que filtre los usuarios por nombre en tiempo real (sin hacer nuevas peticiones).

**Ejercicio 11: Gestor de tareas con persistencia**
> Crea una lista de tareas que guarde los datos en `localStorage`. Al recargar la página, las tareas deben mantenerse.

**Ejercicio 12: Sistema de pestañas con AJAX**
> Crea un sistema de pestañas donde cada pestaña cargue contenido desde un archivo HTML o API diferente usando AJAX.

**Ejercicio 13: Validación completa de formulario**
> Crea un formulario extenso con los campos: nombre, email, teléfono, fecha de nacimiento, dirección y contraseña. Implementa validación completa y envía los datos con AJAX.

**Ejercicio 14: Juego de memoria**
> Crea un juego de memoria con cartas (pares iguales). Las cartas deben girarse con animaciones de flip.

**Ejercicio 15: Dashboard con datos reales**
> Crea un dashboard que muestre datos de una API pública (ej. clima, noticias, o estadísticas). Usa AJAX para obtener los datos y actualiza la interfaz periódicamente.

## Resumen de métodos clave

| Acción | Método jQuery | JavaScript puro |
|--------|---------------|-----------------|
| Seleccionar por ID | `$("#id")` | `document.getElementById("id")` |
| Seleccionar por clase | `$(".clase")` | `document.querySelectorAll(".clase")` |
| Cambiar texto | `.text("nuevo")` | `.textContent = "nuevo"` |
| Cambiar HTML | `.html("html")` | `.innerHTML = "html"` |
| Cambiar CSS | `.css("prop", "val")` | `.style.prop = "val"` |
| Agregar clase | `.addClass("clase")` | `.classList.add("clase")` |
| Evento click | `.click(fn)` | `.addEventListener("click", fn)` |
| Evento dinámico | `.on("click", ".sel", fn)` | - |
| AJAX GET | `$.get(url, fn)` | `fetch(url).then(fn)` |
| Animación fade | `.fadeToggle(400)` | CSS + `requestAnimationFrame` |

## Recursos útiles

- **Documentación oficial**: [api.jquery.com](https://api.jquery.com)
- **jQuery Learning Center**: [learn.jquery.com](https://learn.jquery.com)
- **CDN**: [code.jquery.com](https://code.jquery.com)
- **Plugins**: Más de 50 plugins útiles para layouts, imágenes, formularios, etc. 