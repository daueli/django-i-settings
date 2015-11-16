"""
Django settings for myApp project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from . import BASE_DIR

#Make Translations dummy for the moment
_ = lambda s: s

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'XXXSECRET'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
SITE_ID=1

# A proposed default
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
#    'compressor',
    'myapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'myapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'myapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'myapp',                      # Or path to database file if using sqlite3.
        'USER': 'myapp',                      # Not used with sqlite3.
        'PASSWORD': 'myapp',                  # Not used with sqlite3.
        'HOST': '',                           # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                           # Set to empty string for default. Not used with sqlite3.
    },
    'local-default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.l.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGES = (
    ('en', _('English')),
    ('de', _('German')),
    ('fr', _('French')),
)

COUNTRIES = (
    'AT',
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Zurich'
USE_TZ = True

USE_I18N = True
USE_L10N = True

#Can be a feature
THIS_PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
LOCALE_PATHS = ( os.path.join(BASE_DIR, 'locale'),
                 os.path.join(THIS_PROJECT_PATH, '../locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = ''
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'myapp_media')
MEDIA_URL = '/user_media/'



STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# ##
# ###
# #### COMPRESSOR - STORAGES
# #### MOVED IN FEATURES
# ###
# ##
# ##COMPRESS_ENABLED = True
# ##HTML_MINIFY = True
# ##
# ##COMPRESS_CSS_HASHING_METHOD = 'content'
# ##COMPRESS_CSS_FILTERS = [
# ##    'compressor.filters.css_default.CssAbsoluteFilter',
# ##    'compressor.filters.cssmin.CSSMinFilter',
# ##]
# ##
# ##COMPRESS_JS_FILTERS = [
# ##    'compressor.filters.jsmin.JSMinFilter',
# ##    'compressor.filters.jsmin.SlimItFilter',
# ##]
# ##
# ##KEEP_COMMENTS_ON_MINIFYING = False
# ##
# ###COMPRESS_URL = "http://compressor-test.s3.amazonaws.com/"
# ###STATIC_URL = COMPRESS_URL
# ##COMPRESS_URL = STATIC_URL
# ##STATICFILES_FINDERS = (
# ##    "django.contrib.staticfiles.finders.FileSystemFinder",
# ##    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
# ##    "compressor.finders.CompressorFinder",
# ##)
# #### END

# ##
# ### MOVED IN FEATURES
# ### REDIS - CACHE
# ##
# ##CACHES = {
# ##    'default': {
# ##        'BACKEND': 'redis_cache.RedisCache',
# ##        'LOCATION': '127.0.0.1:6379',
# ##        'OPTIONS': {
# ##            'DB': 1,
# ##            'PARSER_CLASS': 'redis.connection.HiredisParser',
# ##            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
# ##            'CONNECTION_POOL_CLASS_KWARGS': {
# ##                'max_connections': 20,
# ##                'timeout': 4,
# ##            }
# ##        },
# ##    },
# ##}
# ##

## END

# ### MOVED IN FEATURES
# ### LOGGING
# ##
# ##LOGGING = {
# ##    'version': 1,
# ##    'disable_existing_loggers': False,
# ##    'handlers': {
# ##        'file': {
# ##            'level': 'DEBUG',
# ##            'class': 'logging.FileHandler',
# ##            'filename': os.path.join(BASE_DIR, "logs/debug.log"),
# ##        },
# ##    },
# ##    'loggers': {
# ##        'django.request': {
# ##            'handlers': ['file'],
# ##            'level': 'DEBUG',
# ##            'propagate': True,
# ##        },
# ##        'django': {
# ##            'handlers': ['file'],
# ##            'level': 'DEBUG',
# ##            'propagate': False,
# ##        },
# ##    },
# ##}
# ##

