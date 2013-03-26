import datetime
from django.utils.timezone import utc
from django.utils.dateformat import *
from django.db import models
import math

class Task(models.Model):
    summary = models.CharField(max_length=4096)
    date = models.DateTimeField()
    complete = models.BooleanField()
    complete_date = models.DateTimeField(blank=True, null=True)
    complete_task_form = None
    # tmp variable for holding comments as they're handed back to the template when being rendered
    comments = None

    def __unicode__(self):
        return self.summary

    def days_old(self):
        now = datetime.datetime.now().replace(tzinfo=utc)
        difference = self.date - now
        return int(math.fabs(difference.days))

    def pretty_date(self):
        df = DateFormat(self.complete_date)
        return df.format('D jS F')

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

class DeleteTaskForm(forms.Form):
    task_id = forms.CharField()

class AddCommentForm(forms.Form):
    comment = forms.CharField(max_length=4096)


