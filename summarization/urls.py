from django.contrib import admin
from django.urls import URLPattern, path, include, re_path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.summarize, name="summarize")
]
