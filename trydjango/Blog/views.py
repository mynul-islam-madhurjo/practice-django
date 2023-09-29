from django.shortcuts import render,get_object_or_404

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.

from .models import Blog

class BlogListView(ListView):
    # template_name = 'random/random_list.html'
    queryset = Blog.objects.all()

class BlogDetailView(DetailView):
    # template_name = 'random/random_list.html'
    # if we want to pass with  pk
    queryset = Blog.objects.all()

    #if we want to pass with  id
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Blog,id=id_)
