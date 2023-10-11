from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_product_rest, name='get_product'),
]