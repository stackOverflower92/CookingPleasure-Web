from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.login, name='index'),
    url(r'^dashboard/$', views.relogin, name='dashboard'),
    url(r'^thanks/$', views.thanks, name='ShowRecipes'),
    url(r'^$', include('django.contrib.auth.urls')),

]
