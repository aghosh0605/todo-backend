from django.contrib import admin
from todo.models import TodoModel, Tag
from django.contrib.auth.models import Group
from django import forms


# Register your models here.

# admin.site.register(TodoModel)
@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'due_date', 'status')
    list_filter = ('due_date', 'status')
    search_fields = ['title', 'description']


admin.site.unregister(Group)
admin.site.register(Tag)

admin.site.site_header = "Todo App"
