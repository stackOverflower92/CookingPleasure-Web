from django.shortcuts import render
from .forms import *
from .models import *
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.loader import render_to_string
import os
import json

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
    formrec = RecipeForm()
    forming = IngredientForm()
    recipes = Recipe.objects.all().filter(user = request.user)
    formmenu = MenuForm(recipes=recipes)
    template = loader.get_template('FirstApp/dashboard.html')
    context = RequestContext(request,{'recipe_list':rec,'menu_list':menu,'list_list':list,'recipeform':formrec,'ingrform':forming,'menuform':formmenu})

    return HttpResponse(template.render(context))

@csrf_protect
@login_required
def addRecipe(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RecipeForm(request.POST,request.FILES)
        up_file = request.FILES['photo']

        if up_file!=None:
            destination = open('FirstApp/templates/FirstApp/photo/' + up_file.name, 'wb+')
            for chunk in up_file.chunks():
                destination.write(chunk)
                destination.close()
            file = up_file.name
        else:
            file = "logo.jpg"

        print(file)
        if form.is_valid():
            recipe = form.save(commit = False)
            recipe.user = request.user
            recipe.photo = file
            recipe.save()
            return HttpResponseRedirect(reverse('FirstApp:home'))
        print('non valido')
    return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
@login_required
def addIngr(request):
    if request.method == 'POST': # If the form has been submitted...
        cont=0
        ingrnum=request.POST.get('ingrn')
        ing_list = request.POST.getlist('name[]')
        q_list = request.POST.getlist('q[]')
        recipe = request.POST.get('recipe')
        rec = Recipe.objects.get(name=recipe)
        print(request.POST)
        while cont < ingrnum:
            name = ing_list[cont]
            q = q_list[cont]
            ingredient = Ingredient(name=name,quantity=q,recipes=rec)
            ingredient.save()
            cont=cont+1
    return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
@login_required
def addMenu(request):
    if request.method == 'POST': # If the form has been submitted...
        recipes = Recipe.objects.all().filter(user = request.user)
        form = MenuForm(request.POST,recipes=recipes)
        if form.is_valid():
            print("sto inserendo il menu")
            menu = form.save(commit = False)
            menu.user = request.user
            menu.save()

            menu = Menu.objects.get(name = form.cleaned_data['name'])
            print(menu)
            recipe_list = request.POST.getlist("recipes")
            print(recipe_list)
            for recips in recipe_list:
                recipe = Recipe.objects.get(Recipe_id=recips, user=request.user)
                print(recipe)
                menu.recipes.add(recipe)

    return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
@login_required
def addList(request):
    if request.method == 'POST': # If the form has been submitted...
        list = request.POST.get("list")
        rec = Recipe.objects.get(name=list)
        ingredients = Ingredient.objects.all().filter(recipes = rec)
        print(ingredients)
        name = "Shopping List for "+list
        list = List(name= name,user=request.user)
        list.save()
        for ingred in ingredients:
            print(ingred)
            list.ingredients.add(ingred)
    return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
@login_required
def addListMenu(request):
    if request.method == 'POST': # If the form has been submitted...
        list = request.POST.get("list")
        menu = Menu.objects.get(name=list,user=request.user)
        recipe_list=[]
        for recipe in menu.recipes.all():
            print(recipe)
            ingred = Ingredient.objects.all().filter(recipes = recipe)
            recipe_list.append(ingred)
            print(ingred)
        name = "Shopping List for "+list
        list = List(name= name,user=request.user)
        list.save()
        for recipe in recipe_list:
            for ingred in recipe:
                print(ingred)
                list.ingredients.add(ingred)
    return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
@login_required
def getRecipe(request):
    try:
        recipename = request.POST.get('recipename')
        user = request.user
        recipe = Recipe.objects.get(name=recipename, user=user)
        viewrecipeform = RecipeForm(instance=recipe)
        ingredient = Ingredient.objects.all().filter(recipes=recipe.Recipe_id).order_by('Ingredient_id')
        form = render_to_string('FirstApp/viewrecipe.html', {'viewrecipeform':viewrecipeform,'ingredient':ingredient},
                                        context_instance=RequestContext(request))
        return HttpResponse(form,status=200)
    except Recipe.DoesNotExist:
        return HttpResponse(u'no recipe',status=400)
    except Exception as e:
        return HttpResponse('%s %s' % (e.message,e.args),status=500)

@csrf_protect
@login_required
def getMenu(request):
    try:
        menuname = request.POST.get('menuname')
        user = request.user
        menu = Menu.objects.get(name=menuname, user=user)
        recipes = menu.recipes
        viewmenuform = MenuForm(instance=menu,recipes=recipes)
        form = render_to_string('FirstApp/viewmenu.html', {'viewmenuform':viewmenuform},
                                        context_instance=RequestContext(request))
        return HttpResponse(form,status=200)
    except Recipe.DoesNotExist:
        return HttpResponse(u'no recipe',status=400)
    except Exception as e:
        return HttpResponse('%s %s' % (e.message,e.args),status=500)

@csrf_protect
@login_required
def getList(request):
    try:
        listname = request.POST.get('listname')
        user = request.user
        list = List.objects.get(name=listname, user=user)
        form = render_to_string('FirstApp/viewlist.html', {'list':list.name,'ingredients':list.ingredients.all()},
                                        context_instance=RequestContext(request))
        return HttpResponse(form,status=200)
    except Recipe.DoesNotExist:
        return HttpResponse(u'no recipe',status=400)
    except Exception as e:
        return HttpResponse('%s %s' % (e.message,e.args),status=500)
