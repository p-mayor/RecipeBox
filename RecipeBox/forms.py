from django import forms
from django.forms import ModelForm
from .models import Recipe,Author
from django.contrib.auth.models import User

class AuthorForm(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    password = forms.CharField(label='password', max_length=30)
    bio = forms.CharField(widget=forms.Textarea)
    
    # class Meta:
    #     model = Author
    #     fields = ['name','bio','password']
    #     # fields = ['user']

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','description','timeRequired','instructions','author']

# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username','password']

"""
name = models.CharField(max_length=30)
    bio = models.TextField(max_length=200)
"""