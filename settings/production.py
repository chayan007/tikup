from settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '3306',
    }
}

DEFAULT_FILE_STORAGE = 'gcloud.GoogleCloudMediaFileStorage'
STATICFILES_STORAGE = 'gcloud.GoogleCloudStaticFileStorage'

GS_PROJECT_ID = 'tokyo-amphora-240111'
GS_STATIC_BUCKET_NAME = 'misco-static-storage'
GS_MEDIA_BUCKET_NAME = 'misco-storage'

STATIC_URL = 'https://storage.googleapis.com/{}/'.format(GS_STATIC_BUCKET_NAME)
STATIC_ROOT = "static/"

MEDIA_URL = 'https://storage.googleapis.com/{}/'.format(GS_MEDIA_BUCKET_NAME)
MEDIA_ROOT = "media/"

UPLOAD_ROOT = 'media/uploads/'

DOWNLOAD_ROOT = os.path.join(BASE_DIR, "static/media/downloads")
DOWNLOAD_URL = STATIC_URL + "media/downloads"
