from django.shortcuts import render
from .forms import *
from .models import *
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
    recipe_list = Recipe.objects.order_by('-pub_date')
    template = loader.get_template('FirstApp/index.html')
    context = RequestContext(request, {
        'recipe_list': recipe_list,
    })
    return HttpResponse(template.render(context))

def logs(request):
    template = loader.get_template('FirstApp/login.html')

    form = LoginForm()
    context = RequestContext(request, {'form': form, })
    return HttpResponse(template.render(context))


def login(request):
    Users = User.objects
    if request.user.is_authenticated():
            template = loader.get_template('FirstApp/dashboard.html')
    else:
            template = loader.get_template('FirstApp/login.html')
    context = RequestContext(request, {
        'users': Users,
    })
    return HttpResponse(template.render(context))


def ShowRecipes(request):
    recipe_list = Recipe.objects
    context = {'recipe_list': recipe_list}
    return render(request, 'FirstApp/recipe.html', context)

def ShowMenu(request):
    page = 'FirstApp/login.html'
    if request.method == 'POST': # If the form has been submitted...
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request)
                menu_list = Menu.objects.order_by('-name')
                user = User.objects.get(mail='diego.ballotta@gmail.com')
                context = RequestContext(request,{'menu_list': menu_list,'user':user})
                page = 'FirstApp/dashboard.html'

    form1 = LoginForm()
    context = {'form': form1, }

    return render(request, page ,context)

