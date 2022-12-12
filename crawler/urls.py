from django.contrib import admin
from django.urls import path
from crawler import views

urlpatterns = [
    path('search_repo_name/', views.search_reponame),
    path('getInfoRepoName/', views.get_info_repo_name),
    path('getDetailById/', views.get_detail_by_id),
    path('getProgramByName/', views.get_program_by_name),
]
