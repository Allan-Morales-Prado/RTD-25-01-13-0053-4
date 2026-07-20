# Crear páginas con HTML

## Preguntas de Selección Múltiple

### 1. ¿Qué etiqueta se utiliza para mostrar el título de la página en la pestaña del navegador?

A) `<header>`
B) `<title>`
C) `<h1>`
D) `<head>`

---

### 2. ¿Cuál es la función principal de la etiqueta `<meta charset="UTF-8">`?

A) Agregar un título a la página
B) Especificar la codificación de caracteres del documento
C) Insertar una imagen en la página
D) Crear un enlace a otra página

---

### 3. ¿Qué etiqueta se utiliza para crear un párrafo en HTML?

A) `<paragraph>`
B) `<p>`
C) `<text>`
D) `<body>`

---

### 4. ¿Cuántos niveles de encabezados existen en HTML?

A) 3
B) 4
C) 5
D) 6

---

### 5. ¿Qué atributo de la etiqueta `<img>` se utiliza para proporcionar un texto alternativo?

A) `src`
B) `href`
C) `alt`
D) `title`

---

### 6. ¿Qué etiqueta se utiliza para crear una lista ordenada?

A) `<ul>`
B) `<li>`
C) `<ol>`
D) `<list>`

---

### 7. ¿Cuál de las siguientes opciones describe correctamente la diferencia entre una página web y un sitio web?

A) Una página web es un conjunto de sitios web
B) Un sitio web es una colección de páginas web interconectadas sobre un mismo tema
C) Son lo mismo
D) Una página web solo contiene imágenes, mientras que un sitio web contiene texto

---

### 8. ¿Qué atributo de la etiqueta `<a>` permite que el enlace se abra en una nueva pestaña?

A) `href="_new"`
B) `target="_blank"`
C) `rel="external"`
D) `open="new"`

---

### 9. ¿Cuál de las siguientes NO es una función de la etiqueta `<head>`?

A) Definir el título de la página
B) Especificar la codificación de caracteres
C) Mostrar contenido visible al visitante
D) Agregar el favicon

---

### 10. ¿Qué etiqueta se utiliza para crear un elemento dentro de una lista?

A) `<item>`
B) `<list>`
C) `<li>`
D) `<element>`

---

## Preguntas Verdadero o Falso

### 11. La etiqueta `<img>` tiene una etiqueta de cierre `</img>`.

Verdadero
Falso

---

### 12. La jerarquía de los encabezados `<h1>` a `<h6>` se refleja tanto en su estilo por defecto como en su semántica.

Verdadero
Falso

---

### 13. El favicon es una imagen grande que se muestra en el centro de la página web.

Verdadero
Falso

---

### 14. Es posible anidar listas ordenadas dentro de listas no ordenadas en HTML.

Verdadero
Falso

---

### 15. La etiqueta `<body>` contiene todos los elementos que se representan de forma visible al visitante.

Verdadero
Falso

---

## Preguntas de Desarrollo

### 16. Escribe el código HTML necesario para crear un enlace que redirija a "https://www.ejemplo.com" y que se abra en una nueva pestaña.

---

### 17. Escribe el código HTML para mostrar una imagen llamada "logo.png" que se encuentra en la carpeta "assets/imagenes/", con un texto alternativo "Logo de la empresa".

---

### 18. Crea el código HTML de una lista no ordenada con tres elementos y una lista ordenada anidada dentro del segundo elemento.

---

### 19. ¿Qué elementos debe contener la etiqueta `<head>` en un documento HTML bien estructurado? Nombra al menos 3 elementos y explica su función.

---

### 20. Explica con tus propias palabras la diferencia entre un sitio web y una página web, y proporciona un ejemplo de cada uno.

---

## Hoja de Respuestas

<details>
<summary>Ver respuestas</summary>

### Selección Múltiple
1. **B** `<title>`
2. **B** Especificar la codificación de caracteres del documento
3. **B** `<p>`
4. **D** 6
5. **C** `alt`
6. **C** `<ol>`
7. **B** Un sitio web es una colección de páginas web interconectadas sobre un mismo tema
8. **B** `target="_blank"`
9. **C** Mostrar contenido visible al visitante (esto es función del `<body>`)
10. **C** `<li>`

### Verdadero o Falso
11. **Falso** `<img>` no tiene etiqueta de cierre
12. **Verdadero**
13. **Falso** Es una pequeña imagen que se muestra en la pestaña del navegador
14. **Verdadero**
15. **Verdadero**

### Desarrollo (Ejemplos de respuesta)

**16.**
```html
<a href="https://www.ejemplo.com" target="_blank">Visitar Ejemplo</a>
```

**17.**
```html
<img src="assets/imagenes/logo.png" alt="Logo de la empresa">
```

**18.**
```html
<ul>
  <li>Elemento 1</li>
  <li>Elemento 2
    <ol>
      <li>Subelemento ordenado 1</li>
      <li>Subelemento ordenado 2</li>
      <li>Subelemento ordenado 3</li>
    </ol>
  </li>
  <li>Elemento 3</li>
</ul>
```

**19.** La etiqueta `<head>` debe contener:
- `<title>`: Define el título que aparece en la pestaña del navegador
- `<meta charset="UTF-8">`: Especifica la codificación de caracteres para mostrar correctamente letras con tildes y la Ñ
- `<link rel="icon">`: Agrega el favicon (ícono de la página)
- También puede contener `<style>` para estilos CSS o `<script>` para JavaScript

**20.** 
- **Página web**: Es un documento individual que puede visualizarse en un navegador. Ejemplo: Un artículo específico en un blog.
- **Sitio web**: Es una colección de páginas web interconectadas que comparten un mismo tema o propósito. Ejemplo: Wikipedia, que está compuesta por miles de artículos (páginas) interconectados.

</details>