from rest_framework import serializers
from todo.models import TodoModel,Tag



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')
class TodoSerializer(serializers.ModelSerializer):

    due_date = serializers.DateField(required=False)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta():
        model = TodoModel
        fields =  ['title','description','due_date','tags','status']