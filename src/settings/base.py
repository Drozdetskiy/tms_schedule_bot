"""
Django settings for bot_status_finder project.

Generated by "django-admin startproject" using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
# Standard Library
import os

# TODO: add django settings libs
PROJECT = "TMS_SCHEDULE_BOT"
# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "q58rhp6g61&ygrm)x2!5u%7wa)m-d$0-s8srud^uee8h_=*a6v"

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework.authtoken",
    "rest_framework",
    "django_celery_beat",
    "chat_scheduler",
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wsgi.application"


# Databases
DEFAULT_DB = "default"

POSTGRES_DEFAULT_HOST = os.getenv("POSTGRES_DEFAULT_HOST", "localhost")
POSTGRES_DEFAULT_PORT = os.getenv("POSTGRES_DEFAULT_PORT", 5432)
POSTGRES_DEFAULT_USER = os.getenv("POSTGRES_DEFAULT_USER", "postgres")
POSTGRES_DEFAULT_NAME = os.getenv(
    "POSTGRES_DEFAULT_NAME", f"{PROJECT.lower()}_db"
)
POSTGRES_DEFAULT_PASSWORD = os.getenv("POSTGRES_DEFAULT_PASSWORD", "postgres")
POSTGRES_DEFAULT_CONN_MAX_AGE = 0

DATABASES = {
    DEFAULT_DB: {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": POSTGRES_DEFAULT_HOST,
        "PORT": POSTGRES_DEFAULT_PORT,
        "USER": POSTGRES_DEFAULT_USER,
        "NAME": POSTGRES_DEFAULT_NAME,
        "PASSWORD": POSTGRES_DEFAULT_PASSWORD,
        "CONN_MAX_AGE": POSTGRES_DEFAULT_CONN_MAX_AGE,
    },
}

# Workers
EVENT_WORKER_TIMEOUT = 5  # 5 sec

ENABLE_MESSAGE_CALLBACK = True

# Telegram
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "")

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# CELERY

BROKER_SCHEMA = "redis"
BROKER_HOST = "localhost"
BROKER_PORT = "6379"
BROKER_DB = "0"
BROKER_URL = "{schema}://{host}:{port}/{db}".format(
        schema=BROKER_SCHEMA,
        host=BROKER_HOST,
        port=BROKER_PORT,
        db=BROKER_DB,
    )

CELERY_RESULT_SCHEMA = "redis"
CELERY_RESULT_HOST = "localhost"
CELERY_RESULT_PORT = "6379"
CELERY_RESULT_DB = "0"
CELERY_ALWAYS_EAGER = False
CELERY_TASK_RESULT_EXPIRES = 10 * 60
CELERY_MAX_CACHED_RESULTS = 10000
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

CELERY_RESULT_BACKEND = "{schema}://{host}:{port}/{db}".format(
        schema=CELERY_RESULT_SCHEMA,
        host=CELERY_RESULT_HOST,
        port=CELERY_RESULT_PORT,
        db=CELERY_RESULT_DB,
    )

DEFAULT_PERIODIC_TASK = "chat_scheduler.tasks.send_message"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

LOG_DIR = os.path.join(BASE_DIR, "logs")
LOG_LEVEL = "INFO"

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {
        "level": "WARNING",
        "handlers": ["default_handler"],
    },
    "formatters": {
        "default": {
            "format": "[{levelname}]P:{process} T:{thread} "
                      "{asctime} {name}.{funcName}: {message}",
            "datefmt": "%d/%b/%Y %H:%M:%S",
            "style": "{",
        },
        "simple": {
            "format": "[{levelname}] [{message}]",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue"
        },
    },
    "handlers": {
        "console_handler": {
            "level": LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "filters": ["require_debug_true"],
        },
        "default_handler": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": LOG_DIR + "/app.log",
        },
        "worker_handler": {
            "level": LOG_LEVEL,
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": LOG_DIR + "/workers.log",
        },
        "event_handler": {
            "level": LOG_LEVEL,
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": LOG_DIR + "/events.log",
        },
        "null": {
            "class": "logging.NullHandler",
        },
    },
    "loggers": {
        "django.security.DisallowedHost": {
            "handlers": ["null"],
            "propagate": False,
        },
        PROJECT: {
            "handlers": [
                "console_handler", "default_handler",
            ],
            "level": LOG_LEVEL,
        },
    },
}
