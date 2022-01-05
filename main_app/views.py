from typing import cast
from django.db import models
from django.db.models import fields
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Med 

# Create your views here.


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def meds_index(request):
  meds = Med.objects.filter(user=request.user)
  return render(request, 'meds/index.html', {'meds': meds})

@login_required
def meds_detail(request, med_id):
  med = Med.objects.get(id=med_id)
  return render(request, 'meds/detail.html', {"med": med})


class MedCreate (LoginRequiredMixin, CreateView):
  model = Med
  fields = ['name', 'dose', 'notes', 'taken']
  success_url = '/meds/'
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)


class MedUpdate (LoginRequiredMixin, UpdateView):
  model = Med
  fields = ['name', 'dose', 'notes', 'taken']
  success_url = '/meds/'
  

class MedDelete (LoginRequiredMixin, DeleteView):
  model = Med
  success_url = '/meds/'
  
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('meds_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)