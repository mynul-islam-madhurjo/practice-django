import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse  # JsonResponse expects dictionary, HttpResponse String text
from .models import Product
from django.forms.models import model_to_dict

# Create your views here.

""" 
Creating a model instance
Turning into a python dictionary
Returning Json to my client
"""


def get_product(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    # serialization
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['price'] = model_data.price
        # data = model_to_dict(model_data)
        data = model_to_dict(model_data, fields=['title'])

    return JsonResponse(data)
