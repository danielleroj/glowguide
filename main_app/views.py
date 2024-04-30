from django.shortcuts import render, redirect
from .forms import SkinTypeForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Routine, Product, Photo

import boto3, uuid

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def routines_index(request):
    routines = Routine.objects.filter(user=request.user)
    return render(request, 'routines/index.html', {
        'routines': routines
    })

@login_required
def routines_detail(request, routine_id):
    routine = Routine.objects.get(id=routine_id)
    return render(request, 'routines/detail.html', { 'routine': routine })

import os

@login_required
def add_photo(request, product_id):
  #capture form input
  photo_file =  request.FILES.get('photo-file', None)
  #check if file was provided
  if photo_file:
    #setup an s3 uploader client
    s3 = boto3.client('s3')
    #generate a unique name for the file using uuid library
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    #build a url path based on the base url, the bucket name and the photo file name
    #error handle
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f'{os.environ["S3_BASE_URL"]}{bucket}/{key}'
      Photo.objects.create(url=url, product_id=product_id)
    except Exception as e:
      print('Error uploading to S3')
      print(e)
    return redirect('products_detail', pk=product_id)
  
def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            erorr_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_mesage': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def skin_type_quiz(request):
    if request.method == 'POST':
        form = SkinTypeForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('some_view_name')
    else:
        form = SkinTypeForm(instance=request.user.profile)

    return render(request, 'your_template.html', {'form': form})


class RoutineCreate(LoginRequiredMixin, CreateView):
    model = Routine
    fields = ['name', 'description', 'products']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RoutineUpdate(LoginRequiredMixin, UpdateView):
    model = Routine
    fields = ['name', 'description']

class RoutineDelete(LoginRequiredMixin, DeleteView):
    model = Routine
    success_url = '/routines'

class ProductList(LoginRequiredMixin, ListView):
    model = Product
    product_list = 'myapp/product_list.html'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = '__all__'

class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = '__all__'

class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = '/products'
