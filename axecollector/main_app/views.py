from django.shortcuts import render
from .models import Axe
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def axes_index(request):
    axes = Axe.objects.all()
    return render(request, 'axes/index.html', { 'axes': axes })

def axes_detail(request, axe_id):
    axe = Axe.objects.get(id=axe_id)
    return render(request, 'axes/detail.html', { 'axe': axe })
