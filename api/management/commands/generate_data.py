from django.core.management.base import BaseCommand, CommandError
from api.models import Task

class Command(BaseCommand):
    help = 'Generate random data'

    def handle(self, *args, **options):
        task1 = Task.objects.create(name="Task for testing01")
        task2 = Task.objects.create(name="Task for testing02")
        task3 = Task.objects.create(name="Task for testing03")
        task4 = Task.objects.create(name="Task for testing04")
        task5 = Task.objects.create(name="Task for testing05")
        task6 = Task.objects.create(name="Task for testing06")
        task1.save()
        task2.save()
        task3.save()
        task4.save()
        task5.save()
        task6.save()
        print("success")
        
