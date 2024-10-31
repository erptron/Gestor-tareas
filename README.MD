# Proyecto Django con PostgreSQL

Este proyecto utiliza Django en un entorno Windows y se conecta a una base de datos PostgreSQL. 
Aquí puedes encontrar los comandos y pasos necesarios para configurar y manejar las migraciones de tu aplicación.

## Requisitos Previos

- Python instalado
- Django instalado (`pip install django`)
- PostgreSQL instalado y configurado (`pip install psycopg2`)

## Comandos y Pasos

### Configurar Entorno virtual

#### Crear 

```bash
python -m venv venv
```

#### Correr

```bash
.\venv\Scripts\activate
```
### Crear un Proyecto Django

```bash
django-admin startproject django-pruebas
cd django-pruebas
```

### Configurar PostgreSQL en settings.py
 
```python
    DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'django_pruebas',
            'USER': 'postgres',
            'PASSWORD': 'cocodin@2024',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
```

### Crear una Nueva Aplicación

```bash
python manage.py startapp empresas
```

### Registrar la Aplicación
- Añade 'empresas' en INSTALLED_APPS en settings.py:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'empresas',
]
```

### Definir Modelos en models.py
Ejemplo de modelo Empresa:

```python
from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    identificador_fiscal = models.CharField(max_length=50, unique=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
```

### Crear y Aplicar Migraciones
- crear migraciones:

```bash
python manage.py makemigrations empresas
```

- aplicar migraciones:

```bash
python manage.py migrate
```

### Crear un Superusuario
- acceder al panel de administración:

```bash
python manage.py createsuperuser
```

### Ejecutar el Servidor de Desarrollo

```bash
python manage.py runserver
```

### Configurar Rutas (URLs)
- Agrega urls a tu aplicación en empresas/urls.py (crea el archivo si no existe):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### asegúrate de incluir esas urls en PRUEBAS/urls.py:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empresas/', include('empresas.urls')),
]
```

### Configuración de Archivos Estáticos
- Si trabajas con archivos estáticos (CSS, JavaScript, imágenes), asegúrate de configurarlos correctamente en tu settings.py bajo la configuración STATIC_URL y STATICFILES_DIRS.

```markdown
empresas/
├── static/
│   └── empresas/
│       ├── css/
│       │   └── styles.css
│       ├── js/
│       │   └── scripts.js
└── templates/
    └── empresas/
        └── lista_empresas.html
```

#### settings.py

```python
INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    ...
]
```

#### Ruta base para archivos estáticos
```python
STATIC_URL = '/static/'
```

#### Opcional, para desarrollo
```python
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'empresas/static'),
]
```

Usa {% load static %} al principio de tu archivo lista_empresas.html 
para asegurarte de que los archivos estáticos sean correctamente cargados 
a través del motor de plantillas de Django.

### Configuración del ALLOWED_HOSTS
- Al alcanzar otros entornos como producción, recuerda actualizar la variable ALLOWED_HOSTS con el dominio o las IPs permitidas:

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

### Librerias instaladas

#### almacenar dependencias del proyecto
```bash
 pip freeze > requirements.txt
```
#### instalar dependencias del proyecto
```bash
 pip install -r requirements.txt
```

## BD remota DigitalOcean

DB_ENGINE=django.db.backends.postgresql
DB_NAME=django_pruebas
DB_USER=postgres
DB_PASSWORD=Vay1234..
DB_HOST=157.230.110.33
DB_PORT=5432