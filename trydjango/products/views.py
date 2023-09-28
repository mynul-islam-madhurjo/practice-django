from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

from .forms import ProductForm, RawProductForm


# Create your views here.
def create_product(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        'form': my_form
    }
    return render(request, 'create.html', context)


# def create_product(request):
#     if request.method == "POST":
#         my_title = request.POST.get('title')
#         print(my_title)
#     context = {
#     }
#     return render(request, 'create.html', context)

# def create_product(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         # clear the form
#         form = ProductForm
#
#     context = {
#         'form': form
#     }
#     return render(request, 'create.html', context)


def show_product(request):
    obj = Product.objects.get(id=1)
    context = {'product': obj}
    return render(request, 'products/product_view.html', context)
