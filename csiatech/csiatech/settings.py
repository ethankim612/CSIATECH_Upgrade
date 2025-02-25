"""
Django settings for CSIAOnline project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from celery.schedules import crontab
from yaja.tasks import run_reset_script

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-p#s0u&ygrjnecd7rl3^*epzpzn0i14%19=4rsaq*vbpzwbv0uy"

# SECURITY WARNING: don't run with debug turned on in production!
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
    "home",
    "login",
    "yaja",
    "django_celery_results",
    "django_celery_beat",
    "rest_framework",
    "corsheaders",
    "club",
    "seminar",
    "simple_history",
    "csiatech",
]

CELERY_BROKER_URL = "redis://localhost:6379"
accept_content = ["application/json"]
result_serializer = "json"
task_serializer = "json"
result_backend = "django-db"
timezone = "Asia/Seoul"


CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

CELERY_BEAT_SCHEDULE = {
    "run-reset-every-friday": {
        "task": "yaja.tasks.run_reset_script",
        "schedule": crontab(hour=6, minute=59, day_of_week="sat"),
    },
    "run-reset-every-day-9am": {
        "task": "yaja.tasks.run_update_script",
        "schedule": crontab(hour=9, minute=0, day_of_week="mon-fri"),
    },
    "run-reset-every-day-1pm": {
        "task": "yaja.tasks.run_update_script",
        "schedule": crontab(hour=13, minute=0, day_of_week="mon-fri"),
    },
    "run-reset-every-day-5pm": {
        "task": "yaja.tasks.run_update_script",
        "schedule": crontab(hour=17, minute=0, day_of_week="mon-fri"),
    },
    "run-reset-every-day-5pm-29min": {
        "task": "yaja.tasks.run_update_script",
        "schedule": crontab(hour=17, minute=29, day_of_week="mon-fri"),
    },
    "run-clear-room-every-day-8am": {
        "task": "seminar.tasks.run_clear_room",
        "schedule": crontab(hour=8, minute=0),
    },
    "run-update-seminar-every-day-1pm": {
        "task": "seminar.tasks.run_update_seminar",
        "schedule": crontab(hour=13, minute=00),
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "csiatech.urls"

TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "csiatech.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://52.79.74.83",
]


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True

STATICFILES_DIRS = [
    directory for directory in [
        BASE_DIR / "static",
        BASE_DIR / "home" / "static",
        BASE_DIR / "yaja" / "static",
        BASE_DIR / "login" / "static",
        BASE_DIR / "seminar" / "static",
        BASE_DIR / "club" / "static",
    ]  if directory.exists()
]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "login.CustomUser"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    # Add other authentication backends if needed
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",  # Optional: for browsable API
        # Add other renderers as needed
    ],
}


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_ROOT = BASE_DIR / "collected_static"


# Set a session expiration time (optional)
SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_COOKIE_AGE = 1800  # 30 minutes
SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_SECURE = True  # Use only with HTTPS
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = "Strict"