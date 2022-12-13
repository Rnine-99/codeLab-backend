from django.shortcuts import render
import json

from django.views.decorators.csrf import csrf_exempt

from contents.utils import crawl_owner_repo_root_dir
from crawler.demoSpider import crawl_owner_repo_name
from crawler.serializer import serializers_repo
import yaml
from crawler.models import Repo
from contents.models import RepoIssue, RepoPr, RepoContributers
from contents.serializer import serializers_issue, serializers_pr, serializers_contributers
from django.http import JsonResponse


@csrf_exempt
def get_info_repo_name(request):
    owner = request.POST.get('owner')
    repo_name = request.POST.get('repo_name')
    results = crawl_owner_repo_name(owner, repo_name)
    print(results['description'])
    Repo.objects.create(owner=owner,
                        repo_name=repo_name,
                        description=results['description'],
                        stargazers_count=results['stargazers_count'],
                        forks_count=results['forks_count'],
                        open_issues_count=results['open_issues_count'],
                        subscribers_count=results['subscribers_count'],
                        git_url=results['git_url'],
                        clone_url=results['clone_url'],
                        ssh_url=results['ssh_url'],
                        root_dir=crawl_owner_repo_root_dir(owner, repo_name),
                        update_time=results['updated_at'],
                        language=results['language']
                        )

    return JsonResponse({'success': True})


@csrf_exempt
def search_reponame(request):
    repo_name = request.POST.get('repo_name')
    repo_founds = Repo.objects.filter(repo_name=repo_name)
    list_repo = serializers_repo(repo_founds, many=True).data
    if repo_founds:
        return JsonResponse({
            'success': True,
            'info': list_repo,
        })
    else:
        return JsonResponse({
            'success': False
        })


@csrf_exempt
def get_detail_by_id(request):
    id = request.POST.get('program_id')
    repo = Repo.objects.get(id=id)
    issue_list = RepoIssue.objects.filter(repo_id=id).order_by('-issue_id')[0:6]
    pr_list = RepoPr.objects.filter(repo_id=id).order_by('-pr_id')[0:6]
    contributor_list = RepoContributers.objects.filter(repo_id=id)
    return JsonResponse({
        'success': True,
        'info': serializers_repo(repo).data,
        'issue_list': serializers_issue(issue_list, many=True).data,
        'pr_list': serializers_pr(pr_list, many=True).data,
        'contributor_list': serializers_contributers(contributor_list, many=True).data,
    })


@csrf_exempt
def get_program_by_name(request):
    repo_name = request.POST.get('name')
    # search for repo_name like name
    repo = Repo.objects.filter(repo_name__contains=repo_name)
    return JsonResponse({'success': True, 'info': serializers_repo(repo, many=True).data})

