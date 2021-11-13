from django.shortcuts import HttpResponse
from to_do.models import Task


def home(request):
    tasks = Task.objects.all()

    return HttpResponse("Hello from Django app{}{}".format(*tasks))


def new_url(request):
    tasks = Task(title="Task 4 ", description="test", status=0)
    tasks.save()
    return HttpResponse("Okay")


def filtered_data(request):
    task = Task.objects.get(id=1, title="New one")
    # print(task.query)
    return HttpResponse(task)