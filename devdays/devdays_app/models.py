from django.db import models
from django.contrib.auth.models import User
from devdays_app.tools import get_git_commits, get_git_closed, get_git_opened


class Comment(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.text


class Group(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u"%s %d" % (self.name, self.year)

    def __str__(self):
        return u"%s %d" % (self.name, self.year)


class Event(models.Model):
    name = models.CharField(max_length=100, default='Some DEVDAYS EVENT')
    date = models.DateTimeField()
    length = models.IntegerField(default=3) # it means "duration" 
    state = models.CharField(max_length=100, blank=True, null=True, default='initial')
        # initial | selection | ongoing | past

    def get_link(self):
        return self.date.strftime('%m_%Y')

    def __unicode__(self):
        return u"%s %s" % (self.name, str(self.date))

    def __str__(self):
        return u"%s %s" % (self.name, str(self.date))


class Idea(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, blank=True, null=True, related_name='AuthorUserProfile')
    likes = models.ManyToManyField(User, related_name='LikeUser', blank=True, null=True)
    link = models.CharField(max_length=1024, blank=True, null=True)
    event = models.ForeignKey(Event)

    def likes_n(self):
        return self.likes.count()

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return u"%s" % self.name


class Notification(models.Model):
    date = models.DateTimeField()
    text = models.TextField(blank=True, null=True)
    event = models.ForeignKey(Event)


class Project(models.Model):
    idea = models.ForeignKey(Idea, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2048, blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)
    students = models.ManyToManyField(User, blank=True, null=True, through='ProjectUsers')
    comments = models.ManyToManyField(Comment, blank=True, null=True)
    link = models.CharField(max_length=1024, blank=True, null=True)

    def get_link(self):
        return self.link or self.idea.link

    opened_issues = models.IntegerField(blank=True, null=True, default=-1)
    closed_issues = models.IntegerField(blank=True, null=True, default=-1)
    commits = models.IntegerField(blank=True, null=True, default=-1)

    def get_git_commits(self):
        try:
            return get_git_commits(self.link)
        except:
            return -1

    def get_git_closed(self):
        try:
            return get_git_opened(self.link)
        except:
            return -1

    def get_git_opened(self):
        try:
            return get_git_opened(self.link)
        except:
            return -1

    def __unicode__(self):
        if(self.event is not None):
            return u"Project (event: %s, idea: %s)" % (str(self.event.date), str(self.idea))
        else:
            return u"Project (idea: %s)" % str(self.idea)
        
    def __str__(self):
        if(self.event is not None):
            return u"Project (event: %s, idea: %s)" % (str(self.event.date), str(self.idea))
        else:
            return u"Project (idea: %s)" % str(self.idea)


class ProjectUsers(models.Model):
    user = models.ForeignKey(User, blank=False, null=False)
    project = models.ForeignKey(Project, blank=False, null=False)
    date_joined = models.DateField(auto_now_add=True, blank=True)