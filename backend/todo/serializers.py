from taggit.serializers import (TagListSerializerField,TaggitSerializer)
from rest_framework import serializers
from todo.models import TodoModel
from django.core.validators import MinLengthValidator

class TodoSerializer(TaggitSerializer,serializers.ModelSerializer):
    STATUS_OPTIONS = [
        ("O", "Open"),
        ("W", "Working"),
        ("D", "Done"),
        ("v", "Overdue")
    ]
    title = serializers.CharField(max_length=100,validators=[
            MinLengthValidator(5, 'the field must contain at least 5 characters')
            ])
    description = serializers.CharField(max_length=1000,validators=[
            MinLengthValidator(10, 'the field must contain at least 10 characters')
            ])
    due_date = serializers.DateField(required=False)
    tag = TagListSerializerField(required=False)
    status = serializers.ChoiceField(choices=STATUS_OPTIONS,default='O')
    
    class Meta():
        model = TodoModel
        fields =  ['title','description','due_date','tag','status']