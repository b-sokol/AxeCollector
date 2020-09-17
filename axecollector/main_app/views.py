from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Axe, String
from .forms import MaintenanceForm

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
  strings_not_on_axe = String.objects.exclude(id__in = axe.strings.all().values_list('id'))
  maintenance_form = MaintenanceForm()
  return render(request, 'axes/detail.html', {
    'axe': axe, 'maintenance_form': maintenance_form, 'strings': strings_not_on_axe 
  })
  
def assoc_string(request, axe_id, string_id):
  Axe.objects.get(id=axe_id).strings.add(string_id)
  return redirect('detail', axe_id=axe_id)

class AxeCreate(CreateView):
  model = Axe
  fields = '__all__'

class AxeUpdate(UpdateView):
  model = Axe
  fields = '__all__'

class AxeDelete(DeleteView):
  model = Axe
  success_url = '/axes/'

def add_maintenance(request, axe_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.axe_id = axe_id
    new_maintenance.save()
  return redirect('detail', axe_id=axe_id)

class StringList(ListView):
  model = String

class StringDetail(DetailView):
  model = String

class StringCreate(CreateView):
  model = String
  fields = '__all__'

class StringUpdate(UpdateView):
  model = String
  fields = ['brand', 'name', 'material', 'guage']

class StringDelete(DeleteView):
  model = String
  success_url = '/strings/'