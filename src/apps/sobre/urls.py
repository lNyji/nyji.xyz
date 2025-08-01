from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sobre_home, name='sobre_home'),
]