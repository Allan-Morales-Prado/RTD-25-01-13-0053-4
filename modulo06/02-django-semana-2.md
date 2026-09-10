# Guía de Django - Desde Cero hasta Autenticación

## 📚 Índice
1. [Introducción a Django](#introducción-a-django)
2. [Creación de un Proyecto Django](#creación-de-un-proyecto-django)
3. [Estructura de Carpetas](#estructura-de-carpetas-de-un-proyecto-django)
4. [MVC vs MTV](#mvc-vs-mtv)
5. [Templates y Contenido Dinámico](#templates-y-contenido-dinámico)
6. [Herencia de Plantillas](#herencia-de-plantillas)
7. [Iteradores y Control de Flujo](#iteradores-y-control-de-flujo)
8. [Archivos Estáticos](#archivos-estáticos-en-django)
9. [Modelos de Datos](#modelos-de-datos-en-django)
10. [Formularios en Django](#formularios-en-django)
11. [Autenticación y Autorización](#autenticación-y-autorización)

---

## Introducción a Django

### ¿Qué es Django?
Django es un framework web de alto nivel escrito en Python que fomenta el desarrollo rápido y el diseño limpio y pragmático.

### Patrón de Diseño
Django utiliza el patrón **MVT** (Model-View-Template), que es una variación del clásico **MVC**:

| MVC | MVT (Django) |
|-----|--------------|
| Model | Model |
| View | Template |
| Controller | View |

### Componentes Principales
- **Modelo (M)**: Gestiona la capa de datos y la lógica de negocio
- **Vista (V)**: Maneja las peticiones HTTP y la lógica de la aplicación
- **Template (T)**: Gestiona la presentación y la interfaz de usuario

---

## Creación de un Proyecto Django

### Analogía Conceptual
- **Proyecto**: Es la casa completa (todo el sitio web)
- **Aplicación**: Cada habitación de la casa (funcionalidades específicas)

### Comandos Básicos con `django-admin`

```bash
# Crear un nuevo proyecto
django-admin startproject nombre-proyecto

# Crear una nueva aplicación
python manage.py startapp nombre-app
```

### Comandos de `manage.py`

```bash
# Iniciar servidor de desarrollo
python manage.py runserver

# Crear un superusuario
python manage.py createsuperuser

# Generar migraciones
python manage.py makemigrations

# Ejecutar migraciones
python manage.py migrate
```

### Estructura de un Proyecto Django
```
mi_proyecto/
├── manage.py
├── mi_proyecto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── aplicaciones/
```

---

## Estructura de Carpetas de un Proyecto Django

### Archivo `settings.py`
Configuración principal del proyecto:
- `INSTALLED_APPS`: Aplicaciones instaladas
- `DATABASES`: Configuración de base de datos
- `TEMPLATES`: Configuración de plantillas
- `STATIC_URL`: URL para archivos estáticos
- `MEDIA_URL`: URL para archivos de medios

### Archivo `urls.py`
Define las rutas URL del proyecto:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('producto/<int:id>/', views.producto, name='producto'),
]
```

### Archivo `views.py`
Contiene la lógica de las vistas:

```python
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {'nombre': 'Mundo'})
```

### Archivo `models.py`
Define la estructura de la base de datos:

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
```

---

## MVC vs MTV

### Comparativa Detallada

| Componente | MVC Tradicional | MVT (Django) |
|------------|-----------------|--------------|
| **Modelo** | Datos y lógica de negocio | Datos y lógica de negocio |
| **Vista** | Presentación (HTML) | Lógica de la aplicación |
| **Controlador** | Maneja entradas y actualiza modelo | **No existe** |
| **Template** | **No existe** | Presentación (HTML) |

### Flujo de Trabajo en Django (MVT)
1. El usuario hace una petición (URL)
2. La **Vista** procesa la petición
3. La Vista interactúa con el **Modelo** si es necesario
4. La Vista pasa datos al **Template**
5. El **Template** genera el HTML final
6. Se envía la respuesta al usuario

### Ejemplo Práctico
```python
# Modelo (models.py)
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

# Vista (views.py)
def listar_categorias(request):
    categorias = Categoria.objects.all()  # Interactúa con el Modelo
    return render(request, 'categorias.html', {'categorias': categorias})  # Pasa al Template

# Template (categorias.html)
<ul>
{% for categoria in categorias %}
    <li>{{ categoria.nombre }}</li>
{% endfor %}
</ul>
```

---

## Templates y Contenido Dinámico

### Configuración de Templates
En `settings.py`:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Directorio de templates
        'APP_DIRS': True,
        # ...
    }
]
```

### Sintaxis Básica de Templates

#### Variables
```html
<h1>Hola {{ nombre }}</h1>
<p>Edad: {{ edad }}</p>
```

#### Filtros
```html
<p>{{ texto|upper }}</p>        <!-- Mayúsculas -->
<p>{{ texto|lower }}</p>        <!-- Minúsculas -->
<p>{{ texto|length }}</p>        <!-- Longitud -->
<p>{{ fecha|date:"d/m/Y" }}</p>  <!-- Formato de fecha -->
```

### Contexto en Vistas
```python
def contenido_dinamico(request):
    categorias = ['Python', 'Django', 'HTML', 'CSS', 'JavaScript']
    usuario = {
        'nombre': 'Juan',
        'email': 'juan@email.com'
    }
    context = {
        'categorias': categorias,
        'usuario': usuario
    }
    return render(request, 'dinamico.html', context)
```

### Renderizado en Template
```html
<h1>Categorías</h1>
<ul>
{% for categoria in categorias %}
    <li>{{ categoria }}</li>
{% endfor %}
</ul>

<p>Nombre: {{ usuario.nombre }}</p>
<p>Email: {{ usuario.email }}</p>
```

---

## Herencia de Plantillas

### Plantilla Base (`base.html`)
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Mi Sitio{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'styles.css' %}">
</head>
<body>
    <header>
        <h1>Mi Sitio Web</h1>
        {% include "navbar.html" %}
    </header>
    
    <main>
        {% block content %}
        <!-- Contenido específico -->
        {% endblock %}
    </main>
    
    <footer>
        {% include "footer.html" %}
    </footer>
</body>
</html>
```

### Plantilla Hija (`hijo.html`)
```html
{% extends "base.html" %}

{% block title %}Página de Productos{% endblock %}

{% block content %}
<h2>Lista de Productos</h2>
<ul>
    {% for producto in productos %}
        <li>{{ producto.nombre }} - ${{ producto.precio }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

### Plantillas Incrustadas con `{% include %}`
```html
<!-- navbar.html -->
<nav>
    <ul>
        <li><a href="/">Inicio</a></li>
        <li><a href="/productos">Productos</a></li>
        <li><a href="/contacto">Contacto</a></li>
    </ul>
</nav>
```

---

## Iteradores y Control de Flujo

### Estructuras de Control

#### For Loop
```html
<ul>
    {% for curso in cursos %}
        <li>{{ curso }}</li>
    {% empty %}
        <li>No hay cursos disponibles</li>
    {% endfor %}
</ul>
```

#### For con Índice
```html
{% for item in lista %}
    <p>{{ forloop.counter }}. {{ item }}</p>
    <p>Primero: {{ forloop.first }}</p>
    <p>Último: {{ forloop.last }}</p>
{% endfor %}
```

#### Condicionales
```html
{% if usuario %}
    <p>Bienvenido, {{ usuario.nombre }}</p>
{% elif invitado %}
    <p>Bienvenido, invitado</p>
{% else %}
    <p>Por favor, inicia sesión</p>
{% endif %}
```

### Acceso a Datos Anidados
```html
<!-- Lista de diccionarios -->
{% for producto in productos %}
    <p>{{ producto.nombre }} - {{ producto.precio }}</p>
    <p>Categoría: {{ producto.categoria.nombre }}</p>
{% endfor %}

<!-- Diccionario de listas -->
{% for categoria, items in categorias.items %}
    <h3>{{ categoria }}</h3>
    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
{% endfor %}
```

### Filtros Útiles
```html
{{ valor|default:"Sin valor" }}
{{ texto|truncatewords:5 }}
{{ fecha|timesince }}
{{ lista|join:", " }}
{{ numero|add:"5" }}
```

---

## Archivos Estáticos en Django

### Configuración
En `settings.py`:
```python
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"
```

### Estructura de Directorios
```
mi_proyecto/
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   └── images/
│       └── logo.png
└── templates/
```

### Cargar Archivos Estáticos en Templates
```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```

### Archivo CSS de Ejemplo
```css
/* static/css/styles.css */
h1 {
    color: #2c3e50;
    font-family: 'Arial', sans-serif;
}

nav {
    background-color: #3498db;
    padding: 1rem;
}

.btn-primary {
    background-color: #2980b9;
    color: white;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 4px;
}
```

---

## Modelos de Datos en Django

### Creación de Modelos
En `models.py`:
```python
from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
```

### Tipos de Campos Comunes

| Campo | Descripción |
|-------|-------------|
| `CharField` | Texto corto |
| `TextField` | Texto largo |
| `IntegerField` | Números enteros |
| `DecimalField` | Números decimales |
| `BooleanField` | Verdadero/Falso |
| `DateTimeField` | Fecha y hora |
| `ForeignKey` | Relación muchos-a-uno |
| `ManyToManyField` | Relación muchos-a-muchos |

### Configuración de Base de Datos (PostgreSQL)
En `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nombre_bd',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Migraciones
```bash
# Crear migraciones basadas en cambios de modelos
python manage.py makemigrations

# Aplicar migraciones a la base de datos
python manage.py migrate

# Ver SQL que se ejecutará
python manage.py sqlmigrate app_name 0001
```

### Validaciones Personalizadas
```python
from django.core.exceptions import ValidationError

class Article(models.Model):
    # ... campos ...
    
    def clean(self):
        if not self.name:
            raise ValidationError("El nombre es obligatorio.")
        
        if self.price <= 0:
            raise ValidationError("El precio debe ser mayor que 0.")
        
        if len(self.name) < 3:
            raise ValidationError("El nombre debe tener al menos 3 caracteres.")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
```

### Consultas Básicas con ORM
```python
# Obtener todos los registros
articulos = Article.objects.all()

# Filtrar
articulos = Article.objects.filter(name__icontains='Python')

# Obtener un solo registro
articulo = Article.objects.get(id=1)

# Crear un nuevo registro
articulo = Article(name='Nuevo', price=100)
articulo.save()

# Actualizar
articulo.price = 150
articulo.save()

# Eliminar
articulo.delete()
```

---

## Formularios en Django

### ModelForm
Crea formularios automáticamente a partir de modelos:

```python
# forms.py
from django import forms
from .models import Article

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'address', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nombre del Artículo',
            'price': 'Precio ($)',
        }
```

### Vista con Formulario
```python
# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ArticuloForm

def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Artículo creado exitosamente')
            return redirect('lista_articulos')
        else:
            messages.error(request, 'Error al crear el artículo')
    else:
        form = ArticuloForm()
    
    return render(request, 'crear_articulo.html', {'form': form})
```

### Template del Formulario
```html
<form method="POST" action="">
    {% csrf_token %}
    
    <!-- Mostrar mensajes -->
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
    
    <!-- Renderizar campos -->
    <div class="form-group">
        {{ form.name.label_tag }}
        {{ form.name }}
        {{ form.name.errors }}
    </div>
    
    <div class="form-group">
        {{ form.price.label_tag }}
        {{ form.price }}
        {{ form.price.errors }}
    </div>
    
    <button type="submit" class="btn btn-primary">Guardar</button>
</form>
```

### ClassForm (Manual)
```python
# forms.py
from django import forms

class ContactForm(forms.Form):
    customer_email = forms.EmailField(label='Correo')
    customer_name = forms.CharField(
        max_length=64,
        required=False,
        label='Nombre'
    )
    message = forms.CharField(
        widget=forms.Textarea,
        label='Mensaje'
    )
    
    def clean_customer_email(self):
        email = self.cleaned_data['customer_email']
        if not '@' in email:
            raise forms.ValidationError('Email inválido')
        return email
```

### CSRF Protection
Django incluye protección CSRF automática. En los formularios, usar:
```html
<form method="POST">
    {% csrf_token %}
    <!-- Campos del formulario -->
</form>
```

### Inline Formsets (Formularios Relacionados)
```python
# views.py
from django.forms import inlineformset_factory

# Modelos relacionados
class Cliente(models.Model):
    name = models.CharField(max_length=30)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    text = models.TextField()

# En la vista
PedidoInlineFormset = inlineformset_factory(
    parent_model=Cliente,
    model=Pedido,
    fields=['text'],
    extra=1
)

def create_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        formset = PedidoInlineFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            cliente = form.save()
            formset.instance = cliente
            formset.save()
            return redirect('success')
    else:
        form = ClienteForm()
        formset = PedidoInlineFormset()
    
    return render(request, 'create_client.html', {
        'form': form,
        'formset': formset
    })
```

### Mensajes de Error Personalizados
En `settings.py`:
```python
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.WARNING: 'warning',
    messages.ERROR: 'error',
    messages.SUCCESS: 'success',
}
```

---

## Autenticación y Autorización

### Modelo de Autenticación de Django
Django proporciona un sistema completo de autenticación que incluye:
- **User**: Modelo de usuario por defecto
- **Authentication**: Verificación de credenciales
- **Authorization**: Control de permisos
- **Sessions**: Manejo de sesiones

### Configuración Inicial
```bash
# Crear superusuario
python manage.py createsuperuser

# Migrar para crear tablas de autenticación
python manage.py migrate
```

### Registro de Usuarios con UserCreationForm
```python
# views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Usuario {user.username} creado exitosamente')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
```

### Template de Registro
```html
<h1>Registro de Usuario</h1>
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Registrar</button>
</form>
```

### Login Personalizado
```python
# views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
```

### Login por Defecto de Django
```python
# urls.py
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
```

### Protección de Vistas
```python
# Decorador para vistas basadas en funciones
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def perfil(request):
    return render(request, 'perfil.html')

# Mixin para vistas basadas en clases
from django.contrib.auth.mixins import LoginRequiredMixin

class PerfilView(LoginRequiredMixin, TemplateView):
    template_name = 'perfil.html'
    login_url = 'login'
```

### Control de Acceso por Permisos
```python
# Decorador con permisos
from django.contrib.auth.decorators import permission_required

@permission_required('app.puede_editar', login_url='login')
def editar(request):
    return render(request, 'editar.html')

# En el template
{% if perms.app.puede_editar %}
    <a href="/editar/">Editar</a>
{% endif %}
```

### Modelo User y Relaciones
```python
# Extender el modelo User
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'Perfil de {self.user.username}'

# Señal para crear Perfil automáticamente
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def guardar_perfil(sender, instance, **kwargs):
    instance.perfil.save()
```

### Grupos y Permisos
```python
# Crear grupos con permisos
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# Crear grupo
grupo_editores, created = Group.objects.get_or_create(name='Editores')

# Obtener permisos
content_type = ContentType.objects.get_for_model(Article)
permiso_editar = Permission.objects.get(
    codename='change_article',
    content_type=content_type
)

# Asignar permiso al grupo
grupo_editores.permissions.add(permiso_editar)

# Asignar usuario al grupo
usuario.groups.add(grupo_editores)
```

### Autenticación con Email
```python
# settings.py
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Vista de login personalizada con email
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    
    def form_valid(self, form):
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        
        # Buscar usuario por email
        try:
            user = User.objects.get(email=email)
            username = user.username
        except User.DoesNotExist:
            username = email
        
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('home')
        
        return super().form_invalid(form)
```

---

## 🔑 Comandos Esenciales Resumen

| Comando | Descripción |
|---------|-------------|
| `django-admin startproject nombre` | Crear nuevo proyecto |
| `python manage.py startapp nombre` | Crear nueva aplicación |
| `python manage.py runserver` | Iniciar servidor de desarrollo |
| `python manage.py makemigrations` | Crear migraciones |
| `python manage.py migrate` | Ejecutar migraciones |
| `python manage.py createsuperuser` | Crear usuario administrador |
| `python manage.py shell` | Abrir consola interactiva |
| `python manage.py test` | Ejecutar pruebas |

## 🎯 Buenas Prácticas

1. **Siempre usar entornos virtuales** (`venv` o `conda`)
2. **Mantener SECRET_KEY fuera del código** (usar variables de entorno)
3. **Configurar DEBUG=False en producción**
4. **Organizar aplicaciones por funcionalidad**
5. **Usar nombres de templates en plural**
6. **Implementar herencia de plantillas**
7. **Validar datos en formularios y modelos**
8. **Proteger vistas con `@login_required`**
9. **Usar `{% csrf_token %}` en todos los POST**
10. **Mantener el código modular y reutilizable**

## 📖 Recursos Adicionales

- [Documentación Oficial de Django](https://docs.djangoproject.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [MDN Django Tutorial](https://developer.mozilla.org/es/docs/Learn/Server-side/Django)
- [Django REST Framework](https://www.django-rest-framework.org/)