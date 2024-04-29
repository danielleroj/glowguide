from django.contrib import admin
from .models import Routine, Product

# Register your models here.
admin.site.register([Routine, Product])