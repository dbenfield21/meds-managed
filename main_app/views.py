from typing import cast
from django.db import models
from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Med 

# Create your views here.


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def meds_index(request):
  meds = Med.objects.all()
  return render(request, 'meds/index.html', {'meds': meds})

def meds_detail(request, med_id):
  med = Med.objects.get(id=med_id)
  return render(request, 'meds/detail.html', {"med": med})

class MedCreate (CreateView):
  model = Med
  fields = ['name', 'dose', 'notes', 'taken']
  success_url = '/meds/'


