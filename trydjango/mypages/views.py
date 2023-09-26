from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_world(request, *args,**kwargs):
    #print(request.user)
    return HttpResponse("<html><body><h1>Hello, World!</h1></body></html>")