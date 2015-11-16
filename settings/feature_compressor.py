## COMPRESSOR - STORAGES
#
import os
from . import BASE_DIR
from . import INSTALLED_APPS

#Update APPS
INSTALLED_APPS = INSTALLED_APPS + (
    'compressor',
)

COMPRESS_ENABLED = True
HTML_MINIFY = True

COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
    'compressor.filters.jsmin.SlimItFilter',
]

KEEP_COMMENTS_ON_MINIFYING = False

#COMPRESS_URL = "http://compressor-test.s3.amazonaws.com/"
#STATIC_URL = COMPRESS_URL
COMPRESS_URL = STATIC_URL
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)
## END
