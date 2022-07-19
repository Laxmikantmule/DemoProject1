from django.shortcuts import render

from django.http import HttpResponse

def view1(request):
    return HttpResponse("HELLO WORLD")
