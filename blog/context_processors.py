# from django.template import RequestContext
from django.template.context_processors import request

from blog.models import Category


def category_context(request):
    return {'categories': Category.objects.all(), 'path': request.path}