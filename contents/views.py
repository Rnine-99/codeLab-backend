import json

from django.http import JsonResponse
from django.shortcuts import render

from crawler.models import Repo


# Create your views here.
def get_root_dir(request):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'msg': "请求方式错误"})
    owner = request.POST.get('owner')
    repo_name = request.POST.get('repo_name')
    repo = Repo.objects.get(owner=owner, repo_name=repo_name)
    return JsonResponse({'success': True, 'root_dir': json.loads(repo.(root_dir))})
