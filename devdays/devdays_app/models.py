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


class Idea(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(User, blank=True, null=True, related_name='AutorUserProfile')
    likes = models.ManyToManyField(User, related_name='LikeUser', blank=True, null=True)
    link = models.CharField(max_length=1024, blank=True, null=True)

    def likes_n(self):
        return self.likes.count()

    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self):
        return u"%s" % self.name


class Event(models.Model):
    date = models.DateTimeField()
    length = models.IntegerField(default=3)
    state = models.CharField(max_length=100, blank=True, null=True, default='initial')
        # initial | selection | ongoing | past

    def get_link(self):
        return self.date.strftime('%m_%Y')

    def __unicode__(self):
        return u"Event %s" % str(self.date)

    def __str__(self):
        return u"Event %s" % str(self.date)


class Notification(models.Model):
    date = models.DateTimeField()
    text = models.TextField(blank=True, null=True)
    event = models.ForeignKey(Event)


class Project(models.Model):
    idea = models.ForeignKey(Idea, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=2048, blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)
    students = models.ManyToManyField(User, blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True, null=True)
    link = models.CharField(max_length=1024, blank=True, null=True)

    opened_issues = models.IntegerField(blank=True, null=True)
    closed_issues = models.IntegerField(blank=True, null=True)
    commits = models.IntegerField(blank=True, null=True)

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
        return u"Project (event: %s, idea: %s)" % (str(self.event.date), str(self.idea))
        
    def __str__(self):
        return u"Project (event: %s, idea: %s)" % (str(self.event.date), str(self.idea))
