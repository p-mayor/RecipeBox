"""RecipeBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RecipeBox.views import index
from RecipeBox.models import Author,Recipe
from . import views
from django.contrib.auth import views as auth_views #distinguish views
admin.site.register(Author)
admin.site.register(Recipe)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='homepage'),
    path('recipe/<str:title>/', views.detail, name='detail'),
    path('author/<str:author>/', views.author, name='author'),
    path('addauthor/',views.addAuthor,name='addAuthor'),
    path('addrecipe/',views.addRecipe,name='addRecipe'),
    # path('adduser/',views.addUser,name='addUser'),
    path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    
]
