from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
) + patterns('consumer.views',
    url(r'^$', 'index'),
)
