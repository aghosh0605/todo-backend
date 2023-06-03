from django.contrib import admin
from todo.models import TodoModel
from django.contrib.auth.models import Group
from django import forms


# Register your models here.

# admin.site.register(TodoModel)
@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    list_display = ('title','description','due_date','status')
    list_filter = ('title','status')
    search_fields = ['title', 'description']
admin.site.unregister(Group)

admin.site.site_header = "Todo App"