from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Comment(models.Model):
    text = models.CharField(max_length=20000, blank=True, null=True)

    def __str__(self):
        return "%s" % self.text


class Group(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s %d" % (self.name, self.year)


class Role(models.Model):
    name = models.CharField(max_length=1024)  # student | prepod | admin

    def __str__(self):
        return "%s" % self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    group = models.ForeignKey(Group, blank=True, null=True)
    role = models.ForeignKey(Role, blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)


# http://stackoverflow.com/questions/44109/extending-the-user-model-with-custom-fields-in-django
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Idea(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=30000, blank=True, null=True)
    autor = models.ForeignKey(UserProfile, blank=True, null=True, related_name='AutorUserProfile')
    likes = models.ManyToManyField(UserProfile, related_name='LikeUserProfile', blank=True, null=True)
    link = models.CharField(max_length=1024, blank=True, null=True)

    def likes_n(self):
        return self.likes.count()

    def __str__(self):
        return "%s" % self.name


class Event(models.Model):
    date = models.DateTimeField()
    length = models.IntegerField(default=3)
    state = models.CharField(max_length=100, blank=True, null=True, default='initial')
      # initial | poll | active | complete

    def __str__(self):
        return "Event %s" % str(self.date)


class Notification(models.Model):
    date = models.DateTimeField()
    text = models.TextField(blank=True, null=True)
    event = models.ForeignKey(Event)


class Project(models.Model):
    idea = models.ForeignKey(Idea, blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)
    students = models.ManyToManyField(UserProfile, blank=True, null=True)
    comments = models.ManyToManyField(Comment, blank=True, null=True)
    link = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return "Project (event: %s, idea: %s)" % (str(self.event.date), str(self.idea))

