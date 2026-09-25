# Modelos de datos y el ORM de Django
## Aplicaciones Django preinstaladas (Parte I y II)

---

# Parte I: Aplicaciones Django Preinstaladas

## ¿Qué aprenderás en esta sesión?

Reconocer las aplicaciones preinstaladas de Django y su utilidad como apoyo al desarrollo.

**Objetivo general del curso:**
Implementar una aplicación web MVC que realiza operaciones CRUD en la base de datos utilizando los componentes del framework Django para dar solución a un problema.

**Unidades:**
- Unidad 1: Django y su integración con bases de datos
- Unidad 2: Modelos de datos y el ORM de Django — *Aplicaciones Django preinstaladas parte 1*
- Unidad 3: Proyecto

---

## Introducción a las Aplicaciones Preinstaladas

Django, por defecto, trae una serie de aplicaciones preinstaladas que nos entregan gran parte de la funcionalidad del framework. Podemos ver estas aplicaciones en el archivo `settings.py`:

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

---

## django.contrib.admin

Este es otro componente que hace a Django tremendamente competitivo frente a otros frameworks. Gracias a este administrador prefabricado, cada vez que agreguemos un nuevo modelo a la App, podremos listar, agregar, editar y eliminar registros del mismo a través de una interfaz gráfica para realizar pruebas tempranas del mismo, solo agregando unas líneas en la configuración del admin.

Para acceder a este administrador, cuando ejecutamos el proyecto, Django nos disponibiliza la siguiente URL:

```
http://127.0.0.1:8000/admin/
```

### Registro de modelos en el admin

En la siguiente imagen, podemos ver la forma de agregar nuestros modelos al admin. En este caso, importamos el objeto `Admin` y nuestro modelo, luego registramos el modelo. Esto lo realizamos en el archivo `admin.py` que se encuentra en la raíz del directorio de cada aplicación.

```python
from django.contrib import admin
from myproject.myapp.models import Author

admin.site.register(Author)
```

*Fuente: docs.djangoproject.com*

---

## django.contrib.auth

- Esta aplicación maneja todo lo relacionado con la seguridad de un sitio generado con Django.
- Tiene un modelo de usuario genérico llamado `User` con los campos más usuales, el cual se puede extender de ser necesario.
- También nos entrega herramientas de autenticación, manejo de passwords, sesiones de usuario, grupos y permisos.

### Ejemplo: Creación de usuarios

```python
>>> from django.contrib.auth.models import User
>>> u = User.objects.get(username='john')
>>> u.set_password('new password')
>>> u.save()
```

*Fuente: docs.djangoproject.com*

### Ejemplo: Autenticación de usuarios

```python
from django.contrib.auth import authenticate

user = authenticate(username='john', password='secret')
if user is not None:
    # A backend authenticated the credentials
else:
    # No backend authenticated the credentials
```

*Fuente: docs.djangoproject.com*

---

## django.contrib.contenttypes

- Esta aplicación lleva registro de todos los modelos instalados o creados en tu proyecto Django. Provee una interfaz genérica de alto nivel para trabajar con estos modelos.
- Cada instancia de `ContentType` tiene métodos que permiten obtener una instancia del modelo representado en `ContentTypes` o recuperar objetos de ese modelo.

### Ejemplo de contentTypes

En la imagen, tenemos un ejemplo donde recuperamos el modelo `user` de la aplicación "auth" a partir del registro contenido en `ContentTypes`. Entonces, para utilizarlo llamamos el método `model_class()` y esto nos entrega la clase del modelo.

```python
>>> from django.contrib.contenttypes.models import ContentType
>>> user_type = ContentType.objects.get(app_label='auth', model='user')
>>> user_type
<ContentType: user>
```

*Fuente: docs.djangoproject.com*

---

## django.contrib.sessions

Las sesiones son el mecanismo utilizado por Django para mantener registro del estado entre el sitio y un browser (navegador) particular.

Las sesiones permiten almacenar datos arbitrarios por browser y mantiene estos datos disponibles para el sitio cuando el browser se conecta.

### Ejemplo de uso de sesiones

En la imagen, tenemos un ejemplo donde tomamos valores en una vista, recuperados de la variable `request`.

Aquí vemos que podemos leer y guardar información en forma de diccionario, con una clave y un valor.

```python
def post_comment(request, new_comment):
    if request.session.get('has_commented', False):
        return HttpResponse("You've already commented.")
    c = comments.Comment(comment=new_comment)
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')
```

---

## django.contrib.messages

- Es bastante común en las aplicaciones web que necesites mostrar una notificación una sola vez al usuario, después de procesar un formato o algún otro tipo de input.
- Para esto Django provee un soporte completo de mensajes basado en cookies y sesiones, tanto para usuarios anónimos como autenticados.
- El framework de mensajes te permite almacenar temporalmente mensajes de un uso. Todos los mensajes son clasificados con algún nivel determinado de prioridad (como información, error, advertencia).

### Guardando y recuperando un mensaje

```python
from django.contrib import messages
messages.add_message(request, messages.INFO, 'Hello world.')

from django.contrib.messages import get_messages

storage = get_messages(request)
for message in storage:
    do_something_with_the_message(message)
```

*Fuente: docs.djangoproject.com*

---

## django.contrib.staticfiles

Es una colección de archivos estáticos de cada una de las aplicaciones que componen el proyecto en una sola ubicación que puede ser configurada fácilmente en producción.

Posee una serie de variables de configuración:

- `STATIC_ROOT`
- `STATIC_URL`
- `STATICFILES_DIRS`
- `STATICFILES_STORAGE`
- `STATICFILES_FINDERS`

### Configuración de STATICFILES_DIRS

```python
STATICFILES_DIRS = [
    "/home/special.polls.com/polls/static",
    "/home/polls.com/polls/static",
    "/opt/webfiles/common",
]
```

*Fuente: docs.djangoproject.com*

---

## Ejercicio: Personalización de una Aplicación Django Preinstalada

Cada estudiante seleccionará una de las aplicaciones Django preinstaladas (por ejemplo, `django.contrib.admin`, `django.contrib.auth`, etc.) para explorar. La tarea consiste en investigar, en la web o en textos, una funcionalidad principal de la aplicación seleccionada y luego determinar una pequeña personalización o mejora que demuestre comprensión práctica de la aplicación en cuestión.

### Tareas:

1. **Selección e Investigación (5-10 min):** Selecciona una aplicación Django preinstalada y realiza una breve investigación sobre sus funcionalidades principales.

2. **Idea de Personalización (5 min):** Basado en tu investigación, conceptualiza una pequeña característica o mejora que podrías implementar. Ejemplos: añadir un campo personalizado a los usuarios de `django.contrib.auth`, crear acciones personalizadas en el panel de administración de `django.contrib.admin`, o configurar mensajes personalizados en `django.contrib.messages`.

3. **Documentación (10-15 min):** Escribe tu idea en el supuesto de un proyecto Django existente o en uno nuevo para esta actividad. La implementación no necesita ser compleja, pero debería ilustrar cómo tu personalización o mejora se integra con la aplicación preinstalada.

### Reflexión (últimos 5 min):

Al final de la actividad, prepara una breve explicación de lo que hiciste, incluyendo:

1. La aplicación Django preinstalada que elegiste y por qué.
2. La personalización o mejora que implementaste.
3. Cómo tu trabajo demuestra una comprensión de la aplicación y su utilidad.

---

## Resumen — Parte I

En esta sesión, nos sumergimos en el mundo de las aplicaciones Django preinstaladas, explorando cómo estas poderosas herramientas integradas pueden ser aprovechadas para acelerar el desarrollo y enriquecer las funcionalidades de nuestras aplicaciones web. Analizamos aplicaciones clave como:

- `django.contrib.admin` para la administración
- `django.contrib.auth` para autenticación y autorización
- `django.contrib.contenttypes` para tipos de contenido dinámicos
- `django.contrib.sessions` para manejo de sesiones
- `django.contrib.messages` para mensajes temporales entre vistas
- `django.contrib.staticfiles` para la gestión de archivos estáticos

---

## Próxima sesión…

**Aplicaciones Django preinstaladas parte 2:** Inspeccionarás el modelo Django para aplicaciones preinstaladas.

---
---

# Parte II: Aplicaciones Django Preinstaladas (Parte 2)

## ¿Qué aprenderás en esta sesión?

Inspeccionar el modelo Django para aplicaciones preinstaladas.

---

## Repaso completo: Aplicaciones Preinstaladas

Las aplicaciones Django preinstaladas son componentes integrados que ofrecen funcionalidades esenciales para el desarrollo web rápido y seguro. Cada aplicación preinstalada sirve a un propósito específico, ayudando en la autenticación, administración, manejo de sesiones, mensajes entre vistas, y más.

### Aplicaciones Claves:

- `django.contrib.admin`
- `django.contrib.auth`
- `django.contrib.contenttypes`
- `django.contrib.sessions`
- `django.contrib.messages`
- `django.contrib.staticfiles`

---

## Usando los modelos de prueba

### Introducción a Modelos de Prueba

Las aplicaciones Django preinstaladas no solo facilitan funcionalidades esenciales para tu proyecto, sino que también vienen equipadas con modelos de prueba que son extremadamente útiles durante el desarrollo y pruebas de tu aplicación.

### Ejemplo: Modelos de django.contrib.auth

La aplicación `django.contrib.auth` es particularmente rica en características, proporcionando modelos listos para usar que son esenciales para cualquier sistema de gestión de usuarios:

- **User:** El modelo central para la autenticación de usuarios, incluyendo campos como `username`, `email`, `password`, entre otros.
- **Group:** Permite agrupar usuarios y asignar permisos a esos grupos, facilitando la gestión de roles y permisos en tu aplicación.

### Ejemplos de Modelos de Prueba (Repaso y Modelos)

- **django.contrib.sessions:** Esta aplicación maneja la sesión de usuarios a través de la web. Utiliza modelos para almacenar información sobre la sesión actual del usuario.

- **django.contrib.contenttypes:** Esta aplicación permite a Django trabajar con los tipos de contenido de forma genérica. Utiliza un modelo para rastrear todos los modelos en su proyecto Django, lo cual es especialmente útil para relaciones genéricas.

- **django.contrib.admin:** Aunque esta aplicación es más conocida por su interfaz de administración, también utiliza modelos internamente para gestionar la información de registro y configuración de los modelos que aparecen en el sitio administrativo.

- **django.contrib.sites:** Permite asociar objetos con sitios web específicos y es útil en proyectos que se ejecutan en múltiples sitios. Utiliza un modelo para almacenar información sobre los diferentes sitios web.

- **django.contrib.redirects:** Utilizado para gestionar redirecciones de URLs en un sitio web de Django. Tiene modelos para almacenar redirecciones de forma dinámica.

- **django.contrib.flatpages:** Proporciona un simple modelo de página plana que puede ser útil para crear y gestionar secciones de contenido estático de tu sitio, como páginas de "Acerca de" o "Políticas de Privacidad".

---

## Ejercicio: Realizar las tareas solicitadas

### Tarea:

1. Si aún no tienes un superusuario en tu proyecto, créalo utilizando el comando `python manage.py createsuperuser` en tu terminal.
2. Accede al sitio de administración de Django con tus credenciales de superusuario.
3. Navega a las secciones de Usuarios (`auth.User`) y Grupos (`auth.Group`).
4. Explora los detalles de algunos usuarios y grupos. Intenta crear un nuevo usuario y asignarlo a un grupo existente.

---

## Cómo usar las aplicaciones preinstaladas

### Aprovechando las Aplicaciones Preinstaladas de Django

Las aplicaciones preinstaladas de Django ofrecen una base sólida y flexible para construir funcionalidades complejas en tus proyectos con mínimo esfuerzo inicial. Estas aplicaciones están diseñadas para ser configuradas y extendidas, permitiéndote adaptarlas a las necesidades específicas de tu proyecto.

### Configuración y Extensión

- **Configuración:** Muchas aplicaciones preinstaladas requieren poca o ninguna configuración para empezar. Por ejemplo, `django.contrib.admin` se activa simplemente añadiéndolo a tu `INSTALLED_APPS` en el archivo `settings.py` de tu proyecto.

- **Extensión:** Puedes extender los modelos y funcionalidades de las aplicaciones preinstaladas. Por ejemplo, el modelo `User` de `django.contrib.auth` puede extenderse para incluir más información de perfil.

### Personalización

- **django.contrib.admin:** Personaliza el sitio de administración para mostrar, editar o filtrar según los campos específicos de tus modelos.
- **django.contrib.auth:** Implementa autenticación personalizada o extiende el modelo `User` para añadir más campos o métodos.

### Ejemplos Prácticos

- **Personalizar el Panel de Administración:** Añade secciones para modelos personalizados, configura listas de filtros y especifica campos de búsqueda.
- **Extendiendo el Modelo User:** Añade campos adicionales al modelo `User` para capturar más información de perfil, como la dirección o número de teléfono.

---

## Ejercicio: Personalizando el Modelo User

### Contexto

En esta actividad podrás profundizar en la comprensión de cómo las aplicaciones preinstaladas pueden ser extendidas y personalizadas para adaptarse a las necesidades específicas de un proyecto. En esta actividad, nos centraremos en extender el modelo `User` de `django.contrib.auth` para incluir información adicional sobre los usuarios.

### Tareas:

1. **Extender el Modelo User:** Crea un modelo `Perfil` que extienda la información del modelo `User` estándar. Este modelo puede incluir campos adicionales como `bio`, `sitio_web` o `telefono`.

2. **Registrar el Modelo en el Panel de Administración:** Registra el nuevo modelo `Perfil` en el panel de administración de Django para poder gestionarlo desde la interfaz de administración.

3. **Sincronizar con la Base de Datos:** Realiza las migraciones necesarias para añadir el modelo `Perfil` a tu base de datos.

4. **Crear y Asociar Perfiles a Usuarios Existentes:** Utiliza el sitio de administración para crear perfiles para algunos de los usuarios existentes, llenando la información adicional proporcionada por el modelo `Perfil`.

---

## Revisando el modelo de las aplicaciones preinstaladas

### Inspección de Modelos Preinstalados

Una de las grandes ventajas de Django es su rico ecosistema de aplicaciones preinstaladas, las cuales ofrecen modelos listos para ser utilizados en proyectos. Comprender la estructura y el funcionamiento de estos modelos es clave para aprovechar al máximo las capacidades del framework.

### ¿Por Qué Inspeccionar los Modelos?

- **Personalización:** Entender los modelos preinstalados te permite extender y personalizar sus funcionalidades de acuerdo a las necesidades específicas de tu proyecto.

- **Mejor Integración:** Al conocer la estructura de los modelos, puedes integrarlos más eficazmente en tu aplicación, relacionándolos con tus propios modelos o modificándolos para obtener un comportamiento deseado.

- **Optimización del Desarrollo:** Usar y adaptar modelos preinstalados puede acelerar significativamente el proceso de desarrollo.

### Herramientas para la Inspección

Django ofrece varias herramientas y comandos que facilitan la inspección de modelos, siendo `python manage.py shell` una de las más útiles para interactuar directamente con los modelos en un entorno de consola.

### Ejemplos de Comandos de Inspección

- Listar todos los usuarios: `User.objects.all()`
- Mostrar todos los grupos: `Group.objects.all()`

Estos comandos te permiten ver los objetos actuales en la base de datos, proporcionando una visión directa de cómo Django maneja los datos de estas aplicaciones preinstaladas.

---

## Actividad Práctica

1. **Abrir la Shell de Django:** Ejecuta `python manage.py shell` en tu terminal para acceder a la interfaz de consola interactiva de Django.

2. **Importar Modelos:** Importa los modelos `User` y `Group` con los comandos:
   ```python
   from django.contrib.auth.models import User, Group
   ```

3. **Explorar Modelos:** Utiliza los comandos `User.objects.all()` para listar todos los usuarios y `Group.objects.all()` para ver todos los grupos. Experimenta con filtros adicionales como `.filter()` y `.exclude()` para obtener consultas más específicas.

---

## Reflexión

Piensa en cómo podrías utilizar estos modelos en tu proyecto. ¿Hay información o relaciones que podrías agregar para hacerlos más útiles para tus necesidades?

Considera las posibilidades de extensión o personalización basadas en tu inspección.

---

## Resumen — Parte II

En esta sesión teórico-práctica, nos centramos en las aplicaciones Django preinstaladas, explorando cómo pueden configurarse y extenderse para mejorar nuestros proyectos. A través de actividades prácticas, los estudiantes aprendieron a manejar los modelos de usuario y grupo en `django.contrib.auth`, descubriendo la flexibilidad de Django para personalizar la gestión de usuarios. También practicamos la inspección de estos modelos utilizando la shell de Django, lo que nos permitió entender mejor su estructura y funcionamiento. Esta sesión reforzó la importancia de las aplicaciones preinstaladas en el desarrollo rápido y seguro de aplicaciones web con Django.

---

## Próxima sesión…

**Proyecto**

---

Adaptado de: *{desafio} latam_ — Academia de talentos digitales*