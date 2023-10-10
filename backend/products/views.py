import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

# Create your views here.

""" 
Creating a model instance
Turning into a python dictionary
Returning Json to my client
"""


def get_product(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['price'] = model_data.price

    return JsonResponse(data)






































