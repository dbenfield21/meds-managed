from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Med(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=250)
  dose = models.CharField(max_length=250)
  notes = models.TextField(max_length=1000)
  taken = models.BooleanField(default=False)
  created = models.DateField(auto_now_add=True)


  def __str__(self):
    return self.name
  
  class Meta:
    ordering = ['taken']

  def get_absolute_url(self):
    return reverse('meds_detail', kwargs={'med_id': self.id})