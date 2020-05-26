from .base import *

DJANGO_APPS = []
MY_APPS = []

THIRD_PART_APPS = [
    'django_s3_storage',
]

INSTALLED_APPS = INSTALLED_APPS + DJANGO_APPS + MY_APPS + THIRD_PART_APPS

print('is running zappa settings')

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

SECRET_KEY = os.getenv('SECRET_KEY')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

DEBUG = os.getenv('DEBUG') == 'on'

# Email Service
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS') == 'on'
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL') == 'on'

EMAIL_SUBJECT_PREFIX = '[%s] ' % 'Tierra Gourmet'
SERVER_EMAIL = os.getenv('SERVER_EMAIL')
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# Amazon web services info
STATIC_S3_NAME_BUCKET = os.getenv('STATIC_S3_NAME_BUCKET')
STATICFILES_STORAGE = "django_s3_storage.storage.StaticS3Storage"
AWS_S3_BUCKET_NAME_STATIC = STATIC_S3_NAME_BUCKET
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % STATIC_S3_NAME_BUCKET
STATIC_URL = 'https://%s/' % AWS_S3_CUSTOM_DOMAIN
AWS_REGION = "us-east-1"
AWS_S3_MAX_AGE_SECONDS = 60 * 60 * 24 * 365
AWS_S3_GZIP = True
AWS_S3_BUCKET_AUTH_STATIC = False

DEFAULT_FILE_STORAGE = "django_s3_storage.storage.StaticS3Storage"
