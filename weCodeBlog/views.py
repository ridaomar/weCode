from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import AddPostForm, UpdatePostForm
from django.urls import reverse_lazy

# def home(request):
#     return render(request, 'home.html', {})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {
        'cats':cats.title().replace('-', ' '), 
        'category_posts':category_posts
        })

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')