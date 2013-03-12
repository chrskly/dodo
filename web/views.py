
import datetime
from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.timezone import utc
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
    # Group complete tasks by day for summary of things done
    now = datetime.datetime.now().replace(tzinfo=utc)
    monday_found = False
    complete_tasks = []
    minus_days = 0
    witching_hour = datetime.datetime(now.year, now.month, now.day, 23, 59).replace(tzinfo=utc)
    while not monday_found:
        before_this_time = witching_hour - datetime.timedelta(days=minus_days)
        but_after_this_time = witching_hour - datetime.timedelta(days=minus_days + 1)
        print "Between %s and %s" % (before_this_time, but_after_this_time)
        t_tasks = Task.objects.filter(complete=True, complete_date__lt=before_this_time, complete_date__gt=but_after_this_time).order_by('-complete_date')
        print "t_tasks %s" % t_tasks
        complete_tasks.append( t_tasks )
        minus_days += 1
        if before_this_time.weekday() == 0:
            monday_found = True
        if minus_days > 6:
            monday_found = True
    #complete_tasks = Task.objects.filter(complete=True).order_by('date')
    print "Complete tasks %s" % complete_tasks
    return render(request, 'web/view_tasks.html', {
        'active_tasks' : active_tasks,
        'complete_tasks' : complete_tasks,
        'add_task_form' : add_task_form,
    })



