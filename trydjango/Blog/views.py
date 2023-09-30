from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

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


class BlogDeleteView(DeleteView):
    template_name = 'Blog/blog_delete.html'

    # if we want to pass with  pk
    # queryset = Blog.objects.all()
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Blog, id=id_)

    def get_success_url(self):
        return reverse('blogs:show-blogs')


# Function Based View to Class based View

class BlogListView(View):
    template_name = ''
    queryset = Blog.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_queryset
        }
        return render(request, self.template_name, context)


class MyListView(BlogListView):
    queryset = Blog.objects.filter(id=1)


class BlogView(View):
    template_name = ''

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Blog, id=id)
            context['object'] = obj
        return render(request, self.template_name, context)


class BlogCreateView(View):
    template_name = ''

    def get(self, request, *args, **kwargs):
        form = BlogForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            form = BlogForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    class BlogUpdateView(View):
        template_name = ''
        def get_object(self):
            id = self.kwargs.get('id')
            if id is not None:
                obj = get_object_or_404(Blog, id=id)
            return obj
        def get(self, request, id=None, *args, **kwargs):
            context = {}
            obj = self.get_object()
            if obj is not None:
                form = BlogForm(instance=obj)
                context = {
                    'object': obj,
                    'form': form
                }
            return render(request, self.template_name, context)

        def post(self, request, *args, **kwargs):
            context = {}
            obj = self.get_object()
            if obj is not None:
                form = BlogForm(request.POST,instance=obj)
                if form.is_valid():
                    form.save()
                    form = BlogForm()
            context = {
                'form': form
            }
            return render(request, self.template_name, context)