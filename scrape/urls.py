from django.urls import path

from . import views

urlpatterns = [
  path('', views.index),
  path('coursera/', views.coursera, name='coursera'),
  path('stanford/', views.stanford, name='stanford'),
  path('havard/', views.havard, name='havard'),
  
]