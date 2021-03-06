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

# Unstable on local machine, prone to timeouts due to connection to google storage.


import google.oauth2.service_account as service_account

# Where to find static files to collect
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "ML_reviews", "static"),
	os.path.join(BASE_DIR, "weather", "static"),
    os.path.join(BASE_DIR, "homepage", "static"),
    os.path.join(BASE_DIR, "analysis", "static"),
]


# Where static files are collected after collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
GS_BUCKET_NAME = "jackwu.ca"
STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
STATIC_URL = "https://storage.googleapis.com/jackwu.ca/"
GS_CREDENTIALS = service_account.Credentials.from_service_account_file("service_account_key.json")

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": os.getenv("db_engine"),
        "NAME": os.getenv("db_name"),
        "USER": os.getenv("db_user"),
        "PASSWORD": os.getenv("db_password"),
        "HOST": os.getenv("db_host"),
        "PORT": os.getenv("db_port")
    }
}

DEBUG = False

ALLOWED_HOSTS = ["jackwu.ca", ".jackwu.ca"]

SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_EXPIRE_AT_BROWSER_CLOSE=True

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

