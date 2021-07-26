from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'home.html'