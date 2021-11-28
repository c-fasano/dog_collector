from django.forms import ModelForm
from .models import Feeding, Walk 

class WalkForm(ModelForm):
  class Meta:
    model = Walk
    fields = ['date', 'time']
