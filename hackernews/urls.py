"""hackernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views

from story.views import search, frontpage, story,submit,newest,vote
from core.views import signupview

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('s/<int:story_id>/', story, name='story'),
    path('s/<int:story_id>/vote', vote, name='vote'),
    path('u/', include('userprofile.urls')),
    path('newest/', newest, name='newest'),
    path('search/', search, name='search'),
    path('submit/', submit, name='submit'),
    path('signup/', signupview, name='signup'),
    path('login/', views.LoginView.as_view(template_name= 'login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
