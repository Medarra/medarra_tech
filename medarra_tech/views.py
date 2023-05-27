# mysite/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse('Follow along as I continue learning all about web development!')
