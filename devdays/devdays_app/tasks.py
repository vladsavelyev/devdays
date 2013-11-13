from celery.task import task
from devdays_app.models import Project
from celery.contrib import rdb
from celery.utils.log import get_task_logger
import urllib
import hashlib
from datetime import datetime, timedelta
from lxml import html

logger = get_task_logger(__name__)

@task()
def parse_github(links):
    print 'parse_github'
    logger.info('logger parse_github')

    ps = Project.objects.all()

    for p in ps:
        if p.link and p.link.find('github'):
            url = p.link + '/pulse'
            page = html.fromstring(urllib.urlopen(url).read())
            try:
                print 'parse_github try'
                logger.info('logger parse_github try')

                elop = page.xpath('//a[@href="#new-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-opened"]')[0]
                p.opened_issues = int(elop.tail.strip())
                p.save()

                elcl = page.xpath('//a[@href="#closed-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-closed"]')[0]
                p.closed_issues = int(elcl.tail.strip())
                p.save()

                p.commits = int(page.xpath('//div[@class="section diffstat-summary"]/strong[2]/text()')[0].split(' ')[0])
                p.save()

            except:
                pass
