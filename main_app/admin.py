from django.contrib import admin
from .models import Routine, Product, Profile, SkinType

# Register your models here.
admin.site.register([Routine, Product, Profile, SkinType])