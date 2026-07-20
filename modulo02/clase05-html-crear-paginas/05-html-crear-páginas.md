# Crear páginas con HTML

## Página y sitio web

**Página web:**
- Documento que puede ser visto a través de un navegador
- Están construidas en un lenguaje de etiquetas llamado HTML

**Sitio web (Website):**
- Colección de páginas (documentos) agrupadas e interconectadas en relación a un mismo tema
- Ejemplo: Wikipedia (https://es.wikipedia.org/wiki/)

---

## Contenido y formato de una página web

### Etiqueta HEAD

La etiqueta `<head></head>` especifica el contenido que se le entregará al navegador.

**Elementos principales:**

| Etiqueta | Función |
|----------|---------|
| `<title>` | El título de la página |
| `<meta charset="utf-8">` | La codificación de caracteres |
| `<link rel="shortcut icon">` | El favicon |
| `<style>` o `<link rel="stylesheet">` | Los estilos |
| `<script>` | Los scripts |

#### Título
```html
<title>Academia Desafío Latam - Desafío Latam</title>
```
Muestra el título de la página en el tab (pestaña) del navegador.

#### Codificación
```html
<meta charset="UTF-8">
```
Especifica la codificación de los caracteres. UTF-8 permite codificar símbolos y caracteres latinos (como la Ñ y las tildes).

#### Favicon
```html
<link rel="icon" type="image/png" href="/assets/favicon/icono.png">
```
Pequeña imagen asociada al sitio web que se muestra en la pestaña correspondiente.

---

### Etiqueta `<body></body>`

Contiene todos los elementos que se representan de forma visible al visitante de la página web.

#### Párrafos
```html
<p>Texto del párrafo</p>
```
Bloques de texto compuesto por una o más oraciones.

#### Encabezados o Headers
```html
<h1>¡ESTO ES DESAFÍO LATAM!</h1>
```
- Se escriben con la letra `h` seguida de un número del 1 al 6: `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`
- La jerarquía se refleja tanto en el estilo por defecto como en la semántica

#### Imágenes
```html
<img src="" alt="">
```
- **src**: Archivo de origen (URL o ruta)
- **alt**: Texto alternativo
- Es una etiqueta que no tiene cierre

#### Listas

| Tipo | Etiqueta | Descripción |
|------|----------|-------------|
| No ordenada | `<ul>` | Listado de elementos sin un orden particular |
| Ordenada | `<ol>` | Lista de elementos ordenados o enumerados |
| Elemento | `<li>` | Elemento de una lista |

**Ejemplo de listas anidadas:**
```html
<ul>
  <li>Elemento 1</li>
  <li>Elemento 2
    <ol>
      <li>Subelemento ordenado 1</li>
      <li>Subelemento ordenado 2</li>
    </ol>
  </li>
</ul>
```

#### Links (Enlaces)
```html
<a href="link">Texto a mostrar</a>
```

**Tipos de enlaces:**

| Tipo | Ejemplo |
|------|---------|
| A otros sitios | `<a href="https://www.w3schools.com/">Aprende más</a>` |
| A nueva pestaña | `<a href="https://www.w3schools.com/" target="_blank">Aprende más</a>` |
| A páginas internas | `<a href="index.html">Página principal</a>` |

#### Imágenes con links
```html
<a href="https://www.google.cl" target="_blank">
  <img src="http://ejemplo.com/logo.jpg" alt="Google">
</a>
```

---

## Menú

La forma más popular de crear un menú consiste en una barra representada por una lista no ordenada:

```html
<ul>
  <li><a href="index.html">Home</a></li>
  <li><a href="pagina1.html">Página 1</a></li>
  <li><a href="contacto.html">Contacto</a></li>
</ul>
```

---

## Resumen

- Una **página web** es un documento que puede ser visto a través de un navegador (Firefox, Google Chrome, Safari, etc.)
- Un **sitio web** es una colección de páginas agrupadas e interconectadas en relación a un mismo tema
- La etiqueta `<head></head>` especifica el contenido que se le entregará al navegador
- La etiqueta `<body></body>` contiene todos los elementos visibles al visitante

---

## Ejercicio guiado

Crear una estructura base con:
- Una lista no ordenada de cosas que debemos comprar en el supermercado
- Una lista ordenada con tus animales favoritos