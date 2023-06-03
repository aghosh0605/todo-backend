from taggit.serializers import (TagListSerializerField,TaggitSerializer)
from rest_framework import serializers
from todo.models import TodoModel


class TodoSerializer(TaggitSerializer,serializers.ModelSerializer):

    due_date = serializers.DateField(required=False)
    tag = TagListSerializerField(required=False)
    
    class Meta():
        model = TodoModel
        fields =  ['title','description','due_date','tag','status']