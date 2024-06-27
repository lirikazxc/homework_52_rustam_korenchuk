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
        Task.objects.create(description=description, status=status, task_date=task_date)
        return redirect("index")
    return render(request, "task_create.html")


def detail_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})