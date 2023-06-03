from django.db import models
from taggit.managers import TaggableManager
import uuid
from django.core.validators import MinLengthValidator

# Create your models here.
class TodoModel(models.Model):
    STATUS_OPTIONS = [
        ("O", "Open"),
        ("W", "Working"),
        ("D", "Done"),
        ("v", "Overdue")
    ]
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=100,validators=[
            MinLengthValidator(5, 'the field must contain at least 5 characters')
            ])
    description = models.CharField(max_length=1000,validators=[
            MinLengthValidator(10, 'the field must contain at least 10 characters')
            ])
    due_date = models.DateField(blank=True,null=True)
    tag= TaggableManager(blank=True)
    status = models.CharField(max_length=1, choices=STATUS_OPTIONS,default='O')
    timestamp = models.DateTimeField(auto_now_add=True)