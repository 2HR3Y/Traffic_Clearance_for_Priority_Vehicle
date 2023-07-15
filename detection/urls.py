from django.urls import path
from . import views

urlpatterns = [
    path('detection/', views.detect_objects, name='detect_objects'),
    path('', views.home),
]
