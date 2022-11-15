from django.contrib import admin
from django.urls import path
from crawler import views

urlpatterns = [
    path('search_repo_name/', views.search_reponame),
    path('get_info_repo_name/', views.get_info_repo_name),
]
