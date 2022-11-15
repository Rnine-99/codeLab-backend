import json
from urllib.request import urlopen
from urllib.request import Request

import yaml


def crawl_owner_repo_root_dir(owner, repo_name):
    with open('../secrets.yaml', 'r') as f:
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
    result = json.loads(response.decode())
    return result
