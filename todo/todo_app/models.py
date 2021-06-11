from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    details = models.TextField()
    priority = models.IntegerField()
