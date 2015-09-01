from django.db import models
import string


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=100, unique=True)
    mail = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=50)

    def get_full_name(self):
        return '%s %s' % (string.capwords(self.first_name), string.capwords(self.last_name))

    def __unicode__(self):
        return u'%s' % (self.mail)


class Recipe(models.Model):
    Recipe_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ('name',)
    def __unicode__(self):
        return u'%s' % (self.name)

class Ingredient(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    recipes = models.ManyToManyField(Recipe)
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % (self.name)

class Menu(models.Model):
    Menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    recipes = models.ManyToManyField(Recipe)
    class Meta:
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % (self.name)

class List(models.Model):
    List_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    ingredients = models.ManyToManyField(Ingredient)
    class Meta:
        ordering = ('name',)
    def __unicode__(self):
        return u'%s' % (self.name)