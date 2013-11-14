from celery.task import task
from celery.contrib import rdb
from celery.utils.log import get_task_logger
import urllib
import hashlib
from datetime import datetime, timedelta
from lxml import html

#logger = get_task_logger(__name__)


@task(name='parse_github')
def parse_github(links):
    print 'parse_github'

    logger = parse_github.get_logger()

    logger.info('logger parse_github')

    opened_issues, closed_issues, commits = None, None, None
    for link in links:
        print link

        if link and link.find('github'):
            url = link + '/pulse'
            page = html.fromstring(urllib.urlopen(url).read())
            try:
                print 'parse_github try'
                logger.info('logger parse_github try')

                elop = page.xpath('//a[@href="#new-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-opened"]')[0]
                opened_issues = int(elop.tail.strip())

                elcl = page.xpath('//a[@href="#closed-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-closed"]')[0]
                closed_issues = int(elcl.tail.strip())

                commits = int(page.xpath('//div[@class="section diffstat-summary"]/strong[2]/text()')[0].split(' ')[0])

            except:
                pass

    return opened_issues, closed_issues, commits