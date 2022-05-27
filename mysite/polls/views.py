from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 1aace02b is the polls index.")