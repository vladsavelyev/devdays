from django.db import models


class Comment(models.Model):
    text = models.CharField(max_length=20000, blank=True, null=True)


class Group(models.Model):
    name = models.CharField(max_length=1024, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)


class Student(models.Model):
    name = models.CharField(max_length=1024)
    surname = models.CharField(max_length=1024, blank=True, null=True)
    group = models.ForeignKey(Group, blank=True, null=True)


class Idea(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=30000, blank=True, null=True)
    autor = models.ForeignKey(Student, blank=True, null=True, related_name='AutorStudent')
    likes = models.ManyToManyField(Student, related_name='LikeStudent')


class Project(models.Model):
    idea = models.ForeignKey(Idea, blank=True, null=True)
    students = models.ManyToManyField(Student)
    comments = models.ManyToManyField(Comment)


class Event(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    projects = models.ManyToManyField(Project)
