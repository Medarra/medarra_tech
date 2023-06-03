# mysite/views.py

"""

Django Views for medarra_tech Project

"""

from django.http import HttpResponse


def index(request):
    """
    Index Request Function
    """
    return HttpResponse('Follow along as I continue learning all about web development!')
