from django.contrib import admin
from django.urls import path, include
from api.views import get_tasks, add_task, delete_task, delete_all_tasks

urlpatterns = [
    path('get-tasks/', get_tasks, name='get_tasks'),
    path('add-task/', add_task, name='add_task'),
    path('delete-task/', delete_task, name='delete_task'),
    path('delete-all-tasks/', delete_all_tasks, name='delete_all_tasks')
]
