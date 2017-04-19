import os
import sys

from .core import get_env_param_str

SETTINGS_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(SETTINGS_DIR)

SERVER_ROLE_DEV = 'dev'
SERVER_ROLE_PROD = 'prod'

SERVER_ROLE = get_env_param_str('SERVER_ROLE')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x(i8w9-a^ms56)%^y%37$5l8^&3542oc67uf8fvam&9+^entt3'



ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'wsgi.application'


SMS_HANDLER = 'sms.handlers.smscru.SMSHandler'


if SERVER_ROLE == SERVER_ROLE_DEV:
    from .settings_dev import *
elif SERVER_ROLE == SERVER_ROLE_PROD:
    from .settings_prod import *
else:
    raise Exception(u'Incorrect SERVER_ROLE')


from .s_log import *


if len(sys.argv) >= 2 and sys.argv[1] == 'test':
    from .settings_test import *