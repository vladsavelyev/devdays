from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Comment(models.Model):
    pass
    #text = models.TextField(blank=True, null=True)

    #def __str__(self):
    #    return "%s" % self.text


class Group(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s %d" % (self.name, self.year)



class Idea(models.Model):
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(User, blank=True, null=True, related_name='AutorUserProfile')
    likes = models.ManyToManyField(User, related_name='LikeUser', blank=True, null=True)
    link = models.CharField(max_length=1024, blank=True, null=True)

    def likes_n(self):
        return self.likes.count()

    def __str__(self):
        return "%s" % self.name


class Event(models.Model):
    date = models.DateTimeField()
    length = models.IntegerField(default=3)
    state = models.CharField(max_length=100, blank=True, null=True, default='initial')
        # initial | selection | ongoing | past

    def get_link(self):
        return self.date.strftime('%m_%Y')

    def __str__(self):
        return "Event %s" % str(self.date)


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

    def get_github_stats(self):
        pass
        
    def __str__(self):
        return "Project (event: %s, idea: %s)" % (str(self.event.date), str(self.idea))


#User.regular_users = User.objects.all().filter(is_staff=False).filter(is_superuser=False)
#def getFullUserName(self):
#    return self.first_name + " " + self.last_name
#User.full_name = getFullUserName