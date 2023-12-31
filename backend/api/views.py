import json

from django.shortcuts import render
from django.http import JsonResponse


def app_home(request, *args, **kwargs):
    # print(request.GET)  # url query params

    body = request.body
    data = {}
    try:
        data = json.loads(body)  # json data to python dict
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)
