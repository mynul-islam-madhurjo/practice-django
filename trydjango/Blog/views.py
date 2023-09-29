from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.

from .models import Blog
from .froms import BlogForm


class BlogCreateView(CreateView):
    template_name = 'Blog/blog_create.html'
    form_class = BlogForm
    queryset = Blog.objects.all()

    # if we want to define a landing pager after success
    # success_url = '/'
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/'


class BlogUpdateView(UpdateView):
    template_name = 'Blog/blog_create.html'
    form_class = BlogForm
    queryset = Blog.objects.all()

    # if we want to define a landing pager after success
    # success_url = '/'
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Blog, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class BlogListView(ListView):
    # template_name = 'random/random_list.html'
    queryset = Blog.objects.all()


class BlogDetailView(DetailView):
    # template_name = 'random/random_list.html'
    # if we want to pass with  pk
    queryset = Blog.objects.all()

    # if we want to pass with  id
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Blog, id=id_)
