from django.shortcuts import render, redirect
from .models import Med 

# Create your views here.



def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def meds_index(request):
  meds = Med.objects.all()
  return render(request, 'meds/index.html', {'meds': meds})