from django.shortcuts import render
from .forms import *
from .models import *
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse


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
    form1 = MyRegistrationForm()
    context = RequestContext(request,{'form':form,'form1': form1 })
    return HttpResponse(template.render(context))

def signin(request):

    if request.method == 'POST': # If the form has been submitted...
        print('right post')
        form = LoginForm(request.POST)
        if form.is_valid():
            print('right form')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                print('user active')
                login(request,user)
                return HttpResponseRedirect(reverse('FirstApp:home'))
    return HttpResponseRedirect(reverse('FirstApp:logs'))

def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('FirstApp:login'))

def thanks(request):
    if request.method == 'POST': # If the form has been submitted...
        form = MyRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    template = loader.get_template('FirstApp/thanks.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def firstapp(request):
        return HttpResponseRedirect(reverse('FirstApp:home'))

@login_required
def home(request):
    rec = Recipe.objects.all().filter(user=request.user)
    menu = Menu.objects.all().filter(user=request.user)
    list = List.objects.all().filter(user=request.user)
    formrec = RecipeForm();
    template = loader.get_template('FirstApp/dashboard.html')
    context = RequestContext(request,{'recipe_list':rec,'menu_list':menu,'list_list':list,'recipeform':formrec})

    return HttpResponse(template.render(context))

@login_required
def showRecipe(request):
    recipelist = Recipe.objects.all()
    template = loader.get_template('FirstApp/dashboard.html')
    context = RequestContext(request,{'recipelist':recipelist})
    return HttpResponse(template.render(context))

@login_required
def showMenu(request):
    page = 'FirstApp/dashboard.html'
    context = request
    return render(request, page , context)

@login_required
def showList(request):
    page = 'FirstApp/dashboard.html'
    context = request
    return render(request, page , context)