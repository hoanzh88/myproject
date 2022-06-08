from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm

from django.views.generic import TemplateView
# Create your views here.
class StaticView(TemplateView):
   template_name = "login.html"
   # def static(request):
      # return render(request, 'static.html', {})

   def login(request):
      username = "not logged in"

      if request.method == "POST":
         # Get the posted form
         MyLoginForm = LoginForm(request.POST)

         if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
      else:
         MyLoginForm = Loginform()

      return render(request, 'loggedin.html', {"username": username})

def index(request):
   response = HttpResponse()
   response.writelines('<h1>Xin chào</h1>')
   response.write('Đây là app login')
   return response




