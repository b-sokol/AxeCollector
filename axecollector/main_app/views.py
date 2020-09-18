from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
from .models import Axe, String, AxePhoto, StringPhoto
from .forms import MaintenanceForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'axecollector'

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

def curr_string(request, axe_id, string_id):
  Axe.objects.get(id=axe_id).strings.remove(string_id)
  Axe.objects.get(id=axe_id).strings.add(string_id)
  return redirect('detail', axe_id=axe_id)

def remove_string(request, axe_id, string_id):
  Axe.objects.get(id=axe_id).strings.remove(string_id)
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
  fields = '__all__'

class StringDelete(DeleteView):
  model = String
  success_url = '/strings/'
  
def add_axe_photo(request, axe_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      AxePhoto.objects.create(url=url, axe_id=axe_id)
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', axe_id=axe_id)

def add_string_photo(request, string_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      StringPhoto.objects.create(url=url, string_id=string_id)
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', string_id=string_id)