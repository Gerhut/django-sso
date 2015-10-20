# django-sso
Simple SSO implementation in Django

## How to start

    $ python consumer.py migrate
    $ python provider.py migrate
    $ python provider.py createsuperuser
    $ python consumer.py runserver 127.0.0.1:8000 & python provider.py runserver 127.0.0.1:9000
