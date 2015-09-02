__author__ = 'diego'

from django import forms
from django.contrib.auth.models import User,UserManager   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import hashers


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'inputEmail','placeholder':'Email'}),required = True)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'inputFirstName','placeholder':'Name'}),required = True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'inputLastName','placeholder':'Surname'}),required = True)
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'inputUser','placeholder':'Username'}),required = True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password', 'id':'inputPassword1', 'class':'form-control','placeholder':'Password'}),required = True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password', 'id':'inputPassword2', 'class':'form-control','placeholder':'Confirm Password'}),required = True)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')

    def save(self,commit = True):
        if (self.cleaned_data['password1']==self.cleaned_data['password2']):
            user = super(MyRegistrationForm, self).save(commit = False)
            user.nickname = self.cleaned_data['username']
            user.email = self.cleaned_data['email']
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.password = hashers.make_password(self.cleaned_data['password1'], salt=None, hasher='default')
            if commit:
                user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','id':'inputEmail','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password', 'id':'inputPassword', 'class':'form-control','placeholder':'Password'}))

