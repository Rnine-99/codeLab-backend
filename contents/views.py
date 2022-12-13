import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from contents.models import RepoIssue, RepoPr
from contents.serializer import serializers_issue, serializers_pr
from contents.utils import *
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
def get_issue_list_by_repo_id(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'msg': "请求方式错误"})
    program_id = request.POST.get('program_id')
    issue = RepoIssue.objects.filter(repo_id=program_id).order_by('-issue_id')
    return JsonResponse({'success': True,
                         'issueNum': RepoIssue.objects.filter(repo_id=program_id).count(),
                         'issueList': serializers_issue(issue, many=True).data})


@csrf_exempt
def get_pr_list_by_repo_id(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'msg': "请求方式错误"})
    program_id = request.POST.get('program_id')
    pr = RepoPr.objects.filter(repo_id=program_id).order_by('-pr_id')
    return JsonResponse({'success': True,
                         'prNum': RepoPr.objects.filter(repo_id=program_id).count(),
                         'prList': serializers_pr(pr, many=True).data})


@csrf_exempt
def get_issue_detail(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'msg': "请求方式错误"})
    issue_id = request.POST.get('issue_id')
    program_id = request.POST.get('program_id')
    program = Repo.objects.get(id=program_id)
    comments = []
    issue = json.loads(crawl_issue_detail(program.owner, program.repo_name, issue_id))
    comment = json.loads(crawl_issue_comment(program.owner, program.repo_name, issue_id))
    for i in comment:
        comments.append({'author': i['user']['login'],
                         'content': i['body'],
                         'time': i['created_at']})
    return JsonResponse({'author': issue['user']['login'],
                         'content': issue['body'],
                         'title': issue['title'],
                         'time': issue['created_at'],
                         'comments': comments})


@csrf_exempt
def get_pr_detail(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'msg': "请求方式错误"})
    pr_id = request.POST.get('pr_id')
    program_id = request.POST.get('program_id')
    program = Repo.objects.get(id=program_id)
    pr = json.loads(crawl_pr_detail(program.owner, program.repo_name, pr_id))
    comments = []
    comment = json.loads(crawl_pr_comment(program.owner, program.repo_name, pr_id))
    for i in comment:
        comments.append({'author': i['user']['login'],
                         'content': i['body'],
                         'time': i['created_at']})
    return JsonResponse({'author': pr['user']['login'],
                         'content': pr['body'],
                         'title': pr['title'],
                         'time': pr['created_at'],
                         'comments': comments})


@csrf_exempt
def get_issue(request):
    if request.method != "POST":
        return JsonResponse({'success': False, 'msg': "请求方式错误"})
    repo_id = request.POST.get('repo_id')
    program = Repo.objects.get(id=repo_id)
    crawl_new_issue_or_pr(program)
    return JsonResponse({'success': True})
