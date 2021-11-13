from django.shortcuts import render, HttpResponse
from new_app.models import Task


def home(request):
    tasks = Task.objects.all()

    # return HttpResponse("django app {}".format(tasks[0]))
    return render(request, "new_app/home.html")