# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5zt#2b20#=c#r2rq_2=c#hf*w^6u(rbbdid@xbu=8kpj*a#d+^'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'orders_db',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

