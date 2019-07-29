"""
Django settings for aidants_connect project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

HOST = os.environ["HOST"]
# FC as FI
FC_AS_FI_CALLBACK_URL = os.environ["FC_AS_FI_CALLBACK_URL"]
FC_AS_FI_ID = os.environ["FC_AS_FI_ID"]
FC_AS_FI_SECRET = os.environ["FC_AS_FI_SECRET"]

# FC as FS
FC_AS_FS_BASE_URL = os.environ["FC_AS_FS_BASE_URL"]
FC_AS_FS_ID = os.environ["FC_AS_FS_ID"]
FC_AS_FS_SECRET = os.environ["FC_AS_FS_SECRET"]
FC_AS_FS_CALLBACK_URL = os.environ["FC_AS_FS_CALLBACK_URL"]

if os.environ.get("FC_AS_FS_TEST_PORT"):
    FC_AS_FS_TEST_PORT = int(os.environ["FC_AS_FS_TEST_PORT"])
else:
    FC_AS_FS_TEST_PORT = 0


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("APP_SECRET")

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv("DEBUG") == "True":
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = [os.environ["HOST"]]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "aidants_connect_web",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "aidants_connect.urls"

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
            ]
        },
    }
]

WSGI_APPLICATION = "aidants_connect.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_URL"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}

ssl_option = os.getenv("DATABASE_SSL")
if ssl_option:
    DATABASES["default"]["OPTIONS"] = {"sslmode": ssl_option}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = "staticfiles"
STATIC_URL = "/static/"


LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "home_page"

AUTH_USER_MODEL = "aidants_connect_web.User"


DEMARCHES = [
    ("papiers", "Papiers - Citoyenneté"),
    ("famille", "Famille"),
    ("social", "Social - Santé"),
    ("travail", "Travail"),
    ("logement", "Logement"),
    ("Transport", "Transport"),
    ("argent", "Argent"),
    ("justice", "Justice"),
    ("etranger", "Étranger"),
    ("loisir", "Loisir")

]
