from django.db import models
from taggit.managers import TaggableManager
import uuid

# Create your models here.
class TodoModel(models.Model):
    STATUS_OPTIONS = [
        ("O", "Open"),
        ("W", "Working"),
        ("D", "Done"),
        ("v", "Overdue")
    ]
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateField(blank=True,null=True)
    tag= TaggableManager(blank=True)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS)
    timestamp = models.DateTimeField(auto_now_add=True)