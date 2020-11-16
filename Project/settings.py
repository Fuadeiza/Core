import os
from pathlib import Path
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3h-c(v!m-=(-h)3zpncyo18b=2y56c)!##i9of1ly-&yc&umy='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core.apps.CoreConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'Project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path.joinpath(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'Project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = Path.joinpath(BASE_DIR,"static")


MEDIA_URL = '/media/'
MEDIA_ROOT = Path.joinpath(BASE_DIR,"media")


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# DEFAULT_FROM_EMAIL = 'admin@baskotii.ae'
# SERVER_EMAIL = 'admin@baskotii.ae'
# EMAIL_HOST = 'mail.baskotii.ae'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'admin@baskotii.ae'
# EMAIL_HOST_PASSWORD = 'Ww@778899778899'
# EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'bs@baskotii.ae'
SERVER_EMAIL = 'bs@baskotii.ae'
EMAIL_HOST = 'r110.dxb4.mysecurecloudhost.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'bs@baskotii.ae'
EMAIL_HOST_PASSWORD = 'Ww@778899778899'
EMAIL_USE_TLS = True


ACCOUNT_SID = 'AC6b6ee377fa3fb91b41a9a3ce1cdd5183'
AUTH_TOKEN = '958170536894f8ec35cf9ae4ed92069c'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
)


LOCALE_PATHS = [
    os.path.join(BASE_DIR, "locale")]


LANGUAGES = [
    ('en', _('English')),
    ('ar', _('Arabic')),
]

