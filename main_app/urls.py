from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'), 
  path('meds/', views.meds_index, name="meds_index"),
  path('meds/<int:med_id>/', views.meds_detail, name='meds_detail'),
  path('meds/create/', views.MedCreate.as_view(), name='meds_create'),
  # path('meds/<int:pk>/update/', views.MedUpdate.as_view(), name='meds_update'),
  # path('meds/<int:pk>/delete/', views.MedDelete.as_view(), name='meds_delete'),
  ]