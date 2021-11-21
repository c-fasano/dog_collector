from django.shortcuts import render
from .models import Dog

# Create your views here.

def home(request):
  return HttpResponse('Home Page')

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def home(request):
  return render(request, 'home.html')