
import datetime
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from web.models import *

def view_tasks(request):
    if request.method == 'POST':
        task_form = AddTaskForm(request.POST)
        if task_form.is_valid():
            now = datetime.datetime.now()
            new_task = Task(summary=task_form.cleaned_data['summary'], date=now, complete=False)
            new_task.save()
            return HttpResponseRedirect('/')
    else:
        task_form = AddTaskForm()
    active_tasks = Task.objects.filter(complete=False).order_by('date')
    return render(request, 'web/view_tasks.html', {
        'active_tasks' : active_tasks,
        'task_form' : task_form,
    })



