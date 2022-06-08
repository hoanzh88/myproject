from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def index(request):
   model = Book
   response = HttpResponse()
   response.writelines('<h1>Xin chào</h1>')
   response.write('Đây là app home')
   books = Book.objects.filter(title__startswith="Book")

   return response