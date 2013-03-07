from django.db import models

class Task(models.Model):
    summary = models.CharField(max_length=4096)
    date = models.DateTimeField()
    complete = models.BooleanField()

class Comment(models.Model):
    task = models.ForeignKey(Task)
    date = models.DateTimeField()
    comment = models.TextField()

#
# Forms
#
from django import forms

class AddTaskForm(forms.Form):
    summary = forms.CharField(max_length=4096)

class AddCommentForm(forms.Form):
    comment = forms.CharField(max_length=4096)

