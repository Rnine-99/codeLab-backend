from django.shortcuts import render
import json
from demoSpider import crawl_owner_repo_name, crawl_language
import yaml
from models import Repo


def get_info_repo_name(request, owner, repo_name):
    # Modify the GitHub token value
    with open('../secrets.yaml', 'r') as f:
        SECRETS = yaml.safe_load(f)
    secret_key = SECRETS['SECRET_KEY']
    headers = {'User-Agent': 'Mozilla/5.0',
               'Authorization': secret_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }
    owner = 'vuejs'
    repo_name = 'vue'
    results = crawl_owner_repo_name(headers, owner, repo_name)
    Repo.objects.create(full_name=results['full_name'],
                        description=results['description'],
                        stargazers_count=results['stargazers_count'],
                        forks_count=results['forks_count'],
                        open_issues_count=results['open_issues_count'],
                        subscribers_count=results['subscribers_count'],
                        git_url=results['git_url'],
                        clone_url=results['clone_url'],
                        ssh_url=results['ssh_url'])
