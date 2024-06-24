from django.shortcuts import render, redirect

from webapp.models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {'tasks', tasks})


def create_task(request):
    if request.method == "POST":
        description = request.POST.get("description")
        status = request.POST.get("status")
        task_date = request.POST.get("task_date")
        Task.objects.create(description=description, status=status, task_date=task_date)
        return redirect("index")
    return render(request, "task_create.html")
