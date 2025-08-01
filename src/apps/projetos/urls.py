"""
Define o urlpatterns do app 'projetos'.
"""

from django.urls import path, include
from projetos import views

urlpatterns = [
    path('', views.projetos_home, name='projetos_home'),
]