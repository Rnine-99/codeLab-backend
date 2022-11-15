from django.shortcuts import render
import json
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
    list_repo = []
    if repo_founds:
        for repo in repo_founds:
            list_repo.append({
                'owner': repo.owner,
                'repo_name': repo.repo_name,
                'description': repo.description,
                'stargazers_count': repo.stargazers_count,
                'forks_count': repo.forks_count,
                'open_issues_count': repo.open_issues_count,
                'subscribers_count': repo.subscribers_count,
                'git_url': repo.git_url,
                'clone_url': repo.clone_url,
                'ssh_url': repo.ssh_url,
                'root_dir': repo.root_dir
            })
        return JsonResponse({
            'success': True,
            'data': list_repo
        })
    else:
        return JsonResponse({
            'success': False
        })


