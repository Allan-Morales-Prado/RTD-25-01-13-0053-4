# 📋 Formularios HTML

## Introducción

Los formularios HTML son componentes de una página web que permiten **recibir información del usuario**. Piensa en ellos como una "hoja de preguntas" que el usuario completa: registro en una página, búsqueda de productos, contacto, etc. 

> **Concepto clave**: El formulario es la única forma que tiene HTML de enviar datos **desde el usuario hacia el servidor**. Sin formularios, la comunicación sería solo unidireccional (servidor → usuario). 


## 🏗️ Estructura Básica de un Formulario

### La etiqueta `<form>`: el contenedor principal

Todo formulario comienza y termina con la etiqueta `<form>`. Dentro de ella se colocan todos los controles (campos, botones, etc.). 

```html
<form>
  <!-- Aquí van todos los elementos del formulario -->
</form>
```

### Atributos esenciales de `<form>`

| Atributo | ¿Para qué sirve? | Valores posibles |
|----------|------------------|------------------|
| `action` | Indica **dónde** enviar los datos (la URL del programa que los procesará) | Una dirección URL (ej: `/procesar-formulario`) |
| `method` | Indica **cómo** enviar los datos | `get` (por defecto) o `post` |
| `target` | Indica **dónde mostrar** la respuesta | `_self` (misma pestaña), `_blank` (nueva pestaña) |

### ¿`get` o `post`? 

| Método | Cómo funciona | Cuándo usarlo |
|--------|---------------|----------------|
| `get` | Los datos se **ven en la barra de direcciones** (ej: `?nombre=Ana&edad=25`) | Búsquedas, filtros, cuando el formulario no cambia datos |
| `post` | Los datos **no se ven** en la barra de direcciones | Formularios de contacto, registro, envío de archivos, datos sensibles |

```html
<!-- Búsqueda (GET - se ve en la URL) -->
<form action="/buscar" method="get">
  ...
</form>

<!-- Registro de usuario (POST - datos ocultos) -->
<form action="/registrar-usuario" method="post">
  ...
</form>
```


## 📝 Etiquetas para Crear Formularios

### 1. `<label>`: la etiqueta que describe cada campo

La etiqueta `<label>` se asocia a un campo para **describir qué debe ingresar el usuario**. Al hacer clic en el texto del `<label>`, el campo correspondiente se activa automáticamente. 

```html
<label for="nombre">Nombre completo:</label>
<input type="text" id="nombre" name="nombre">
```

> **Relación `for` e `id`**: El valor del atributo `for` en `<label>` debe ser **idéntico** al valor del atributo `id` en el campo al que se asocia. Así se vinculan correctamente.

### 2. `<input>`: el campo de entrada más versátil

`<input>` es la etiqueta más importante y versátil. Su comportamiento cambia completamente según el valor del atributo `type`. 

| type | Apariencia | Uso típico |
|------|------------|-------------|
| `text` | Caja de texto de una línea | Nombre, dirección, texto libre |
| `password` | Los caracteres se ven como puntos o asteriscos | Contraseñas |
| `email` | Caja de texto + validación de formato email | Correo electrónico |
| `tel` | Caja de texto (puede mostrar teclado numérico en móviles) | Teléfono |
| `number` | Caja con flechas arriba/abajo | Cantidades, edades |
| `search` | Similar a text, pero con diseño de buscador | Búsquedas |
| `url` | Caja de texto con validación de URL | Direcciones web |
| `date` | Calendario desplegable | Fechas de nacimiento, eventos |
| `time` | Selector de hora | Horarios |
| `datetime-local` | Fecha + hora combinados | Citas, eventos |
| `month` | Selección de mes y año | Fecha de expiración de tarjeta |
| `week` | Selección de semana del año | Planificación semanal |
| `color` | Selector de color | Personalización de temas |
| `checkbox` | Casilla que se marca/desmarca | Aceptar términos, seleccionar opciones múltiples |
| `radio` | Botón circular (solo uno del grupo puede estar marcado) | Seleccionar género, tamaño, etc. |
| `file` | Botón para seleccionar archivos | Subir fotos, documentos |
| `hidden` | Campo invisible (para enviar datos sin que el usuario los vea) | IDs, tokens |
| `submit` | Botón que envía el formulario | Enviar datos |
| `reset` | Botón que borra todo lo ingresado | Limpiar formulario |
| `button` | Botón sin acción automática | (Requiere JavaScript) |

#### Ejemplos de cada tipo:

```html
<!-- Texto normal -->
<label for="nombre">Nombre:</label>
<input type="text" id="nombre" name="nombre">

<!-- Contraseña (oculta) -->
<label for="clave">Contraseña:</label>
<input type="password" id="clave" name="clave">

<!-- Email con validación -->
<label for="correo">Correo electrónico:</label>
<input type="email" id="correo" name="correo">

<!-- Teléfono -->
<label for="telefono">Teléfono:</label>
<input type="tel" id="telefono" name="telefono">

<!-- Número con límites -->
<label for="edad">Edad:</label>
<input type="number" id="edad" name="edad" min="18" max="99">

<!-- Fecha -->
<label for="nacimiento">Fecha de nacimiento:</label>
<input type="date" id="nacimiento" name="nacimiento">

<!-- Checkbox -->
<input type="checkbox" id="terminos" name="terminos">
<label for="terminos">Acepto los términos y condiciones</label>
```

### 3. `<textarea>`: texto multilínea

Cuando necesitas que el usuario escriba varias líneas (comentarios, descripciones largas), usa `<textarea>` en lugar de `<input type="text">`. 

```html
<label for="mensaje">Mensaje:</label>
<textarea id="mensaje" name="mensaje" rows="5" cols="40"></textarea>
```

**Atributos útiles para `<textarea>`**:

| Atributo | ¿Qué hace? |
|----------|-------------|
| `rows` | Número de filas visibles (alto) |
| `cols` | Número de columnas visibles (ancho) |
| `maxlength` | Máximo de caracteres permitidos |
| `placeholder` | Texto de ejemplo dentro del área |

### 4. `<select>` y `<option>`: listas desplegables

Para ofrecer opciones predefinidas en un menú desplegable. 

```html
<label for="pais">País:</label>
<select id="pais" name="pais">
  <option value="cl">Chile</option>
  <option value="ar">Argentina</option>
  <option value="pe">Perú</option>
  <option value="mx">México</option>
</select>
```

**Atributos importantes**:

| Atributo | ¿Dónde se usa? | ¿Qué hace? |
|----------|----------------|-------------|
| `selected` | En `<option>` | Marca esa opción como seleccionada por defecto |
| `multiple` | En `<select>` | Permite seleccionar múltiples opciones |
| `size` | En `<select>` | Cuántas opciones se ven sin desplegar |

```html
<!-- Opción preseleccionada -->
<select id="mes" name="mes">
  <option value="1">Enero</option>
  <option value="2" selected>Febrero</option>
  <option value="3">Marzo</option>
</select>

<!-- Grupo de opciones con <optgroup> -->
<select id="producto" name="producto">
  <optgroup label="Electrónica">
    <option value="laptop">Laptop</option>
    <option value="mouse">Mouse</option>
  </optgroup>
  <optgroup label="Ropa">
    <option value="camisa">Camisa</option>
    <option value="pantalon">Pantalón</option>
  </optgroup>
</select>
```

### 5. `<button>`: el botón

El botón puede tener tres comportamientos según su `type`. 

```html
<!-- Botón que envía el formulario -->
<button type="submit">Enviar formulario</button>

<!-- Botón que borra todos los datos -->
<button type="reset">Limpiar formulario</button>

<!-- Botón sin acción automática (requiere JavaScript) -->
<button type="button">Hacer algo</button>
```

> **Dato importante**: Si no especificas `type`, el botón por defecto actúa como `submit`. 


## 🧩 Agrupación de Controles: `<fieldset>` y `<legend>`

Cuando tienes muchos campos relacionados, puedes agruparlos visual y semánticamente con `<fieldset>` y darle un título con `<legend>`. 

```html
<fieldset>
  <legend>Información personal</legend>
  
  <label for="nombre">Nombre:</label>
  <input type="text" id="nombre" name="nombre">
  
  <label for="apellido">Apellido:</label>
  <input type="text" id="apellido" name="apellido">
</fieldset>

<fieldset>
  <legend>Información de contacto</legend>
  
  <label for="email">Email:</label>
  <input type="email" id="email" name="email">
  
  <label for="telefono">Teléfono:</label>
  <input type="tel" id="telefono" name="telefono">
</fieldset>
```

**¿Por qué agrupar?**

- Mejora la **organización visual** del formulario
- Ayuda a los **lectores de pantalla** a entender la estructura
- Permite **deshabilitar grupos enteros** con el atributo `disabled` en `<fieldset>`


## 🔘 Controles de Selección Especiales

### Checkboxes (varias opciones)

Los checkboxes permiten **seleccionar múltiples opciones**. 

```html
<fieldset>
  <legend>¿Qué lenguajes te interesan?</legend>
  
  <input type="checkbox" id="html" name="intereses" value="html">
  <label for="html">HTML</label>
  
  <input type="checkbox" id="css" name="intereses" value="css">
  <label for="css">CSS</label>
  
  <input type="checkbox" id="js" name="intereses" value="js">
  <label for="js">JavaScript</label>
</fieldset>
```

**Características importantes de checkboxes** :
- Pueden tener el mismo `name` o diferente
- Si tienen el mismo `name`, se enviarán múltiples valores
- Si están marcados, se envía `nombre=valor`; si no, no se envía nada
- El atributo `checked` los marca por defecto

### Radio buttons (una sola opción)

Los radio buttons permiten **seleccionar solo una opción dentro de un grupo**. Para que funcionen como grupo, deben tener el **mismo `name`**. 

```html
<fieldset>
  <legend>Género</legend>
  
  <input type="radio" id="femenino" name="genero" value="femenino">
  <label for="femenino">Femenino</label>
  
  <input type="radio" id="masculino" name="genero" value="masculino">
  <label for="masculino">Masculino</label>
  
  <input type="radio" id="otro" name="genero" value="otro">
  <label for="otro">Otro</label>
</fieldset>
```

**Características importantes de radio buttons** :
- **Todos** los radio buttons del mismo grupo deben tener el **mismo `name`**
- Solo **uno** puede estar seleccionado a la vez
- Si uno se selecciona, los demás se desmarcan automáticamente
- El atributo `checked` en uno lo marca por defecto
- Si ninguno tiene `checked`, todos comienzan desmarcados


## 🔧 Atributos Comunes para Inputs

Estos atributos se pueden usar en casi cualquier tipo de input:

| Atributo | ¿Qué hace? | Ejemplo |
|----------|------------|---------|
| `name` | **Obligatorio para enviar datos**. Es la clave que identifica el campo | `<input name="usuario">` |
| `value` | Valor inicial/predefinido del campo | `<input value="Texto por defecto">` |
| `placeholder` | Texto de ejemplo que desaparece al escribir | `<input placeholder="Escribe tu nombre">` |
| `required` | El campo debe completarse sí o sí | `<input required>` |
| `readonly` | El usuario no puede modificar el valor | `<input readonly value="Fijo">` |
| `disabled` | El campo está deshabilitado (no se envía al servidor) | `<input disabled>` |
| `maxlength` | Número máximo de caracteres | `<input maxlength="10">` |
| `minlength` | Número mínimo de caracteres | `<input minlength="3">` |
| `size` | Ancho visible del campo (en caracteres) | `<input size="30">` |
| `min` | Valor mínimo (para number, date, etc.) | `<input type="number" min="1">` |
| `max` | Valor máximo (para number, date, etc.) | `<input type="number" max="100">` |
| `step` | Incremento permitido (para number, date, etc.) | `<input type="number" step="5">` |
| `autofocus` | El campo recibe el foco al cargar la página | `<input autofocus>` |
| `autocomplete` | Permite autocompletado del navegador | `<input autocomplete="on">` |


## 🔍 Validación en HTML (sin JavaScript)

HTML5 incluye **validaciones automáticas** que no requieren JavaScript. El navegador verifica los datos antes de enviarlos. 

### Tipos de validación automática

| Tipo de validación | Cómo se hace | ¿Qué hace el navegador? |
|--------------------|--------------|--------------------------|
| Campo obligatorio | `required` | Bloquea el envío si está vacío |
| Tipo email | `type="email"` | Exige formato válido (ej: `algo@algo.com`) |
| Tipo url | `type="url"` | Exige formato de URL válido |
| Número en rango | `min` y `max` en `type="number"` | Exige valor dentro del rango |
| Longitud de texto | `minlength` y `maxlength` | Exige cantidad de caracteres |
| Patrón personalizado | `pattern` con expresión regular | Exige formato específico |

### Ejemplo de formulario con validaciones

```html
<form action="/registro" method="post">
  
  <!-- Campo obligatorio -->
  <label for="nombre">Nombre completo:</label>
  <input type="text" id="nombre" name="nombre" required>
  
  <!-- Email con formato válido -->
  <label for="email">Correo electrónico:</label>
  <input type="email" id="email" name="email" required>
  
  <!-- Teléfono con patrón (formato: 9xxxxxxx) -->
  <label for="telefono">Teléfono (9 números):</label>
  <input type="tel" id="telefono" name="telefono" pattern="[0-9]{9}" required>
  
  <!-- Edad con rango numérico -->
  <label for="edad">Edad (18-99):</label>
  <input type="number" id="edad" name="edad" min="18" max="99" required>
  
  <!-- Contraseña con longitud mínima -->
  <label for="clave">Contraseña (mínimo 8 caracteres):</label>
  <input type="password" id="clave" name="clave" minlength="8" required>
  
  <!-- Fecha con rango -->
  <label for="fecha">Fecha de nacimiento (a partir de 1900):</label>
  <input type="date" id="fecha" name="fecha" min="1900-01-01" max="2025-12-31">
  
  <button type="submit">Registrarse</button>
  <button type="reset">Limpiar</button>
  
</form>
```

### ¿Qué es el atributo `pattern`?

El atributo `pattern` permite definir **expresiones regulares** para validar formatos específicos. 

```html
<!-- Solo letras -->
<input type="text" pattern="[A-Za-záéíóúüñ]+" title="Solo letras">

<!-- Número de teléfono chileno -->
<input type="tel" pattern="[0-9]{9}" title="9 números sin espacios">

<!-- Código postal argentino -->
<input type="text" pattern="[0-9]{4}" title="4 números">
```

> **Importante**: La validación HTML NO es suficiente por sí sola. Siempre se debe validar también en el servidor por seguridad. 


## 📤 Envío de Archivos con `type="file"`

Para permitir que los usuarios suban archivos (imágenes, documentos, etc.), se necesita:
1. Un `<input type="file">`
2. `method="post"` (obligatorio)
3. `enctype="multipart/form-data"` en el `<form>` 

```html
<form action="/subir-archivo" method="post" enctype="multipart/form-data">
  <label for="foto">Selecciona una foto:</label>
  <input type="file" id="foto" name="foto" accept="image/*">
  
  <button type="submit">Subir foto</button>
</form>
```

**Atributos útiles para `type="file"`**:

| Atributo | ¿Qué hace? |
|----------|-------------|
| `accept` | Restringe los tipos de archivo (`image/*`, `.pdf`, `audio/*`) |
| `multiple` | Permite seleccionar varios archivos |


## 📊 Resumen de Elementos de Formulario

| Etiqueta | Descripción | ¿Tiene cierre? | ¿Obligatoria? |
|----------|-------------|----------------|----------------|
| `<form>` | Contenedor del formulario | `</form>` | Sí |
| `<label>` | Etiqueta descriptiva | `</label>` | Recomendada |
| `<input>` | Campo de entrada | No (se cierra con `/>`) | Sí (al menos uno) |
| `<textarea>` | Texto multilínea | `</textarea>` | No |
| `<select>` | Lista desplegable | `</select>` | No |
| `<option>` | Opción de lista | `</option>` | Dentro de `<select>` |
| `<optgroup>` | Grupo de opciones | `</optgroup>` | Dentro de `<select>` |
| `<button>` | Botón | `</button>` | No |
| `<fieldset>` | Agrupación de controles | `</fieldset>` | No |
| `<legend>` | Título de agrupación | `</legend>` | Dentro de `<fieldset>` |


## ✅ Checklist de Buenas Prácticas

Para cada formulario que crees, verifica:

- [ ] ¿Usé `<form>` para encerrar todos los controles?
- [ ] ¿Cada campo tiene su `<label>` asociado con `for`?
- [ ] ¿Todos los campos tienen un `name`? (sin `name` no se envían)
- [ ] ¿Usé el `type` apropiado para cada campo?
- [ ] ¿Para radio buttons, todos tienen el mismo `name`?
- [ ] ¿Para agrupar controles relacionados, usé `<fieldset>` y `<legend>`?
- [ ] ¿Los campos obligatorios tienen `required`?
- [ ] ¿Usé `method="post"` para datos sensibles?
- [ ] ¿Para subir archivos, agregué `enctype="multipart/form-data"`?
- [ ] ¿El botón de envío tiene `type="submit"`?


## 📝 Ejemplo Completo: Formulario de Registro

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Formulario de Registro</title>
</head>
<body>
    <h1>Registro de Usuario</h1>
    
    <form action="/procesar-registro" method="post">
        
        <!-- Datos personales -->
        <fieldset>
            <legend>Datos personales</legend>
            
            <div>
                <label for="nombre">Nombre completo:</label>
                <input type="text" id="nombre" name="nombre" required minlength="3">
            </div>
            
            <div>
                <label for="email">Correo electrónico:</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div>
                <label for="telefono">Teléfono:</label>
                <input type="tel" id="telefono" name="telefono" pattern="[0-9]{9}">
            </div>
            
            <div>
                <label for="nacimiento">Fecha de nacimiento:</label>
                <input type="date" id="nacimiento" name="nacimiento">
            </div>
            
            <div>
                <label for="pais">País:</label>
                <select id="pais" name="pais">
                    <option value="">Selecciona un país</option>
                    <option value="cl">Chile</option>
                    <option value="ar">Argentina</option>
                    <option value="pe">Perú</option>
                    <option value="mx">México</option>
                </select>
            </div>
        </fieldset>
        
        <!-- Información de cuenta -->
        <fieldset>
            <legend>Información de cuenta</legend>
            
            <div>
                <label for="usuario">Nombre de usuario:</label>
                <input type="text" id="usuario" name="usuario" required minlength="4">
            </div>
            
            <div>
                <label for="clave">Contraseña:</label>
                <input type="password" id="clave" name="clave" required minlength="8">
            </div>
            
            <div>
                <label for="confirmar">Confirmar contraseña:</label>
                <input type="password" id="confirmar" name="confirmar" required minlength="8">
            </div>
        </fieldset>
        
        <!-- Preferencias -->
        <fieldset>
            <legend>Preferencias</legend>
            
            <div>¿Cómo conociste nuestro sitio?</div>
            <div>
                <input type="radio" id="redes" name="origen" value="redes">
                <label for="redes">Redes sociales</label>
                
                <input type="radio" id="buscador" name="origen" value="buscador">
                <label for="buscador">Buscador</label>
                
                <input type="radio" id="recomendacion" name="origen" value="recomendacion">
                <label for="recomendacion">Recomendación</label>
            </div>
            
            <div>
                <input type="checkbox" id="noticias" name="noticias" value="si">
                <label for="noticias">Deseo recibir noticias y novedades</label>
            </div>
            
            <div>
                <input type="checkbox" id="terminos" name="terminos" required>
                <label for="terminos">Acepto los <a href="/terminos">términos y condiciones</a></label>
            </div>
        </fieldset>
        
        <!-- Botones -->
        <div>
            <button type="submit">Registrarse</button>
            <button type="reset">Limpiar formulario</button>
        </div>
        
    </form>
</body>
</html>
```


## ❌ Errores Comunes que Debes Evitar

1. **Olvidar el atributo `name`**: Sin `name`, el campo NO se envía al servidor.
2. **No usar `<label>`**: Dificulta la accesibilidad (lectores de pantalla) y la usabilidad.
3. **Confundir `id` y `name`**: El `id` es para vincular con `<label>`, el `name` es para enviar datos.
4. **Radio buttons con diferentes `name`**: No funcionarán como grupo y se podrían seleccionar varios.
5. **Usar `method="get"` para enviar contraseñas**: Las contraseñas se verían en la URL.
6. **Olvidar `enctype` para archivos**: Sin `enctype="multipart/form-data"`, los archivos no se suben.
7. **No usar `fieldset` para agrupar**: El formulario se vuelve confuso y menos accesible.
8. **Usar `placeholder` como reemplazo de `<label>`**: El `placeholder` desaparece al escribir, dejando al usuario sin referencia.


## 🔍 Comparativa: `<input>` vs `<textarea>` vs `<select>`

| Característica | `<input>` | `<textarea>` | `<select>` |
|----------------|-----------|--------------|------------|
| Texto en una línea | ✅ Sí | ❌ No (multilínea) | ❌ No |
| Texto en múltiples líneas | ❌ No | ✅ Sí | ❌ No |
| Opciones predefinidas | ❌ Solo con `datalist` | ❌ No | ✅ Sí |
| Validación de formato | ✅ Sí (`type`) | ❌ No | ❌ No |
| Atributo `value` | ✅ Sí | ❌ No (el texto va entre etiquetas) | ✅ Sí (en `<option>`) |