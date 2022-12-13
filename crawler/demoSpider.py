import json
from urllib.request import urlopen
from urllib.request import Request

import yaml


# get the results by owner and repo_name
def crawl_owner_repo_name(owner, repo_name):
    with open('./secrets.yaml', 'r') as f:
        SECRETS = yaml.safe_load(f)
    secret_key = SECRETS['AUTHORIZATION_CODE']
    headers = {'User-Agent': 'Mozilla/5.0 3578.98 Safari/537.36',
               'Authorization': secret_key,
               'Content-Type': 'application/json',
               'Accept': 'application/json'
               }
    url = 'https://api.github.com/repos/{owner}/{repo_name}'.format(owner=owner, repo_name=repo_name)
    print(url)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = json.loads(response.decode())

    return result


# get the results by language
def crawl_language(headers, language):
    url = 'https://api.github.com/search/repositories?q=language:{language}&sort=stars'.format(language=language)
    req = Request(url, headers=headers)
    response = urlopen(req).read()
    result = json.loads(response.decode())
    return result
