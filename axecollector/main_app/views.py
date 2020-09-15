from django.shortcuts import render
from django.http import HttpResponse

class Axe:
  def __init__(self, name, make, model, description, year):
    self.name = name
    self.year = year
    self.make = make
    self.model = model
    self.description = description

axes = [
  Axe('Marilyn', 'Fender', 'American Vintage Reissue 1952 Telecaster', 'Road worn 52 Tele reissue, mint green pickguard, reversed control plate, blackguard replica electronics', 2013),
]

# Create your views here.

def home(request):
    return HttpResponse('<h1>🤘</h1>')

def about(request):
    return render(request, 'about.html')

def axes_index(request):
    return render(request, 'axes/index.html', { 'axes': axes })


