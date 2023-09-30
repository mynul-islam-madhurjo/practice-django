from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # path('', views.BlogListView.as_view(), name='show-blogs'),
    # path('<int:pk>', views.BlogDetailView.as_view(), name='blog-details'),

    # path('create/', views.BlogCreateView.as_view(), name='create_blog'),
    # path('<int:id>', views.BlogDetailView.as_view(), name='blog-details'),
    # path('<int:id>/update', views.BlogUpdateView.as_view(), name='blog-update'),
    # path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog-delete'),

    # Function Based View to Class based View
    path('', views.BlogListView.as_view(template_name='Blog/blog_list.html'), name='blogs-list'),
    path('<int:id>', views.BlogView.as_view(template_name='Blog/blog_detail.html'), name='blogs-detail'),

    path('filter', views.MyListView.as_view(template_name='Blog/blog_list.html'), name='blogs-list'),

]
