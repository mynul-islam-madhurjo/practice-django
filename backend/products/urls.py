from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_product_rest_srlz_post, name='get_product'),
]