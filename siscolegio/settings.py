# -*- coding: utf-8 -*-
from os.path import join
import os
import django_heroku

#from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP  # Admin Suit

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_DIRS = (
    join(BASE_DIR,  'templates'),
)

# login required redirect
LOGIN_URL = 'inicio:sislogin'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')ibwzl2hfpzzf6dvj-1&!m7z*-$r@rv1kwad*2p5qqxj$$nt)q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'inicio',
    'sisacademico',
)

# Admin Suit

SUIT_CONFIG = {
    'ADMIN_NAME': 'Administración Colegio Amelia Gallegos'
}


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'siscolegio.urls'

WSGI_APPLICATION = 'siscolegio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'colegio_db_fkrs'),        # El nombre de la base de datos
        'USER': os.getenv('DB_USER', 'colegio_db_fkrs_user'),        # El nombre de usuario de la base de datos
        'PASSWORD': os.getenv('DB_PASSWORD', 'B66zEUfOs3k83A8PQEl0JOfDr83SELAV'),  # La contraseña de la base de datos
        'HOST': os.getenv('DB_HOST', 'dpg-d03tjigdl3ps73c6kp2g-a'),        # La URL de la base de datos en Render
        'PORT': os.getenv('DB_PORT', '5432'),                # El puerto, normalmente 5432
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-me'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),)

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

django_heroku.settings(locals())
