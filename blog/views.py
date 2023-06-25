from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from blog.models import Category


# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'blog/index.html'
    # slug_field = 'slug'
    # context_object_name = 'categories'