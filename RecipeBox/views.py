from django.shortcuts import render
from RecipeBox.models import Author, Recipe


def index(request, *args, **kwargs):
    items = Recipe.objects.all()
    return render(request,"hello.html",{'recipes':items})

def detail(request, title):
    items = Recipe.objects.all().filter(title=title)
    return render(request,"recipe.html",{'recipes':items})

def author(request, title,author):
    items = Author.objects.all().filter(name=author)
    return render(request,"author.html",{'author':items})
