import json
import os
import psycopg2

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Disadvantages of Secret Key Rotation. Invalidates:
# All sessions.
# All messages if you are using CookieStorage or FallbackStorage.
# All PasswordResetView tokens.
# Any usage of cryptographic signing.

# ------------------------------- Change here when alternating between production and dev ------------------------------
STATIC_URL = "/static/"

SECRET_KEY="+inuldj)buk5fujgx$%z3$g09t1#f*8@bgs3ywomes$sk&bh4q"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "site_db",
        "USER": "postgres",
        "PASSWORD": "753951456852",
        "HOST": "127.0.0.1",
        "PORT": "5432"
    }
}

# Set to False to debug 404
DEBUG = True

ALLOWED_HOSTS = ["jackwu.ca", ".jackwu.ca", "127.0.0.1"]

SECURE_SSL_REDIRECT = False

# ----------------------------------------------------------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "homepage.apps.HomepageConfig",
    "ML_reviews.apps.MlReviewsConfig",
    "analysis.apps.AnalysisConfig",
    "weather.apps.WeatherConfig",
    "text_speech.apps.TextSpeechConfig"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'jackwu_ca.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'jackwu_ca.wsgi.application'

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "America/Toronto"

USE_I18N = True

USE_L10N = True

USE_TZ = True

