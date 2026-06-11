# Proyecto: Galería de Gatitos - Aprendiendo Flexbox para entender Bootstrap

## 🎯 Objetivo del proyecto

Construir una **galería de imágenes de gatitos** que te enseñará **TODO lo que necesitas saber de Flexbox** para después entender el sistema de grillas de Bootstrap.

### ¿Qué aprenderás?

| Concepto Flexbox | Clase equivalente en Bootstrap |
|-----------------|-------------------------------|
| `display: flex` | `.d-flex` |
| `flex-wrap: wrap` | `.flex-wrap` |
| `justify-content` | `.justify-content-*` |
| `align-items` | `.align-items-*` |
| `flex: 1` | `.flex-grow-1` |
| `gap` | `.g-*` (Bootstrap 5) |
| `flex-direction` | `.flex-column`, `.flex-row` |
| `order` | `.order-*` |

---

## 📁 Estructura del proyecto

```
galeria-gatitos/
│
├── index.html          # Página principal
├── css/
│   └── estilos.css     # Todos nuestros estilos Flexbox
└── imagenes/           # (opcional) imágenes locales
```

---

## 🐱 Paso 1: Estructura HTML base

Crea un archivo `index.html` con la estructura básica:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galería de Gatitos - Aprendiendo Flexbox</title>
    <link rel="stylesheet" href="css/estilos.css">
</head>
<body>
    <div class="contenedor-principal">
        <!-- Aquí construiremos nuestra galería -->
    </div>
</body>
</html>
```

---

## 🐱 Paso 2: El contenedor padre - `display: flex`

### Teoría
`display: flex` convierte un elemento en **contenedor flexible**. Todos sus hijos directos se convierten en **ítems flex**.

### Ejercicio
Vamos a crear un header con logo y navegación.

```html
<!-- Dentro de .contenedor-principal -->
<header class="header">
    <div class="logo">🐱 Gatitos Galería</div>
    <nav class="nav">
        <a href="#">Inicio</a>
        <a href="#">Galería</a>
        <a href="#">Contacto</a>
    </nav>
</header>
```

```css
/* css/estilos.css */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background: #f5f5f5;
    padding: 20px;
}

.contenedor-principal {
    max-width: 1200px;
    margin: 0 auto;
}

/* ========== PASO 2: ACTIVANDO FLEXBOX ========== */
.header {
    background: #2c3e50;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 30px;
    
    /* ¡Aquí activamos Flexbox! */
    display: flex;
}

.logo {
    color: white;
    font-size: 24px;
    font-weight: bold;
}

.nav {
    /* Por ahora, los links se ven pegados al logo */
}

.nav a {
    color: white;
    text-decoration: none;
    margin-left: 20px;
}
```

**🔍 Observa:** Al activar `display: flex`, el logo y la navegación se colocaron **en la misma fila** (horizontalmente). Sin Flexbox, estarían uno debajo del otro.

---

## 🐱 Paso 3: `justify-content` - Distribución horizontal

### Teoría
`justify-content` controla **cómo se distribuye el espacio SOBRANTE** horizontalmente.

| Valor | Efecto | Bootstrap equivalente |
|-------|--------|----------------------|
| `flex-start` | Elementos a la izquierda | `.justify-content-start` |
| `flex-end` | Elementos a la derecha | `.justify-content-end` |
| `center` | Elementos centrados | `.justify-content-center` |
| `space-between` | Espacio entre elementos | `.justify-content-between` |
| `space-around` | Espacio alrededor | `.justify-content-around` |
| `space-evenly` | Espacio igualitario | `.justify-content-evenly` |

### Ejercicio
Queremos que el logo esté a la izquierda y los links a la derecha.

```css
/* Actualiza .header en estilos.css */
.header {
    background: #2c3e50;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 30px;
    display: flex;
    
    /* Distribuye el espacio: logo izquierda, nav derecha */
    justify-content: space-between;
    
    /* También queremos que estén centrados verticalmente */
    align-items: center;
}
```

**🎯 Ejercicio práctico:** Cambia `space-between` por `center`, `flex-end`, `space-around`. Observa cómo se mueven los elementos.

---

## 🐱 Paso 4: Galería básica - `flex-wrap`

### Teoría
`flex-wrap: wrap` permite que los elementos **pasen a la siguiente línea** cuando no caben en el ancho disponible.

### Ejercicio
Vamos a crear las tarjetas de los gatitos.

```html
<!-- Después del </header> -->
<main>
    <h1 class="titulo">🐾 Nuestros Gatitos</h1>
    
    <div class="galeria">
        <!-- Tarjeta 1 -->
        <div class="tarjeta">
            <div class="imagen">🐱</div>
            <h3>Bigotes</h3>
            <p>Gatito naranja muy juguetón</p>
            <button>Adoptar</button>
        </div>
        
        <!-- Tarjeta 2 -->
        <div class="tarjeta">
            <div class="imagen">🐱</div>
            <h3>Luna</h3>
            <p>Gatita negra cariñosa</p>
            <button>Adoptar</button>
        </div>
        
        <!-- Tarjeta 3 -->
        <div class="tarjeta">
            <div class="imagen">🐱</div>
            <h3>Simba</h3>
            <p>Gatito blanco y gris, muy activo</p>
            <button>Adoptar</button>
        </div>
        
        <!-- Tarjeta 4 -->
        <div class="tarjeta">
            <div class="imagen">🐱</div>
            <h3>Michi</h3>
            <p>Gatito tricolor, muy tranquilo</p>
            <button>Adoptar</button>
        </div>
        
        <!-- Tarjeta 5 -->
        <div class="tarjeta">
            <div class="imagen">🐱</div>
            <h3>Copito</h3>
            <p>Gatito blanco como la nieve</p>
            <button>Adoptar</button>
        </div>
    </div>
</main>
```

```css
/* Añade esto a estilos.css */
.titulo {
    text-align: center;
    margin-bottom: 30px;
    color: #2c3e50;
}

/* ========== PASO 4: GALERÍA CON FLEX WRAP ========== */
.galeria {
    /* Activamos Flexbox */
    display: flex;
    
    /* Permitimos que las tarjetas pasen a nueva línea */
    flex-wrap: wrap;
    
    /* Espacio entre tarjetas */
    gap: 20px;
}

.tarjeta {
    background: white;
    border-radius: 10px;
    padding: 15px;
    width: 250px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    transition: transform 0.3s;
}

.tarjeta:hover {
    transform: translateY(-5px);
}

.imagen {
    background: #ecf0f1;
    height: 150px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 60px;
    margin-bottom: 15px;
}

.tarjeta h3 {
    margin-bottom: 10px;
    color: #2c3e50;
}

.tarjeta p {
    color: #7f8c8d;
    margin-bottom: 15px;
}

.tarjeta button {
    background: #e74c3c;
    color: white;
    border: none;
    padding: 8px 15px;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
}

.tarjeta button:hover {
    background: #c0392b;
}
```

**🔍 Observa:**
- Con `flex-wrap: wrap`, las tarjetas se ajustan automáticamente
- Cuando no caben 4 tarjetas, algunas pasan a la siguiente línea
- `gap: 20px` crea espacio entre las tarjetas

**🎯 Ejercicio práctico:** Cambia el ancho de las tarjetas a `width: 300px` y redimensiona la ventana del navegador. Observa cómo se comporta el wrap.

---

## 🐱 Paso 5: `justify-content` en la galería

### Teoría
Podemos controlar cómo se alinean las tarjetas cuando hay espacio sobrante.

### Ejercicio
Prueba diferentes alineaciones en la galería.

```css
/* Prueba estos valores en .galeria */
.galeria {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    
    /* Cambia este valor y observa */
    justify-content: center;  /* prueba: flex-start, center, space-between, space-evenly */
}
```

**🎯 Desafío:** ¿Qué valor usarías para que las tarjetas se distribuyan uniformemente y la última se alinee a la izquierda? (Respuesta: `flex-start`)

---

## 🐱 Paso 6: `align-items` y `align-content` - Alineación vertical

### Teoría

| Propiedad | ¿Qué controla? | ¿Cuándo se nota? |
|-----------|----------------|------------------|
| `align-items` | Alineación vertical de los ítems en UNA fila | Cuando los ítems tienen diferentes alturas |
| `align-content` | Alineación vertical de MÚLTIPLES filas | Cuando hay wrap y varias líneas |

### Ejercicio
Vamos a crear un footer con 3 columnas de diferentes alturas.

```html
<!-- Antes de cerrar .contenedor-principal -->
<footer class="footer">
    <div class="footer-col">
        <h4>🐱 Sobre nosotros</h4>
        <p>Somos una fundación dedicada a encontrar hogar para gatitos.</p>
    </div>
    <div class="footer-col">
        <h4>📞 Contacto</h4>
        <p>Email: hola@gatitos.com<br>Tel: +56 9 1234 5678</p>
    </div>
    <div class="footer-col">
        <h4>❤️ Síguenos</h4>
        <p>Instagram<br>Facebook<br>TikTok</p>
    </div>
</footer>
```

```css
/* ========== PASO 6: ALIGN-ITEMS ========== */
.footer {
    background: #2c3e50;
    color: white;
    padding: 30px;
    border-radius: 10px;
    margin-top: 40px;
    
    display: flex;
    flex-wrap: wrap;
    gap: 30px;
    
    /* Prueba diferentes valores */
    align-items: center;  /* Prueba: flex-start, center, flex-end, stretch */
}

.footer-col {
    flex: 1;  /* Explicaremos esto en el paso 7 */
    min-width: 200px;
}

.footer-col h4 {
    margin-bottom: 15px;
    color: #e74c3c;
}
```

**🔍 Observa:**
- Con `align-items: center`, todas las columnas se centran verticalmente (aunque tengan diferente altura)
- Con `align-items: stretch` (valor por defecto), todas toman la altura de la más grande

---

## 🐱 Paso 7: `flex: 1` - El poder de crecer

### Teoría
La propiedad `flex` es una abreviación de:

```css
flex: 1;  /* equivale a: */
flex-grow: 1;
flex-shrink: 1;
flex-basis: 0;
```

- **`flex-grow: 1`** → El elemento PUEDE crecer para ocupar espacio sobrante
- **`flex-grow: 0`** → El elemento NO crece (como las columnas de Bootstrap `.col-*`)

### Ejercicio
Observa cómo se comporta el footer con y sin `flex: 1`.

```css
/* Prueba comentando flex: 1 en .footer-col */
.footer-col {
    /* flex: 1;  ← Comenta esta línea */
    min-width: 200px;
}
```

**🔍 Diferencia:**
- **Con `flex: 1`** → Las columnas se expanden para ocupar todo el ancho disponible
- **Sin `flex: 1`** → Cada columna ocupa solo el ancho de su contenido

### Analogía para estudiantes
Imagina que tienes 3 personas y una pizza (el espacio sobrante):
- `flex: 1` = "Quiero mi parte de la pizza"
- `flex: 0` = "No quiero pizza, solo lo mío"

---

## 🐱 Paso 8: Sistema de 12 columnas (como Bootstrap)

### Teoria
Ahora vamos a construir **nuestro propio sistema de grillas** similar al de Bootstrap.

```css
/* ========== PASO 8: SISTEMA DE 12 COLUMNAS ========== */
.grid-demo {
    background: #ecf0f1;
    padding: 20px;
    border-radius: 10px;
    margin: 30px 0;
}

.grid-row {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-bottom: 15px;
}

/* Columnas base (como Bootstrap pero más simple) */
.col {
    flex: 1;  /* Ocupa espacio proporcional */
}

.col-4 {
    flex: 0 0 auto;
    width: calc(33.333% - 10px);  /* Restamos un poco por el gap */
}

.col-6 {
    flex: 0 0 auto;
    width: calc(50% - 7.5px);
}

.col-8 {
    flex: 0 0 auto;
    width: calc(66.666% - 10px);
}

.col-12 {
    flex: 0 0 auto;
    width: 100%;
}

/* Estilos de demostración */
.demo-caja {
    background: #3498db;
    color: white;
    padding: 15px;
    text-align: center;
    border-radius: 5px;
}
```

```html
<!-- Añade esto después de la galería -->
<section class="grid-demo">
    <h2>📐 Nuestro propio sistema de 12 columnas</h2>
    <p>¡Como Bootstrap, pero hecho por nosotros!</p>
    
    <div class="grid-row">
        <div class="col-4"><div class="demo-caja">col-4 (33.33%)</div></div>
        <div class="col-4"><div class="demo-caja">col-4 (33.33%)</div></div>
        <div class="col-4"><div class="demo-caja">col-4 (33.33%)</div></div>
    </div>
    
    <div class="grid-row">
        <div class="col-6"><div class="demo-caja">col-6 (50%)</div></div>
        <div class="col-6"><div class="demo-caja">col-6 (50%)</div></div>
    </div>
    
    <div class="grid-row">
        <div class="col-8"><div class="demo-caja">col-8 (66.66%)</div></div>
        <div class="col-4"><div class="demo-caja">col-4 (33.33%)</div></div>
    </div>
</section>
```

---

## 🐱 Paso 9: `flex-direction` - Cambiando la dirección

### Teoría
`flex-direction` cambia la dirección principal del eje.

| Valor | Efecto | Cuándo usarlo |
|-------|--------|---------------|
| `row` (default) | Horizontal, izquierda a derecha | La mayoría de los casos |
| `row-reverse` | Horizontal, derecha a izquierda | Layouts en idiomas RTL |
| `column` | Vertical, arriba a abajo | Barras laterales, menús verticales |
| `column-reverse` | Vertical, abajo a arriba | Casos específicos |

### Ejercicio
Vamos a crear un menú vertical en una barra lateral.

```html
<!-- Añade esto antes del footer -->
<div class="layout-demo">
    <aside class="sidebar">
        <h3>📁 Categorías</h3>
        <div class="menu-vertical">
            <a href="#">😺 Todos los gatitos</a>
            <a href="#">🐱 Naranjos</a>
            <a href="#">🐈‍⬛ Negros</a>
            <a href="#">🤍 Blancos</a>
            <a href="#">🎀 Con moño</a>
        </div>
    </aside>
    
    <div class="contenido-sidebar">
        <h3>Contenido principal</h3>
        <p>Aquí iría el contenido relacionado con la categoría seleccionada.</p>
    </div>
</div>
```

```css
/* ========== PASO 9: FLEX-DIRECTION ========== */
.layout-demo {
    display: flex;
    gap: 30px;
    margin: 40px 0;
}

.sidebar {
    background: #ecf0f1;
    padding: 20px;
    border-radius: 10px;
    width: 250px;
}

.menu-vertical {
    display: flex;
    flex-direction: column;  /* ← Cambiamos a vertical */
    gap: 10px;
    margin-top: 15px;
}

.menu-vertical a {
    background: white;
    padding: 10px;
    text-decoration: none;
    color: #2c3e50;
    border-radius: 5px;
    transition: background 0.3s;
}

.menu-vertical a:hover {
    background: #3498db;
    color: white;
}

.contenido-sidebar {
    flex: 1;
    background: white;
    padding: 20px;
    border-radius: 10px;
}
```

---

## 🐱 Paso 10: `order` - Cambiando el orden visual

### Teoría
La propiedad `order` permite cambiar el **orden visual** de los elementos sin modificar el HTML.

- Valor por defecto: `order: 0`
- Número más pequeño = aparece primero
- Números negativos también funcionan

### Ejercicio
Vamos a crear una sección donde podamos reordenar las tarjetas.

```html
<!-- Sección para demostrar order -->
<section class="order-demo">
    <h2>🔄 Gatitos por orden de adopción</h2>
    <p>Los números indican el orden visual (no el orden en HTML)</p>
    
    <div class="galeria-order">
        <div class="tarjeta-order" style="order: 3">
            <div class="imagen-order">🐱</div>
            <h3>Bigotes <span class="order-badge">order: 3</span></h3>
        </div>
        <div class="tarjeta-order" style="order: 1">
            <div class="imagen-order">🐱</div>
            <h3>Luna <span class="order-badge">order: 1</span></h3>
        </div>
        <div class="tarjeta-order" style="order: 4">
            <div class="imagen-order">🐱</div>
            <h3>Simba <span class="order-badge">order: 4</span></h3>
        </div>
        <div class="tarjeta-order" style="order: 2">
            <div class="imagen-order">🐱</div>
            <h3>Michi <span class="order-badge">order: 2</span></h3>
        </div>
    </div>
</section>
```

```css
/* ========== PASO 10: ORDER ========== */
.order-demo {
    margin: 40px 0;
    padding: 20px;
    background: #fff3e0;
    border-radius: 10px;
}

.galeria-order {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 20px;
}

.tarjeta-order {
    background: white;
    border-radius: 10px;
    padding: 15px;
    width: 200px;
    text-align: center;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.imagen-order {
    font-size: 60px;
    margin-bottom: 10px;
}

.order-badge {
    display: inline-block;
    background: #e74c3c;
    color: white;
    font-size: 10px;
    padding: 2px 8px;
    border-radius: 20px;
    margin-left: 5px;
}
```

**🎯 Desafío:** Cambia los valores de `order` en el HTML y observa cómo se reordenan las tarjetas.

---

## 🐱 Paso 11: Responsive con Flexbox

### Teoría
Flexbox + Media Queries = Layouts responsivos como Bootstrap

### Ejercicio
Vamos a hacer que nuestra galería se adapte a diferentes tamaños de pantalla.

```css
/* ========== PASO 11: RESPONSIVE ========== */

/* Tablets (pantallas menores a 768px) */
@media (max-width: 768px) {
    .galeria {
        justify-content: center;
    }
    
    .tarjeta {
        width: 280px;
    }
    
    .layout-demo {
        flex-direction: column;
    }
    
    .sidebar {
        width: 100%;
    }
    
    .header {
        flex-direction: column;
        gap: 15px;
        text-align: center;
    }
    
    .nav a {
        display: inline-block;
        margin: 0 10px;
    }
}

/* Móviles (pantallas menores a 480px) */
@media (max-width: 480px) {
    .tarjeta {
        width: 100%;
    }
    
    .footer {
        flex-direction: column;
        text-align: center;
    }
    
    .grid-row {
        flex-direction: column;
    }
    
    .col-4, .col-6, .col-8 {
        width: 100%;
    }
}
```

---

## 🐱 Paso 12: Comparativa Bootstrap vs nuestro Flexbox

Para finalizar, añade esta sección que resume todo lo aprendido:

```html
<!-- Sección comparativa -->
<section class="comparativa">
    <h2>📚 Resumen: Lo que aprendimos = Lo que usa Bootstrap</h2>
    
    <table class="tabla-comparativa">
        <thead>
            <tr>
                <th>Concepto Flexbox</th>
                <th>Código que escribimos</th>
                <th>Clase equivalente en Bootstrap</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Activar Flexbox</td>
                <td><code>display: flex</code></td>
                <td><code>.d-flex</code></td>
            </tr>
            <tr>
                <td>Distribución horizontal</td>
                <td><code>justify-content: space-between</code></td>
                <td><code>.justify-content-between</code></td>
            </tr>
            <tr>
                <td>Alineación vertical</td>
                <td><code>align-items: center</code></td>
                <td><code>.align-items-center</code></td>
            </tr>
            <tr>
                <td>Pasar a nueva línea</td>
                <td><code>flex-wrap: wrap</code></td>
                <td><code>.flex-wrap</code></td>
             </tr>
            <tr>
                <td>Columna de 4/12 (33.33%)</td>
                <td><code>flex: 0 0 auto; width: 33.33%</code></td>
                <td><code>.col-4</code></td>
             </tr>
            <tr>
                <td>Dirección vertical</td>
                <td><code>flex-direction: column</code></td>
                <td><code>.flex-column</code></td>
             </tr>
            <tr>
                <td>Cambiar orden</td>
                <td><code>order: 1</code></td>
                <td><code>.order-1</code></td>
             </tr>
        </tbody>
    </table>
    
    <div class="conclusion">
        <h3>🎉 ¡Conclusión importante!</h3>
        <p>Todo lo que hace Bootstrap con su sistema de grillas es <strong>exactamente lo mismo</strong> que acabamos de aprender con Flexbox puro. 
        Bootstrap solo le pone nombres más cortos y clases predefinidas.</p>
        <p><strong>¡Ahora entiendes cómo funciona Bootstrap por dentro!</strong></p>
    </div>
</section>
```

```css
/* Estilos para la tabla comparativa */
.comparativa {
    background: white;
    border-radius: 10px;
    padding: 20px;
    margin: 40px 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.tabla-comparativa {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

.tabla-comparativa th,
.tabla-comparativa td {
    border: 1px solid #ddd;
    padding: 12px;
    text-align: left;
}

.tabla-comparativa th {
    background: #2c3e50;
    color: white;
}

.tabla-comparativa tr:nth-child(even) {
    background: #f9f9f9;
}

.tabla-comparativa code {
    background: #ecf0f1;
    padding: 2px 6px;
    border-radius: 4px;
    font-family: monospace;
}

.conclusion {
    background: #d5f5e3;
    border-left: 4px solid #27ae60;
    padding: 20px;
    border-radius: 8px;
    margin-top: 20px;
}

.conclusion h3 {
    color: #27ae60;
    margin-bottom: 10px;
}
```

---

## 🚀 Versión final del HTML completo

Aquí tienes el `index.html` completo con todas las secciones:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galería de Gatitos - Aprendiendo Flexbox</title>
    <link rel="stylesheet" href="css/estilos.css">
</head>
<body>
    <div class="contenedor-principal">
        <!-- Header -->
        <header class="header">
            <div class="logo">🐱 Gatitos Galería</div>
            <nav class="nav">
                <a href="#">Inicio</a>
                <a href="#">Galería</a>
                <a href="#">Contacto</a>
            </nav>
        </header>

        <!-- Galería principal -->
        <main>
            <h1 class="titulo">🐾 Nuestros Gatitos</h1>
            
            <div class="galeria">
                <div class="tarjeta">
                    <div class="imagen">🐱</div>
                    <h3>Bigotes</h3>
                    <p>Gatito naranja muy juguetón</p>
                    <button>Adoptar</button>
                </div>
                <div class="tarjeta">
                    <div class="imagen">🐱</div>
                    <h3>Luna</h3>
                    <p>Gatita negra cariñosa</p>
                    <button>Adoptar</button>
                </div>
                <div class="tarjeta">
                    <div class="imagen">🐱</div>
                    <h3>Simba</h3>
                    <p>Gatito blanco y gris, muy activo</p>
                    <button>Adoptar</button>
                </div>
                <div class="tarjeta">
                    <div class="imagen">🐱</div>
                    <h3>Michi</h3>
                    <p>Gatito tricolor, muy tranquilo</p>
                    <button>Adoptar</button>
                </div>
                <div class="tarjeta">
                    <div class="imagen">🐱</div>
                    <h3>Copito</h3>
                    <p>Gatito blanco como la nieve</p>
                    <button>Adoptar</button>
                </div>
            </div>
        </main>

        <!-- Demo del sistema de 12 columnas -->
        <section class="grid-demo">
            <h2>📐 Nuestro propio sistema de 12 columnas</h2>
            <p>¡Como Bootstrap, pero hecho por nosotros!</p>
            
            <div class="grid-row">
                <div class="col-4"><div class="demo-caja">col-4 (33.33%)</div></div>
                <div class="col-4"><div class="demo-caja">col-4 (33.33%)</div></div>
                <div class="col-4"><div class="demo-caja">col-4 (33.33%)</div></div>
            </div>
            
            <div class="grid-row">
                <div class="col-6"><div class="demo-caja">col-6 (50%)</div></div>
                <div class="col-6"><div class="demo-caja">col-6 (50%)</div></div>
            </div>
            
            <div class="grid-row">
                <div class="col-8"><div class="demo-caja">col-8 (66.66%)</div></div>
                <div class="col-4"><div class="demo-caja">col-4 (33.33%)</div></div>
            </div>
        </section>

        <!-- Demo de layout con sidebar -->
        <div class="layout-demo">
            <aside class="sidebar">
                <h3>📁 Categorías</h3>
                <div class="menu-vertical">
                    <a href="#">😺 Todos los gatitos</a>
                    <a href="#">🐱 Naranjos</a>
                    <a href="#">🐈‍⬛ Negros</a>
                    <a href="#">🤍 Blancos</a>
                    <a href="#">🎀 Con moño</a>
                </div>
            </aside>
            <div class="contenido-sidebar">
                <h3>Contenido principal</h3>
                <p>Aquí iría el contenido relacionado con la categoría seleccionada.</p>
            </div>
        </div>

        <!-- Demo de order -->
        <section class="order-demo">
            <h2>🔄 Gatitos por orden de adopción</h2>
            <p>Los números indican el orden visual (no el orden en HTML)</p>
            <div class="galeria-order">
                <div class="tarjeta-order" style="order: 3">
                    <div class="imagen-order">🐱</div>
                    <h3>Bigotes <span class="order-badge">order: 3</span></h3>
                </div>
                <div class="tarjeta-order" style="order: 1">
                    <div class="imagen-order">🐱</div>
                    <h3>Luna <span class="order-badge">order: 1</span></h3>
                </div>
                <div class="tarjeta-order" style="order: 4">
                    <div class="imagen-order">🐱</div>
                    <h3>Simba <span class="order-badge">order: 4</span></h3>
                </div>
                <div class="tarjeta-order" style="order: 2">
                    <div class="imagen-order">🐱</div>
                    <h3>Michi <span class="order-badge">order: 2</span></h3>
                </div>
            </div>
        </section>

        <!-- Tabla comparativa -->
        <section class="comparativa">
            <h2>📚 Resumen: Lo que aprendimos = Lo que usa Bootstrap</h2>
            <table class="tabla-comparativa">
                <thead>
                    <tr>
                        <th>Concepto Flexbox</th>
                        <th>Código que escribimos</th>
                        <th>Clase equivalente en Bootstrap</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>Activar Flexbox</td><td><code>display: flex</code></td><td><code>.d-flex</code></td></tr>
                    <tr><td>Distribución horizontal</td><td><code>justify-content: space-between</code></td><td><code>.justify-content-between</code></td></tr>
                    <tr><td>Alineación vertical</td><td><code>align-items: center</code></td><td><code>.align-items-center</code></td></tr>
                    <tr><td>Pasar a nueva línea</td><td><code>flex-wrap: wrap</code></td><td><code>.flex-wrap</code></td></tr>
                    <tr><td>Columna de 4/12 (33.33%)</td><td><code>flex: 0 0 auto; width: 33.33%</code></td><td><code>.col-4</code></td></tr>
                    <tr><td>Dirección vertical</td><td><code>flex-direction: column</code></td><td><code>.flex-column</code></td></tr>
                    <tr><td>Cambiar orden</td><td><code>order: 1</code></td><td><code>.order-1</code></td></tr>
                </tbody>
            </table>
            
            <div class="conclusion">
                <h3>🎉 ¡Conclusión importante!</h3>
                <p>Todo lo que hace Bootstrap con su sistema de grillas es <strong>exactamente lo mismo</strong> que acabamos de aprender con Flexbox puro. Bootstrap solo le pone nombres más cortos y clases predefinidas.</p>
                <p><strong>¡Ahora entiendes cómo funciona Bootstrap por dentro!</strong></p>
            </div>
        </section>

        <!-- Footer -->
        <footer class="footer">
            <div class="footer-col">
                <h4>🐱 Sobre nosotros</h4>
                <p>Somos una fundación dedicada a encontrar hogar para gatitos.</p>
            </div>
            <div class="footer-col">
                <h4>📞 Contacto</h4>
                <p>Email: hola@gatitos.com<br>Tel: +56 9 1234 5678</p>
            </div>
            <div class="footer-col">
                <h4>❤️ Síguenos</h4>
                <p>Instagram<br>Facebook<br>TikTok</p>
            </div>
        </footer>
    </div>
</body>
</html>
```

---

## 📝 Checklist de aprendizaje para el alumno

Marca cada concepto cuando lo hayas entendido y practicado:

### Fundamentos básicos
- [ ] `display: flex` activa el contenedor flexible
- [ ] Los hijos directos se convierten en ítems flex
- [ ] `flex-direction: row` es el valor por defecto (horizontal)

### Distribución y alineación
- [ ] `justify-content` controla la alineación horizontal
- [ ] `align-items` controla la alineación vertical en una fila
- [ ] `align-content` controla la alineación de múltiples filas

### Comportamiento responsivo
- [ ] `flex-wrap: wrap` permite que los elementos pasen a nueva línea
- [ ] `gap` crea espacio entre elementos

### Crecimiento y tamaño
- [ ] `flex: 1` permite que un elemento crezca
- [ ] `flex: 0 0 auto` + `width` crea columnas fijas (como Bootstrap)

### Avanzado
- [ ] `flex-direction: column` para layouts verticales
- [ ] `order` para cambiar el orden visual
- [ ] Media queries + Flexbox para responsive

### Conexión con Bootstrap
- [ ] Identifico qué clase de Bootstrap corresponde a cada propiedad Flexbox
- [ ] Puedo explicar por qué `.col-4` ocupa 33.33%
- [ ] Entiendo que Bootstrap NO es magia, es Flexbox con nombres bonitos

---

## 🎯 Ejercicios propuestos para practicar en casa

### Ejercicio 1: Modifica la galería
Cambia el número de columnas para que siempre muestren:
- 4 columnas en escritorio
- 2 columnas en tablet
- 1 columna en móvil

### Ejercicio 2: Crea un nuevo componente
Diseña una "barra de filtros" horizontal con:
- Un título a la izquierda
- 3 botones de filtro centrados
- Un contador de resultados a la derecha

### Ejercicio 3: Construye una navbar responsiva
Crea una barra de navegación que:
- En escritorio: logo izquierda, links derecha
- En móvil: logo arriba, links abajo centrados

### Ejercicio 4: El desafío final
Sin usar Bootstrap, recrea exactamente este layout que normalmente harías con Bootstrap:
```
┌────────────────────────────────────────┐
│  Header con logo y 3 links             │
├────────┬───────────────────────────────┤
│        │                               │
│ Menu   │   Contenido principal         │
│ lateral│   (grid de tarjetas 3 columnas)│
│        │                               │
├────────┴───────────────────────────────┤
│  Footer con 3 columnas                 │
└────────────────────────────────────────┘
```

---

## 🏁 Conclusión final del proyecto

**¡Felicidades!** Has construido una galería de gatitos que te ha enseñado:

1. **Todos los conceptos clave de Flexbox** que necesitas saber
2. **Cómo Bootstrap implementa su sistema de grillas** por debajo
3. **A crear layouts responsivos** sin dependencias externas

**Lo más importante:** Ahora cuando veas `<div class="row">` y `<div class="col-4">` en Bootstrap, sabrás exactamente qué está pasando: un contenedor flex con hijos que tienen `flex: 0 0 auto` y `width: 33.33%`.

**No eres solo un usuario de Bootstrap. Eres alguien que entiende cómo funciona.** 🚀