from .base import *

DEBUG = False

ALLOWED_HOSTS = ["dfvrn.pythonanywhere.com"]

ROOT_URLCONF = "mysite.urls"

SECRET_KEY = "django-insecure-*4%s8&baig50^rhk%(@e(0fxij=k!trv))!q#v8d8ec$zb9=u&"

try:
    from .local import *
except ImportError:
    pass
