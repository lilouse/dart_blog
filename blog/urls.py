from django.urls import path
from .views import *

urlpatterns=[
    path('', index, name='home'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_page')
]