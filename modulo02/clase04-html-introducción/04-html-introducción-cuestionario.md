# Introducción a HTML

## Sección 1: Conceptos Básicos de Desarrollo Web

### Pregunta 1
**¿Qué es el desarrollo web?**

<details>
<summary>Ver respuesta</summary>

El desarrollo web es el proceso de construcción de aplicaciones o sitios web, abarcando distintos roles que conforman el espectro moderno del desarrollo web.
</details>

---

### Pregunta 2
**Describe las diferencias entre los siguientes roles:**

a) Front-End Developer  
b) Back-End Developer  
c) Full Stack Developer

<details>
<summary>Ver respuesta</summary>

- **Front-End Developer**: Se encarga de desarrollar la interfaz gráfica que interactúa con los usuarios de un sitio web.
- **Back-End Developer**: Responsable de implementar un sitio web o aplicación web y todos sus componentes, desarrollando la lógica y las soluciones para implementar correctamente las operaciones necesarias.
- **Full Stack Developer**: Tiene conocimientos en todas las áreas y coopera con la comunicación efectiva y técnica de las piezas del rompecabezas.
</details>

---

## Sección 2: HTML y su Evolución

### Pregunta 3
**¿Qué significa HTML y para qué sirve?**

<details>
<summary>Ver respuesta</summary>

HTML significa **HyperText Markup Language** (Lenguaje de Marcas de Hipertexto). Sirve para la elaboración de páginas web, permitiendo estructurar y escribir contenido que luego es interpretado por un navegador web.
</details>

---

### Pregunta 4
**Menciona al menos 3 características principales de HTML5.**

<details>
<summary>Ver respuesta</summary>

1. **Multimedia nativo**: `<audio>`, `<video>` sin necesidad de plugins
2. **Elementos semánticos**: `<header>`, `<nav>`, `<section>`, `<article>`
3. **Canvas y SVG**: Gráficos dinámicos
4. **APIs modernas**: Geolocalización, almacenamiento local
5. **Formularios mejorados**: Nuevos tipos de input
6. **Responsive design**: Mejor adaptación móvil
</details>

---

### Pregunta 5
**Relaciona cada versión de HTML con su característica principal:**

| Versión | Característica |
|---------|----------------|
| HTML 1.0 | a) Separación de contenido y presentación, introducción de CSS |
| HTML 2.0 | b) Multimedia nativo y elementos semánticos |
| HTML 4.0/4.01 | c) Estructura básica de documentos y enlaces |
| HTML 5 | d) Formularios interactivos y tablas de datos |

<details>
<summary>Ver respuesta</summary>

- **HTML 1.0** → c) Estructura básica de documentos y enlaces
- **HTML 2.0** → d) Formularios interactivos y tablas de datos
- **HTML 4.0/4.01** → a) Separación de contenido y presentación, introducción de CSS
- **HTML 5** → b) Multimedia nativo y elementos semánticos
</details>

---

## Sección 3: Las 3 Tecnologías Fundamentales

### Pregunta 6
**Completa la siguiente tabla sobre las 3 tecnologías fundamentales del desarrollo web front-end:**

| Tecnología | Función | ¿Qué hace? | Ejemplos (menciona 2) |
|------------|---------|------------|----------------------|
| HTML | | | |
| CSS | | | |
| JavaScript | | | |

<details>
<summary>Ver respuesta</summary>

| Tecnología | Función | ¿Qué hace? | Ejemplos |
|------------|---------|------------|----------|
| **HTML** | Estructura y contenido | Define elementos y su significado semántico | Textos, títulos, imágenes, videos, enlaces, listas, formularios |
| **CSS** | Estilo y diseño visual | Controla la apariencia y el layout | Colores, tipografías, espaciado, animaciones, responsive design, Grid/Flexbox |
| **JavaScript** | Interactividad y lógica | Añade dinamismo y funcionalidad | Validación de formularios, efectos dinámicos, manipulación del DOM, APIs |
</details>

---

## Sección 4: Herramientas y Estructura HTML

### Pregunta 7
**¿Cuáles son las dos herramientas principales necesarias para el desarrollo front-end según el ppt?**

<details>
<summary>Ver respuesta</summary>

1. **Navegador Web** (recomendado: Google Chrome)
2. **Editor de Código** (recomendado: Visual Studio Code)
</details>

---

### Pregunta 8
**Escribe la estructura base de un documento HTML.**

<details>
<summary>Ver respuesta</summary>

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
</details>

---

### Pregunta 9
**¿Qué función cumple la etiqueta `<head>` y la etiqueta `<body>` en un documento HTML?**

<details>
<summary>Ver respuesta</summary>

- **`<head>`**: Contiene toda la información que es para el navegador (metadatos, títulos, enlaces a CSS, scripts, etc.)
- **`<body>`**: Contiene todo el contenido que es para el usuario (textos, imágenes, videos, enlaces, formularios, etc.)
</details>

---

## Sección 5: Estructura de Assets

### Pregunta 10
**¿Qué es la carpeta "assets" y qué tipo de archivos debe contener?**

<details>
<summary>Ver respuesta</summary>

**"Assets"** es una convención que indica dónde se deben almacenar los archivos adicionales de un proyecto. Debe contener:
- Hojas de estilo (**CSS**)
- Archivos JavaScript (**JS**)
- Imágenes (**img**)
</details>

---

### Pregunta 11
**Dibuja o describe la estructura de carpetas recomendada para un proyecto web que incluya HTML, CSS, JavaScript e imágenes.**

<details>
<summary>Ver respuesta</summary>

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

Los archivos HTML se guardan en el directorio principal, mientras que los recursos adicionales se almacenan en subcarpetas dentro de la carpeta "assets".
</details>

---

## Sección 6: Sintaxis y Etiquetas

### Pregunta 12
**¿Cuál es la sintaxis general de una etiqueta HTML? Proporciona un ejemplo.**

<details>
<summary>Ver respuesta</summary>

La sintaxis general es:
```html
<etiqueta atributo="valor">Contenido</etiqueta>
```

Ejemplo:
```html
<div class="div-contenedor" id="principal">
    <!-- Contenido -->
</div>
```
</details>

---

### Pregunta 13
**Nombra al menos 5 atributos comunes que pueden usarse en las etiquetas HTML.**

<details>
<summary>Ver respuesta</summary>

1. `class` - Define una clase CSS
2. `id` - Define un identificador único
3. `src` - Especifica la fuente de un recurso (imagen, video, etc.)
4. `alt` - Texto alternativo para imágenes
5. `type` - Define el tipo de elemento
6. `href` - Especifica la URL de un enlace
7. `style` - Aplica estilos CSS en línea
</details>

---

### Pregunta 14
**¿Qué atajo o método se puede usar en Visual Studio Code para generar rápidamente la estructura de un documento HTML?**

<details>
<summary>Ver respuesta</summary>

Escribir `html` (o `html:5`) y presionar la tecla **Tab** para autocompletar la estructura básica del documento HTML.
</details>

---

## Sección 7: Preguntas de Investigación

### Pregunta 15 (Investigación)
**¿Qué es la W3C y cuál es su función en el desarrollo web?**

<details>
<summary>Ver respuesta</summary>

La **W3C** (World Wide Web Consortium) es una comunidad internacional que desarrolla estándares abiertos para garantizar el crecimiento a largo plazo de la Web. Su función principal es crear y mantener estándares web como HTML, CSS, y otras tecnologías para asegurar la compatibilidad y accesibilidad en todos los navegadores y dispositivos.
</details>

---

### Pregunta 16 (Investigación)
**¿Qué rol tiene el navegador en HTML?**

<details>
<summary>Ver respuesta</summary>

El navegador es el **intérprete** del código HTML. Su función es:
1. Leer el archivo HTML
2. Interpretar las etiquetas y su estructura
3. Renderizar (mostrar) el contenido visualmente en la pantalla del usuario
4. Ejecutar CSS para aplicar estilos y JavaScript para añadir interactividad
5. Gestionar la comunicación con servidores web
</details>

---

## 🎯 Pregunta Final

### Pregunta 17
**¿Cuál es el objetivo principal que se busca lograr al emplear adecuadamente la estructura y sintaxis de las etiquetas de un documento HTML?**

<details>
<summary>Ver respuesta</summary>

El objetivo principal es **dar solución a una problemática** mediante la correcta estructuración y marcado del contenido web, asegurando que el navegador interprete correctamente la información y la presente de manera adecuada a los usuarios.
</details>
