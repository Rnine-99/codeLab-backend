from django.contrib import admin
from django.urls import path
from crawler import views

urlpatterns = [
    path('search_reponame/', views.search_reponame()),
    path('get_info_repo_name/<str:owner>/<str:repo_name>/', views.get_info_repo_name(owner=owner, repo_name=repo_name)),
]