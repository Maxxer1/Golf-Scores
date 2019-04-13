"""golf_scores URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from web import views as web_views

app_name='web'
urlpatterns = [
    path('', web_views.index, name='index'),
    path('golf_courses/', web_views.golf_courses, name='golf_courses'),
    path('delete_course/', web_views.delete_course, name='delete_course'),
    path('scores/', web_views.scores, name='scores'),
    path('delete_score/', web_views.delete_score, name='delete_score'),
]