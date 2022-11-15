from django.contrib import admin
from django.urls import path

from contents.views import *

urlpatterns = [
    path('get_root_dir/', get_root_dir),
]
