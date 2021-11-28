from django.db import models

from django.urls import reverse

from datetime import date
# Create your models here.

TIMES = (
  ('M', 'Morning'),
  ('A', 'Afternoon'), 
  ('E', 'Evening'), 
  ('N', 'Night'),
)

class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

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