from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='show-blogs'),
    # path('<int:pk>', views.BlogDetailView.as_view(), name='blog-details'),
    path('<int:id>', views.BlogDetailView.as_view(), name='blog-details'),
    # path('create/', views.create_product, name='create_product'),
    # path('product/<int:my_id>', views.show_product_details, name='show_product_details'),
    # path('product/<int:id>/delete', views.delete_product, name='delete_product'),
    # path('product/list', views.product_list, name='product_list'),
]