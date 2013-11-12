
# import code for encoding urls and generating md5 hashes
from django.http import HttpRequest
import urllib, hashlib
import sys


def getGravatarUrl(request, email, size = 80):
    default = 'https://dl.dropboxusercontent.com/u/34699053/user_avatar_default.jpg'
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
    return gravatar_url