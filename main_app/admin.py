from django.contrib import admin
from .models import Routine, Product, Profile, SkinType, SuggestedProduct

# Register your models here.
admin.site.register([Routine, Product, Profile, SkinType, SuggestedProduct])