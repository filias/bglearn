import os

from .base import *

ALLOWED_HOSTS = ["filipa.pythonanywhere.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME", "mac"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": "",
    }
}

# Media files
MEDIA_URL = f"https://filipa.pythonanywhere.com/media/"
