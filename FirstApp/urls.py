from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.firstapp,name='firstapp'),
    url(r'^login/$', views.logs, name='login'),
    url(r'^signin/$',views.signin,name='signin'),
    url(r'^logout/$',views.signout,name='logout'),
    url(r'^dashboard/$', views.home, name='home'),
    url(r'^thanks/$', views.thanks, name='thanks'),
    url(r'^$', include('django.contrib.auth.urls')),
    url(r'^dashboard/recipe', views.showRecipe, name='recipe'),
    url(r'^dashboard/menu', views.showMenu, name='menu'),
    url(r'^dashboard/list', views.showList, name='list'),

]
