from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def salom(request):
    return HttpResponse("BU calculate oynasi")

