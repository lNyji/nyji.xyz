
from django.shortcuts import render

def sobre_home(request):
    return render(request, 'sobre/index.html')
