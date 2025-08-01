"""
Define o request do app 'projetos'.
"""

from django.shortcuts import render
    
def projetos_home(request):
    return render(request, 'projetos/index.html')
