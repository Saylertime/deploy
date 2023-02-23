import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']


SECRET_KEY = 'django-insecure-w-sfdsds332_d^nxf@-dsqfi@37tcpr$dy(sgib+$'




STATICFILES_DIRS = ((os.path.join(BASE_DIR, 'static')),)