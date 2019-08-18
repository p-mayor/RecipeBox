from django.shortcuts import render, HttpResponseRedirect,reverse
from RecipeBox.models import Author, Recipe
from RecipeBox.forms import AuthorForm, RecipeForm


def index(request, *args, **kwargs):
    items = Recipe.objects.all()
    return render(request,"hello.html",{'recipes':items})

def detail(request, title):
    items = Recipe.objects.all().filter(title=title)
    return render(request,"recipe.html",{'recipes':items})

def author(request,author):
    items = Author.objects.all().filter(name=author)
    return render(request,"author.html",{'author':items})

def addAuthor(request,*args,**kwargs):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            Author.objects.create(
                name = data['name'],
                bio = data['bio'],
            )
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('homepage'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthorForm()
    
    return render(request,"addAuthor.html",{'form':form})


def addRecipe(request,*args,**kwargs):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RecipeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            Recipe.objects.create(
                title = data['title'],
                description = data['description'],
                timeRequired = data['timeRequired'],
                instructions = data['instructions'],
                author = data['author']
            )
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('homepage'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RecipeForm()
    
    return render(request,"addRecipe.html",{'form':form})