from pathlib import Path


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = "django-insecure-==pzw&*sm_gho_o&ji5y_0w)*$ggmymawkc)cj1-#d!=j4@jj^"
DEBUG = True
ALLOWED_HOSTS = []

# Applications
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "agtsdata_app",  
    'widget_tweaks',
    'django.contrib.humanize',
]

# Middlewares
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URLs
ROOT_URLCONF = "agtsdata_site.urls"

# Templates
TEMPLATES = [
    {   
        "DIRS": [BASE_DIR / "templates"],  # ajoute ce dossier si tu utilises templates global
        "APP_DIRS": True,
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "agtsdata_site.wsgi.application"

# Base de données
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Validation mot de passe
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

# Langue et fuseau horaire
LANGUAGE_CODE = "fr"  # Changement en français
TIME_ZONE = "Africa/Douala"  # Fuseau horaire du Cameroun

USE_I18N = True
USE_TZ = True

# Fichiers statiques
STATIC_URL = "static/"

# Fichiers médias (images des projets et de l'équipe)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Clé primaire par défaut
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



# Envoi des emails avec un compte Gmail par exemple :
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ngomaignoumba@gmail.com'         # Remplace par ton adresse
EMAIL_HOST_PASSWORD = '#Alchimisteecarlate777#'     # ⚠️ Utilise un mot de passe d'application sécurisé
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
import os

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

