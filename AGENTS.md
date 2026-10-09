# AGENTS.md — Repositorio educativo de aprendizaje de Django

## Propósito del repositorio

Este repositorio es un **recurso educativo orientado a la enseñanza de Django**. Su objetivo no es introducir los fundamentos del framework ni del lenguaje, sino **consolidar, profundizar y llevar a la práctica** los conocimientos que el estudiante ya posee. El código y la documentación deben servir como material de referencia avanzada, laboratorio de ejercicios y guía de buenas prácticas.

El principio rector sigue siendo la **legibilidad y el valor pedagógico**, pero ahora en un nivel de exigencia propio de estudiantes con una base sólida ya adquirida.

---

## Perfil del estudiante

El material de este repositorio está dirigido a estudiantes que **ya dominan** los siguientes contenidos. El agente debe asumirlos como conocidos y **no debe explicarlos ni introducirlos de nuevo**, salvo cuando sea imprescindible para conectar con un concepto nuevo:

- Fundamentos de Python y uso de entornos virtuales (`venv`, `pip`, `requirements.txt`).
- Creación y configuración de un proyecto Django (`django-admin`, `startproject`, `startapp`, `manage.py`, `settings.py`, `urls.py`).
- Estructura MVC/MVT de Django, herencia de plantillas, templates y contenido dinámico con Bootstrap.
- Formularios de Django (`Form`, `ModelForm`), procesamiento y validación, mensajes de error en plantillas.
- Autenticación y autorización: modelo `auth`, Login/Logout, `LOGIN_REDIRECT_URL`, permisos, grupos y Mixins (`LoginRequiredMixin`, `PermissionRequiredMixin`).
- Sitio administrativo de Django: creación de superusuarios, gestión de usuarios, grupos y permisos.
- Integración con bases de datos: conexión a PostgreSQL, migraciones (`makemigrations`, `migrate`).
- Modelos de datos y el ORM de Django: definición de campos, claves primarias simples y compuestas, operaciones CRUD.
- Relaciones en el ORM: uno a uno, uno a muchos y muchos a muchos, con entidades intermedias.
- Consultas personalizadas: filtros con ORM, sentencias SQL con `raw()`, parámetros, cursores y procedimientos almacenados.
- Aplicaciones preinstaladas de Django (`admin`, `auth`, `contenttypes`, `sessions`, `messages`, `staticfiles`).

En consecuencia, el agente **no debe** asumir que el estudiante necesita definiciones básicas, ejemplos elementales ni repaso de sintaxis. Sí debe asumir que necesita **claridad en la aplicación práctica, criterios de decisión y buenas prácticas**.

---

## Principios de la experiencia del estudiante

### Legibilidad del código ante todo
- **Explícito mejor que implícito**: aunque el estudiante domina las abstracciones de Python, prioriza implementaciones progresivas y desglosadas cuando el objetivo sea didáctico. Reserva las construcciones concisas para ejemplos etiquetados explícitamente como "versión avanzada".
- **El nombre es documentación**: variables, funciones y clases deben expresar su intención con claridad. Prohibido usar `x`, `temp`, `data1` u otros nombres similares.
- **Los comentarios explican el "por qué"**: explican decisiones de diseño, no repiten lo que hace el código. Cada vista, modelo o comando de gestión personalizado debe incluir un comentario breve sobre su intención pedagógica.

### Mensajes de error comprensibles
- Las excepciones y errores de validación personalizados deben describir el problema con claridad, **en español o inglés**. Se espera que el estudiante sepa leerlos, pero no que adivine el origen.

### Progresión hacia el dominio, no desde cero
- No repitas conceptos ya dominados. Cuando un ejemplo requiera un concepto previo, referencia el módulo donde se trató en lugar de reexplicarlo.
- Los nuevos temas deben presentarse como **extensión o profundización** de lo ya sabido, no como introducción.
- Al añadir una característica nueva de Django, **debes incluir en el mismo PR o archivo un ejemplo mínimo ejecutable** que la contraste con lo que el estudiante ya conoce.

---

## Convenciones de código Django

### Versión y dependencias
- Versión objetivo de Django: **6.x LTS** (según el `requirements.txt` real).
- Versión de Python: **3.14+**.
- Sigue el estilo oficial de Django (PEP 8 + convenciones de Django).

### Capa de vistas
- A este nivel se espera que el estudiante sepa distinguir cuándo usar vistas basadas en funciones y cuándo basadas en clases. Los ejemplos deben **justificar la elección** y no solo mostrarla.
- Responsabilidad única de la vista: solo analizar la petición y devolver la respuesta. La lógica de negocio va en `services.py` o en métodos del modelo.
- Debes manejar los casos límite habituales (queryset vacío, formulario inválido) y dar retroalimentación clara.

### Capa de modelos
- Cada modelo debe tener un método `__str__`.
- Los campos deben usar `verbose_name` con etiquetas legibles para humanos.
- Los archivos de migración deben permanecer limpios; no edites migraciones ya aplicadas a mano.

### Plantillas
- Evita lógica compleja en las plantillas. Bucles y condicionales deben ser simples; los cálculos complejos van en la vista o en template tags.
- Incluye comentarios HTML significativos que expliquen el propósito de cada bloque.

### Pruebas
- Cada ejemplo didáctico debe tener su prueba correspondiente, con nombres que describan el comportamiento verificado (por ejemplo, `test_article_list_shows_only_published`).
- Las pruebas actúan como **documentación ejecutable** y deben cubrir también los casos límite, no solo el camino feliz.

---

## Normas de revisión de documentación Markdown

### Requisitos generales
- Cada guía debe comenzar con **objetivos de aprendizaje** formulados como capacidades aplicables (qué podrá hacer el estudiante al terminar), no como repaso de contenidos previos.
- Los bloques de código deben indicar el lenguaje (`python`, `html`, `bash`).
- Se asume que los términos del dominio Django ya son conocidos; solo se definen los términos **nuevos** que introduzca la guía.

### Revisión de diagramas Mermaid / PlantUML

**Validez sintáctica ante todo**: los diagramas deben renderizarse correctamente. Al revisar:
- Mermaid: verifica que las declaraciones `graph TD`, `sequenceDiagram`, `erDiagram`, etc. sean correctas y que los ID de nodo no contengan caracteres especiales.
- PlantUML: verifica que `@startuml` / `@enduml` estén emparejados y que la sintaxis de participantes y flechas sea correcta.
- **Si no hay un error sintáctico claro, no modifiques la estructura del diagrama** — el diagrama es una herramienta didáctica y simplificarlo puede eliminar información.

**Idoneidad pedagógica**:
- La complejidad del diagrama debe corresponder al contenido del texto. Como el estudiante ya domina los fundamentos, **se permite un nivel de detalle mayor** que en un curso introductorio: relaciones completas en ER, flujos de autenticación, ciclos de vida de migraciones.
- En un diagrama ER pueden mostrarse todas las entidades del módulo en curso, incluidas sus relaciones, siempre que sean relevantes.
- En un diagrama de secuencia pueden mostrarse los participantes necesarios para representar el flujo real, sin forzar una simplificación artificial.

**Coherencia**:
- Los términos del diagrama deben coincidir exactamente con los del texto (no llames `Article` en un sitio y `Post` en otro al mismo concepto).
- La lógica descrita por el diagrama debe coincidir con el ejemplo de código correspondiente.

### Estructura de la documentación
```markdown
# Nombre del módulo

## Objetivos de aprendizaje
- [ ] Objetivo uno (capacidad aplicable)
- [ ] Objetivo dos

## Contenido (con ejemplos de código)

## Decisiones de diseño y buenas prácticas

## Errores comunes y solución de problemas

## Ejercicios
```

---

## Lista de verificación para la revisión de código

Al revisar código de estudiantes o ejemplos didácticos generados, confirma punto por punto:

- [ ] Los nombres de variables/funciones expresan su intención con claridad
- [ ] No hay números ni cadenas mágicas
- [ ] Existe manejo de errores y los mensajes son comprensibles
- [ ] La lógica clave incluye comentarios del "por qué"
- [ ] La elección entre FBV/CBV (u otras alternativas) está justificada
- [ ] Se respetan las convenciones de Django (nombres de URL, ubicación de plantillas, migraciones)
- [ ] Si se introduce un concepto nuevo, existe un ejemplo mínimo ejecutable que lo contrasta con lo ya conocido
- [ ] Existen pruebas y sus nombres describen el comportamiento
- [ ] El ejemplo no reexplica contenidos que el estudiante ya domina

---

## Prohibiciones

- **Prohibido** introducir o reexplicar los contenidos básicos ya dominados por el estudiante (entornos virtuales, estructura del proyecto, plantillas básicas, CRUD elemental, etc.) como si fueran nuevos.
- **Prohibido** usar técnicas de optimización de producción (decoradores de caché, vistas asíncronas) sin contexto, salvo que el tema del módulo sea precisamente esa técnica.
- **Prohibido** generar guías sin objetivos de aprendizaje aplicables.
- **Prohibido** modificar el contenido de los diagramas Mermaid/PlantUML más allá de la sintaxis (nombres de nodos, relaciones) salvo que sean incoherentes con el texto.
- **Prohibido** colocar lógica de negocio dentro de las funciones de vista.