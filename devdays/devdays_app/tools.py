import os
import urllib
import hashlib
from datetime import datetime, timedelta
from lxml import html


pages = {}


def get_raw_page(giturl):
    url = giturl + '/pulse'
    if url in pages:
        page, date_loaded = pages[url]
        if datetime.now() - date_loaded < timedelta(seconds=10):
            return page

    page = html.fromstring(urllib.urlopen(url).read())
    pages[giturl] = page, datetime.now()
    return page


def get_git_opened(giturl):
    page = get_raw_page(giturl)
    try:
        elop = page.xpath('//a[@href="#new-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-opened"]')[0]
    except:
        raise
    return int(elop.tail.strip())


def get_git_closed(giturl):
    page = get_raw_page(giturl)
    try:
        elcl = page.xpath('//a[@href="#closed-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-closed"]')[0]
    except:
        raise
    return int(elcl.tail.strip())


def get_git_commits(giturl):
    page = get_raw_page(giturl)
    try:
        elop = page.xpath('//a[@href="#new-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-opened"]')[0]
    except:
        raise
    return int(page.xpath('//div[@class="section diffstat-summary"]/strong[2]/text()')[0].split(' ')[0])


def get_gravatar_url(request, email, size=80):
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d': 'identicon', 's': str(size)})
    return gravatar_url
