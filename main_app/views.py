from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from .forms import WalkForm
# Create your views here.

def about(request):
  return render(request, 'about.html')

def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def home(request):
  return render(request, 'home.html')

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  walk_form = WalkForm()
  return render(request, 'dogs/detail.html', { 'dog': dog, 'walk_form': walk_form })

def add_walk(request, dog_id):
  form = WalkForm(request.POST)
  if form.is_valid():
    new_walk = form.save(commit=False)
    new_walk.dog_id = dog_id
    new_walk.save()
  return redirect('dogs_detail', dog_id=dog_id)

class DogCreate(CreateView):
  model = Dog
  fields = '__all__'
  success_url= '/dogs/'

class DogUpdate(UpdateView):
  model = Dog
  fields = ['description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'