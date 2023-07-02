from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from todo.serializers import TodoSerializer
from todo.models import TodoModel, Tag
from django.core import serializers
from django.core.validators import ValidationError
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def todo_formatter(todos):
    new_tags = []
    for ele in todos:
        tags_todo = ele['tags']
        for tag in tags_todo:
            new_tags.append(tag['title'])
        ele['tags'] = new_tags
    # print(todos)
    return todos


def tags_handler(tags, todo):
    try:
        if tags:
            todo.tags.clear()
            for tag_title in tags:
                tag = Tag.objects.get(title=tag_title)
                todo.tags.add(tag)
    except Tag.DoesNotExist:
        tag = Tag.objects.create(title=tag_title)
        todo.tags.add(tag)


def todo_save(todo, data, id):
    try:
        del data['tags']
        TodoModel.objects.filter(id=id).update(**data)
    except KeyError:
        TodoModel.objects.filter(id=id).update(**data)


@method_decorator(csrf_exempt, name='dispatch')
class TodoBasic(APIView):
    permission_classes = [IsAuthenticated, ]

    """
    Retrieve, update or delete a todo.
    """

    def get(self, request, format=None, id=None):
        try:
            if id:
                todo = TodoModel.objects.get(id=id)
                serializer = TodoSerializer(todo)
                data = todo_formatter([serializer.data])[0]

            else:
                todos = TodoModel.objects.all()
                serializer = TodoSerializer(todos, many=True)
                data = todo_formatter(serializer.data)

            return Response(data, status=status.HTTP_200_OK)
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
            data = todo_formatter([serializer.data])[0]
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, format=None):
        # print(request.data)
        todo_id = request.data['id']
        if todo_id:
            data = request.data
            tags = request.data.get('tags')
            try:
                todo = TodoModel.objects.get(id=request.data.get('id'))
                todo_save(todo, data, todo_id)
                tags_handler(tags, todo)
                data['tags'] = tags
                # print(data)
                return Response(data, status=status.HTTP_201_CREATED)
            except TodoModel.DoesNotExist as e:
                return Response(data={"message": "No Todo found with the ID"}, status=status.HTTP_404_NOT_FOUND)
            # except KeyError as e:
            #     return Response(data={"message": "Please provide the id"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={"message": "Please provide the id"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None, id=None):
        try:
            todo = TodoModel.objects.get(id=id)
            name = todo.title

            todo.delete()
            return Response(data={"message": f'Deleted Todo: {name}'}, status=status.HTTP_200_OK)
        except TodoModel.DoesNotExist as e:
            return Response(data={"message": "No Todo found with the ID"}, status=status.HTTP_404_NOT_FOUND)
