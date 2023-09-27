from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

from .forms import ProductForm


# Create your views here.


def create_product(request):

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        #clear the form
        form = ProductForm

    context = {
        'form' : form
    }
    return render(request,'create.html', context)


def show_product(request):

    obj = Product.objects.get(id=1)
    context = {'product': obj}
    return render(request,'products/product_view.html', context)
