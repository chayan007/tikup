import os

from tikup.base import BASE_DIR

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': '5432',
    }
}

DEFAULT_FILE_STORAGE = 'tikup.gcloud.GoogleCloudMediaFileStorage'
STATICFILES_STORAGE = 'tikup.gcloud.GoogleCloudStaticFileStorage'

GS_PROJECT_ID = 'tokyo-amphora-240111'
GS_STATIC_BUCKET_NAME = 'misco-static-storage'
GS_MEDIA_BUCKET_NAME = 'misco-storage'

STATIC_URL = 'https://storage.googleapis.com/{}/'.format(GS_STATIC_BUCKET_NAME)
STATIC_ROOT = 'static/'

MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_MEDIA_BUCKET_NAME)
MEDIA_ROOT = 'media/'

UPLOAD_ROOT = 'media/uploads/'

DOWNLOAD_ROOT = os.path.join(BASE_DIR, 'static/media/downloads')
DOWNLOAD_URL = STATIC_URL + 'media/downloads'
