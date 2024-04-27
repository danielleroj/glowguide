from django.shortcuts import render
from .models import Routine

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