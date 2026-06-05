# 🎨 Dale Vida a tu Web con CSS

## Introducción

Imagina que tu página web es una casa recién construida. El **HTML** serían las paredes, el techo y el suelo: la estructura. Pero una casa sin pintar, sin muebles ni decoración... ¡no es muy acogedora! **CSS (Cascading Style Sheets)** es la herramienta que usamos para pintar, decorar y darle estilo a nuestra casa digital.

En esta guía, aprenderás las propiedades CSS más importantes para transformar un documento HTML básico en una interfaz web atractiva y profesional.

---

## 📚 Teoría: Los Fundamentos del Estilo

Aquí tienes los conceptos clave que vimos en la presentación, pero con un poco más de detalle y ejemplos.

### 1. Los Colores en CSS

El color es una de las formas más poderosas de transmitir una sensación o emoción. En CSS, podemos definir el color de varias maneras :

| Método | Sintaxis | Ejemplo | ¿Cuándo usarlo? |
| :--- | :--- | :--- | :--- |
| **Palabras Clave** | `red`, `blue`, `green`... | `color: tomato;` | Fácil y rápido, pero con opciones limitadas a 147 colores . |
| **Hexadecimal** | `#` + código de 6 cifras (RRGGBB) | `color: #FF5733;` | El más común en la industria. Preciso y versátil. |
| **RGB (numérico)** | `rgb(rojo, verde, azul)` | `color: rgb(255, 87, 51);` | Intuitivo si piensas en "mezclar" luces de color. |
| **RGB (porcentual)** | `rgb(r%, g%, b%)` | `color: rgb(100%, 34%, 20%);` | Menos común, pero útil en ciertos contextos. |
| **HSL** | `hsl(tono, saturación, claridad)` | `color: hsl(11, 100%, 60%);` | El más fácil de modificar para crear paletas de colores . |

### 2. El Arte de la Tipografía

No es lo mismo leer un texto en Times New Roman que en una fuente moderna como Montserrat. CSS te da el control total sobre tu texto.

*   **`font-family`**: Define la fuente del texto. La mejor práctica es dar una lista de "fallback" por si el navegador no puede cargar tu primera opción.
    ```css
    p {
        font-family: "Montserrat", "Arial", sans-serif;
    }
    /* Si no encuentra Montserrat, usa Arial, y si no, cualquier fuente sans-serif */
    ```

*   **`font-size`**: Controla el tamaño del texto. Aquí es clave la diferencia entre `em` y `rem` :
    *   **`rem`**: "Root EM". Es relativo al tamaño de la fuente del elemento raíz (`<html>`). Es **predecible y recomendado para la mayoría de los casos**.
    *   **`em`**: Es relativo al tamaño de la fuente de su **elemento padre directo**. Puede volverse difícil de manejar en layouts complejos.

*   **`font-weight`**: Define el grosor (o "peso") de la fuente. Puedes usar palabras clave (`normal`, `bold`) o valores numéricos del 100 al 900 (donde 400 es normal y 700 es bold) .
    ```css
    h1 { font-weight: 700; } /* bold */
    .subtitulo { font-weight: 300; } /* más delgado */
    ```

*   **`text-align`**: Alinea el texto horizontalmente. Sus valores son: `left` (izquierda, por defecto), `right` (derecha), `center` (centrado) y `justify` (justificado) .

### 3. Fondos que Impresionan (`background`)

Podemos cambiar el fondo de cualquier elemento con las propiedades `background-*`. La más poderosa es la propiedad abreviada (shorthand) `background`.

| Propiedad | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| **`background-color`** | Establece un color de fondo sólido. | `background-color: #f0f0f0;` |
| **`background-image`** | Establece una imagen como fondo. | `background-image: url("mi-foto.jpg");` |
| **`background-repeat`** | Controla si la imagen se repite (`repeat`, `no-repeat`). | `background-repeat: no-repeat;` |
| **`background-position`** | Posiciona la imagen (`center`, `top`, `10px 20px`). | `background-position: center bottom;` |
| **`background-size`** | Controla el tamaño de la imagen (`cover`, `contain`, `100px`). | `background-size: cover;` |

> **✨ Pro-tip: La propiedad `background` (shorthand)**
> Para no escribir tanto, podemos combinar todo en una sola línea:
> ```css
> body {
>     background: #2c3e50 url("fondo.jpg") no-repeat center center / cover;
> }
> ```
> El orden sugerido es: `color` `imagen` `repetición` `posición` / `tamaño` .

---

## ✍️ Ejercicios Resueltos

Aprendamos haciendo. Vamos a construir el "Hero Section" del ejercicio guiado.

**Escenario:** Queremos crear una sección de cabecera (hero) que tenga una imagen de fondo, texto centrado y un botón.

**Paso 1: La Estructura HTML**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Hero Section</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="hero">
        <h1>Bienvenido al Futuro</h1>
        <p>Descubre un mundo de posibilidades con CSS</p>
        <a href="#" class="btn">Explorar Ahora</a>
    </header>
</body>
</html>
```

**Paso 2: El Estilo CSS (archivo `styles.css`)**

```css
/* 1. RESETEO BÁSICO de márgenes y paddings */
body {
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif; /* Fuente base para todo */
}

/* 2. ESTILOS DE NUESTRO HERO */
.hero {
    /* Fondo: imagen, sin repetición, centrada, y que cubra todo */
    background-image: url('https://picsum.photos/id/104/1200/600'); /* imagen de ejemplo */
    background-repeat: no-repeat;
    background-position: center center;
    background-size: cover;
    
    /* Añadimos una sombra interna oscura para que el texto blanco se lea mejor */
    background-color: #333; /* Color de respaldo mientras carga la imagen */
    
    /* Altura de la sección */
    height: 100vh; /* 100% del alto de la ventana (viewport height) */
    
    /* Flexbox para centrar el contenido (lo verás a detalle después) */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    
    text-align: center; /* Centramos el texto */
    color: white; /* Color de texto blanco */
}

.hero h1 {
    font-size: 4rem; /* Tamaño grande */
    font-weight: 700;
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.7); /* Sombra para mejorar legibilidad  */
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.5rem;
    margin-bottom: 2rem;
}

.btn {
    background-color: #ff6600; /* Color naranja */
    color: white;
    padding: 12px 24px;
    text-decoration: none; /* Quita el subrayado del enlace */
    font-weight: bold;
    border-radius: 8px; /* Bordes redondeados */
    transition: all 0.3s ease; /* Para una animación suave */
}

.btn:hover {
    background-color: #cc5200; /* Cambia de color al pasar el ratón */
    transform: scale(1.05); /* Se agranda ligeramente */
}
```

---

## 🧠 Ejercicios Propuestos

¡Es tu turno! Crea un archivo HTML y otro CSS para resolver lo siguiente:

1.  **Selectores y Colores:** Crea un `div` con la clase `caja`. Dale un fondo de color azul (`#3498db`) y un texto de color blanco.
2.  **Tipografía:** Crea una lista (`<ul>`) con tres ítems. Aplica a los ítems de la lista una fuente `'Courier New'`, tamaño `1.2rem` y un grosor de `bold` para los elementos pares (investiga la pseudo-clase `:nth-child(even)`).
3.  **Fondos:** Crea un elemento `<section>` de 300px de ancho y 200px de alto. Coloca una imagen de fondo que **no se repita**, esté centrada y tenga un tamaño de `contain`.

---

## 🚀 Proyecto Guiado: Mi Tarjeta de Presentación (Profile Card)

Llegó el momento de unir todo lo aprendido en un pequeño proyecto.

### Enunciado

Debes construir una "tarjeta de presentación" (profile card) para un usuario de una red social. La tarjeta debe mostrar una foto de perfil, el nombre, la biografía y un par de estadísticas (seguidores, publicaciones). El objetivo es aplicar estilos de texto, color, fondo y modelo de cajas (aunque el modelo de cajas lo veremos a profundidad después, ya estamos usando `padding`, `margin` y `border`).

### Código HTML (proporcionado)

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mi Tarjeta de Perfil</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="card">
        <div class="card-header"></div>
        <div class="card-body">
            <img src="https://randomuser.me/api/portraits/women/68.jpg" alt="Avatar" class="avatar">
            <h2>Ana López García</h2>
            <p class="bio">Desarrolladora web en formación. Amante del café y el código limpio. ✨</p>
            <div class="stats">
                <div class="stat">
                    <span class="stat-number">150</span>
                    <span class="stat-label">Fotos</span>
                </div>
                <div class="stat">
                    <span class="stat-number">1,200</span>
                    <span class="stat-label">Seguidores</span>
                </div>
                <div class="stat">
                    <span class="stat-number">280</span>
                    <span class="stat-label">Siguiendo</span>
                </div>
            </div>
            <button class="follow-btn">Seguir</button>
        </div>
    </div>
</body>
</html>
```

### Historias de Usuario

Para guiar el desarrollo, usaremos estas historias de usuario:

1.  **Yo, como visitante,** quiero que la tarjeta tenga un fondo atractivo y sutil, para que sea agradable a la vista.
2.  **Yo, como visitante,** quiero ver la foto de perfil como un círculo perfecto y que sobresalga del borde de la tarjeta.
3.  **Yo, como visitante,** quiero que el nombre y la biografía tengan una tipografía legible y moderna, y que la biografía esté en cursiva.
4.  **Yo, como visitante,** quiero que las estadísticas se muestren en una línea horizontal, bien espaciadas y con números resaltados en negrita.

### Tests (Autoevaluación)

Responde sí o no para saber si tu proyecto está completo. También puedes inspeccionar tu código con las herramientas de desarrollador del navegador (F12).

- **Test 1 (Estructura):** ¿He vinculado correctamente mi archivo `styles.css` en el HTML?
- **Test 2 (Fondo):** ¿El `body` tiene un color de fondo degradado (por ejemplo, `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`) y la `card` tiene un fondo blanco?
- **Test 3 (Foto de Perfil):** ¿La clase `.avatar` tiene un `border-radius: 50%` y un borde blanco para que parezca una insignia?
- **Test 4 (Posicionamiento):** ¿La clase `.avatar` tiene `margin-top` con un valor negativo (ej. `-50px`) para que sobresalga de la `card-header`?
- **Test 5 (Tipografía):** ¿La `font-family` de la tarjeta es `'Poppins'` o `'Roboto'` (con `sans-serif` de respaldo)? ¿La `.bio` tiene `font-style: italic`?
- **Test 6 (Layout):** ¿Las `.stats` usan `display: flex` y `justify-content: space-around` para alinear los números en una fila?
- **Test 7 (Interacción):** ¿El botón `.follow-btn` cambia de color de fondo y de texto (ej. de `#3498db` a `white`) cuando el ratón pasa por encima (`:hover`)?