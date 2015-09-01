from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^$', views.logs, name='index'),
    url(r'^dashboard/$', views.ShowMenu, name='dashboard'),
    url(r'^recipe/$', views.ShowRecipes, name='ShowRecipes'),
    url(r'^$', include('django.contrib.auth.urls')),

]
