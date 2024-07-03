import datetime

from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {'tasks': tasks})


def create_task(request):
    if request.method == "POST":
        description = request.POST.get("description")
        status = request.POST.get("status")
        task_date = request.POST.get("task_date")
        task_detail = request.POST.get("detail_description")
        Task.objects.create(description=description, status=status, task_date=task_date, detail_description=task_detail)
        return redirect("index")
    return render(request, "task_create.html")


def update_task(request, task_id):
    if request.method == "GET":
        return render(request, "update_task.html", context={"task": get_object_or_404(Task, pk=task_id)})
    else:
        description = request.POST.get("description")
        status = request.POST.get("status")
        task_detail = request.POST.get("detail_description")
        task = get_object_or_404(Task, pk=task_id)
        task.description = description
        task.status = status
        task.task_date = datetime.datetime.now()
        task.detail_description = task_detail
        task.save()
        return redirect("index")


def detail_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})