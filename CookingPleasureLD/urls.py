from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import settings
from FirstApp import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CookingPleasureLD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^FirstApp/', include('FirstApp.urls', namespace="FirstApp")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    (r'^FirstApp/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    )