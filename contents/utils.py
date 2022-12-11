import json
from urllib.request import urlopen
from urllib.request import Request

import yaml

from contents.models import *


def crawl_owner_repo_root_dir(owner, repo_name):
    with open('./secrets.yaml', 'r') as f:
        SECRETS = yaml.safe_load(f)
    secret_key = SECRETS['AUTHORIZATION_CODE']
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': secret_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }
    url = 'https://api.github.com/repos/{owner}/{repo_name}/contents'.format(owner=owner, repo_name=repo_name)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = response.decode()
    return result


def crawl_issue_by_id(owner, repo_name, page):
    with open('./secrets.yaml', 'r') as f:
        SECRETS = yaml.safe_load(f)
    secret_key = SECRETS['AUTHORIZATION_CODE']
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': secret_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }
    url = 'https://api.github.com/repos/{owner}/{repo_name}/issues?page={page}'. \
        format(owner=owner, repo_name=repo_name, page=page)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = response.decode()
    return result


def crawl_issue_detail(owner, repo_name, issue):
    with open('./secrets.yaml', 'r') as f:
        SECRETS = yaml.safe_load(f)
    secret_key = SECRETS['AUTHORIZATION_CODE']
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': secret_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }
    url = 'https://api.github.com/repos/{owner}/{repo_name}/issues/{id}'. \
        format(owner=owner, repo_name=repo_name, id=issue)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = response.decode()
    return result


# 传入项目模型
def crawl_new_issue_or_pr(program):
    page = 1
    issue_biggest = RepoIssue.objects.filter(repo_id=program.id).order_by('-issue_id').first().issue_id
    while True:
        issue = json.loads(crawl_issue_by_id(program.owner, program.repo_name, page))
        for i in issue:
            if i['id'] == issue_biggest:
                return
            if "pull_request" not in i:
                num = RepoIssue.objects.get(repo_id=program.id, issue_id=i['number'])
                if num is None:
                    RepoIssue.objects.create(repo_id=program.id, issue_id=i['number'])
            else:
                numPr = RepoPr.objects.get(repo_id=program.id, pr_id=i['number'])
                if numPr is None:
                    RepoPr.objects.create(repo_id=program.id, pr_id=i['number'])
        page = page + 1
