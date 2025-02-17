from corsheaders.defaults import default_headers

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(no#j@8q@)2)&e)=pdl$a5h*8gvn=%c8g*bt-3(g#&x3lk#$r&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['backend.tarixmanba.uz', '127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS = [
    # 'unfold',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # APPS
    'corsheaders',
    'admin_panel',
    'user',
    'api',
    'resources',
    'other_app',

    # Additional library
    'rest_framework',
    'django_filters',
    'rest_framework_swagger',  # Swagger
    'drf_yasg',  # Yet Another Swagger generator
    'ckeditor',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'Config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates/'],
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

WSGI_APPLICATION = 'Config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tarixmanba_db',  # Baza nomi
        'USER': 'tarixmanba_user',  # Foydalanuvchi nomi
        'PASSWORD': 'tarixmanba_password',  # Foydalanuvchi paroli
        'HOST': '93.188.84.132',  # Baza xost nomi (Docker Compose'dagi xost nomi)
        'PORT': '5432',  # PostgreSQLning standart porti
    }
}


  # 'PASSWORD': 'tarixmanba_password',  
        # 'HOST': 'db',
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/


TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [BASE_DIR / 'static', ]

# CSRF_TRUSTED_ORIGINS = [
#     'http://backend.tarixmanba.uz',
#     'https://backend.tarixmanba.uz',
# ]

CSRF_COOKIE_DOMAIN = 'backend.tarixmanba.uz'

# Agar SSL ishlatmasangiz, bu sozlamalarni False ga o'zgartiring
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False


CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_HEADERS = list(default_headers) + [
    'language-code',
]


CSRF_TRUSTED_ORIGINS = ['https://backend.tarixmanba.uz',]
# CORS_ALLOWED_ORIGINS = [
#     'https://backend.tarixmanba.uz',
# ]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',

    ],
}

# AUTH_USER_MODEL = "user.CustomUser"
FILE_UPLOAD_MAX_MEMORY_SIZE = 209715200  # 200 MB (baytlarda)
DATA_UPLOAD_MAX_MEMORY_SIZE = 209715200  # 200 MB




# CKEditor Settings
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js' 
CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
}
