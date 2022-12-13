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
    url = 'http://api.github.com/repos/{owner}/{repo_name}/contents'.format(owner=owner, repo_name=repo_name)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = response.decode()
    return result


def crawl_issue_by_id(owner, repo_name):
    with open('./secrets.yaml', 'r') as f:
        SECRETS = yaml.safe_load(f)
    secret_key = SECRETS['AUTHORIZATION_CODE']
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': "token "+secret_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }
    url = 'https://api.github.com/repos/{owner}/{repo_name}/issues'. \
        format(owner=owner, repo_name=repo_name)
    print(url)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = response.decode()
    return result


def crawl_issue_detail(owner, repo_name, issue):
    with open('./secrets.yaml', 'r') as f:
        SECRETS = yaml.safe_load(f)
    secret_key = SECRETS['AUTHORIZATION_CODE']
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': "token "+ secret_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }
    url = 'https://api.github.com/repos/{owner}/{repo_name}/issues/{id}'. \
        format(owner=owner, repo_name=repo_name, id=issue)
    # print(url)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = response.decode()
    return result


def crawl_pr_detail(owner, repo_name, pr):
    with open('./secrets.yaml', 'r') as f:
        SECRETS = yaml.safe_load(f)
    secret_key = SECRETS['AUTHORIZATION_CODE']
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': "token "+secret_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }
    url = 'https://api.github.com/repos/{owner}/{repo_name}/pulls/{id}'. \
        format(owner=owner, repo_name=repo_name, id=pr)
    # print(url)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = response.decode()
    return result


def crawl_pr_comment(owner, repo_name, pr):
    with open('./secrets.yaml', 'r') as f:
        SECRETS = yaml.safe_load(f)
    secret_key = SECRETS['AUTHORIZATION_CODE']
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': secret_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }
    url = 'https://api.github.com/repos/{owner}/{repo_name}/pulls/{id}/comments'. \
        format(owner=owner, repo_name=repo_name, id=pr)
    # print(url)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = response.decode()
    return result


def crawl_issue_comment(owner, repo_name, pr):
    with open('./secrets.yaml', 'r') as f:
        SECRETS = yaml.safe_load(f)
    secret_key = SECRETS['AUTHORIZATION_CODE']
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': secret_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }
    url = 'https://api.github.com/repos/{owner}/{repo_name}/issues/{id}/comments'. \
        format(owner=owner, repo_name=repo_name, id=pr)
    # print(url)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = response.decode()
    return result

# 传入项目模型
def crawl_new_issue_or_pr(program):
    a = json.loads(crawl_issue_by_id(program.owner, program.repo_name))
    issue_biggest_id = a[0]['number']
    try:
        issue_biggest = RepoIssue.objects.filter(repo_id=program.id).order_by('-issue_id').first().issue_id
    except:
        issue_biggest = 0
    page = 52
    while page > 0:
        try:
            issue = json.loads(crawl_issue_detail(program.owner, program.repo_name, page))
        except:
            print("error at page %d", page)
            page -= 1
            continue
        if len(issue) == 0:
            return
        if issue['number'] == issue_biggest:
            return
        if "pull_request" not in issue:
            try:
                num = RepoIssue.objects.get(repo_id=program.id, issue_id=issue['number'])
            except:
                RepoIssue.objects.create(repo_id=program.id, issue_id=issue['number'], title=issue['title'],
                                         status=issue['state'] == "open")
                print("add issue repo = %d, issue = %d", program.id, issue['number'])
        else:
            try:
                numPr = RepoPr.objects.get(repo_id=program.id, pr_id=issue['number'])
            except:
                RepoPr.objects.create(repo_id=program.id, pr_id=issue['number'], title=issue['title'],
                                      status=issue['state'] == "open")
                print("add pr repo = %d, pr = %d", program.id, issue['number'])
        page -= 1
