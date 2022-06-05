from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from api.models import Task
from rest_framework.response import Response
from api.serializers import TaskSerializer
from rest_framework.renderers import JSONRenderer


# Create your views here.


@api_view(['GET'])
def get_tasks(request):
    tasks = Task.objects.all().order_by("-created_at")
    if request.GET.get("done") == "false":
        tasks = tasks.exclude(is_done=True)
    elif request.GET.get("done") == "true":
        tasks = tasks.exclude(is_done=False)
    tasks = list(tasks.values())
    return JsonResponse({"data": tasks})


@api_view(['POST'])
def add_task(request):
    try:
        Task.objects.create(name=request.data.get("taskName"), importance=request.data.get("priority"))
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status": "fail"})


@api_view(['POST'])
def delete_task(request):
    try:
        task = Task.objects.get(id=request.data.get("taskId"))
        task.is_done = True
        task.save()
        return JsonResponse({"status": "success"})
    except Task.DoesNotExist:
        return JsonResponse({"status": "fail"})


@api_view(['POST'])
def delete_all_tasks(request):
    tasks = Task.objects.all().exclude(is_done=False)
    tasks.delete()
    return JsonResponse({"status": "success"})
