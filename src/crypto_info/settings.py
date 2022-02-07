"""Django settings for crypto_info project."""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

SECRET_KEY = os.getenv('BACKEND_SECRET_KEY', default='django-insecure-yn7v9)crlc_fan&4)rqz4j#-m%67tpq6=-0-tw2#c#n(w2xb-w')
DEBUG = os.getenv('DEBUG', default='True').upper() in ('TRUE', '1', 'YES')
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', default='*').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    'crypto.apps.CryptoConfig',

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

ROOT_URLCONF = 'crypto_info.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'src/templates']
        ,
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

WSGI_APPLICATION = 'crypto_info.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_DB', default='crypto_info_db'),
        'USER': os.getenv('POSTGRES_USER', default='crypto_info_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='crypto_info_password'),
        'HOST': os.getenv('POSTGRES_HOST', default='postgresql'),
        'PORT': int(os.getenv('POSTGRES_PORT', default=5432)),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CELERY configuration
RABBITMQ_USER = os.getenv('RABBITMQ_USER', default='guest')
RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD', default='guest')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', default='rabbitmq')
RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', default=5672))
RABBITMQ_VHOST = os.getenv('RABBITMQ_VHOST', default='/')

CELERY_BROKER_URL = 'amqp://{user}:{password}@{host}:{port}/{vhost}'.format(
    user=RABBITMQ_USER, password=RABBITMQ_PASSWORD, host=RABBITMQ_HOST, port=RABBITMQ_PORT, vhost=RABBITMQ_VHOST
)
CELERY_TIMEZONE = 'UTC'

CELERY_IMPORTS = ['crypto.tasks']

ALPHAVANTAGE_EXCHANGE = {
    'API_KEY': os.getenv('ALPHAVANTAGE_EXCHANGE_API_KEY'),
    'RATE_URL': os.getenv('ALPHAVANTAGE_EXCHANGE_RATE_URL', default='https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}'),
}
