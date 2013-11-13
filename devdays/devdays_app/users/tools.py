import urllib, hashlib

def getGravatarUrl(request, email, size = 80):
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':'identicon', 's':str(size)})
    return gravatar_url