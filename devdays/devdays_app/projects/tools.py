
import urllib
from lxml import html

TEST_GIT_URL = 'https://github.com/vladsaveliev/devdays/'  
def getRawPage(giturl):
    url = giturl + "pulse"
    return html.fromstring(urllib.urlopen(url).read())    


def getGitTasks(giturl = TEST_GIT_URL):
    page = getRawPage(giturl)
    elcl = page.xpath('//a[@href="#closed-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-closed"]')[0]
    closed = int(elcl.tail.strip())
    
    elop = page.xpath('//a[@href="#new-issues"]/span[@class="num"]/span[@class="octicon octicon-issue-opened"]')[0]
    opened = int(elop.tail.strip())
    return (opened, closed)
