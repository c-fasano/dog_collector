from django.shortcuts import render


from django.http import HttpResponse
# Create your views here.

def home(request):
  return HttpResponse('Home Page')

def about(request):
  return render(request, 'about.html')

class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Lolo', 'tabby', 'Kinda rude.', 3),
  Dog('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Dog('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Dog('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })