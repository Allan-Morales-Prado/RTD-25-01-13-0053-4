# Guía Ejemplo 2: Grid responsivo con auto-fit y minmax()

## Vista previa del concepto
Este ejemplo crea un grid que se adapta automáticamente al ancho de la pantalla. Cada tarjeta tiene un ancho mínimo de 280px y máximo de 1 fracción (1fr), y el navegador decide cuántas columnas caben.

## Estructura completa del código

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid CSS - Ejemplo 2: Responsivo con minmax</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            min-height: 100vh;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        h1 {
            text-align: center;
            margin-bottom: 2rem;
            color: white;
            font-weight: 600;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .desc {
            text-align: center;
            color: rgba(255,255,255,0.9);
            margin-bottom: 2rem;
            font-size: 1.1rem;
        }

        /* ========== CÓDIGO GRID RESPONSIVO ========== */
        .grid-demo {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 1.5rem;
        }

        /* ========== ESTILOS DE PRODUCTO ========== */
        .product-card {
            background: white;
            border-radius: 20px;
            overflow: hidden;
            transition: all 0.3s ease;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        .product-card:hover {
            transform: scale(1.02);
            box-shadow: 0 20px 30px rgba(0,0,0,0.3);
        }

        .product-img {
            height: 200px;
            background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 4rem;
        }

        .product-info {
            padding: 1.5rem;
        }

        .product-info h3 {
            color: #1e293b;
            margin-bottom: 0.5rem;
            font-size: 1.3rem;
        }

        .price {
            font-size: 1.5rem;
            font-weight: bold;
            color: #3b82f6;
            margin: 0.75rem 0;
        }

        .btn {
            display: inline-block;
            background: #3b82f6;
            color: white;
            border: none;
            padding: 0.6rem 1.2rem;
            border-radius: 40px;
            cursor: pointer;
            font-weight: 600;
            transition: background 0.2s;
            text-decoration: none;
        }

        .btn:hover {
            background: #2563eb;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛍️ Grid Responsivo | auto-fit + minmax()</h1>
        <div class="desc">Las tarjetas se ajustan automáticamente al ancho de la pantalla</div>
        
        <div class="grid-demo">
            <div class="product-card">
                <div class="product-img">🎧</div>
                <div class="product-info">
                    <h3>Audífonos Bluetooth</h3>
                    <p>Sonido envolvente y batería de larga duración.</p>
                    <div class="price">$49.99</div>
                    <button class="btn">Comprar</button>
                </div>
            </div>
            <!-- Más product-cards... -->
        </div>
    </div>
</body>
</html>
```

## Explicación paso a paso del CSS (código nuevo o relevante)

### Bloque 1: Fondo degradado del body

```css
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

| Propiedad | Explicación |
|-----------|-------------|
| `background: linear-gradient(...)` | Crea un degradado: `135deg` es diagonal (esquina inferior izquierda a superior derecha). Comienza con `#667eea` (azul púrpura) y termina con `#764ba2` (púrpura intenso) |

**Relación con el HTML:** Fondo atractivo para toda la página, típico de tiendas modernas.

---

### Bloque 2: Texto con sombra

```css
h1 {
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
```

| Valor componente | Significado |
|------------------|-------------|
| `0` | Desplazamiento horizontal (0 = centrado) |
| `2px` | Desplazamiento vertical (2px hacia abajo) |
| `4px` | Radio de difuminado (qué tan borrosa es la sombra) |
| `rgba(0,0,0,0.1)` | Color negro con 10% de opacidad |

**Relación con el HTML:** Hace que el texto blanco destaque sobre el fondo degradado.

---

### Bloque 3: ⭐ **EL CÓDIGO GRID MÁS PODEROSO** ⭐

```css
.grid-demo {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
}
```

**Desglose de `repeat(auto-fit, minmax(280px, 1fr))`:**

| Parte | ¿Qué significa? |
|-------|-----------------|
| `repeat()` | Función que repite un patrón de columnas |
| `auto-fit` | Crea TANTAS columnas como quepan. Si sobra espacio, las estira para llenarlo |
| `minmax(280px, 1fr)` | Cada columna: mínimo 280px, máximo `1fr` (una fracción del espacio restante) |

**Comportamiento visual según el ancho:**

| Ancho de pantalla | Cuántas columnas | Explicación |
|-------------------|------------------|-------------|
| 1920px (escritorio) | 6 columnas | 6 × 280px = 1680px, cabe perfectamente |
| 1200px | 4 columnas | 4 × 280px = 1120px, espacio restante se reparte |
| 900px | 3 columnas | 3 × 280px = 840px, cabe justo |
| 600px | 2 columnas | 2 × 280px = 560px, cabe |
| 300px | 1 columna | Solo cabe 1 columna de 280px |

**Diferencia clave con `auto-fill`:**
- `auto-fill` crearía columnas vacías adicionales (espacio en blanco)
- `auto-fit` elimina las columnas vacías y estira las existentes

**Relación con el HTML:** Afecta directamente al `<div class="grid-demo">` y sus 5 hijos `product-card`. Sin media queries, el grid se reconfigura solo.

---

### Bloque 4: Tarjeta de producto con overflow hidden

```css
.product-card {
    background: white;
    border-radius: 20px;
    overflow: hidden;
    transition: all 0.3s ease;
    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
}
```

| Propiedad | ¿Qué hace? |
|-----------|-------------|
| `overflow: hidden` | Oculta cualquier contenido que se salga del borde redondeado (especialmente útil para la imagen) |
| `transition: all 0.3s ease` | Anima TODAS las propiedades que cambien durante 0.3 segundos con una aceleración suave |

```css
.product-card:hover {
    transform: scale(1.02);
    box-shadow: 0 20px 30px rgba(0,0,0,0.3);
}
```

Al pasar el mouse: la tarjeta crece un 2% (`scale(1.02)`) y su sombra se hace más grande y oscura.

---

### Bloque 5: Imagen del producto

```css
.product-img {
    height: 200px;
    background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4rem;
}
```

| Propiedad | ¿Qué hace? |
|-----------|-------------|
| `height: 200px` | Altura fija para todas las imágenes (uniformidad) |
| `background: linear-gradient(...)` | Degradado diagonal (`45deg`) de rosa claro a rosa intenso |
| `display: flex` | Convierte esta área en contenedor flex (para centrar el emoji) |
| `align-items: center` | Centra verticalmente el emoji dentro del área |
| `justify-content: center` | Centra horizontalmente el emoji |
| `font-size: 4rem` | Emoji enorme de 64px (4 × 16px) |

**Relación con el HTML:** Cada `<div class="product-img">` contiene un emoji (🎧, ⌚, 📱, etc.) que se centra perfectamente gracias a Flexbox dentro de Grid.

---

### Bloque 6: Botón de compra

```css
.btn {
    display: inline-block;
    background: #3b82f6;
    color: white;
    border: none;
    padding: 0.6rem 1.2rem;
    border-radius: 40px;
    cursor: pointer;
    font-weight: 600;
    transition: background 0.2s;
}

.btn:hover {
    background: #2563eb;
}
```

| Propiedad | ¿Qué hace? |
|-----------|-------------|
| `display: inline-block` | Permite aplicar padding y margin, pero se comporta como texto en línea |
| `border: none` | Elimina el borde por defecto de los botones |
| `border-radius: 40px` | Bordes completamente redondeados (píldora) |
| `cursor: pointer` | Cambia el cursor a una mano al pasar sobre el botón |
| `transition: background 0.2s` | Solo anima el cambio de color de fondo |

---

### Bloque 7: La descripción

```css
.desc {
    text-align: center;
    color: rgba(255,255,255,0.9);
    margin-bottom: 2rem;
    font-size: 1.1rem;
}
```

**Relación con el HTML:** El `<div class="desc">` es un subtítulo que explica el concepto de responsividad al usuario.

---

## Mapa visual: CSS ↔ HTML para el Ejemplo 2

| HTML | CSS | Propósito |
|------|-----|-----------|
| `<div class="grid-demo">` | `display: grid` | Contenedor grid principal |
| | `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` | Responsividad automágica |
| | `gap: 1.5rem` | Espacio entre tarjetas |
| `<div class="product-card">` | `.product-card` | Tarjeta individual con sombra y hover |
| `<div class="product-img">` | `.product-img` | Área de 200px con emoji centrado |
| `<div class="product-info">` | `.product-info` | Padding para el contenido textual |
| `<button class="btn">` | `.btn` + `.btn:hover` | Botón azul redondeado |

---
