
import datetime
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from web.models import *


def add_task(request):
    if request.method == "POST":
        add_task_form = AddTaskForm(request.POST)
        if add_task_form.is_valid():
            now = datetime.datetime.now()
            new_task = Task(summary=add_task_form.cleaned_data['summary'], date=now, complete=False)
            new_task.save()
    return HttpResponseRedirect('/')

def complete_task(request):
    if request.method == "POST":
        complete_task_form = CompleteTaskForm(request.POST)
        if complete_task_form.is_valid():
            now = datetime.datetime.now()
            my_task = Task.objects.filter(id=complete_task_form.cleaned_data['task_id'])[0]
            my_task.complete = True
            my_task.complete_date = now
            my_task.save()
    return HttpResponseRedirect('/')
    
        

def view_tasks(request):
    add_task_form = AddTaskForm()
    active_tasks = Task.objects.filter(complete=False).order_by('date')
    for active_task in active_tasks:
        active_task.complete_task_form = CompleteTaskForm()
        active_task.complete_task_form.task_id = int(active_task.id)
    complete_tasks = Task.objects.filter(complete=True).order_by('date')
    return render(request, 'web/view_tasks.html', {
        'active_tasks' : active_tasks,
        'complete_tasks' : complete_tasks,
        'add_task_form' : add_task_form,
    })



