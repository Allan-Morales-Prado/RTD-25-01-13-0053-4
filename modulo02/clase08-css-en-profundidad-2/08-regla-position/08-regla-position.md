# Guía sobre propiedad `position` en CSS

## ¿Qué es `position`?

La propiedad `position` en CSS te permite controlar **cómo y dónde se ubica un elemento** en la página. Piensa en ella como una herramienta que puede "sacar" elementos de su lugar natural o "pegarlos" en una posición específica.

### Concepto fundamental: El flujo normal

Cuando no usas `position` (o usas `position: static`), los elementos se colocan siguiendo el **flujo normal** del documento:

- Los elementos `block` se apilan verticalmente (uno debajo del otro)
- Los elementos `inline` e `inline-block` fluyen horizontalmente como texto

La propiedad `position` te permite **alterar** este flujo.

---

## Los 5 valores de `position`

| Valor | ¿Sigue el flujo normal? | ¿Se mueve desde su lugar? | ¿Referencia para moverlo? |
|-------|------------------------|---------------------------|---------------------------|
| `static` | ✅ Sí | ❌ No | No aplica |
| `relative` | ✅ Sí (deja su hueco) | ✅ Sí | Su posición original |
| `absolute` | ❌ No (sale del flujo) | ✅ Sí | El ancestro posicionado más cercano |
| `fixed` | ❌ No (sale del flujo) | ✅ Sí | La ventana del navegador (viewport) |
| `sticky` | ✅ Sí (híbrido) | ✅ Sí (condicional) | Su contenedor de desplazamiento |

### Propiedades de desplazamiento

Para mover un elemento posicionado (todos excepto `static`), usamos:

```css
.elemento {
    position: relative;  /* o absolute, fixed, sticky */
    top: 20px;      /* Desde el borde superior */
    right: 30px;    /* Desde el borde derecho */
    bottom: 40px;   /* Desde el borde inferior */
    left: 50px;     /* Desde el borde izquierdo */
}
```

---

## Ejemplos prácticos paso a paso

### Ejemplo 1: `position: static` (el valor por defecto)

**Concepto:** El elemento se coloca en el flujo normal. No se puede mover con `top`, `left`, etc.

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .caja {
            width: 200px;
            height: 100px;
            background: lightblue;
            margin: 10px;
        }
        
        .static {
            position: static;  /* Este es el valor por defecto */
            /* top: 20px;  <- NO FUNCIONA con static */
        }
        
        .normal {
            background: lightgreen;
        }
    </style>
</head>
<body>
    <div class="caja normal">Caja normal (block)</div>
    <div class="caja static">Caja con position: static</div>
    <div class="caja normal">Otra caja normal</div>
    
    <p>💡 Las tres cajas se apilan verticalmente igual. 
    'static' no cambia nada.</p>
</body>
</html>
```

**Resultado visual:**
```
┌─────────────────────┐
│ Caja normal (block)  │
├─────────────────────┤
│ Caja con static      │
├─────────────────────┤
│ Otra caja normal     │
└─────────────────────┘
```

---

### Ejemplo 2: `position: relative`

**Concepto:** El elemento se desplaza RELATIVO a su posición original. **Su espacio original se respeta** (otros elementos no se mueven).

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial;
            padding: 20px;
        }
        
        .contenedor {
            background: #f0f0f0;
            padding: 10px;
            border: 2px solid #ccc;
        }
        
        .caja {
            width: 200px;
            height: 80px;
            background: #3498db;
            color: white;
            text-align: center;
            line-height: 80px;
            margin: 10px;
        }
        
        /* La caja relativa se mueve PERO deja su hueco */
        .relativa {
            position: relative;
            top: 30px;      /* Baja 30px desde su posición original */
            left: 40px;     /* Se mueve 40px a la derecha */
            background: #e74c3c;
        }
        
        .info {
            background: #ecf0f1;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>📐 position: relative</h1>
    
    <div class="contenedor">
        <div class="caja">Caja 1 (normal)</div>
        <div class="caja relativa">Caja 2: relative<br>top:30px; left:40px</div>
        <div class="caja">Caja 3 (normal)</div>
    </div>
    
    <div class="info">
        <strong>🔍 Observa:</strong>
        <ul>
            <li>La caja roja se movió 30px hacia ABAJO y 40px hacia la DERECHA</li>
            <li>✅ El espacio DONDE DEBERÍA ESTAR la caja roja permanece VACÍO (se respeta)</li>
            <li>✅ Las otras cajas NO se movieron (siguen donde estaban)</li>
            <li>⚠️ La caja roja se superpone a la caja 3 porque se movió sobre ella</li>
        </ul>
    </div>
</body>
</html>
```

**Explicación clave:** `relative` mueve el elemento visualmente, pero otros elementos actúan como si siguiera en su lugar original.

---

### Ejemplo 3: `position: absolute`

**Concepto:** El elemento se SACA COMPLETAMENTE del flujo normal. Los demás elementos lo IGNORAN. Se posiciona relativo a su **ancestro posicionado más cercano** (cualquier elemento con `position` diferente a `static`).

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .contenedor-relative {
            position: relative;  /* ← ANCESTRO POSICIONADO */
            background: #e8e8e8;
            padding: 30px;
            margin: 20px;
            min-height: 300px;
            border: 2px dashed #999;
        }
        
        .caja {
            width: 150px;
            height: 80px;
            background: #2ecc71;
            margin: 10px;
            text-align: center;
            line-height: 80px;
            display: inline-block;
        }
        
        .absoluta {
            position: absolute;
            top: 20px;
            right: 20px;
            background: #e67e22;
            width: 120px;
            height: 60px;
            line-height: 60px;
        }
        
        .absoluta-2 {
            position: absolute;
            bottom: 10px;
            left: 10px;
            background: #9b59b6;
            width: 100px;
            height: 40px;
            line-height: 40px;
            font-size: 12px;
        }
        
        .destacado {
            background: #f1c40f;
            border: 2px solid #000;
        }
    </style>
</head>
<body>
    <h1>🎯 position: absolute</h1>
    
    <div class="contenedor-relative">
        <p><strong>Este contenedor tiene position: relative</strong> (ancestro posicionado)</p>
        
        <div class="caja">Caja A</div>
        <div class="caja">Caja B</div>
        <div class="caja">Caja C</div>
        
        <div class="absoluta">
            ¡Soy ABSOLUTA!<br>
            top:20px; right:20px
        </div>
        
        <div class="absoluta-2">
            ¡Otra absoluta!<br>
            bottom:10px; left:10px
        </div>
    </div>
    
    <div class="info" style="background:#ecf0f1; padding:15px; margin-top:20px;">
        <strong>🔍 Observaciones importantes:</strong>
        <ul>
            <li>❌ Las cajas A, B, C IGNORAN por completo a las cajas absolutas (como si no existieran)</li>
            <li>✅ Las cajas absolutas se posicionan respecto al contenedor GRIS (que tiene position: relative)</li>
            <li>✅ Si no hubiera un ancestro posicionado, se posicionarían respecto al &lt;body&gt;</li>
            <li>💡 Las cajas absolutas se superponen sobre los demás elementos</li>
        </ul>
    </div>
</body>
</html>
```

**Visualización del ejemplo:**
```
┌─────────────────────────────────────────────┐
│ Contenedor (position: relative)          ┌──┼────┐
│ ┌─────┐ ┌─────┐ ┌─────┐                   │ABS│ │
│ │ A   │ │ B   │ │ C   │                   │(1)│ │
│ └─────┘ └─────┘ └─────┘                   └──┼────┘
│                                              │
│ ┌────┐                                       │
│ │ABS │ (2)                                   │
│ └────┘                                       │
└─────────────────────────────────────────────┘
```

---

### Ejemplo 4: `position: fixed`

**Concepto:** Similar a `absolute`, pero se posiciona respecto a la **ventana del navegador (viewport)**. Al hacer scroll, el elemento **permanece fijo** en su lugar.

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: Arial;
        }
        
        /* Elemento fixed: siempre visible al hacer scroll */
        .boton-flotante {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #e74c3c;
            color: white;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            text-align: center;
            line-height: 60px;
            font-size: 30px;
            cursor: pointer;
            box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            z-index: 100;
        }
        
        .header-fixed {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: #2c3e50;
            color: white;
            padding: 15px;
            text-align: center;
            z-index: 99;
        }
        
        /* Contenido normal con padding para que no quede tapado por el header fixed */
        .contenido {
            margin-top: 80px;   /* Para que el contenido no quede debajo del header fijo */
            padding: 20px;
        }
        
        .caja {
            background: #3498db;
            color: white;
            padding: 40px;
            margin: 10px 0;
            text-align: center;
        }
        
        .advertencia {
            background: #f39c12;
            padding: 15px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <!-- Header que se queda fijo arriba -->
    <div class="header-fixed">
        📌 ESTE HEADER ES FIJO - Siempre visible al hacer scroll
    </div>
    
    <!-- Botón flotante fijo -->
    <div class="boton-flotante">
        ↑
    </div>
    
    <div class="contenido">
        <h1>Contenido de la página</h1>
        
        <div class="caja">Sección 1</div>
        <div class="caja">Sección 2</div>
        <div class="caja">Sección 3</div>
        <div class="caja">Sección 4</div>
        <div class="caja">Sección 5</div>
        
        <div class="advertencia">
            <strong>🧪 PRUEBA:</strong> Haz scroll hacia abajo.
            <ul>
                <li>✅ El header azul oscuro SIEMPRE permanece arriba</li>
                <li>✅ El botón rojo circular SIEMPRE permanece abajo a la derecha</li>
                <li>✅ El contenido normal se desplaza por debajo</li>
                <li>💡 Los elementos fixed IGNORAN el scroll del usuario</li>
            </ul>
        </div>
        
        <div class="caja">Sección 6</div>
        <div class="caja">Sección 7</div>
        <div class="caja">Sección 8</div>
    </div>
</body>
</html>
```

**Usos típicos de `fixed`:**
- Barras de navegación fijas (sticky headers)
- Botones "volver arriba"
- Menús laterales fijos
- Banners de cookies o notificaciones

---

### Ejemplo 5: `position: sticky`

**Concepto:** Comportamiento **híbrido**. Se comporta como `relative` normalmente, pero cuando el scroll alcanza cierto punto, se "pega" y se comporta como `fixed` dentro de su contenedor.

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body {
            font-family: Arial;
            margin: 0;
            padding: 20px;
        }
        
        .contenedor {
            max-width: 600px;
            margin: 0 auto;
        }
        
        /* Elemento sticky - se pega al hacer scroll */
        .encabezado-seccion {
            position: sticky;
            top: 10px;          /* Se pega cuando llega a 10px del borde superior */
            background: #3498db;
            color: white;
            padding: 15px;
            margin: 20px 0;
            border-radius: 8px;
            font-weight: bold;
        }
        
        /* Elemento sticky diferente */
        .sidebar-sticky {
            position: sticky;
            top: 20px;
            background: #e74c3c;
            color: white;
            padding: 20px;
            width: 200px;
            float: right;
            margin-left: 20px;
            border-radius: 8px;
        }
        
        .contenido-largo {
            background: #ecf0f1;
            padding: 15px;
            margin: 10px 0;
            line-height: 1.6;
        }
        
        .card {
            background: white;
            border: 1px solid #ddd;
            padding: 15px;
            margin: 15px 0;
            border-radius: 8px;
        }
        
        hr {
            margin: 30px 0;
        }
    </style>
</head>
<body>
    <div class="contenedor">
        <h1>📌 position: sticky</h1>
        
        <!-- Sidebar sticky (flota a la derecha) -->
        <div class="sidebar-sticky">
            🟢 ¡SOY STICKY!<br>
            Me pego cuando haces scroll<br>
            📍 top: 20px
        </div>
        
        <p>El elemento <strong>sticky</strong> se comporta como <strong>relative</strong> normalmente, pero cuando el scroll alcanza su posición, se "pega" y se comporta como <strong>fixed</strong> DENTRO de su contenedor.</p>
        
        <!-- Primer sticky header -->
        <div class="encabezado-seccion">
            📌 SECCIÓN 1 - Este encabezado se pegará al hacer scroll
        </div>
        
        <div class="contenido-largo">
            <p>Contenido extenso de la sección 1. Haz scroll para ver el efecto sticky.</p>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.</p>
            <p>Cuando este encabezado llegue al borde superior (top:10px), se pegará hasta que termine su sección contenedora.</p>
        </div>
        
        <!-- Segundo sticky header -->
        <div class="encabezado-seccion">
            📌 SECCIÓN 2 - Otro encabezado sticky
        </div>
        
        <div class="contenido-largo">
            <p>Más contenido aquí. Observa cómo el encabezado anterior desaparece cuando sale de su contenedor y este nuevo encabezado toma su lugar pegajoso.</p>
            <p>Continua scroleando para ver el comportamiento del sidebar sticky a la derecha.</p>
        </div>
        
        <!-- Tercer sticky header -->
        <div class="encabezado-seccion">
            📌 SECCIÓN 3 - Último sticky
        </div>
        
        <div class="contenido-largo">
            <p>Y más contenido para terminar. Los elementos sticky son ideales para:</p>
            <ul>
                <li>✅ Encabezados de sección en listas largas</li>
                <li>✅ Tablas con cabeceras fijas</li>
                <li>✅ Barras laterales que acompañan al scroll</li>
                <li>✅ Menús contextuales</li>
            </ul>
        </div>
        
        <hr>
        
        <div class="card">
            <strong>🔍 Diferencia clave sticky vs fixed:</strong>
            <ul>
                <li><strong>fixed:</strong> Se queda fijo SIEMPRE, en toda la página</li>
                <li><strong>sticky:</strong> Se queda fijo SOLO dentro de su contenedor, y luego "sale" cuando el contenedor termina</li>
            </ul>
        </div>
    </div>
</body>
</html>
```

---

## Guía teórica completa sobre `position`

### Tabla comparativa definitiva

| Característica | static | relative | absolute | fixed | sticky |
|----------------|--------|----------|----------|-------|--------|
| **Flujo normal** | ✅ Sí | ✅ Sí (deja hueco) | ❌ No | ❌ No | ✅ Sí (hasta que se pega) |
| **Otros elementos lo ignoran** | ❌ No | ❌ No | ✅ Sí | ✅ Sí | ❌ No |
| **Se puede mover con top/left** | ❌ No | ✅ Sí | ✅ Sí | ✅ Sí | ✅ Sí |
| **Referencia para movimiento** | N/A | Su posición original | Ancestro posicionado | Viewport | Contenedor de scroll |
| **Afecta al scroll** | ❌ No | ❌ No | ❌ No | ❌ No (permanece) | ✅ Sí (se pega) |
| **Uso típico** | Valor por defecto | Ajustes finos, crear contexto para absolute | Tooltips, modales, superposiciones | Headers fijos, botones flotantes | Encabezados de sección |

---

### ¿Qué es un "ancestro posicionado"?

Cuando usas `position: absolute`, el elemento se posiciona respecto al **primer ancestro** (elemento padre, abuelo, etc.) que tenga una `position` diferente a `static`.

```html
<div style="position: relative;">  ← Este es el ancestro posicionado
    <div>
        <div style="position: absolute; top: 0; left: 0;">
            ← Este absolute se posiciona respecto al div con relative
        </div>
    </div>
</div>
```

**Regla práctica:** Si usas `absolute`, asegúrate de que su contenedor tenga `position: relative` (o `absolute`, `fixed`, `sticky`) para que se posicione correctamente.

---

### La propiedad `z-index`: control de profundidad

Cuando los elementos se superponen (como con `relative`, `absolute`, `fixed`, `sticky`), `z-index` determina **quién está encima de quién**.

```css
.elemento-superior {
    position: absolute;
    z-index: 10;  /* Número mayor = más arriba */
}

.elemento-inferior {
    position: absolute;
    z-index: 5;   /* Número menor = más abajo */
}
```

**Importante:** `z-index` SOLO funciona en elementos posicionados (cualquier `position` excepto `static`).

---

### Errores comunes y cómo evitarlos

#### ❌ Error 1: Usar `top`/`left` en elementos `static`

```css
/* ❌ Esto NO funciona */
.elemento {
    position: static;
    top: 20px;   /* IGNORADO */
}
```

```css
/* ✅ Correcto */
.elemento {
    position: relative;  /* o absolute, fixed, sticky */
    top: 20px;
}
```

#### ❌ Error 2: Olvidar el ancestro posicionado para `absolute`

```html
<!-- ❌ El absolute se posicionará respecto al <body> (probablemente no deseado) -->
<div>
    <div style="position: absolute; top: 0;">
        Menu flotante
    </div>
</div>
```

```html
<!-- ✅ Correcto: el contenedor tiene position: relative -->
<div style="position: relative;">
    <div style="position: absolute; top: 0;">
        Menu flotante
    </div>
</div>
```

#### ❌ Error 3: Usar `sticky` sin definir `top`, `bottom`, etc.

```css
/* ❌ No se pegará porque no sabe DÓNDE pegarse */
.elemento {
    position: sticky;
    /* falta top, bottom, left o right */
}
```

```css
/* ✅ Correcto */
.elemento {
    position: sticky;
    top: 0;   /* Se pega cuando llega al borde superior */
}
```

#### ❌ Error 4: Creer que `z-index` funciona sin `position`

```css
/* ❌ NO funciona (elemento sin position) */
.elemento {
    z-index: 100;
}
```

```css
/* ✅ Correcto */
.elemento {
    position: relative;
    z-index: 100;
}
```

---

### Cuándo usar cada valor (guía práctica)

| Si necesitas... | Usa... |
|-----------------|--------|
| El comportamiento normal por defecto | `static` |
| Mover un elemento SIN afectar a los demás | `relative` |
| Un elemento que flote sobre otros SIN ocupar espacio | `absolute` |
| Un elemento que SIEMPRE sea visible al hacer scroll | `fixed` |
| Un elemento que se "pegue" al scrolear SOLO en su sección | `sticky` |

---

### Ejemplos del mundo real

#### 1. Tooltip (información emergente)

```html
<style>
    .boton {
        position: relative;
        display: inline-block;
        background: #3498db;
        color: white;
        padding: 10px 20px;
        cursor: pointer;
    }
    
    .tooltip {
        position: absolute;
        bottom: 120%;
        left: 50%;
        transform: translateX(-50%);
        background: #333;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        white-space: nowrap;
        display: none;
    }
    
    .boton:hover .tooltip {
        display: block;
    }
</style>

<div class="boton">
    Pasa el mouse
    <span class="tooltip">¡Información extra!</span>
</div>
```

#### 2. Modal (ventana emergente centrada)

```html
<style>
    .modal-fondo {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0,0,0,0.5);
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .modal-contenido {
        background: white;
        padding: 20px;
        border-radius: 10px;
        width: 300px;
    }
</style>

<div class="modal-fondo">
    <div class="modal-contenido">
        <h3>¡Soy un modal!</h3>
        <p>Estoy centrado y fijo en la pantalla</p>
        <button>Cerrar</button>
    </div>
</div>
```

#### 3. Badge de notificación

```html
<style>
    .icono {
        position: relative;
        display: inline-block;
        font-size: 30px;
    }
    
    .badge {
        position: absolute;
        top: -10px;
        right: -10px;
        background: red;
        color: white;
        font-size: 12px;
        padding: 2px 6px;
        border-radius: 50%;
    }
</style>

<div class="icono">
    🔔
    <span class="badge">3</span>
</div>
```

---

### Resumen final para el estudiante trainee

```css
/* FÓRMULA DE ORO para recordar */

position: static;    /* → NADA especial (valor por defecto) */
position: relative;  /* → Me muevo PERO dejo mi hueco vacío */
position: absolute;  /* → Salgo del flujo Y uso referencia a un ancestro */
position: fixed;     /* → Salgo del flujo Y uso referencia a la ventana */
position: sticky;    /* → Me comporto como relative PERO me pego al scrollear */
```

**Pro tips:**
1. Todo elemento con `position` (excepto `static`) puede usar `top/right/bottom/left`
2. `absolute` siempre busca un ancestro con `position` diferente a `static`
3. `z-index` solo funciona en elementos posicionados
4. `fixed` ignora completamente el scroll de la página
5. `sticky` necesita un valor `top`, `bottom`, `left` o `right` para funcionar

**Ejercicio para practicar:**
Crea una página con un encabezado `fixed` en la parte superior, una barra lateral `sticky` que acompañe el scroll, y varios tooltips `absolute` que aparezcan al hacer hover sobre diferentes elementos.