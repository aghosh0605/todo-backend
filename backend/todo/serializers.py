from rest_framework import serializers
from todo.models import TodoModel, Tag
from datetime import date
from django.core.validators import MinValueValidator, ValidationError


def no_future(value):
    today = date.today()
    if value < today:
        raise ValidationError('Due date cannot be earlier than today')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title')


class TodoSerializer(serializers.ModelSerializer):

    due_date = serializers.DateField(required=False, validators=[no_future])
    tags = TagSerializer(many=True, read_only=True)
    timestamp = serializers.DateTimeField(read_only=True)

    class Meta():
        model = TodoModel
        fields = '__all__'
