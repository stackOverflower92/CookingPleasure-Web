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
    url(r'^add_recipe/', views.addRecipe, name='recipe'),
    url(r'^dashboard/add_ingredients/', views.addIngr, name='ingredients'),
    url(r'^add_menu', views.addMenu, name='menu'),
    url(r'^dashboard/add_list/', views.addList, name='list'),
    url(r'^dashboard/add_list_menu/', views.addListMenu, name='listmenu'),
    url(r'^dashboard/get_recipe/', views.getRecipe, name='grecipe'),
    url(r'^dashboard/get_menu/', views.getMenu, name='gmenu'),
    url(r'^dashboard/get_list/', views.getList, name='glist'),
]
