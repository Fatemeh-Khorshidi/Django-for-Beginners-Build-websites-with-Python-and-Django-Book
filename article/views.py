from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin  # new
)
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin  # new
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from django.urls import reverse_lazy  # new
from .models import Article


class ArticleListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):  # new
    model = Article
    template_name = 'article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # new
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # new
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')


class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):  # new
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body',)

    def form_valid(self, form):  # new
        form.instance.author = self.request.user

        return super().form_valid(form)
