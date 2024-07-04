import datetime

from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})


def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})


def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form})


def detail_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('index')
    return render(request, 'task_confirm_delete.html', {'task': task})