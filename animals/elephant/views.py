from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def oyna_1(request):
    return HttpResponse("<h2>Elephant 1 oynasi</h2>")


def oyna_2(request):
    return HttpResponse("<h2>Elephant 2 oynasi</h2>")


def oyna_3(request):
    return HttpResponse("<h2>Elephant 3 oynasi</h2>")


def oyna_4(request):
    return HttpResponse("<h2>Elephant 4 oynasi</h2>")


def oyna_5(request):
    return HttpResponse("<h2>Elephant 5 oynasi</h2>")
