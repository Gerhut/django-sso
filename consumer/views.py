from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.views import redirect_to_login
from django.conf import settings

from importlib import import_module

SessionStore = import_module(settings.SESSION_ENGINE).SessionStore

def index(request):
    if request.user.is_authenticated():
        return HttpResponse('Hello, ' + request.user.username)
    elif 'code' in request.GET:
        request.session = SessionStore(request.GET['code'])
        request.session.modified = True
        return redirect(index)
    else:
        return redirect_to_login(
            request.build_absolute_uri(),
            settings.SSO_AUTH_URL, 'callback')
