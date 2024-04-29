from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Routine, Product

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

class RoutineCreate(CreateView):
    model = Routine
    fields = '__all__'

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
