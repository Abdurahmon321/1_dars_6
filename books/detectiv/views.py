from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def oyna_1(request):
    return HttpResponse(" detectic 1 oyna")


def oyna_2(request):
    return HttpResponse(" detectic 2 oyna")


def oyna_3(request):
    return HttpResponse(" detectic 3 oyna")


def oyna_4(request):
    return HttpResponse(" detectic 4 oyna")
