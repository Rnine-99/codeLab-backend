from django.contrib import admin
from django.urls import path

from contents.views import *

urlpatterns = [
    path('get_root_dir', get_root_dir),
    path('get_issue_list_by_id', get_issue_list_by_id),
    path('get_issue', get_issue),
    path('get_issue/detail', get_issue_detail),
]
