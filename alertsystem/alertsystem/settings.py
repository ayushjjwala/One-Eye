"""
Django settings for alertsystem project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
MEDIA_ROOT = "/Users/Hemanth/Documents/Code/FaceRec/OneEye/imaginate_oneeye/alertsystem/media"
MEDIA_URL = "/media/"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x0+x@e&=jj2v@a5#lk2hg(p4spxeoq1@3txn+x7xg(w47%$he&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'testmailerapp',
    'alertshandler',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
 )
ROOT_URLCONF = 'alertsystem.urls'

WSGI_APPLICATION = 'alertsystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

##Mailer settings
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=465
EMAIL_USE_SSL=True
EMAIL_HOST_USER='abhimanyu@imaginate.in'
EMAIL_HOST_PASSWORD='sasankimaginate'

##SMS
SMS_SEND_STRING='http://api.mvaayoo.com/mvaayooapi/MessageCompose?user=hemanth@imaginate.in:imaginate&senderID=DOCTOR&receipientno=9866796699&dcs=0&msgtxt=OneEye%20ALERT!%20{0}&state=4'
