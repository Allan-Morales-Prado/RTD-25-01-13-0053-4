# HTML5 y Etiquetas Semánticas

## ¿Qué es HTML5?

HTML5 introduce etiquetas semánticas que permiten:

- Definir la estructura del documento
- Facilitar que la página web sea mejor **indexada** por los buscadores
- Dar significado al contenido más allá de la apariencia visual

---

## Dividiendo nuestra página en secciones

Tradicionalmente, se usaban etiquetas `<div>` para agrupar información:

```html
<div>
  <!-- Contenido -->
</div>
```

**Problema:** Las etiquetas `<div>` solo dividen el contenido, pero **no tienen semántica**.

---

## Etiquetas Semánticas de HTML5

HTML5 nos proporciona etiquetas con significado:

```html
<nav>
<header>
<section>
<footer>
```

---

## ¿Por qué se habla de etiquetas semánticas?

**Pregunta clave:** ¿Por qué `<div>` no es una etiqueta semántica?

**Respuesta:** Porque `<div>` no transmite información sobre el tipo de contenido que contiene, mientras que las etiquetas semánticas describen su propósito y estructura.

---

## Analizando secciones de nuestro HTML

Para analizar correctamente nuestro HTML de Meet & Coffee, usaremos el **"HTML5 Element Flowchart"** de HTML5 Doctor.

---

### Primera Sección: Barra de Navegación

**Preguntas de análisis:**

- ¿Es un bloque de navegación? ✅ **Sí**
- Por lo tanto, la etiqueta que usaremos será `<nav>`

```html
<nav>
    <ul>
        <li><a href="#">Ícono</a></li>
        <li><a href="#">Ubicación</a></li>
        <li><a href="#">Próxima Charla</a></li>
        <li><a href="#">Eventos anteriores</a></li>
        <li><a href="#">Contacto</a></li>
    </ul>
</nav>
```

---

### Segunda Sección: Sección Principal (Hero Section)

**Análisis:**

- ¿Es un bloque de navegación? ❌ No
- ¿Tiene sentido por sí misma? ❌ No, es parte de un contenido mayor
- ¿Se requiere para entender el contenido? ✅ Sí
- ¿Podría moverse a un apéndice? ❌ No
- ¿Tiene lógica añadirle un encabezado? ✅ Sí → Sería un `<section>`

**Pero existe una sección más específica que `<section>`:**

- Está el encabezado principal `<h1>`
- Es lo primero que se ve después del menú de navegación
- Incluye información que contextualiza el sitio

✅ **Por lo tanto, esta sección la podemos etiquetar como `<header>`**

```html
<header>
    <img src="assets/img/bg-hero.png" alt="Hero image">
    <h1>Descubre lo último en tecnología bebiendo café</h1>
    <h2>Charlas, eventos y simposios sobre tecnología</h2>
</header>
```

---

### Tercera Sección: Sección de Lugar

**Análisis:**

- ¿Es un bloque de navegación? ❌ No
- ¿Tiene sentido por sí misma? ❌ No, depende de otras secciones
- ¿Se requiere para entender el contenido? ✅ Sí
- ¿Podría moverse a un apéndice? ❌ No
- ¿Tiene lógica añadirle un encabezado? ✅ Sí → Sería un `<section>`

```html
<section>
    <img src="assets/img/we-work.jpg" alt="We work location">
    <h2>¿Donde nos juntamos?</h2>
    <p>Todos los martes y viernes, de 19:00 a 22:00 en We Work, Calle Baker 133, Providencia, Santiago.</p>
</section>
```

---

### Sección Final: Contacto (Footer)

`<footer>` representa un pie de página para el elemento principal.

Generalmente contiene:
- Información sobre la sección (quién lo escribió)
- Enlaces a documentos relacionados
- Datos de derechos de autor

```html
<footer>
    <p>Meet & coffee 2018. Todos los derechos reservados.</p>
</footer>
```