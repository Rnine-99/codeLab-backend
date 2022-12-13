from django.contrib import admin
from django.urls import path

from contents.views import *

urlpatterns = [
    path('get_root_dir', get_root_dir),
    path('getIssueListById', get_issue_list_by_repo_id),
    path('getPrListById', get_pr_list_by_repo_id),
    path('get_issue', get_issue),
    path('getIssueById', get_issue_detail),
    path('getPrById', get_pr_detail),
    path('crawlContributor', crawl_contributor),
]
