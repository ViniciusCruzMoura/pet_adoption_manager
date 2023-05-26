import os
from pathlib import Path

CONFIG_DEBUG = os.getenv("CONFIG_DEBUG", default="True")
CONFIG_SECRET_KEY = os.getenv("CONFIG_SECRET_KEY", default="django-insecure-#gs@=g+_dtk$xo@6v^q^+hmr6ev=1s2bsh_neyn7a&ti!8y67e")
CONFIG_ALLOWED_HOSTS = os.getenv("CONFIG_ALLOWED_HOSTS", default="*")
CONFIG_CSRF_TRUSTED_ORIGINS = os.getenv('CONFIG_CSRF_TRUSTED_ORIGINS', default='https://127.0.0.1')
CONFIG_POSTGRESQL_NAME = os.getenv("CONFIG_POSTGRESQL_NAME", default="public")
CONFIG_POSTGRESQL_USER = os.getenv("CONFIG_POSTGRESQL_USER", default="postgres")
CONFIG_POSTGRESQL_PASSWORD = os.getenv("CONFIG_POSTGRESQL_PASSWORD", default="postgres")
CONFIG_POSTGRESQL_HOST = os.getenv("CONFIG_POSTGRESQL_HOST", default="postgres")
CONFIG_POSTGRESQL_PORT = os.getenv("CONFIG_POSTGRESQL_PORT", default="5432")

for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))

#DATABASE_ROUTERS = ['core.DatabaseRoutes.DatabaseRoutes']
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = CONFIG_SECRET_KEY
DEBUG = CONFIG_DEBUG
ALLOWED_HOSTS = [CONFIG_ALLOWED_HOSTS]
CSRF_TRUSTED_ORIGINS = [CONFIG_CSRF_TRUSTED_ORIGINS]
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'management_system.apps.ManagementSystemConfig',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'core.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'core.wsgi.application'
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': f'{CONFIG_POSTGRESQL_NAME}',
        'USER': f'{CONFIG_POSTGRESQL_USER}',
        'PASSWORD': f'{CONFIG_POSTGRESQL_PASSWORD}',
        'HOST': f'{CONFIG_POSTGRESQL_HOST}',
        'PORT': f'{CONFIG_POSTGRESQL_PORT}',
    },
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'static')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LANGUAGE_CODE = 'pt-br'
USE_I18N = True
TIME_ZONE = 'America/Campo_Grande'
USE_TZ = True
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')