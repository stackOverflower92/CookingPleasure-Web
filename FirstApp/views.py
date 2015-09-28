from django.shortcuts import render
from .forms import *
from .models import *
from CookingPleasureLD import settings
from django.core.mail import send_mail
from django.template import RequestContext, loader
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template.loader import render_to_string
from django.core.mail import send_mail
import os

def index(request):
    recipe_list = Recipe.objects.order_by('-pub_date')
    template = loader.get_template('FirstApp/index.html')
    context = RequestContext(request, {
        'recipe_list': recipe_list,
    })
    return HttpResponse(template.render(context))

def logins(request):

    if request.method == 'POST': # If the form has been submitted...
        print('right post')
        form = LoginForm(request.POST)
        if form.is_valid():
            print('right form')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(request.POST)
            user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                print('user active')
                login(request,user)
                return HttpResponseRedirect(reverse('FirstApp:home'))

    template = loader.get_template('FirstApp/login.html')
    form = LoginForm()
    form1 = MyRegistrationForm()
    context = RequestContext(request,{'form':form,'form1': form1 })
    return HttpResponse(template.render(context))
   # return HttpResponseRedirect(reverse('FirstApp:logs'))

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


@login_required
def home(request):
    rec = Recipe.objects.all().filter(user=request.user)
    menu = Menu.objects.all().filter(user=request.user)
    list = List.objects.all().filter(user=request.user)
    formrec = RecipeForm()
    recipes = Recipe.objects.all().filter(user = request.user)
    formmenu = MenuForm(recipes=recipes)
    template = loader.get_template('FirstApp/dashboard.html')
    context = RequestContext(request,{'recipe_list':rec,'menu_list':menu,'list_list':list,'recipeform':formrec,'menuform':formmenu})

    return HttpResponse(template.render(context))

@csrf_protect
@login_required
def addRecipe(request):
    if request.method == 'POST': # If the form has been submitted...
        form = RecipeForm(request.POST,request.FILES)
        up_file = request.FILES['photo']
        destination = open('FirstApp/templates/FirstApp/photo/' + request.POST.get('name') + "_" + request.user.username + "_" + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
            destination.close()
        file = request.POST.get('name') + "_" + request.user.username + "_" + up_file.name

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
        rec = Recipe.objects.get(name=list,user=request.user)
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
        ingredient = Ingredient.objects.all().filter(recipes=recipe.Recipe_id).order_by('Ingredient_id')
        rec = render_to_string('FirstApp/viewrecipe.html', {'recipe':recipe,'ingredient':ingredient},
                                        context_instance=RequestContext(request))
        return HttpResponse(rec,status=200)
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
        recipes = menu.recipes.all()
        form = render_to_string('FirstApp/viewmenu.html', {'menu':menu,'recipes':recipes},
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

@csrf_protect
@login_required
def deleteRecipe(request):
    if request.method == 'POST': # If the form has been submitted...

        recipe = request.POST.get("recipe")

        recipe = Recipe.objects.get(name=recipe,user=request.user)
        #os.remove("template/FirstApp/photo/"+recipe.photo)
        Ingredient.objects.filter(recipes=recipe,recipes_id=recipe.Recipe_id).delete()
        recipe.delete()
    return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
@login_required
def deleteMenu(request):
    if request.method == 'POST': # If the form has been submitted...
        Menu.objects.filter(name=request.POST.get('menu'),user=request.user).delete()

    return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
@login_required
def deleteList(request):
    if request.method == 'POST': # If the form has been submitted...
        print(request.POST.get('list'))
        List.objects.filter(name=request.POST.get('list'),user=request.user).delete()
    return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
def contactUs(request):
    if request.method == 'POST': # If the form has been submitted...
        print ("Sending Email")
        mail_title = request.POST.get('name')
        message = "From: " + request.POST.get('email') + "\nUser: " + request.POST.get('name') + "\nSubject:\n" + request.POST.get('message')
        print(message)
        send_mail(mail_title, message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_TO_EMAIL],fail_silently=False)
        print ("Email Sent")
        return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
@login_required
def mailRecipe(request):
    if request.method == 'POST': # If the form has been submitted...
        user=request.user
        print(user.email);
        recipe = Recipe.objects.get(name=request.POST.get("recipename"), user=user)
        ingredient_list = Ingredient.objects.all().filter(recipes=recipe.Recipe_id).order_by('Ingredient_id')
        print ("Sending Email")
        mail_title = "Cooking Pleasure: " + recipe.name
        message = "Recipe name: " + recipe.name + "\nAuthor: " + recipe.author + "\nContent:\n" + recipe.content + "\nIngredients:"
        for ingredient in ingredient_list:
            message= message + "\n" + ingredient.name + ", " + ingredient.quantity
        send_mail(mail_title, message, settings.DEFAULT_FROM_EMAIL, [user.email],fail_silently=False)
        print ("Email Sent")
        return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
@login_required
def mailMenu(request):
    if request.method == 'POST': # If the form has been submitted...
        user=request.user
        print(user.email);
        menu = Menu.objects.get(name=request.POST.get("menuname"), user=user)
        print ("Sending Email")
        mail_title = "Cooking Pleasure: " + menu.name
        message = "Menu name: " + menu.name + "\nRecipes: "
        for recipe in menu.recipes.all():
            message= message + "\n" + recipe.name + ", " + recipe.author
        send_mail(mail_title, message, settings.DEFAULT_FROM_EMAIL, [user.email],fail_silently=False)
        print ("Email Sent")
        return HttpResponseRedirect(reverse('FirstApp:home'))

@csrf_protect
@login_required
def mailList(request):
    if request.method == 'POST': # If the form has been submitted...
        user=request.user
        print(user.email);
        list = List.objects.get(name=request.POST.get("listname"), user=user)
        print ("Sending Email")
        mail_title = "Cooking Pleasure: " + list.name
        message = list.name + ":\nIngredients:"
        for ingredient in list.ingredients.all():
            message= message + "\n" + ingredient.name + ", " + ingredient.quantity

        send_mail(mail_title, message, settings.DEFAULT_FROM_EMAIL, [user.email],fail_silently=False)
        print ("Email Sent")
        return HttpResponseRedirect(reverse('FirstApp:home'))
