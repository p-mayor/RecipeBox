from django.shortcuts import render, HttpResponseRedirect,reverse
from RecipeBox.models import Author, Recipe
from RecipeBox.forms import AuthorForm, RecipeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User


def index(request, *args, **kwargs):
    items = Recipe.objects.all()
    return render(request,"hello.html",{'recipes':items})

def detail(request, title):
    items = Recipe.objects.all().filter(title=title)
    return render(request,"recipe.html",{'recipes':items})

def author(request,author):
    items = Author.objects.all().filter(name=author)
    return render(request,"author.html",{'author':items})
    
@staff_member_required
def addAuthor(request,*args,**kwargs):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthorForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            u = User.objects.create_user(username=data['name'],password=data['password'])
            Author.objects.create(
                user = u,
                name = data['name'],
                bio = data['bio'],
            )
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('homepage'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AuthorForm()
    
    return render(request,"addAuthor.html",{'form':form})

@login_required
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


# @staff_member_required
# def addUser(request,*args,**kwargs):
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = UserForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             data = form.cleaned_data
#             User.objects.create_user(
#                 username = data['username'],
#                 password = data['password'],
#             )
#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse('homepage'))

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = UserForm()
    
#     return render(request,"addUser.html",{'form':form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return HttpResponseRedirect(reverse('login'))
    else:
        form = UserCreationForm()
    return render(request, "register.html",{'form':form})