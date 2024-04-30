from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Routine, Product, Photo

import boto3, uuid

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def routines_index(request):
    routines = Routine.objects.all()
    return render(request, 'routines/index.html', {
        'routines': routines
    })

def routines_detail(request, routine_id):
    routine = Routine.objects.get(id=routine_id)
    return render(request, 'routines/detail.html', { 'routine': routine })

import os

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

class RoutineCreate(CreateView):
    model = Routine
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RoutineUpdate(UpdateView):
    model = Routine
    fields = ['name', 'description']

class RoutineDelete(DeleteView):
    model = Routine
    success_url = '/routines'

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'

class ProductDelete(DeleteView):
    model = Product
    success_url = '/products'
