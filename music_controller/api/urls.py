# Stores URLS local to app
from django.urls import path
# Function created in views
from .views import main

urlpatterns = [
    path('home', main),
    path('', main)
]