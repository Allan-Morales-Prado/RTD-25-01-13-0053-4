# Guía Ejemplo 3: Grid avanzado con áreas nombradas

## Vista previa del concepto
Este ejemplo construye un **dashboard completo** usando `grid-template-areas`. Es la técnica más legible para layouts complejos porque el CSS "dibuja" el layout con palabras.

## Estructura completa del código

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Grid CSS - Ejemplo 3: Layout con áreas nombradas</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
            background: #0f172a;
            min-height: 100vh;
            padding: 1.5rem;
        }

        /* ========== EL LAYOUT GRID CON ÁREAS NOMBRADAS ========== */
        .dashboard {
            display: grid;
            grid-template-areas:
                "header header header"
                "sidebar main main"
                "sidebar main main"
                "footer footer footer";
            grid-template-columns: 260px 1fr 1fr;
            grid-template-rows: auto 1fr auto 60px;
            gap: 1rem;
            max-width: 1400px;
            margin: 0 auto;
            min-height: 95vh;
        }

        /* ========== ASIGNACIÓN DE CADA ÁREA A SU ELEMENTO ========== */
        .header {
            grid-area: header;
            background: linear-gradient(135deg, #1e293b, #0f172a);
            color: white;
            padding: 1.2rem 2rem;
            border-radius: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        .sidebar {
            grid-area: sidebar;
            background: #1e293b;
            border-radius: 16px;
            padding: 1.5rem;
            color: #cbd5e1;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }

        .main {
            grid-area: main;
            background: #0f172a;
            border-radius: 16px;
            padding: 1.5rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1rem;
            align-content: start;
        }

        .footer {
            grid-area: footer;
            background: #1e293b;
            color: #94a3b8;
            padding: 1rem 2rem;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        /* ========== ESTILOS INTERNOS DE COMPONENTES ========== */
        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            background: #3b82f6;
            padding: 0.3rem 1rem;
            border-radius: 40px;
        }

        .nav-links {
            display: flex;
            gap: 1.5rem;
        }

        .nav-links a {
            color: white;
            text-decoration: none;
        }

        .sidebar-item {
            padding: 0.75rem 1rem;
            margin-bottom: 0.5rem;
            background: #334155;
            border-radius: 12px;
            cursor: pointer;
            transition: background 0.2s;
        }

        .sidebar-item:hover {
            background: #3b82f6;
            color: white;
        }

        .widget {
            background: #1e293b;
            border-radius: 16px;
            padding: 1.2rem;
            color: white;
            border-left: 4px solid #3b82f6;
        }

        .widget h3 {
            margin-bottom: 0.75rem;
            font-size: 1.1rem;
        }

        .stat-number {
            font-size: 2rem;
            font-weight: bold;
            color: #3b82f6;
        }

        hr {
            margin: 1rem 0;
            border-color: #334155;
        }

        /* ========== RESPONSIVE ========== */
        @media (max-width: 768px) {
            .dashboard {
                grid-template-areas:
                    "header"
                    "sidebar"
                    "main"
                    "footer";
                grid-template-columns: 1fr;
                grid-template-rows: auto auto 1fr auto;
            }
        }
    </style>
</head>
<body>
    <div class="dashboard">
        <header class="header">
            <div class="logo">✨ GridCSS</div>
            <div class="nav-links">
                <a href="#">Inicio</a>
                <a href="#">Dashboard</a>
                <a href="#">Analytics</a>
                <a href="#">Configuración</a>
            </div>
            <div>👤 Admin</div>
        </header>

        <aside class="sidebar">
            <h3 style="color:white; margin-bottom:1rem;">📂 Menú</h3>
            <div class="sidebar-item">📊 Estadísticas</div>
            <div class="sidebar-item">📦 Productos</div>
            <div class="sidebar-item">👥 Usuarios</div>
            <div class="sidebar-item">⚙️ Ajustes</div>
            <hr>
            <div class="sidebar-item">🚪 Cerrar sesión</div>
        </aside>

        <main class="main">
            <div class="widget">
                <h3>📈 Ventas Totales</h3>
                <div class="stat-number">$12,450</div>
                <p>↑ 23% vs mes anterior</p>
            </div>
            <div class="widget">
                <h3>👥 Usuarios activos</h3>
                <div class="stat-number">1,284</div>
                <p>+120 nuevos esta semana</p>
            </div>
            <div class="widget">
                <h3>⭐ Calificación</h3>
                <div class="stat-number">4.8/5</div>
                <p>Basado en 342 reseñas</p>
            </div>
            <div class="widget">
                <h3>🕒 Tiempo promedio</h3>
                <div class="stat-number">8.4 min</div>
                <p>Duración de sesión</p>
            </div>
            <div class="widget">
                <h3>📱 Conversión</h3>
                <div class="stat-number">3.2%</div>
                <p>Objetivo: 4%</p>
            </div>
        </main>

        <footer class="footer">
            <span>© 2025 Grid CSS - Todos los derechos reservados</span>
            <span>🚀 Layout con grid-template-areas</span>
        </footer>
    </div>
</body>
</html>
```

## Explicación paso a paso del CSS (enfoque en áreas nombradas)

### Bloque 1: ⭐ **CONFIGURACIÓN DEL LAYOUT CON ÁREAS** ⭐

```css
.dashboard {
    display: grid;
    grid-template-areas:
        "header header header"
        "sidebar main main"
        "sidebar main main"
        "footer footer footer";
    grid-template-columns: 260px 1fr 1fr;
    grid-template-rows: auto 1fr auto 60px;
    gap: 1rem;
    max-width: 1400px;
    margin: 0 auto;
    min-height: 95vh;
}
```

#### Desglose de `grid-template-areas`:
Este es el "dibujo" del layout. Cada texto entre comillas es una **fila**, y cada palabra dentro es una **celda**.

```
Fila 1: "header header header"   → El header ocupa las 3 columnas
Fila 2: "sidebar main main"      → Sidebar col1, Main col2 y col3
Fila 3: "sidebar main main"      → Igual que fila 2 (main ocupa 2 columnas)
Fila 4: "footer footer footer"   → Footer ocupa las 3 columnas
```

**Visualización en matriz (3 columnas × 4 filas):**

| Fila | Columna 1 | Columna 2 | Columna 3 |
|------|-----------|-----------|-----------|
| 1 | header | header | header |
| 2 | sidebar | main | main |
| 3 | sidebar | main | main |
| 4 | footer | footer | footer |

#### Desglose de `grid-template-columns: 260px 1fr 1fr`:

| Valor | Significado |
|-------|-------------|
| `260px` | Primera columna (donde va `sidebar`) mide 260px fijos |
| `1fr` | Segunda columna (parte izquierda de `main`) ocupa 1 fracción |
| `1fr` | Tercera columna (parte derecha de `main`) ocupa 1 fracción |

**Efecto:** El sidebar tiene ancho fijo, y el área principal se divide en DOS columnas iguales (donde irán los widgets).

#### Desglose de `grid-template-rows: auto 1fr auto 60px`:

| Valor | Significado |
|-------|-------------|
| `auto` | Primera fila (`header`) se ajusta a su contenido automáticamente |
| `1fr` | Segunda fila (primera parte de `main`) ocupa espacio flexible |
| `auto` | Tercera fila (segunda parte de `main`) también flexible (junto con la anterior forma el main completo) |
| `60px` | Cuarta fila (`footer`) mide exactamente 60px |

---

### Bloque 2: Asignación de áreas a elementos HTML

```css
.header {
    grid-area: header;
}

.sidebar {
    grid-area: sidebar;
}

.main {
    grid-area: main;
}

.footer {
    grid-area: footer;
}
```

**Relación con el HTML:**
Cada elemento HTML (`.header`, `.sidebar`, `.main`, `.footer`) recibe la propiedad `grid-area` con el nombre que coincide con el "dibujo" de `grid-template-areas`.

| CSS | HTML | Ubicación en el grid |
|-----|------|---------------------|
| `.header { grid-area: header; }` | `<header class="header">` | Toda la fila superior |
| `.sidebar { grid-area: sidebar; }` | `<aside class="sidebar">` | Columna izquierda, 2 filas de alto |
| `.main { grid-area: main; }` | `<main class="main">` | 2 columnas × 2 filas en la zona derecha |
| `.footer { grid-area: footer; }` | `<footer class="footer">` | Toda la fila inferior |

---

### Bloque 3: Header con Flexbox interno

```css
.header {
    grid-area: header;
    background: linear-gradient(135deg, #1e293b, #0f172a);
    color: white;
    padding: 1.2rem 2rem;
    border-radius: 16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.2);
}
```

| Propiedad | ¿Qué hace? |
|-----------|-------------|
| `display: flex` | El header usa Flexbox para alinear sus hijos HORIZONTALMENTE |
| `justify-content: space-between` | Distribuye el espacio: logo a la izquierda, links al centro, avatar a la derecha |
| `align-items: center` | Centra verticalmente todos los elementos del header |

**Nota importante:** El header tiene `display: flex` porque su interior necesita organización horizontal. El hecho de que esté dentro de un **grid** no impide que use **flexbox** internamente. De hecho, es una práctica excelente.

---

### Bloque 4: Sidebar con elementos de menú

```css
.sidebar {
    grid-area: sidebar;
    background: #1e293b;
    border-radius: 16px;
    padding: 1.5rem;
    color: #cbd5e1;
    box-shadow: 0 4px 6px rgba(0,0,0,0.2);
}

.sidebar-item {
    padding: 0.75rem 1rem;
    margin-bottom: 0.5rem;
    background: #334155;
    border-radius: 12px;
    cursor: pointer;
    transition: background 0.2s;
}
```

**Relación con el HTML:** 
- El `<aside class="sidebar">` es el contenedor del menú
- Cada `<div class="sidebar-item">` es una opción del menú

---

### Bloque 5: Main con GRID ANIDADO (¡Grid dentro de Grid!)

```css
.main {
    grid-area: main;
    background: #0f172a;
    border-radius: 16px;
    padding: 1.5rem;
    display: grid;                    /* ← ¡OTRO GRID! */
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1rem;
    align-content: start;
}
```

**Concepto importante: Grid anidado**
El área `.main` es un **ítem del grid exterior** (el dashboard), pero también es un **contenedor grid para los widgets**.

| Propiedad | ¿Qué hace en este contexto? |
|-----------|----------------------------|
| `display: grid` | Convierte el `<main>` en un contenedor grid |
| `grid-template-columns: repeat(auto-fit, minmax(240px, 1fr))` | Los widgets internos se distribuyen automáticamente (misma técnica del Ejemplo 2) |
| `gap: 1rem` | Espacio entre los widgets |
| `align-content: start` | Los widgets se alinean al inicio verticalmente (no se estiran) |

**Visualización de grids anidados:**
```
Grid exterior (.dashboard)
├── header
├── sidebar
├── main (este es un Grid interior)
│   ├── widget 1
│   ├── widget 2
│   ├── widget 3
│   └── widget 4
└── footer
```

---

### Bloque 6: Widgets

```css
.widget {
    background: #1e293b;
    border-radius: 16px;
    padding: 1.2rem;
    color: white;
    border-left: 4px solid #3b82f6;
}

.stat-number {
    font-size: 2rem;
    font-weight: bold;
    color: #3b82f6;
}
```

| Propiedad de `.widget` | ¿Qué hace? |
|------------------------|-------------|
| `border-left: 4px solid #3b82f6` | Añade una línea azul vertical en el borde izquierdo (detalle de diseño moderno) |

**Relación con el HTML:** Cada `<div class="widget">` contiene un título, un número grande y una descripción.

---

### Bloque 7: Media query para móvil

```css
@media (max-width: 768px) {
    .dashboard {
        grid-template-areas:
            "header"
            "sidebar"
            "main"
            "footer";
        grid-template-columns: 1fr;
        grid-template-rows: auto auto 1fr auto;
    }
}
```

**¿Qué cambia en móvil?**

| Antes (escritorio) | Después (móvil ≤ 768px) |
|--------------------|-------------------------|
| 3 columnas | 1 columna |
| `"header header header"` | `"header"` |
| `"sidebar main main"` | `"sidebar"` |
| `"sidebar main main"` | `"main"` |
| `"footer footer footer"` | `"footer"` |

**Efecto visual:** Los elementos se apilan verticalmente en móvil: Header → Sidebar → Main → Footer

---

## Mapa visual completo: CSS ↔ HTML (Ejemplo 3)

| Elemento HTML | Clase CSS | Rol en el grid | Propiedades clave |
|---------------|-----------|----------------|-------------------|
| `<div class="dashboard">` | `.dashboard` | Contenedor grid principal | `grid-template-areas`, `grid-template-columns`, `grid-template-rows` |
| `<header class="header">` | `.header` | Área `header` | `grid-area: header`, Flexbox interno |
| `<aside class="sidebar">` | `.sidebar` | Área `sidebar` | `grid-area: sidebar` |
| `<main class="main">` | `.main` | Área `main` | `grid-area: main`, **Grid anidado** |
| `<footer class="footer">` | `.footer` | Área `footer` | `grid-area: footer`, Flexbox interno |
| `<div class="widget">` | `.widget` | Elemento del grid anidado | Dentro del `main`, se organiza con `auto-fit` |

---

## Resumen de aprendizajes por ejemplo

| Ejemplo | Concepto principal | Lo más importante que aprende el estudiante |
|---------|--------------------|---------------------------------------------|
| **1** | Columnas fijas + media queries | `grid-template-columns` con valores fijos, `justify-content: center`, responsividad manual |
| **2** | Grid totalmente responsivo | `repeat(auto-fit, minmax())` → un solo grid que se adapta solo, SIN media queries |
| **3** | Áreas nombradas + Grid anidado | `grid-template-areas` para layouts complejos, y un grid puede contener otro grid |