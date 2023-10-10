from django.shortcuts import render
from django.http import JsonResponse


def app_home(request, *args, **kwargs):
    return JsonResponse({'msg': 'Hello User'})
