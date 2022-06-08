from django.urls import path
# from django.views.generic import TemplateView

from login.views import StaticView
from . import views

app_name = 'login'
urlpatterns = [
   path('connect', StaticView.as_view(), name="connect"),
   path('', views.index, name='index'),
]