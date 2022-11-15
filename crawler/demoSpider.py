from urllib.request import urlopen
from urllib.request import Request


# get the results by owner and repo_name
def crawl_owner_repo_name(headers, owner, repo_name):
    url = 'https://api.github.com/repos/{owner}/{repo_name}'.format(owner=owner, repo_name=repo_name)
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
