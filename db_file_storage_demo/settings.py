# -*- coding: utf-8 -*-

from unipath import Path

PROJECT_PATH = Path(__file__).parent

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'cj33louyit#jhcq%it)swv_(*_b$q%jv5%d8s-hjj#=l=swi^y'
ROOT_URLCONF = 'db_file_storage_demo.urls'
WSGI_APPLICATION = 'db_file_storage_demo.wsgi.application'

DATABASES = {
    'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': PROJECT_PATH.child('database.db'),}
}

TEMPLATE_DIRS = (
    PROJECT_PATH.parent.child('templates'),
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.sessions',
    #
    'db_file_storage',
    #
    'console',
    'game',
)

DEFAULT_FILE_STORAGE = 'db_file_storage.storage.DatabaseFileStorage'
