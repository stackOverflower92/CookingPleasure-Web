from django.conf.urls import patterns, include, url
from django.contrib import admin
from FirstApp import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CookingPleasureLD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^FirstApp/', include('FirstApp.urls', namespace="FirstApp")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),)
