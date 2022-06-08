# posts/urls.py

# from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from posts.views import (
  ListPostView,
  CreatePostView,
  UpdatePostView,
)
from . import views
app_name = 'posts'
urlpatterns = [
    path('list-posts', ListPostView.as_view(), name='list-posts'),
    path('create-post', CreatePostView.as_view(), name='create-post'),
    path('^update-post/(?P<pk>[-\w]+)$', UpdatePostView.as_view(), name='update-post'),
    path('^delete-post/(?P<pk>[-\w]+)$', views.delete_post, name='delete-post'),
]
