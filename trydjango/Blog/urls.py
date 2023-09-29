from django.urls import path
from . import views



app_name = 'blogs'
urlpatterns = [
    path('', views.BlogListView.as_view(), name='show-blogs'),
    # path('<int:pk>', views.BlogDetailView.as_view(), name='blog-details'),
    path('<int:id>', views.BlogDetailView.as_view(), name='blog-details'),
    path('<int:id>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    path('create/', views.BlogCreateView.as_view(), name='create_blog'),
]