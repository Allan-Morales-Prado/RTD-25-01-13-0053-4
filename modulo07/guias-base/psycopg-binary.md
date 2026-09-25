# `psycopg[binary]` para conectar Django con PostgreSQL

>[!NOTE]
>Es preciso gestionar las bases de datos y entornos virtuales creados

La siguiente es una plantilla SQL para la creación de bases de datos PostgreSQL:

```sql
-- Database: nombre_base_de_datos

-- DROP DATABASE IF EXISTS nombre_base_de_datos;

CREATE DATABASE sep24_db
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Spain.1252'
    LC_CTYPE = 'Spanish_Spain.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
```

La siguiente es una lista de nombres de bases de datos configuradas para los proyectos de este módulo:

- sep10_p1db
- sep10_p2db

Asegúrate de crear archivos de entorno para cada proyecto si vas a probar su funcionamiento incluyendo la conexión con PostgreSQL:

```python
# settings.py

import environ
import os
# ...
env = environ.Env(
    DEBUG=(bool, False)
)
# ...
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# ...
SECRET_KEY = env('SECRET_KEY')
# ...
DEBUG = env('DEBUG')
# ...
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}
# ...
```

```env
# .env
DEBUG=on
SECRET_KEY=tu_clave_secreta
DB_NAME=nombre_base_de_datos
DB_USER=postgres
DB_PASS=tu_clave_de_usuario
DB_HOST=localhost
DB_PORT=5432
```