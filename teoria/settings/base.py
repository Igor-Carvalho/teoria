"""Configurações gerais do projeto teoria."""

import environ
from django.conf import global_settings

root = environ.Path(__file__) - 3
env = environ.Env()
environ.Env.read_env()

admins = env.dict('ADMINS')
ADMINS = admins.items()
MANAGERS = env.dict('MANAGERS', default=admins).items()

# Build paths inside the project like this: join(BASE_DIR, ...)
BASE_DIR = root()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {'default': env.db()}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Email
# https://docs.djangoproject.com/en/dev/topics/email/
env.EMAIL_SCHEMES.update(postoffice='post_office.EmailBackend')
vars().update(env.email_url())

DEFAULT_CHARSET = env('DEFAULT_CHARSET', default='utf-8')  # default charset in django.core.email.
# default from_email in EmailMessage.
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default='webmaster@localhost')
# default prefix + subject in mail_admins/managers.
EMAIL_SUBJECT_PREFIX = env('EMAIL_SUBJECT_PREFIX', default='[Django]')
# default from: header in mail_admins/managers.
SERVER_EMAIL = env('SERVER_EMAIL', default='admin@localhost')
OWNER_EMAIL = env('OWNER_EMAIL')

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.postgres',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'auditlog',
    'django_celery_results',
    'pipeline',
    'post_office',
    'rest_framework',
    'widget_tweaks',
]

PROJECT_APPS = [
    'core.apps.CoreConfig',
    'artigos.apps.ArtigosConfig',
    'contato.apps.ContatoConfig',
    'inscritos.apps.InscritosConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'core.middleware.HttpsOnlyMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',
]

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root.path('teoria')('templates')],
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

# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
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

ROOT_URLCONF = 'teoria.urls'

WSGI_APPLICATION = 'teoria.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Belem'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = '/public/'
STATIC_ROOT = root.path('')('public')
STATICFILES_DIRS = [root.path('teoria')('assets'), root.path('')('node_modules')]
STATICFILES_STORAGE = 'pipeline.storage.PipelineStorage'
STATICFILES_FINDERS = global_settings.STATICFILES_FINDERS + ['pipeline.finders.PipelineFinder']

MEDIA_URL = '/media/'
MEDIA_ROOT = root.path('')('media')

PIPELINE = dict()
PIPELINE['JAVASCRIPT'] = {
    'main': {
        'source_filenames': [
            'app/artigos/**/*.es6',
            'app/inscritos/**/*.es6',
            'app/inscritos/*.es6',
            'app/contato/**/*.es6',
            'app/contato/*.es6',
            'app/app.config.es6',
            'app/app.main.es6',
        ],
        'output_filename': 'js/main.min.js',
    },
    'scripts': {
        'source_filenames': [
            'js/plugin.js',
            'js/scripts.js',
            'js/syntaxhighlighter.js',
        ],
        'output_filename': 'js/scripts.min.js',
    }
}
PIPELINE['STYLESHEETS'] = {
    'base': {
        'source_filenames': [
            'css/plugin.css',
            'css/style.css',
            'css/syntaxhighlighter.css',
            'css/base.css',
        ],
        'output_filename': 'css/base.min.css'
    }
}
PIPELINE['COMPILERS'] = [
    'pipeline.compilers.es6.ES6Compiler',
]
PIPELINE['BABEL_ARGUMENTS'] = '--presets env'

AUTH_USER_MODEL = 'core.Usuário'

CACHES = {'default': env.cache_url()}
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

HTML_MINIFY = True

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
}

# Celery
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER_URL = env('BROKER_URL')

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
            'datefmt': '%d/%b/%Y %H/%M/%S',
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'py.warnings': {
            'handlers': ['console'],
        },
        'artigos': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
