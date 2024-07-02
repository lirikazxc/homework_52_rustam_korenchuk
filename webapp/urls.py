from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("create/", views.create_task, name="task_create"),
    path("detail/<int:task_id>/", views.detail_task, name="task_detail"),
    path("detail/<int:task_id>/edit/", views.update_task, name="task_update"),
]