from django.db import models


class Group(models.Model):
    name = models.CharField()
    year = models.IntegerField()


class Student(models.Model):
    name = models.CharField()
    surname = models.CharField(blank=True, null=True)
    group = models.ForeignKey(Group, blank=True, null=True)


class Event(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    projects = models.ManyToManyField(Project)


class Project(models.Model):
    name = models.CharField()
    description = models.CharField(blank=True, null=True)
    students = models.ManyToManyField(Student)
    comments = models.ManyToManyField(Comment)


class Comment(models.Model):
    text = models.CharField(blank=True, null=True)