import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse  # JsonResponse expects dictionary, HttpResponse String text
from .models import Product
from .serializers import ProductSerializer
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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


""" 
DRF API VIEW
"""


@api_view(["GET"])
def get_product_rest(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}

    if model_data:
        # sale_price wont show
        data = model_to_dict(model_data, fields=['title', 'sale_price'])
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "No data available"}, status=status.HTTP_404_NOT_FOUND)


""" 
DRF Serializer
"""


@api_view(["GET"])
def get_product_rest_srlz(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}

    if instance:
        # sale_price wont show
        data = ProductSerializer(instance).data
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response({"message": "No data available"}, status=status.HTTP_404_NOT_FOUND)
















