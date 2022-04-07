from importlib.resources import path
from unittest.mock import patch
from django.contrib import admin
from django.urls import include, path
from recipes.urls import home

urlpatterns = [
    path('', home)
]
