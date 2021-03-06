from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Axe, String, AxePhoto, StringPhoto
from .forms import MaintenanceForm, RegistrationForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'axecollector'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def axes_index(request):
  axes = request.user.axe_set.all()
  return render(request, 'axes/index.html', { 'axes': axes })

@login_required
def axes_detail(request, axe_id):
  axe = Axe.objects.get(id=axe_id)
  strings_not_on_axe = String.objects.exclude(id__in = axe.strings.all().values_list('id'))
  maintenance_form = MaintenanceForm()
  return render(request, 'axes/detail.html', {
    'axe': axe, 'maintenance_form': maintenance_form, 'strings': strings_not_on_axe 
  })

@login_required
def assoc_string(request, axe_id, string_id):
  Axe.objects.get(id=axe_id).strings.add(string_id)
  return redirect('detail', axe_id=axe_id)

@login_required
def curr_string(request, axe_id, string_id):
  Axe.objects.get(id=axe_id).strings.remove(string_id)
  Axe.objects.get(id=axe_id).strings.add(string_id)
  return redirect('detail', axe_id=axe_id)

@login_required
def unassoc_string(request, axe_id, string_id):
  Axe.objects.get(id=axe_id).strings.remove(string_id)
  return redirect('detail', axe_id=axe_id)

class AxeCreate(LoginRequiredMixin, CreateView):
  model = Axe
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class AxeUpdate(LoginRequiredMixin, UpdateView):
  model = Axe
  fields = '__all__'

class AxeDelete(LoginRequiredMixin, DeleteView):
  model = Axe
  success_url = '/axes/'

@login_required
def add_maintenance(request, axe_id):
  form = MaintenanceForm(request.POST)
  if form.is_valid():
    new_maintenance = form.save(commit=False)
    new_maintenance.axe_id = axe_id
    new_maintenance.save()
  return redirect('detail', axe_id=axe_id)

class StringList(LoginRequiredMixin, ListView):
  model = String

class StringDetail(LoginRequiredMixin, DetailView):
  model = String

class StringCreate(LoginRequiredMixin, CreateView):
  model = String
  fields = '__all__'

class StringUpdate(LoginRequiredMixin, UpdateView):
  model = String
  fields = '__all__'

class StringDelete(LoginRequiredMixin, DeleteView):
  model = String
  success_url = '/strings/'

@login_required
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

@login_required
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

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = RegistrationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)