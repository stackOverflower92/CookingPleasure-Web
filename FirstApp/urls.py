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
    url(r'^addrecipe/', views.addRecipe, name='recipe'),
    url(r'^addmenu', views.addMenu, name='menu'),
    url(r'^addlist', views.addList, name='list'),


]
