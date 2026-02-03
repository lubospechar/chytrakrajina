from pathlib import Path
from decouple import config, Csv
from configurations import Configuration
from django.utils.translation import gettext_lazy as _

class Base(Configuration):
    BASE_DIR = Path(__file__).resolve().parent.parent
    SECRET_KEY = config("SECRET_KEY")

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("DB_NAME"),
            "USER": config("DB_USER"),
            "PASSWORD": config("DB_PASSWORD"),
            "HOST": config("DB_HOST", default="127.0.0.1"),
            "PORT": config("DB_PORT", default="5432"),
        }
    }

    ROOT_URLCONF = "chytrakrajina.urls"

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [BASE_DIR / 'templates']
            ,
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "chytrakrajina.wsgi.application"

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

    LANGUAGE_CODE = "en"
    TIME_ZONE = "Europe/Prague"
    USE_I18N = True
    USE_TZ = True

    LANGUAGES = [
        ("cs", _("Czech")),
        ("en", _("English")),
    ]

    STATIC_URL = "static/"
    MEDIA_URL = "media/"

    STATIC_ROOT = config('STATIC_ROOT', default="/tmp/static/")
    MEDIA_ROOT = config('MEDIA_ROOT', default="/tmp/media/")

class Local(Base):
    DEBUG = True
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

class Dev(Base):
    DEBUG = config("DEBUG", default=True, cast=bool)
    ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="", cast=Csv())

class Prod(Base):
    DEBUG = config("DEBUG", default=False, cast=bool)
    ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="", cast=Csv())