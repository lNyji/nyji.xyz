"""
Define views do app 'main'.
"""

from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')
