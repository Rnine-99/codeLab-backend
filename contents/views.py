import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from contents.models import RepoIssue, RepoPr
from contents.serializer import serializers_issue, serializers_pr
from contents.utils import crawl_issue_by_id, crawl_issue_detail
from crawler.models import Repo


# Create your views here.
@csrf_exempt
def get_root_dir(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'msg': "请求方式错误"})
    owner = request.POST.get('owner')
    repo_name = request.POST.get('repo_name')
    repo = Repo.objects.get(owner=owner, repo_name=repo_name)
    return JsonResponse({'success': True, 'root_dir': json.loads(repo.root_dir)})


@csrf_exempt
def get_issue_list_by_id(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'msg': "请求方式错误"})
    program_id = request.POST.get('program_id')
    page = request.POST.get('page')
    issue = RepoIssue.objects.filter(repo_id=program_id).order_by('-issue_id')[(page - 1) * 10:page * 10]
    return JsonResponse({'success': True,
                         'issueNum': RepoIssue.objects.filter(repo_id=program_id).count(),
                         'issueList': serializers_issue(issue, many=True).data})


@csrf_exempt
def get_pr_list_by_id(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'msg': "请求方式错误"})
    program_id = request.POST.get('program_id')
    page = request.POST.get('page')
    pr = RepoPr.objects.filter(repo_id=program_id).order_by('-pr_id')[(page - 1) * 10:page * 10]
    return JsonResponse({'success': True,
                         'issueNum': RepoPr.objects.filter(repo_id=program_id).count(),
                         'issueList': serializers_pr(pr, many=True).data})


@csrf_exempt
def get_issue_detail(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'msg': "请求方式错误"})
    issue_id = request.POST.get('issue_id')
    program_id = request.POST.get('program_id')
    program = Repo.objects.get(id=program_id)
    issue = crawl_issue_detail(program.owner, program.repo_name, issue_id)

