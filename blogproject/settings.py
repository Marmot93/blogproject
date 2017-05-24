"""
Django settings for blogproject project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# 七牛云测试1 start
QINIU_ACCESS_KEY = 'vKQNTxH_Za1JWGVllKRo7SI5oBmPIhVXIRjlE1oW'
QINIU_SECRET_KEY = 'EYd-BgvxwD_OOGO9IFmqwY82h-rrX3nFOcABatR8'
QINIU_BUCKET_NAME = 'marmot'
QINIU_BUCKET_DOMAIN = 'oor3iu2zw.bkt.clouddn.com/'
QINIU_SECURE_URL = False  # 使用http

PREFIX_URL = 'http://'

# 七牛云测试1 end
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bx=(^6b7bfsin3an^==%+jstb=v24w06ofarks=w!3v+8q9tl)'

# SECURITY WARNING: don't run with debug turned on in production!
# 部署之后改为False
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

# * 接受所有的头
CORS_ALLOW_HEADERS = ('*',
                      # 'accept',
                      # 'accept-encoding',
                      # 'authorization',
                      # 'content-type',
                      # 'dnt',
                      # 'origin',
                      # 'user-agent',
                      # 'x-csrftoken',
                      # 'x-requested-with',
                      # 'x-file-name',
                      # 'identity',
                      )

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'corsheaders',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BolgConfig',
    'comments'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'blogproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'  # 把国际时区改为中国时区

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# 本地static
STATIC_URL = '/static/'

# 七牛云测试2 start
# 七牛云上的static
# STATIC_URL = QINIU_BUCKET_DOMAIN + '/static/'
#
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'
#
# DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuStorage'

# 七牛云测试2 end
