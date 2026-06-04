# 📊 Tablas HTML

## Introducción

Las tablas en HTML permiten organizar información en **filas y columnas**, como una hoja de cálculo. Se utilizan para mostrar datos que tienen una relación entre sí: horarios, precios, listados, comparativas, etc.

> **Regla fundamental**: Las tablas son para **datos tabulares**, no para maquetar páginas. Usar tablas para diseño está mal visto y causa problemas de accesibilidad. 


## 🏗️ Estructura Básica de una Tabla

### Etiquetas Fundamentales

| Etiqueta | Significado | Descripción |
|----------|-------------|-------------|
| `</table>` | Contenedor principal | Define el inicio y fin de la tabla |
| `<tr>` | Table Row | Define una **fila** |
| `<th>` | Table Header | Celda de **encabezado** (texto en negrita y centrado) |
| `<td>` | Table Data | Celda de **dato** normal |

### Ejemplo Mínimo

```html
<table>
  <tr>
    <th>Nombre</th>
    <th>Edad</th>
  </tr>
  <tr>
    <td>Ana</td>
    <td>25</td>
  </tr>
</table>
```

**Resultado visual:**

| Nombre | Edad |
|--------|------|
| Ana | 25 |


## 📐 Etiquetas Semánticas para Tablas (¡Importante!)

Al igual que usas `<header>`, `<nav>`, `<section>` para estructurar una página, las tablas tienen sus propias etiquetas semánticas para organizar el contenido. 

### Estructura Completa

```html
<table>
  <caption>Título de la tabla</caption>
  
  <thead>
    <tr>
      <th>Encabezado 1</th>
      <th>Encabezado 2</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <td>Dato 1</td>
      <td>Dato 2</td>
    </tr>
  </tbody>
  
  <tfoot>
    <tr>
      <td>Total: 100</td>
    </tr>
  </tfoot>
</table>
```

### Explicación de cada etiqueta

| Etiqueta | ¿Qué agrupa? | Equivalente en página web |
|----------|--------------|---------------------------|
| `<caption>` | Título de la tabla | El título de la página (`<h1>`) |
| `<thead>` | Filas de encabezado | `<header>` de la página |
| `<tbody>` | Filas de datos | `<main>` o `<section>` |
| `<tfoot>` | Filas de resumen/pie | `<footer>` de la página |

### ¿Por qué usar estas etiquetas?

- **Accesibilidad**: Los lectores de pantalla entienden mejor la estructura
- **Navegación**: Usuarios pueden saltar directamente al cuerpo de la tabla
- **Impresión**: El `<thead>` y `<tfoot>` pueden repetirse en cada página impresa
- **Mantenimiento**: Código más limpio y fácil de entender 


## 🔗 El Atributo `scope` (Para Encabezados)

Cuando usas `<th>`, debes indicar **a qué se aplica ese encabezado** usando el atributo `scope`. 

### Valores de `scope`

| Valor | Significado | Ejemplo de uso |
|-------|-------------|----------------|
| `scope="col"` | Encabeza una **columna** | Encabezados arriba de la tabla |
| `scope="row"` | Encabeza una **fila** | Primera columna que nombra cada fila |
| `scope="colgroup"` | Encabeza un **grupo de columnas** | Varias columnas bajo un mismo título |
| `scope="rowgroup"` | Encabeza un **grupo de filas** | Varias filas bajo un mismo título |

### Ejemplo práctico

```html
<table border="1">
  <caption>Ventas por trimestre</caption>
  
  <thead>
    <tr>
      <th scope="col">Producto</th>      <!-- Encabeza su columna -->
      <th scope="col">Q1</th>            <!-- Encabeza columna Q1 -->
      <th scope="col">Q2</th>            <!-- Encabeza columna Q2 -->
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <th scope="row">Laptop</th>        <!-- Encabeza su fila -->
      <td>$500</td>
      <td>$600</td>
    </tr>
    <tr>
      <th scope="row">Mouse</th>         <!-- Encabeza su fila -->
      <td>$20</td>
      <td>$25</td>
    </tr>
  </tbody>
</table>
```


## 🧩 Unir Celdas: `colspan` y `rowspan`

A veces necesitas que una celda ocupe más de una columna o más de una fila. 

### `colspan` - Unir columnas (horizontal)

```html
<table border="1">
  <caption>Horario de atención</caption>
  <tr>
    <th colspan="2">Horario de Atención al Cliente</th>
  </tr>
  <tr>
    <th>Día</th>
    <th>Horario</th>
  </tr>
  <tr>
    <td>Lunes a Viernes</td>
    <td>09:00 - 18:00</td>
  </tr>
  <tr>
    <td colspan="2">Cerrado fines de semana</td>
  </tr>
</table>
```

**Resultado:**

| Horario de Atención al Cliente ||
|:-|:-|
| Día | Horario |
| Lunes a Viernes | 09:00 - 18:00 |
| Cerrado fines de semana ||

### `rowspan` - Unir filas (vertical)

```html
<table border="1">
  <caption>Eventos de marzo</caption>
  <thead>
    <tr>
      <th>Fecha</th>
      <th>Evento</th>
      <th>Ubicación</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">15 de marzo</td>
      <td>Conferencia Web</td>
      <td>Sala A</td>
    </tr>
    <tr>
      <td>Taller de CSS</td>
      <td>Sala B</td>
    </tr>
    <tr>
      <td>22 de marzo</td>
      <td>Hackathon</td>
      <td>Auditorio</td>
    </tr>
  </tbody>
</table>
```

**Resultado:**

| Fecha | Evento | Ubicación |
|-------|--------|-----------|
| 15 de marzo | Conferencia Web | Sala A |
| 15 de marzo | Taller de CSS | Sala B |
| 22 de marzo | Hackathon | Auditorio |


## 🎯 Tablas Complejas: Combinando todo

### Ejemplo: Horario de clases con grupos

```html
<table border="1">
  <caption>Horario de Clases - Curso Full Stack</caption>
  
  <thead>
    <tr>
      <th rowspan="2">Hora</th>
      <th colspan="5">Días de la semana</th>
    </tr>
    <tr>
      <th scope="col">Lunes</th>
      <th scope="col">Martes</th>
      <th scope="col">Miércoles</th>
      <th scope="col">Jueves</th>
      <th scope="col">Viernes</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <th scope="row">09:00 - 11:00</th>
      <td>HTML</td>
      <td>CSS</td>
      <td>JS</td>
      <td>React</td>
      <td>Node</td>
    </tr>
    <tr>
      <th scope="row">11:00 - 13:00</th>
      <td colspan="5">Prácticas en laboratorio</td>
    </tr>
    <tr>
      <th scope="row">14:00 - 16:00</th>
      <td>SQL</td>
      <td>APIs</td>
      <td>Auth</td>
      <td>Testing</td>
      <td>Deploy</td>
    </tr>
  </tbody>
  
  <tfoot>
    <tr>
      <td colspan="6">Total horas semanales: 25 horas</td>
    </tr>
  </tfoot>
</table>
```

### Ejemplo con `scope="colgroup"` y `scope="rowgroup"`

Para tablas con encabezados que agrupan múltiples columnas o filas: 

```html
<table border="1">
  <caption>Resultados por región y trimestre</caption>
  
  <thead>
    <tr>
      <td colspan="2" rowspan="2"></td>
      <th colspan="3" scope="colgroup">Trimestre 1</th>
      <th colspan="3" scope="colgroup">Trimestre 2</th>
    </tr>
    <tr>
      <th scope="col">Ene</th>
      <th scope="col">Feb</th>
      <th scope="col">Mar</th>
      <th scope="col">Abr</th>
      <th scope="col">May</th>
      <th scope="col">Jun</th>
    </tr>
  </thead>
  
  <tbody>
    <tr>
      <th rowspan="2" scope="rowgroup">Norte</th>
      <th scope="row">Ventas</th>
      <td>100</td><td>120</td><td>110</td>
      <td>130</td><td>140</td><td>135</td>
    </tr>
    <tr>
      <th scope="row">Gastos</th>
      <td>30</td><td>35</td><td>32</td>
      <td>38</td><td>40</td><td>39</td>
    </tr>
  </tbody>
  
  <tbody>
    <tr>
      <th rowspan="2" scope="rowgroup">Sur</th>
      <th scope="row">Ventas</th>
      <td>80</td><td>90</td><td>85</td>
      <td>95</td><td>100</td><td>105</td>
    </tr>
    <tr>
      <th scope="row">Gastos</th>
      <td>25</td><td>28</td><td>26</td>
      <td>30</td><td>32</td><td>31</td>
    </tr>
  </tbody>
</table>
```


## 📝 Ejercicios Guiados

### Ejercicio 1: Lista de compras semanal

**Enunciado:** Crear una tabla que muestre una lista de compras con producto, cantidad y precio unitario.

---

### Ejercicio 2: Directorio de contactos

**Enunciado:** Crear una tabla que muestre un directorio de contactos con nombre, teléfono, email y ciudad.

---

### Ejercicio 3: Calificaciones de estudiantes (con promedios)

**Enunciado:** Crear una tabla que muestre calificaciones de 4 estudiantes en 3 asignaturas, incluyendo el promedio de cada uno.

---

## ✏️ Ejercicios Propuestos

### Ejercicio 1: Tabla de horario de clases (Fácil)

Crear una tabla que muestre el horario de clases de Lunes a Viernes con las siguientes horas:
- 08:00 - 09:00
- 09:00 - 10:00
- 10:00 - 11:00
- 11:00 - 12:00

**Requisitos:**
- Usar `<caption>`
- Usar `<thead>` y `<tbody>`
- Los días deben ser encabezados con `scope="col"`
- Las horas deben ser encabezados de fila con `scope="row"`

---

### Ejercicio 2: Tabla de precios de productos (Fácil)

Crear una tabla de 5 productos con:
- Nombre del producto
- Precio unitario
- Cantidad en stock
- Subtotal (precio × cantidad)

**Requisitos:**
- Incluir `<tfoot>` con el valor total del inventario
- Usar `scope` en todos los encabezados

---

### Ejercicio 3: Tabla con colspan (Intermedio)

Crear una tabla que muestre los resultados de un torneo de fútbol:

| Equipo | PJ | PG | PE | PP | GF | GC | PTS |
|--------|----|----|----|----|----|----|-----|

Con datos de 4 equipos.

**Además:** Agregar una fila de encabezado que diga "Estadísticas del Torneo" usando `colspan="7"`.

---

### Ejercicio 4: Tabla con rowspan (Intermedio)

Crear una tabla de eventos donde una misma fecha tenga múltiples eventos:

| Fecha | Evento | Hora | Lugar |
|-------|--------|------|-------|
| 15/03 | Conferencia Web | 10:00 | Sala A |
| 15/03 | Taller de CSS | 14:00 | Sala B |
| 22/03 | Hackathon | 09:00 | Auditorio |
| 22/03 | Premiación | 17:00 | Auditorio |

Usar `rowspan` para combinar las celdas de fecha.

---

### Ejercicio 5: Tabla compleja con colspan y rowspan (Avanzado)

Crear una tabla de horario laboral semanal que muestre:

| Horario | Lunes a Jueves | Viernes | Sábado | Domingo |
|---------|----------------|---------|--------|---------|
| 09-13 | Recepción | Recepción | Cerrado | Cerrado |
| 13-15 | Almuerzo | Almuerzo | Cerrado | Cerrado |
| 15-18 | Atención | Atención | Cerrado | Cerrado |

**Requisitos:**
- Usar `colspan` para "Lunes a Jueves" (4 días en una celda)
- Usar `rowspan` para "Almuerzo" si corresponde
- Usar `scope` correctamente

---

### Ejercicio 6: Tabla de factura (Avanzado)

Crear una tabla que represente una factura de compra con:

**Encabezado principal** (usando `colspan`):
- "FACTURA N° 001-1234567"
- Fecha de emisión
- RUT del cliente

**Cuerpo de la tabla:**
| Código | Producto | Cantidad | Precio Unitario | Subtotal |
|--------|----------|----------|-----------------|----------|

**Pie de tabla:**
- Subtotal
- IVA (19%)
- Total

**Requisitos:**
- Usar `<caption>` para el título de la factura
- Usar `<thead>`, `<tbody>`, `<tfoot>`
- Usar `colspan` en el pie de tabla
- Usar `scope="col"` y `scope="row"`


## 📊 Resumen de Etiquetas y Atributos

### Etiquetas de tablas HTML

| Etiqueta | ¿Qué hace? | ¿Dónde va? |
|----------|------------|-------------|
| `<table>` | Contenedor principal | Envuelve toda la tabla |
| `<caption>` | Título de la tabla | Primera etiqueta dentro de `<td>` |
| `<colgroup>` | Grupo de columnas | Después de `<caption>`, antes de `<thead>` |
| `<col>` | Define propiedades de columna | Dentro de `<colgroup>` |
| `<thead>` | Agrupa filas de encabezado | Después de `<colgroup>` |
| `<tbody>` | Agrupa filas de datos | Después de `<thead>` (puede haber varios) |
| `<tfoot>` | Agrupa filas de pie | Después de `<tbody>` |
| `<tr>` | Fila | Dentro de `<thead>`, `<tbody>` o `<tfoot>` |
| `<th>` | Celda de encabezado | Dentro de `<tr>` |
| `<td>` | Celda de datos | Dentro de `<tr>` |

### Atributos importantes

| Atributo | Aplica a | Valores posibles | ¿Qué hace? |
|----------|----------|------------------|-------------|
| `border` | `</table>` | `"1"` o `""` | Agrega bordes a la tabla (solo para indicar que es tabla de datos)  |
| `scope` | `<th>` | `"col"`, `"row"`, `"colgroup"`, `"rowgroup"` | Indica qué celdas encabeza este `<th>` |
| `colspan` | `<th>`, `<td>` | Número entero (ej: `"3"`) | Cuántas columnas ocupa la celda |
| `rowspan` | `<th>`, `<td>` | Número entero (ej: `"2"`) | Cuántas filas ocupa la celda |
| `headers` | `<td>` | IDs de `<th>` | Asocia una celda con sus encabezados |


## ⚠️ Errores comunes que debes evitar

1. **Usar tablas para maquetar páginas**: Las tablas son para DATOS. Para diseño se usa CSS. 

2. **No usar `<th>` para encabezados**: Usar `<td>` con negrita manual no es semántico y los lectores de pantalla no lo entienden.

3. **Olvidar `scope`**: Sin `scope`, los lectores de pantalla no saben qué encabezado corresponde a cada celda.

4. **Celdas vacías en `<th>`**: Si una celda de encabezado no tiene texto, los usuarios de lectores de pantalla se pierden.

5. **No usar `<caption>`**: El título de la tabla es esencial para entender el contexto. 

6. **Anidar tablas innecesariamente**: Las tablas dentro de tablas son difíciles de leer y navegar.

7. **Mezclar `<tbody>` con filas sueltas**: Si usas `<tbody>`, todas las filas de datos deben ir dentro. No puedes mezclar filas directas con filas dentro de `<tbody>`.


## ✅ Checklist de verificación

Para cada tabla que crees, verifica:

- [ ] ¿Usé `<caption>` para darle título?
- [ ] ¿Usé `<thead>` para agrupar los encabezados?
- [ ] ¿Usé `<th>` en lugar de `<td>` para los encabezados?
- [ ] ¿Agregué `scope="col"` a los encabezados de columna?
- [ ] ¿Agregué `scope="row"` a los encabezados de fila?
- [ ] ¿Usé `<tbody>` para agrupar los datos?
- [ ] ¿Usé `<tfoot>` para resúmenes o totales?
- [ ] ¿Usé `colspan` y `rowspan` correctamente (sin superponer celdas)?
- [ ] ¿La tabla tiene sentido sin CSS? (prueba visual)
- [ ] ¿Estoy usando la tabla para DATOS, no para diseño?