from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def show_product(request):

    obj = Product.objects.get(id=1)
    context = {'product': obj}
    return render(request,'view.html', context)
