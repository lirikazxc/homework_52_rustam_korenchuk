from django.db import models

class Task(models.Model):
    status_choices = [
        ('new', "Новая"),
        ('in_progress', "В процессе"),
        ('done', "Сделано"),
    ]

    status = models.CharField(max_length=30, choices=status_choices, default="New")
    description = models.CharField(max_length=200)
    task_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.description