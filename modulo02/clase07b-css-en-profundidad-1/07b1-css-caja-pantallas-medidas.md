# 📐 CSS en profundidad (parte 1): La Caja, la Pantalla y las Medidas

## Introducción: ¿Por qué mi `<div>` no se pone al lado del otro?

Seguro que te ha pasado. Quieres dos elementos uno al lado del otro, pero el navegador insiste en poner uno debajo del otro. O quieres un margen, y no se aplica. La respuesta a estos problemas está en tres conceptos clave que veremos hoy:

1.  **El modelo de cajas:** Todo en CSS es una caja. Para maquetar, debes entender cómo se mide cada caja.
2.  **La propiedad `display`:** Define cómo se comporta esa caja en relación con las que están a su alrededor. ¿Es una caja que ocupa toda una línea (`block`)? ¿O una que se coloca al lado de otras (`inline`)?
3.  **Las unidades de medida:** ¿Usas `px`, `rem`, `%` o `vh`? Cada una tiene un propósito y un comportamiento diferente.

---

## 📚 Teoría: Los Pilares del Layout

### 1. El Modelo de Cajas (Box Model)

Este es, sin duda, el concepto más importante en CSS. El navegador representa cada elemento HTML como una caja rectangular. El modelo de cajas describe el espacio que ocupa esta caja y se compone de cuatro capas :

*   **Área de Contenido (Content):** El espacio donde va tu texto o imagen. Sus dimensiones se controlan con `width` y `height`.
*   **Relleno (Padding):** Espacio transparente **dentro** de la caja, alrededor del contenido. Crea separación entre el contenido y el borde.
*   **Borde (Border):** Una línea que rodea el relleno (y el contenido). Puede tener grosor (`border-width`), estilo (`border-style`) y color (`border-color`).
*   **Margen (Margin):** Espacio transparente **fuera** de la caja, que la separa de otros elementos. Crea separación entre cajas.

Hay una forma de ver esta caja en tu navegador en este momento:
1.  Abre cualquier página web.
2.  Haz clic derecho y selecciona **"Inspeccionar"** o **"Inspeccionar elemento"**.
3.  En la pestaña "Estilos" o "Styles", verás una representación gráfica del modelo de cajas del elemento que hayas seleccionado . ¡Pruébalo!

**El "Reseteo" (CSS Reset)**
Es muy común empezar una hoja de estilos eliminando los márgenes y rellenos que los navegadores aplican por defecto a ciertos elementos (como el `<body>` o los `<h1>`). El código `* { margin: 0; padding: 0; }` es un comodín que selecciona **todos** los elementos para quitarles esos espacios predeterminados y empezar desde cero.

### 2. La Propiedad `display`: `inline`, `block` y `inline-block`

Esta propiedad decide el "comportamiento social" de nuestra caja. ¿Quiere ser un elemento solitario que ocupa toda una fila, o un elemento gregario que se sienta al lado de los demás? 

| Tipo (`display`) | Comportamiento | ¿Responde a `width`/`height`? | Ejemplos comunes |
| :--- | :--- | :--- | :--- |
| **`block`** | Ocupa todo el ancho disponible y **siempre empieza en una nueva línea**. | ✅ Sí | `<div>`, `<h1>`, `<p>`, `<section>` |
| **`inline`** | Ocupa solo el espacio de su contenido. **Se coloca en línea** con otros elementos. | ❌ No | `<span>`, `<a>`, `<strong>`, `<img>` |
| **`inline-block`** | Se coloca en línea **pero** permite ajustar su ancho y alto. 🚀 | ✅ Sí | Útil para menús de navegación o botones. |

> **¿Por qué no puedo darle un `width` a un `<span>`?** Porque el `<span>`, por defecto, es un elemento `inline`. Para poder cambiar su ancho o alto, debes convertirlo en `inline-block` o `block` con CSS .

**Ejemplo visual:**
```html
<!-- Código de ejemplo -->
<div>SOY UN DIV (block)</div>
<a href="#">Soy un enlace (inline)</a>
<a href="#">Otro enlace (inline)</a>
<span class="especial">Span con inline-block</span>
```
```css
.especial {
    display: inline-block;
    width: 150px; /* Esto SÍ funciona */
    background-color: lightblue;
}
```

### 3. Unidades de Medida: Absolutas vs. Relativas

Para establecer el tamaño de una caja (`width`, `height`), un margen (`margin`) o un texto (`font-size`), tenemos dos grandes familias de unidades .

*   **Unidades Absolutas:** Son fijas y predecibles. Siempre miden lo mismo.
    *   `px` (píxeles): La reina de las absolutas. Es la unidad más común para bordes, sombras y detalles finos.
*   **Unidades Relativas:** Son flexibles y dependen de un contexto (el tamaño de la pantalla o de la fuente "padre"). Son **fundamentales para crear diseños responsivos (que se adaptan a móviles)**.
    *   `%` (porcentaje): Relativo al tamaño del elemento **padre**.
    *   `em`: Relativo al tamaño de la fuente del elemento **padre** directo .
    *   `rem` (Root EM): Relativo al tamaño de la fuente del elemento **raíz (`<html>`)**. Es la unidad más recomendable para tamaños de texto, ya que es mucho más predecible que `em` .
    *   `vw` / `vh` (Viewport Width / Height): Relativo al **ancho (1% de la pantalla)** o **alto (1% de la pantalla)** de la ventana del navegador. Ideales para crear secciones que ocupen toda la pantalla (`height: 100vh;`).

| Unidad | Tipo | ¿Relativo a qué? |
| :--- | :--- | :--- |
| `px` | Absoluta | Nada |
| `%` | Relativa | Elemento padre |
| `em` | Relativa | Fuente del elemento padre |
| `rem` | Relativa | Fuente del elemento raíz (`<html>`) |
| `vh`/`vw` | Relativa | Ventana del navegador (viewport) |

---

## ✍️ Ejercicio Resuelto: "Codo a codo" (como en el PPT)

Repliquemos el famoso layout de imagen a la izquierda y texto a la derecha.

**HTML (Estructura base)**
```html
<section class="charla-section">
    <div class="contenedor-charla">
        <img class="img-charla" src="https://picsum.photos/id/1/300/200" alt="Computador">
        <div class="texto-charla">
            <h2>Próxima Charla: CSS Avanzado</h2>
            <p>Aprende los secretos del layout moderno. ¡No te lo pierdas!</p>
        </div>
    </div>
</section>
```

**CSS (La solución)**
```css
/* 1. Reset básico */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box; /* ¡Esto es clave! Ver recuadro */
}

/* 2. Estilos de la sección */
.charla-section {
    background-color: #1a1a2e;
    color: #fff;
    padding: 100px 0; /* Espacio arriba/abajo */
    text-align: center; /* Para centrar el título si lo hubiera */
}

/* 3. El contenedor que usa la magia */
.contenedor-charla {
    width: 80%;
    margin: 0 auto; /* Centra el contenedor horizontalmente */
    background-color: #16213e;
    border-radius: 20px;
    overflow: hidden; /* Para respetar el borde redondeado */
}

/* 4. Haciendo que imagen y texto sean inline-block */
.img-charla, .texto-charla {
    display: inline-block; /* ¡La clave del ejercicio! */
    vertical-align: middle; /* Centrado vertical */
}

/* 5. Anchos específicos */
.img-charla {
    width: 40%;
}

.texto-charla {
    width: 59%; /* 40% + 59% = 99%, dejamos 1% para posibles padding/bordes */
    padding: 20px;
    text-align: left;
}
```
**💡 Pro-tip: `box-sizing: border-box;`**
Por defecto, si a una caja le pones `width: 300px` y luego `padding: 20px`, el ancho total se convertirá en `340px`. Esto es un dolor de cabeza. La propiedad `box-sizing: border-box;` hace que el `width` y `height` que definas sean el **ancho total final**, incluyendo padding y borde . ¡Es una práctica estándar aplicarlo a todo con `* { box-sizing: border-box; }`!

---

## 🧠 Ejercicios Propuestos

Pon a prueba lo que has aprendido:

1.  **Analizando cajas:** Dado un `<div>` con `width: 200px; padding: 20px; border: 5px solid black; margin: 15px;`. Calcula el ancho total que ocupará este elemento en la pantalla (sin `box-sizing`).
2.  **Menú de navegación:** Crea una lista `<ul>` con varios `<li>` que contengan enlaces `<a>`. Usa CSS para que los elementos de la lista se muestren **en horizontal**, tengan un `padding` de `10px` y un `width` de `100px`. ¿Qué valor de `display` necesitas?
3.  **Fuente flexible:** Quieres que el texto de tu página se adapte si el usuario cambia el zoom por defecto del navegador. ¿Usarías `px` o `rem` para el `font-size` del texto general? ¿Por qué?

---

## 🚀 Proyecto Guiado: Landing Page de un Podcast

Vamos a construir la sección principal de una landing page para un podcast ficticio. Aplicaremos todo: box model, display y unidades de medida.

### Enunciado

Necesitamos una sección "Hero" que presente el nuevo episodio. Debe tener una imagen de fondo que ocupe toda la pantalla, un título, una descripción y un botón. Debajo, una sección con dos columnas: una con una imagen del anfitrión y otra con los detalles del episodio.

### Código HTML (proporcionado)

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Podcast: CSS Ninja</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="hero">
        <div class="contenido-hero">
            <h1>CSS Ninja Podcast</h1>
            <p>Domina el layout de la web en 10 episodios.</p>
            <a href="#" class="boton">Escuchar Ahora</a>
        </div>
    </header>

    <section class="episodio">
        <div class="contenedor">
            <div class="columna">
                <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="Anfitrión" class="img-anfitrion">
            </div>
            <div class="columna detalles">
                <h2>Nuevo Episodio: "Modelo de Cajas"</h2>
                <p>En este episodio, desglosamos el misterioso CSS Box Model. Aprende a controlar márgenes, bordes y rellenos como un profesional.</p>
                <p><strong>Duración:</strong> 45 minutos</p>
            </div>
        </div>
    </section>
</body>
</html>
```

### Historias de Usuario

1.  **Layout Hero:** Como visitante, quiero que el `header` tenga una imagen de fondo (`background-image`) que cubra toda la pantalla y que el texto esté perfectamente centrado.
2.  **Comportamiento de Cajas:** Como visitante, quiero que al hacer clic en el botón, este tenga un margen superior (`margin-top`) para separarlo del texto, y un relleno interno (`padding`) grande para que sea fácil de pulsar.
3.  **Diseño de Columnas:** Como visitante, quiero que la sección "episodio" muestre la imagen y el texto lado a lado en pantallas grandes, pero que se vea limpio y ordenado.
4.  **Unidades Relativas:** Como desarrollador, debo usar `rem` para los tamaños de fuente y `vh` para la altura del Hero, asegurando que el diseño sea responsivo.

### Tests (Autoevaluación)

*   **Test 1 (Hero):** ¿La clase `.hero` tiene `height: 100vh;` y `background-size: cover;`? (Asumiendo que le pusiste una imagen de fondo).
*   **Test 2 (Centrado):** ¿El `.contenido-hero` está centrado vertical y horizontalmente? (Pista: podrías usar `display: flex` en `.hero` o un `margin` inteligente).
*   **Test 3 (Modelo de Cajas):** ¿El `.boton` tiene `padding: 12px 24px;` y `margin-top: 20px;`? Al inspeccionarlo en el navegador, ¿ves el padding y margin reflejados?
*   **Test 4 (Columnas):** ¿Las `.columna` tienen `display: inline-block;` y un `width` adecuado (ej. `49%`)? ¿O usaste `float` o `flex`? (Cualquiera vale, pero `inline-block` es el reto).
*   **Test 5 (Medidas):** ¿El `h1` usa `font-size: 3rem;` en lugar de `px`? ¿Los textos generales usan `rem` o `em`?