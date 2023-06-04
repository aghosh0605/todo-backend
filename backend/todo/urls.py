from django.urls import path
from todo.views import TodoBasic

urlpatterns = [
    path('todo/create',
         TodoBasic.as_view(http_method_names=['post']), name='create-todo'),
    path('todo/fetch/<int:id>',
         TodoBasic.as_view(http_method_names=['get']), name='get-todo'),
    path('todo/fetch',
         TodoBasic.as_view(http_method_names=['get']), name='get-all-todo'),
    path('todo/update',
         TodoBasic.as_view(http_method_names=['patch']), name='update-todo'),
    path('todo/delete/<int:id>',
         TodoBasic.as_view(http_method_names=['delete']), name='delete-todo'),
]
