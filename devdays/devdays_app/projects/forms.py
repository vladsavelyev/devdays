# coding=utf-8
__author__ = 'annie'
from django.forms import forms, CharField, URLField, Textarea


class CreateIdea(forms.Form):
    name = CharField()
    description = CharField(widget=Textarea, initial=u'Введите описание')
    autor = CharField()
    link = URLField(required=False)