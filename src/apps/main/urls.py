"""
Define URL patterns do app 'main'.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
