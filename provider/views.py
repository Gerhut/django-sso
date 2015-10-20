from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.views import redirect_to_login
from django.conf import settings

def index(request):
    if request.user.is_authenticated():
        return redirect(request.GET['callback'] +
            '?code=' + request.COOKIES[settings.SESSION_COOKIE_NAME])
    else:
        return redirect_to_login(
            request.get_full_path(), reverse('admin:login'))

