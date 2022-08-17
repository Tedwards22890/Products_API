# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_ja651k54bh7q^lbb#3zwu&cd)_3#4+%ld=vobd1&ci6*e!&vo'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Colette1!'
    }
}