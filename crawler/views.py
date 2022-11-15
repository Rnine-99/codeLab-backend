from django.shortcuts import render
import json
from demoSpider import crawl_owner_repo_name, crawl_language
import yaml


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
    print("full_name:", results['full_name'])
    print("description:", results['description'])
    print("stargazers_count:", results['stargazers_count'])
    print("forks_count:", results['forks_count'])
    print("open_issues_count:", results['open_issues_count'])
    print("subscribers_count:", results['subscribers_count'])
    print("git_url:", results['git_url'])
    print("clone_url:", results['clone_url'])
    print("ssh_url:", results['ssh_url'])

