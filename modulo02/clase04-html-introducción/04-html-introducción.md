# Introducción a HTML

---

## 🌐 ¿Qué es Desarrollo Web?

El **desarrollo web** se refiere al proceso de construcción de aplicaciones o sitios web, abarcando distintos roles que conforman el espectro moderno del desarrollo web.

---

## 👥 Diferencias entre Front-End, Back-End y Fullstack

### 🎨 Front-End Developer
Se encarga de desarrollar la **interfaz gráfica** que interactúa con los usuarios de un sitio web.

### ⚙️ Back-End Developer
Responsable de implementar un sitio web o aplicación web y todos sus componentes, desarrollando la **lógica** y las soluciones para implementar correctamente las operaciones necesarias.

### 🧩 Full Stack Developer
Rol que tiene **conocimientos en todas las áreas** y coopera con la comunicación efectiva y técnica de las piezas del rompecabezas.

> 🧠 **Investiguemos**: ¿Qué rol tiene el navegador en HTML? ¿Qué es la W3C?

---

## 📄 ¿Qué es HTML?

HTML son siglas que provienen del inglés **HyperText Markup Language** (Lenguaje de Marcas de Hipertexto), que sirve para la elaboración de páginas web.

```html
<p> Hola </p>
<!-- ¡Esto es una etiqueta! -->
```

---

## 📊 Evolución de HTML

| Versión | Características principales |
|---------|----------------------------|
| **HTML 1.0** | Estructura básica de documentos, enlaces hipertexto, encabezados simples, listas básicas |
| **HTML 2.0** | Formularios interactivos, tablas de datos, soporte para imágenes, elementos de texto enriquecido |
| **HTML 3.2** | Mejor soporte para tablas, applets de Java, scripts básicos, estilos en línea |
| **HTML 4.0/4.01** | Separación de contenido y presentación, introducción de CSS, mejor accesibilidad, soporte para scripts |
| **XHTML** | Sintaxis XML más estricta, documentos bien formados, mayor compatibilidad, validación más rigurosa |
| **HTML 5** | Multimedia nativo, elementos semánticos, APIs avanzadas, mejor soporte móvil |

---

## ⭐ Principales innovaciones de HTML5

- 🎵 **Multimedia nativo**: `<audio>`, `<video>` sin plugins
- 🏗️ **Elementos semánticos**: `<header>`, `<nav>`, `<section>`, `<article>`
- 🎨 **Canvas y SVG**: Gráficos dinámicos
- 🔌 **APIs modernas**: Geolocalización, almacenamiento local
- 📝 **Formularios mejorados**: Nuevos tipos de input
- 📱 **Responsive design**: Mejor adaptación móvil

---

## 🔧 Las 3 Tecnologías Fundamentales

### 📝 HTML - Contenido
- **Función**: Estructura y contenido
- **Qué hace**: Define elementos y su significado semántico
- **Ejemplos**: Textos, títulos, imágenes, videos, enlaces, listas, formularios

### 🎨 CSS - Presentación
- **Función**: Estilo y diseño visual
- **Qué hace**: Controla la apariencia y el layout
- **Ejemplos**: Colores, tipografías, espaciado, animaciones, responsive design, layouts (Grid, Flexbox)

### ⚡ JavaScript - Comportamiento
- **Función**: Interactividad y lógica
- **Qué hace**: Añade dinamismo y funcionalidad
- **Ejemplos**: Validación de formularios, efectos dinámicos, comunicación con servidores, manipulación del DOM, aplicaciones web complejas

---

## 🛠️ Herramientas Necesarias

| Herramienta | Descripción |
|-------------|-------------|
| **Navegador Web** | Google Chrome (recomendado) |
| **Editor de Código** | Visual Studio Code |

> 👨‍💻 **Demostración**: "Conociendo el inspector de elementos"

---

## 🏗️ Estructura Base de un Documento HTML

```html
<!DOCTYPE html>
<html>
<head>
    <!-- Aquí va la información para el navegador -->
</head>
<body>
    <!-- Aquí va el contenido para el usuario -->
</body>
</html>
```

### Ayuda para generar la estructura HTML en VSCode

1. Asegurarse de que estamos escribiendo en HTML
2. Escribir `html` (o `html:5`) y presionar la tecla **Tab**
3. Autocompletado

> 📖 Para profundizar y conocer más acerca de las funciones de VSC, revisa la [documentación oficial](https://code.visualstudio.com/docs).

---

## 🏷️ Etiquetas HTML

HTML se organiza en base a **etiquetas**, que son los elementos con los que puedes dar formato y estructura a un archivo HTML.

### Sintaxis de una etiqueta

```html
<etiqueta atributo="valor">Contenido</etiqueta>
```

### Ejemplo con atributos

```html
<div class="div-contenedor" id="principal">
    <!-- Contenido -->
</div>
```

**Atributos comunes**: `id`, `type`, `alt`, `src`, `class`, entre otros.

> 📚 Para conocer más en detalle la sintaxis de una etiqueta, revisa el [enlace](https://developer.mozilla.org/es/docs/Web/HTML/Element).

---

## 📁 Estructura de Assets

Los archivos HTML se guardarán en el **directorio principal**, mientras que los recursos adicionales se almacenarán en subcarpetas dentro de una carpeta común llamada **"assets"**.

### Modelo de organización por tipo de archivo

```
proyecto/
├── index.html
├── assets/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js
│   └── img/
│       ├── logo.png
│       └── fondo.jpg
```

### ¿Qué es "Assets"?

**"Assets"** corresponde a una convención que indica dónde se deben almacenar los archivos adicionales de nuestro proyecto:
- Hojas de estilo **(css)**
- JavaScript **(js)**
- Imágenes **(img)**

---

## 📝 Resumen

| Concepto | Descripción |
|----------|-------------|
| **Editor de texto** | Programa que se instala en el computador para escribir lenguaje que luego interpretará el navegador |
| **HTML** | Lenguaje de marcado que se utiliza para estructurar y escribir contenido, interpretado por un navegador web |
| **Estructura básica** | `<head>` (información para el navegador) y `<body>` (contenido para el usuario) |
| **Carpeta Assets** | Almacena archivos adicionales del proyecto: CSS, JS, imágenes |

### 🎯 Objetivo final

Emplear adecuadamente la estructura y sintaxis de las etiquetas de un documento HTML, para dar solución a una problemática.

---

> ✨ *"El desarrollo web es el arte de construir experiencias digitales que conectan personas con información y servicios."*