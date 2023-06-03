from django.urls import path
from todo.views import TodoBasic

urlpatterns = [
  path('todo/create', TodoBasic.as_view(), name='create-todo'),
]