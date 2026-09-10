# Configuración aislada de variables de entorno: el archivo `.env`
*Una medida de seguridad para publicar tus proyectos*

## Pasos previos
- Crear un repositorio remoto
- Clonar el repositorio creado
- Modificar el archivo `.gitignore` para el stack que se va a utilizar
- Crearun entorno virtual con un nombre convencional (ej: *venv*)
- Crear un proyecto en el repositorio

## `.env` para un proyecto Django
Se requiere la instalación de `django-environ` para utilizarlo en `settings.py`

```cmd
py -m pip install django-environ
```

A continuación, utilizaremos Django para crear un valor nuevo que será nuestra nueva clave secreta:

```cmd
py manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())" > .env
```

El comando anterior creará un archivo llamado `.env` en el directorio actual e ingresará el valor de la nueva clave secreta en su interior.

A continuación, ingresamos al archivo `.env` y lo editamos de este modo:

```env
# .env
DEBUG=on
SECRET_KEY=tu_clave_secreta
```

>[!NOTE]
>`DEBUG` y `SECRET_KEY` son constantes del archivo `settings.py` de tu proyecto Django
>Los nombres de las constantes en ambos archivos deben ser idénticos
>La sintáxis es simple: `NOMBRE_CONSTANTE=valor` (sin espacios)

>[!IMPORTANT]
>Utiliza este método para aislar las configuraciones sensibles de cada entorno con el que trabajes: desarrollo, pruebas y producción
>Este tipo de archivos no es versionable y por lo tanto, intransferible

El archivo `.env` está listo para utilizarlo en `settings.py`:

```python
# settings.py

import environ
import os
# ...
env = environ.Env(
    DEBUG=(bool, False)
)
# ...
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# ...
SECRET_KEY = env('SECRET_KEY')
# ...
DEBUG = env('DEBUG')
# ...
```

Hecho esto, solo resta probar que el proyecto funcione:
- Ten activado el entorno para el proyecto
- Levanta el servidor local

Si todo funciona normal, entonces la lección habrá terminado

### Consideraciones

`python-dotenv` es una alternativa que tiene menos alcance para proyectos Django, prefiere `django-environ` en su lugar

### Más información
- https://djangowaves.com/gitignore-for-a-django-project/
- https://django-environ.readthedocs.io/en/latest/install.html