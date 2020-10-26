"""
Django settings for aidants_connect project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from datetime import datetime, timedelta
import os

from dotenv import load_dotenv

from aidants_connect.postgres_url import turn_psql_url_into_param


load_dotenv(verbose=True)

HOST = os.environ["HOST"]
# FC as FI
FC_AS_FI_CALLBACK_URL = os.environ["FC_AS_FI_CALLBACK_URL"]
FC_AS_FI_ID = os.environ["FC_AS_FI_ID"]
HASH_FC_AS_FI_SECRET = os.environ["HASH_FC_AS_FI_SECRET"]
FC_AS_FI_HASH_SALT = os.environ["FC_AS_FI_HASH_SALT"]
FC_AS_FI_LOGOUT_REDIRECT_URI = os.environ["FC_AS_FI_LOGOUT_REDIRECT_URI"]

# FC as FS
FC_AS_FS_BASE_URL = os.environ["FC_AS_FS_BASE_URL"]
FC_AS_FS_ID = os.environ["FC_AS_FS_ID"]
FC_AS_FS_SECRET = os.environ["FC_AS_FS_SECRET"]
FC_AS_FS_CALLBACK_URL = os.environ["FC_AS_FS_CALLBACK_URL"]

FC_CONNECTION_AGE = int(os.environ["FC_CONNECTION_AGE"])

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


# We support a comma-separated list of allowed hosts.
ENV_SEPARATOR = ","
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost").split(ENV_SEPARATOR)


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "nested_admin",
    "tabbed_admin",
    "magicauth",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "aidants_connect_web",
    "admin_honeypot",
    "django_otp",
    "django_otp.plugins.otp_static",
    "django_otp.plugins.otp_totp",
    "django_celery_beat",
    "django_extensions",
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
    "django.contrib.sites.middleware.CurrentSiteMiddleware",
    "django_referrer_policy.middleware.ReferrerPolicyMiddleware",
    "csp.middleware.CSPMiddleware",
    "django_otp.middleware.OTPMiddleware",
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

postgres_url = os.getenv("POSTGRESQL_URL")
if postgres_url:
    environment_info = turn_psql_url_into_param(postgres_url)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": environment_info.get("db_name"),
            "USER": environment_info.get("db_user"),
            "PASSWORD": environment_info.get("db_password"),
            "HOST": environment_info.get("db_host"),
            "PORT": environment_info.get("db_port"),
        }
    }

    ssl_option = environment_info.get("sslmode")

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DATABASE_NAME"),
            "USER": os.getenv("DATABASE_USER"),
            "PASSWORD": os.getenv("DATABASE_PASSWORD"),
            "HOST": os.getenv("DATABASE_HOST"),
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

LANGUAGE_CODE = "fr"

TIME_ZONE = "Europe/Paris"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_ROOT = "staticfiles"
STATIC_URL = "/static/"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "home_page"
ACTIVITY_CHECK_URL = "activity_check"
ACTIVITY_CHECK_THRESHOLD = int(os.getenv("ACTIVITY_CHECK_THRESHOLD"))
ACTIVITY_CHECK_DURATION = timedelta(minutes=ACTIVITY_CHECK_THRESHOLD)

AUTH_USER_MODEL = "aidants_connect_web.Aidant"

DEMARCHES = {
    "papiers": {
        "titre": "Papiers - Citoyenneté",
        "description": "État-civil, Passeport, Élections, Papiers à conserver, Carte d'identité…",
        "service_exemples": ["ANTS", "Défenseur des droits"],
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png/papiers.png",
    },
    "famille": {
        "titre": "Famille",
        "description": "Allocations familiales, Naissance, Mariage, Pacs, Scolarité…",
        "service_exemples": ["CAF", "ameli.fr", "EduConnect"],
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
        "/famille.png",
    },
    "social": {
        "titre": "Social - Santé",
        "description": "Carte vitale, Chômage, Handicap, RSA, Personnes âgées…",
        "service_exemples": ["ameli.fr", "MSA", "RSI"],
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
        "/sante.png",
    },
    "travail": {
        "titre": "Travail",
        "description": "CDD, Concours, Retraite, Démission, Période d'essai…",
        "service_exemples": ["Pôle emploi", "Mon compte formation", "info-retraite.fr"],
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
        "/travail.png",
    },
    "logement": {
        "titre": "Logement",
        "description": "Allocations logement, Permis de construire, Logement social, Fin de bail…",
        "service_exemples": ["CAF", "Enedis"],
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
        "/logement.png",
    },
    "transports": {
        "titre": "Transports",
        "description": "Carte grise, Permis de conduire, Contrôle technique, Infractions…",
        "service_exemples": ["ANTS", "ANTAI", "Crit'air"],
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
        "/transports.png",
    },
    "argent": {
        "titre": "Argent",
        "description": "Crédit immobilier, Impôts, Consommation, Livret A, Assurance, "
        "Surendettement…",
        "service_exemples": ["Impots.gouv", "Timbres fiscaux", "Banque"],
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
        "/argent.png",
    },
    "justice": {
        "titre": "Justice",
        "description": "Casier judiciaire, Plainte, Aide juridictionnelle, Saisie…",
        "service_exemples": ["Télérecours citoyens"],
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
        "/justice.png",
    },
    "etranger": {
        "titre": "Étranger",
        "description": "Titres de séjour, Attestation d’accueil, Regroupement familial…",
        "service_exemples": ["OFPRA"],
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
        "/etrangers.png",
    },
    "loisirs": {
        "titre": "Loisirs",
        "description": "Animaux, Permis bateau, Tourisme, Permis de chasser…",
        "service_exemples": ["Ariane"],
        "icon": "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png"
        "/loisirs.png",
    },
}

MANDAT_TEMPLATE_PATH = "aidants_connect_web/mandat_templates/20201209_mandat.html"
ATTESTATION_SALT = os.getenv("ATTESTATION_SALT", "")

# Magic Auth
MAGICAUTH_EMAIL_FIELD = "email"
MAGICAUTH_FROM_EMAIL = os.getenv("MAGICAUTH_FROM_EMAIL")
MAGICAUTH_LOGGED_IN_REDIRECT_URL_NAME = "espace_aidant_home"
MAGICAUTH_LOGIN_VIEW_TEMPLATE = "login/login.html"
MAGICAUTH_EMAIL_SENT_VIEW_TEMPLATE = "login/email_sent.html"
MAGICAUTH_EMAIL_HTML_TEMPLATE = "login/email_template.html"
MAGICAUTH_EMAIL_TEXT_TEMPLATE = "login/email_template.txt"
MAGICAUTH_ENABLE_2FA = True

# https://github.com/betagouv/django-magicauth/blob/8a8143388bb15fad2823528201e22a31817da243/magicauth/settings.py#L54  # noqa
MAGICAUTH_TOKEN_DURATION_SECONDS = int(
    os.getenv("MAGICAUTH_TOKEN_DURATION_SECONDS", 5 * 60)
)

# TOTP
OTP_TOTP_ISSUER = os.getenv("OTP_TOTP_ISSUER", "Aidants Connect")

# Emails
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)
## if file based email backend is used (debug)
EMAIL_FILE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/tmp_email_as_file"
## if smtp backend is used
EMAIL_HOST = os.getenv("EMAIL_HOST", None)
EMAIL_PORT = os.getenv("EMAIL_PORT", None)
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", None)
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", None)
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", None)
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", None)

## Emails from the server
SERVER_EMAIL = os.getenv("SERVER_EMAIL", os.getenv("ADMIN_EMAIL"))
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", SERVER_EMAIL)
ADMIN_HONEYPOT_EMAIL_ADMINS = os.getenv("ADMIN_HONEYPOT_EMAIL_ADMINS", SERVER_EMAIL)

# Security headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
REFERRER_POLICY = "strict-origin"

# Content security policy
CSP_DEFAULT_SRC = ("'self'",)
CSP_IMG_SRC = (
    "'self'",
    "https://www.service-public.fr/resources/v-5cf79a7acf/web/css/img/png/",
)
CSP_SCRIPT_SRC = (
    "'self'",
    "'sha256-FUfFEwUd+ObSebyGDfkxyV7KwtyvBBwsE/VxIOfPD68='",  # tabbed_admin
    "'sha256-dzE1fiHF13yOIlSQf8CYbmucPoYAOHwQ70Y3OO70o+E='",  # main.html
    "'sha256-qtDLNBeXbQEZ6BoCPDfxDpo3OOJsnlVc/NGAMBmfHq0='",  # new_mandat.html
)
CSP_STYLE_SRC = ("'self'",)
CSP_OBJECT_SRC = ("'none'",)
CSP_FRAME_SRC = (
    "https://www.youtube.com/embed/hATrqHG4zYQ",
    "https://www.youtube.com/embed/WTHj_kQXnzs",
    "https://www.youtube.com/embed/ihsm-36I-fE",
)

# Admin Page settings
ADMIN_URL = os.getenv("ADMIN_URL")
ADMINS = [(os.getenv("ADMIN_NAME"), os.getenv("ADMIN_EMAIL"))]

# Sessions
SESSION_COOKIE_AGE = int(
    os.getenv("SESSION_COOKIE_AGE", 86400)
)  # default: 24 hours, in seconds
SESSION_EXPIRE_AT_BROWSER_CLOSE = False

# Cookie security
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False if os.getenv("SESSION_COOKIE_SECURE") == "False" else True
CSRF_COOKIE_SECURE = False if os.getenv("CSRF_COOKIE_SECURE") == "False" else True

# SSL security
SECURE_SSL_REDIRECT = False if os.getenv("SECURE_SSL_REDIRECT") == "False" else True
SECURE_HSTS_SECONDS = os.getenv("SECURE_HSTS_SECONDS")

# django_OTP_throttling
OTP_TOTP_THROTTLE_FACTOR = int(os.getenv("OTP_TOTP_THROTTLE_FACTOR", 1))

# Functional tests behaviour
HEADLESS_FUNCTIONAL_TESTS = (
    False if os.getenv("HEADLESS_FUNCTIONAL_TESTS") == "False" else True
)
BYPASS_FIRST_LIVESERVER_CONNECTION = (
    True if os.getenv("BYPASS_FIRST_LIVESERVER_CONNECTION") == "True" else False
)

# Celery settings
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
JSON_CONTENT_TYPE = "application/json"
JSON_SERIALIZER = "json"

CELERY_BROKER_URL = REDIS_URL
CELERY_RESULT_BACKEND = REDIS_URL
CELERY_RESULT_SERIALIZER = JSON_SERIALIZER
CELERY_TASK_SERIALIZER = JSON_SERIALIZER
CELERY_ACCEPT_CONTENT = [JSON_CONTENT_TYPE]

# COVID-19 changes
ETAT_URGENCE_2020_LAST_DAY = datetime.strptime(
    os.getenv("ETAT_URGENCE_2020_LAST_DAY"), "%d/%m/%Y %H:%M:%S %z"
)

# Staff Organisation name
STAFF_ORGANISATION_NAME = "BetaGouv"

# Tabbed Admin
TABBED_ADMIN_USE_JQUERY_UI = True

# Shell Plus
SHELL_PLUS_IMPORTS = [
    "from datetime import datetime, timedelta",
]

# Datapass
DATAPASS_KEY = os.getenv("DATAPASS_KEY", None)
