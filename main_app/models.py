from django.db import models

from django.urls import reverse

from datetime import date

from django.contrib.auth.models import User
# Create your models here.

TIMES = (
  ('M', 'Morning'),
  ('A', 'Afternoon'), 
  ('E', 'Evening'), 
  ('N', 'Night'),
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})


class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
      return reverse("dogs_detail", kwargs={"dog_id": self.id})
  
class Walk(models.Model):
  date = models.DateField('Walk Date')
  time = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
  )

  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

  class Meta:
    ordering = ['-date']

  def __str__(self):
    return f"{self.get_walk_display()} on {self.date}"

  def walked_today(self):
    return self.walk_set.filter(date=date.today()).count() >= 1

