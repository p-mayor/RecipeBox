from django import forms
from django.forms import ModelForm
from .models import Recipe

class AuthorForm(forms.Form):
    name = forms.CharField(label='name', max_length=30)
    bio = forms.CharField(widget=forms.Textarea)

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title','description','timeRequired','instructions','author']

"""
name = models.CharField(max_length=30)
    bio = models.TextField(max_length=200)
"""