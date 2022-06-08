from django.urls import path
from . import views
app_name = 'dreamreal'
urlpatterns = [
   path('', views.index, name='index'),
   path('list', views.list, name='list'),
   # path('create', views.list, name='create'),
   path('endpoint', views.endpoint, name='endpoint'),
   path('publishdata', views.publishdata, name='publishdata'),
]