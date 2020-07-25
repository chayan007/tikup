from settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_NAME'),
        'PASSWORD': os.environ.get('DB_NAME'),
        'HOST': os.environ.get('DB_NAME'),
        'PORT': '3306',
    }
}
