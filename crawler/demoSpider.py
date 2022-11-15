# a crawler demo: get the github project's star number, fork number, and issue number(Opened and Closed)
from urllib import request
import re
class demoSpider():
    def __init__(self):
        self.name = 'demo'
        self.start_urls = [
                            'https://github.com/vuejs/vue',
                            'https://github.com/expo/expo',
                            'https://github.com/hexojs/hexo',
                            'https://github.com/torvalds/linux',
                            'https://github.com/yuzu-emu/yuzu',
                            'https://github.com/qiurunze123/miaosha'
                          ]

    def get_html(self,urls):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        for url in urls:
            req = request.Request(url, headers=headers)
            response = request.urlopen(req)
            html = response.read().decode('utf-8')# get the html
            issue_url = url + '/issues'
            issue_req = request.Request(issue_url, headers=headers)
            issue_response = request.urlopen(issue_req)
            issue_html = issue_response.read().decode('utf-8')# get the issue page's html
            self.parse_html(html, issue_html)
        

    def parse_html(self, html, issue_html):
        # title
        re_title = re.compile(r'<title>(.*?):.*?</title>')
        title = re.findall(re_title, html)
        # star number
        re_star = re.compile(
            r'aria-label="(.*?) users starred this repository"')
        star = re.findall(re_star, html)
        # fork number
        re_fork = re.compile(
            r'<span id="repo-network-counter" data-pjax-replace="true" data-turbo-replace="true" title="(.*?)" data-view-component="true" class="Counter">.*?</span>')
        fork = re.findall(re_fork, html)
        # Open issues
        re_issues = re.compile(
            r'</svg>\n(.*?) Open\n.*?</a>')
        issues = re_issues.findall(issue_html)
        # Closed issues
        re_closed = re.compile(
            r'</svg>\n(.*?) Closed\n.*?</a>')
        closed = re_closed.findall(issue_html)
        # languages
        re_languages = re.compile(
            r'itemprop="keywords" aria-label="(.*?)" data-view-component="true" class="Progress-item color-bg-success-emphasis">')
        languages = re_languages.findall(html)
        if len(languages) != 0:
            main_language = languages[0].split(' ')[0]
        # commits
        re_commits = re.compile(
            r'<strong>(.*?)</strong>\n.*?<span aria-label="Commits on .*?" class="color-fg-muted d-none d-lg-inline">\n.*?commits')
        commits = re_commits.findall(html)


        # print all information we crawled
        print('title:', title[0])
        print('star:', star[0])
        print('fork:', fork[0])
        print('opend issues:', issues[0].strip())
        print('closed issues:', closed[0].strip())
        if len(languages) != 0:
            print('main language:', main_language)# default: the main language is the first language in the list
        print('commits:', commits[0])
        


    # def write_html(self):
        

    def run(self):
        self.get_html(self.start_urls)



if __name__ == '__main__':
    spider = demoSpider()
    spider.run()
    
