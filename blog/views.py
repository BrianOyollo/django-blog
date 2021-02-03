from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'all_blog_posts'
    ordering = ['-id']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'all_blog_posts'


class NewPostView(CreateView):
    model = Post
    template_name = 'blog/new_post.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url=reverse_lazy('home-page')
