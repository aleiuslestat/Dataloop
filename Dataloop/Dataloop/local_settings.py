import os 
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'NAME'    : 'postgres',
        'USER'    : 'postgres',
        'PASSWORD': 'postgres',
#         'HOST'   : 'db_postgres',
         'HOST'   : 'localhost',
        'PORT'    : 5432,
    }
}
