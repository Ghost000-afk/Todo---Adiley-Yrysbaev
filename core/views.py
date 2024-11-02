from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializers
from rest_framework import viewsets



def all_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'core/all_tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
    else:
        form = TaskForm()


def task_info(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'core/task_info.html', {
        'task': task
    })


def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('all_tasks')
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'core/task_update.html', {
        'form': form
    })


def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('all_tasks')
    return render(request, 'core/confirmation.html', {
        'task': task
    })


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers

