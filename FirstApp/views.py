from django.shortcuts import render

from .models import *
from django.template import RequestContext, loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('FirstApp/index.html')
    context = RequestContext(request, {
        'recipe_list': recipe_list,
    })
    return HttpResponse(template.render(context))

def login(request):
    Users = User.objects
    template = loader.get_template('FirstApp/login.html')
    context = RequestContext(request, {
        'users': Users,
    })
    return HttpResponse(template.render(context))

#TODO:creare i template e le pagine html e aggiustare i return
def ShowRecipes(request):
    recipe_list = Recipe.objects.order_by('-Recipe_id')
    context = {'recipe_list': recipe_list}
    return render(request, 'FirstApp/recipe.html', context)

def ShowMenu(request, Menu_id):
    try:
        menu = Menu.objects.get(pk=Menu_id)
    except Menu.DoesNotExist:
        raise Http404("Menu does not exist")
    return render(request, 'FirstApp/showMenu.html', {'menu': menu})


