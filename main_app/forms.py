from django import forms
from .models import Profile

class SkinTypeForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['skin_type']