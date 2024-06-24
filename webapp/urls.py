from django.urls import path
import views

urlpatterns = [
    path("", views.index),
    path("create/", views.create_task),
]