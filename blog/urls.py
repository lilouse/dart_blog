from django.urls import path
from .views import *

urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_page'),
    path('post/<slug:slug>', PostView.as_view(), name='post_page'),
]