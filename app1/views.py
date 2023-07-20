from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def stringresponse(request):
    return HttpResponse('<h1><marquee>my first project</marquee></h1>')

