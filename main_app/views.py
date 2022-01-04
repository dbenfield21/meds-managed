from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Med 

# Create your views here.


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def meds_index(request):
  meds = Med.objects.all()
  return render(request, 'meds/index.html', {'meds': meds})

def meds_details(request):
  meds = Med.objects.get(id=med_id)
  return render(request, 'meds/detail.html', {"meds": meds})



