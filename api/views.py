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
    print(request)
    tasks = list(Task.objects.all().order_by("-created_at").values())
    return JsonResponse({"data": tasks})


@api_view(['POST'])
def add_task(request):
    print("POST request:", request.data)
    try:
        Task.objects.create(name=request.data.get("taskName"), importance=request.data.get("priority"))
        return JsonResponse({"status": "success"})
    except Exception as e:
        return JsonResponse({"status": "fail"})


@api_view(['POST'])
def delete_task(request):
    print("POST request:", request.data)
    try:
        Task.objects.get(id=request.data.get("taskId")).delete()
        return JsonResponse({"status": "success"})
    except Task.DoesNotExist:
        return JsonResponse({"status": "fail"})
