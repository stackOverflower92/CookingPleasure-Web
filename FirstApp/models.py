from django.db import models
from django.contrib.auth.models import User
import string


#class MyUser(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE)
  #  photo = models.ImageField()
   # def get_full_name(self):
    #    return '%s %s' % (string.capwords(self.first_name), string.capwords(self.last_name))

    #def __unicode__(self):
     #   return u'%s' % (self.mail)

class Recipe(models.Model):
    Recipe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to = 'FirstApp/photo/')
    class Meta:
        ordering = ('name',)
    def __unicode__(self):
        return u'%s' % (self.name)

class Ingredient(models.Model):
    Ingredient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    recipes = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % (self.name)

class Menu(models.Model):
    Menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % (self.name)


class List(models.Model):
    List_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    class Meta:
        ordering = ('name',)
    def __unicode__(self):
        return u'%s' % (self.name)