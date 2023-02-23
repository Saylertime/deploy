import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-w-ft5*b7g4psjz(tg_3)_d^nxf@-dsqfi@37tcpr$dy(sgib+$'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'diplomadb',
        'USER': 'alexeyglinkin',
        'PASSWORD': 'Glin33A4',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}