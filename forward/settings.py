# -*- coding: utf-8 -*-
# Global settings for football project.

from os.path import abspath, dirname, basename, join, split

MAIN_APPS_PATH = abspath(dirname(__file__))
MAIN_APPS_NAME = basename(MAIN_APPS_PATH)
PROJECT_PATH = split(MAIN_APPS_PATH)[0]
PROJECT_NAME = basename(PROJECT_PATH)

FILE_UPLOAD_PERMISSIONS = 0644



DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Krasnoyarsk'
LANGUAGE_CODE = 'RU-ru'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = join(PROJECT_PATH, 'static')
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL
MEDIA_ROOT = join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
STATICFILES_DIRS = ()
TEMPLATE_DIRS = ()

CKEDITOR_UPLOAD_PATH = "media/uploads"
CKEDITOR_UPLOAD_PREFIX = "/media/uploads"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    },
}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ANONYMOUS_USER_ID = -1
SITE_ID = 1
SECRET_KEY = 's5=xwz&y$qi=vbl0f6r12%i$t2x9o-_t329s+sv%asd^yg(*5+'
ROOT_URLCONF = 'forward.urls'
WSGI_APPLICATION = 'forward.wsgi.application'


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

DAJAXICE_MEDIA_PREFIX="dajaxice"

DAJAX_FUNCTIONS=(
    'ajaxapp.ajax.send_form',
    'ajaxapp.ajax.load_form',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'ckeditor',
    'autoslug',
    'south',
    'sorl.thumbnail',
    'flatblocks',
    'dajaxice',
    'dajax',
)

LOCAL_APPS = (
    'blog',
    'main',
    'slider',
    'review',
    'portfolio',
    'feedback',
    'grammars',
    'ajaxapp',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

for item in LOCAL_APPS:
    INSTALLED_APPS+=(item,)
    TEMPLATE_DIRS+=(join(PROJECT_PATH, item,'templates'),)
    STATICFILES_DIRS+=((item,join(PROJECT_PATH, item,'static')),)

from local import *
