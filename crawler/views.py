from django.shortcuts import render
import json

from crawler.serializer import serializers_repo
from demoSpider import crawl_owner_repo_name, crawl_language
import yaml
from models import Repo
from django.http import JsonResponse


def get_info_repo_name(request, owner, repo_name):
    # owner = 'vuejs'
    # repo_name = 'vue'
    results = crawl_owner_repo_name(owner, repo_name)
    Repo.objects.create(owner=owner,
                        repo_name=repo_name,
                        description=results['description'],
                        stargazers_count=results['stargazers_count'],
                        forks_count=results['forks_count'],
                        open_issues_count=results['open_issues_count'],
                        subscribers_count=results['subscribers_count'],
                        git_url=results['git_url'],
                        clone_url=results['clone_url'],
                        ssh_url=results['ssh_url'])


def search_reponame(request):
    repo_name = request.POST.get('repo_name')
    repo_founds = Repo.objects.filter(repo_name=repo_name)
    list_repo = serializers_repo(repo_founds, many=True).data
    if repo_founds:
        return JsonResponse({
            'success': True,
            'data': list_repo
        })
    else:
        return JsonResponse({
            'success': False
        })

