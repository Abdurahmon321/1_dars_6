from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def oyna_1(request):
    return HttpResponse("bestseller 1 - oynasi")


def oyna_2(request):
    return HttpResponse("bestseller 2 - oynasi")


def oyna_3(request):
    return HttpResponse("bestseller 3 - oynasi")


def oyna_4(request):
    return HttpResponse("bestseller 4 - oynasi")
