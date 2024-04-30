from django.contrib import admin
from .models import Routine, Product, Profile

# Register your models here.
admin.site.register([Routine, Product, Profile])