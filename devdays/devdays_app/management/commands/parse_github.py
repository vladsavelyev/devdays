from django.core.management.base import BaseCommand, CommandError
from devdays_app.models import Project
import urllib
from lxml import html


class Command(BaseCommand):
    help = 'Updates github stats for projects.'

    def handle(self, *args, **options):
        self.stdout.write('Starting updating projects.\n')

        for p in Project.objects.all():
            link = p.link or p.idea.link
            if link and link.find('github'):
                url = link + '/pulse'
                page = html.fromstring(urllib.urlopen(url).read())
                try:
                    elop = page.xpath('//a[@href="#new-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-opened"]')[0]
                    p.opened_issues = int(elop.tail.strip())

                    elcl = page.xpath('//a[@href="#closed-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-closed"]')[0]
                    p.closed_issues = int(elcl.tail.strip())

                    p.commits = int(page.xpath('//div[@class="section diffstat-summary"]/strong[2]/text()')[0].split(' ')[0])
                    p.save()
                    self.stdout.write('  updated %s.\n' % p.idea.name)

                except Exception, e:
                    self.stderr.write('  cannot parse %s\n' % p.idea.name)
