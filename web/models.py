from django.db import models

class Task(models.Model):
    summary = models.CharField(max_length=4096)
    date = models.DateTimeField()
    complete = models.BooleanField()
    complete_date = models.DateTimeField(blank=True, null=True)
    complete_task_form = None
    # tmp variable for holding comments as they're handed back to the template when being rendered
    comments = None

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

class CompleteTaskForm(forms.Form):
    task_id = forms.CharField()

class AddCommentForm(forms.Form):
    comment = forms.CharField(max_length=4096)


