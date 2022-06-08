from django.shortcuts import render, redirect
# from __future__ import unicode_literals
from django.views.generic import ListView, CreateView, UpdateView
from .models import Post
from .forms import CreatePostForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

# Create your views here.
class ListPostView(ListView):
  model = Post
  def get (self, request, *args, **kwargs):
    template_name = 'posts/list-posts.html' # sẽ được tạo ở phần dưới
    obj = {
      'posts': Post.objects.all()
    }
    # books = Post.objects.filter(name="999") # where name = '999'
    # books = Post.objects.all() # All
    # books = Post.objects.all()[:2] # limit 2
    # books = Post.objects.all()[3:2] # limit 3,2
    # books = Post.objects.all().order_by('name')

    # books = Post.objects.filter(id__lte='10') # id <= 10
    # books = Post.objects.filter(id__gte='10') # id >= 10
    # books = Post.objects.filter(id__gt='10') # id > 10




    # books = Post.objects.filter(name__contains='99') # WHERE name LIKE '%99%';
    # books = Post.objects.filter(name__exact='999') # WHERE name = '999';
    books = Post.objects.raw('SELECT * FROM posts_post LIMIT 5')

    for book in books:
        print(book.name)


    return render(request, template_name, obj)

class CreatePostView(SuccessMessageMixin, CreateView):
  template_name = 'posts/create-post.html'
  form_class = CreatePostForm
  success_message = 'Crate Post successfully!'

class UpdatePostView(SuccessMessageMixin, UpdateView):
  template_name = 'posts/edit-post.html'
  model = Post
  fields = ['name', 'content',]
  success_message = 'Update Post successfully!'

  def get_success_url(self):
    return reverse('posts:list-posts', kwargs={})

def delete_post(request, pk):
    post = Post.objects.filter(id=pk)
    post.delete()
    context = {
      "messages": "Delete Post successfully",
      'posts': Post.objects.all()
    }
    return render(request, 'posts/list-posts.html', context)