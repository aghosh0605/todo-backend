from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todo.serializers import TodoSerializer
from todo.models import TodoModel, Tag
from django.core import serializers
from django.core.validators import ValidationError
# Create your views here.


class TodoBasic(APIView):
    """
    Retrieve, update or delete a todo.
    """

    def get(self, request, format=None, id=None):
        try:
            if id:
                todo = TodoModel.objects.get(id=id)
                serializer = TodoSerializer(todo)
            else:
                todos = TodoModel.objects.all()
                serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except TodoModel.DoesNotExist as e:
            return Response(data={"message": "No Todo found with the ID"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            todo = serializer.save()
            if request.data.get('tags'):
                for tag_title in request.data.get('tags'):
                    try:
                        tag = Tag.objects.get(title=tag_title)
                        todo.tags.add(tag)
                    except Tag.DoesNotExist:
                        tag = Tag.objects.create(title=tag_title)
                        todo.tags.add(tag)
                    # except ValidationError as error:
                    #     return Response(error, status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                todo = TodoModel.objects.get(id=request.data.get('id'))
                todo.title = serializer.data['title']
                todo.description = serializer.data['description']
                todo.due_date = serializer.data['due_date']
                todo.status = serializer.data['status']
                todo.save()
                try:
                    if request.data.get('tags'):
                        todo.tags.clear()
                        for tag_title in request.data.get('tags'):
                            tag = Tag.objects.get(title=tag_title)
                            todo.tags.add(tag)
                except Tag.DoesNotExist:
                    tag = Tag.objects.create(title=tag_title)
                    todo.tags.add(tag)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except TodoModel.DoesNotExist as e:
                return Response(data={"message": "No Todo found with the ID"}, status=status.HTTP_404_NOT_FOUND)
            except KeyError as e:
                return Response(data={"message": "Please provide all the keys"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None, id=None):
        try:
            todo = TodoModel.objects.get(id=id)
            name = todo.title
            serializer = TodoSerializer(todo)
            todo.delete()
            return Response(data={"message": f'Deleted Todo: {name}'}, status=status.HTTP_200_OK)
        except TodoModel.DoesNotExist as e:
            return Response(data={"message": "No Todo found with the ID"}, status=status.HTTP_404_NOT_FOUND)
