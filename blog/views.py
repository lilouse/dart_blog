from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from blog.models import Category, Post, Tag


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Classic Blog Design'
        return context


class PostView(DetailView):
    model = Post
    template_name = 'blog/single_post.html'
    context_object_name = 'post'


# def index(request):
#     return render(request, 'blog/index.html')


class CategoryDetailView(ListView):
    template_name = 'blog/index.html'
    allow_empty = True
    paginate_by = 1
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    # slug_field = 'slug'
    # context_object_name = 'categories'