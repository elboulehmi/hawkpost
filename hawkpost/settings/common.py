"""
Django settings for hawkpost project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'timezone_field',
    'axes',
    'humans',
    'boxes',
    'pages',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hawkpost.middleware.TimezoneMiddleware',
    'hawkpost.middleware.LanguageMiddleware',
]

ROOT_URLCONF = 'hawkpost.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + "/templates/"],
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

WSGI_APPLICATION = 'hawkpost.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Authentication settings

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


# For Django AllAuth

SITE_ID = 1


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
            ('en-us', _('English')),
            ('pt-pt', _('Portuguese'))
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media Files

MEDIA_URL = '/media/'

# Custom User Model

AUTH_USER_MODEL = 'humans.User'


# AllAUth Config
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True
LOGIN_REDIRECT_URL = reverse_lazy("boxes_list")
LOGIN_URL = reverse_lazy("account_login")

ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

ACCOUNT_LOGOUT_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': ['user:email']
    }
}

# Authentication Limits Config (AXES)
AXES_LOGIN_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1  # hour
AXES_USERNAME_FORM_FIELD = 'login'
AXES_DISABLE_SUCCESS_ACCESS_LOG = True

# Email Settings
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")

# Celerey Settings
CELERY_BROKER_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

# SITE DOMAIN
SITE_DOMAIN = os.environ.get("SITE_DOMAIN")

# LOCALE_PATH for translations
# https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-LOCALE_PATHS
LOCALE_PATHS = ['locale']


# File Uploads
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640  # bytes == 15Mb

# Data about the instance
SUPPORT_NAME = os.environ.get("SUPPORT_NAME")
SUPPORT_EMAIL = os.environ.get("SUPPORT_EMAIL")
INSTANCE_DESCRIPTION = os.environ.get("INSTANCE_DESCRIPTION", "")
VERSION = "1.3.0"
