from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('routines/', views.routines_index, name='index'),
    # /routines/:id
    path('routines/<int:routine_id>/', views.routines_detail, name='detail')
]