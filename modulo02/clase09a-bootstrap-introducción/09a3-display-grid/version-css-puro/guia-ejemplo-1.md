# Guía Ejemplo 1: Grid con columnas fijas

## Vista previa del concepto
Este ejemplo crea una cuadrícula con columnas de ancho fijo (300px cada una). Es útil cuando necesitas tamaños predecibles, como en una galería de productos con dimensiones uniformes.

## Estructura completa del código

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid CSS - Ejemplo 1: Columnas fijas</title>
    <style>
        /* ========== RESET Y ESTILOS BASE ========== */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
            background: #f5f7fa;
            padding: 2rem;
            min-height: 100vh;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        h1 {
            text-align: center;
            margin-bottom: 2rem;
            color: #1e293b;
            font-weight: 600;
        }

        /* ========== CÓDIGO GRID PRINCIPAL ========== */
        .grid-demo {
            display: grid;
            grid-template-columns: 300px 300px 300px;
            gap: 20px;
            justify-content: center;
        }

        /* ========== ESTILOS VISUALES (SOLO PARA QUE SE VEA BONITO) ========== */
        .card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
            transition: transform 0.2s, box-shadow 0.2s;
            border: 1px solid #e2e8f0;
        }

        .card:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
        }

        .card h3 {
            color: #2c3e66;
            margin-bottom: 0.75rem;
            font-size: 1.25rem;
        }

        .card p {
            color: #475569;
            line-height: 1.5;
        }

        .badge {
            display: inline-block;
            background: #3b82f6;
            color: white;
            font-size: 0.75rem;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            margin-top: 1rem;
        }

        /* ========== MEDIA QUERIES PARA RESPONSIVE ========== */
        @media (max-width: 1000px) {
            .grid-demo {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 640px) {
            .grid-demo {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📐 Grid CSS | Columnas fijas (300px)</h1>
        <div class="grid-demo">
            <div class="card">
                <h3>📌 Tarjeta 1</h3>
                <p>Grid con columnas fijas. Cada columna mide exactamente 300px de ancho.</p>
                <div class="badge">300px</div>
            </div>
            <div class="card">
                <h3>📌 Tarjeta 2</h3>
                <p>El tamaño no se adapta al contenedor, se mantiene fijo.</p>
                <div class="badge">300px</div>
            </div>
            <div class="card">
                <h3>📌 Tarjeta 3</h3>
                <p>Perfecto para layouts donde necesitas anchos predecibles.</p>
                <div class="badge">300px</div>
            </div>
            <div class="card">
                <h3>📌 Tarjeta 4</h3>
                <p>Las columnas adicionales pasan automáticamente a la siguiente fila.</p>
                <div class="badge">extra</div>
            </div>
            <div class="card">
                <h3>📌 Tarjeta 5</h3>
                <p>Usamos `justify-content: center` para centrar la cuadrícula.</p>
                <div class="badge">extra</div>
            </div>
        </div>
    </div>
</body>
</html>
```

## Explicación paso a paso del CSS (bloque por bloque)

### Bloque 1: Reset universal `* {}`

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
```

| Propiedad | Valor | ¿Qué hace? |
|-----------|-------|-------------|
| `margin` | `0` | Elimina todos los márgenes por defecto que los navegadores aplican (como el margen del `<body>`) |
| `padding` | `0` | Elimina todos los rellenos por defecto |
| `box-sizing` | `border-box` | Hace que el `width` y `height` incluyan padding y borde. Ejemplo: un div con `width:300px` + `padding:20px` seguirá midiendo 300px totales |

**Relación con el HTML:** Afecta a **todos los elementos** de la página (`*` es el selector universal). Sin este reset, los navegadores añaden márgenes inconsistentes.

---

### Bloque 2: Estilos del `<body>`

```css
body {
    font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
    background: #f5f7fa;
    padding: 2rem;
    min-height: 100vh;
}
```

| Propiedad | Valor | ¿Qué hace? |
|-----------|-------|-------------|
| `font-family` | `system-ui, ...` | Aplica la fuente nativa del sistema operativo (más rápida y consistente) |
| `background` | `#f5f7fa` | Color gris muy claro de fondo para toda la página |
| `padding` | `2rem` | Espacio interior de 32px (2 × 16px) alrededor de todo el contenido del body |
| `min-height` | `100vh` | Altura mínima igual al 100% del alto de la ventana (`vh` = viewport height) |

**Relación con el HTML:** El `<body>` contiene todo el contenido visible. Este fondo gris y el padding crean un "margen" visual alrededor del contenido principal.

---

### Bloque 3: Contenedor `.container`

```css
.container {
    max-width: 1200px;
    margin: 0 auto;
}
```

| Propiedad | Valor | ¿Qué hace? |
|-----------|-------|-------------|
| `max-width` | `1200px` | El contenedor no crecerá más de 1200px de ancho |
| `margin` | `0 auto` | `0` arriba/abajo, `auto` izquierda/derecha → centra horizontalmente el contenedor |

**Relación con el HTML:** El `<div class="container">` envuelve todo el contenido (título + grid). Esto evita que en pantallas enormes el contenido se estire demasiado.

---

### Bloque 4: Título `<h1>`

```css
h1 {
    text-align: center;
    margin-bottom: 2rem;
    color: #1e293b;
    font-weight: 600;
}
```

| Propiedad | Valor | ¿Qué hace? |
|-----------|-------|-------------|
| `text-align` | `center` | Centra el texto horizontalmente |
| `margin-bottom` | `2rem` | Espacio de 32px debajo del título |
| `color` | `#1e293b` | Color gris oscuro azulado |
| `font-weight` | `600` | Semi-negrita (400 es normal, 700 es negrita completa) |

---

### Bloque 5: ⭐ **EL CÓDIGO GRID MÁS IMPORTANTE** ⭐

```css
.grid-demo {
    display: grid;
    grid-template-columns: 300px 300px 300px;
    gap: 20px;
    justify-content: center;
}
```

| Propiedad | Valor | ¿Qué hace? |
|-----------|-------|-------------|
| `display` | `grid` | Convierte el elemento en un **contenedor grid**. Sus hijos directos se vuelven "ítems grid" |
| `grid-template-columns` | `300px 300px 300px` | Crea **3 columnas**, cada una de exactamente 300px de ancho |
| `gap` | `20px` | Espacio de 20px **entre** las columnas Y entre las filas |
| `justify-content` | `center` | Centra todo el conjunto de columnas dentro del contenedor grid |

**Relación con el HTML:** 
- El `<div class="grid-demo">` es el contenedor grid
- Sus hijos directos son los 5 `<div class="card">`
- Los primeros 3 cards ocupan la primera fila (columnas 1, 2 y 3)
- Los siguientes 2 cards pasan automáticamente a la **segunda fila** (ocupan columna 1 y 2 de la fila 2, dejando un hueco)

**Visualización:**
```
Fila 1: [Card1 - 300px] [Card2 - 300px] [Card3 - 300px]
Fila 2: [Card4 - 300px] [Card5 - 300px] [vacío]
```

---

### Bloque 6: Estilos de tarjeta `.card`

```css
.card {
    background: white;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07);
    transition: transform 0.2s, box-shadow 0.2s;
    border: 1px solid #e2e8f0;
}
```

| Propiedad | ¿Qué hace? |
|-----------|-------------|
| `background: white` | Fondo blanco para cada tarjeta |
| `border-radius: 12px` | Esquinas redondeadas |
| `padding: 1.5rem` | Espacio interior de 24px en todos los lados |
| `box-shadow` | Sombra sutil que da profundidad |
| `transition` | Animación suave al cambiar `transform` o `box-shadow` |
| `border` | Borde gris muy claro |

```css
.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 20px rgba(0, 0, 0, 0.1);
}
```
Cuando el mouse pasa sobre una tarjeta (`:hover`):
- `transform: translateY(-4px)` → se levanta 4px hacia arriba
- Sombra más grande y oscura → efecto flotante

---

### Bloque 7: Estilos internos de tarjeta

```css
.card h3 {
    color: #2c3e66;
    margin-bottom: 0.75rem;
    font-size: 1.25rem;
}

.card p {
    color: #475569;
    line-height: 1.5;
}

.badge {
    display: inline-block;
    background: #3b82f6;
    color: white;
    font-size: 0.75rem;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    margin-top: 1rem;
}
```

| Selector | ¿Qué hace? |
|----------|-------------|
| `.card h3` | Estilos específicos para los títulos DENTRO de cada tarjeta |
| `.card p` | Estilos para los párrafos DENTRO de cada tarjeta |
| `.badge` | Crea una "etiqueta" redondeada azul con texto blanco |

---

### Bloque 8: Media queries (responsividad)

```css
@media (max-width: 1000px) {
    .grid-demo {
        grid-template-columns: repeat(2, 1fr);
    }
}
```

**¿Qué es una media query?** Una regla que solo aplica cuando se cumple una condición (en este caso, cuando el ancho de la pantalla es ≤ 1000px).

| Condición | Cambio que aplica |
|-----------|-------------------|
| Pantalla ≤ 1000px | `grid-template-columns: repeat(2, 1fr)` → Ahora **2 columnas** flexibles que reparten el espacio equitativamente (`1fr`) |

```css
@media (max-width: 640px) {
    .grid-demo {
        grid-template-columns: 1fr;
    }
}
```

| Condición | Cambio que aplica |
|-----------|-------------------|
| Pantalla ≤ 640px (móvil) | `grid-template-columns: 1fr` → **1 sola columna** que ocupa todo el ancho |

**Relación con el HTML:** Estas reglas hacen que el diseño se adapte automáticamente a diferentes tamaños de pantalla sin modificar el HTML.

---

## Relación completa entre CSS y HTML (mapeo visual)

| Elemento HTML | Clase/Etiqueta | CSS que lo afecta |
|---------------|----------------|-------------------|
| `<body>` | - | `body` (fondo, padding, fuente) |
| `<div class="container">` | `.container` | max-width, centrado |
| `<h1>` | `h1` | texto centrado, color, margen inferior |
| `<div class="grid-demo">` | `.grid-demo` | **display: grid**, columnas, gap, justify-content |
| `<div class="card">` (cada uno) | `.card` | fondo blanco, bordes, sombra, padding, hover |
| `<h3>` dentro de card | `.card h3` | color, tamaño, margen |
| `<p>` dentro de card | `.card p` | color, interlineado |
| `<div class="badge">` | `.badge` | fondo azul, texto blanco, esquinas redondeadas |

---
