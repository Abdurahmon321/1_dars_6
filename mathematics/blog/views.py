from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def blog1(request):
    return HttpResponse("bu blog 1")


def blog2(request):
    return HttpResponse("bu blog 2")


def blog3(request):
    return HttpResponse("bu blog 3")


def blog4(request):
    return HttpResponse("bu blog 4")
