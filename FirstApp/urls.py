from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),

    url(r'^login/$', views.login, name='login'),
    url(r'^dashboard/$', views.ShowMenu, name='dashboard'),
    # ex: /polls/5/
    url(r'^recipe/$', views.ShowRecipes, name='ShowRecipes'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.Ingredient, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.Menu, name='vote'),

]
