from django.shortcuts import render
from .forms import *
from .models import Recipe,Ingredient,List,Menu
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
    recipe_list = Recipe.objects.order_by('-pub_date')
    template = loader.get_template('FirstApp/index.html')
    context = RequestContext(request, {
        'recipe_list': recipe_list,
    })
    return HttpResponse(template.render(context))

def login(request):
    template = loader.get_template('FirstApp/login.html')

    form = LoginForm()
    form1 = MyRegistrationForm()
    context = RequestContext(request, {'form': form,'form1': form1 })
    return HttpResponse(template.render(context))

def thanks(request):
    if request.method == 'POST': # If the form has been submitted...
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            User=form.save()
    template = loader.get_template('FirstApp/thanks.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def relogin(request):
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
                user = User.objects.get(username=username)
                context = {'menu_list': menu_list,'user':user}
                page = 'FirstApp/dashboard.html'
        else:
            form = LoginForm()
            form1 = MyRegistrationForm()
            context = {'form':form,'form1': form1 }

    return render(request, page ,context)

