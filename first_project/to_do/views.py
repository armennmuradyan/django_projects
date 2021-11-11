from django.shortcuts import HttpResponse


def home(request):
    print(request.__dict__)
    return HttpResponse("Hello from Django app")


def present(request):

    return HttpResponse("Tigran Danielyan")
