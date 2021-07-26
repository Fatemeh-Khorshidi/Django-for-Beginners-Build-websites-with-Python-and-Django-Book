from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
# Create your views here.


def FirstHomePage(ListView):
    model = Post
    template_name = 'first_home.html'
    context_object_name = 'all_posts_list'


