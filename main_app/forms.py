from django import forms
from .models import Profile

class SkinTypeForm(forms.ModelForm):
    #questions for user's skin condition
    hydration = forms.ChoiceField(choices=[
        ('very_dry', 'Very Dry'),
        ('dry', 'Dry'),
        ('normal', 'Normal'),
        ('oily', 'Oily'),
    ], label="How does your skin feel after cleansing?")

    sensitivity = forms.ChoiceField(choices=[
        ('not_sensitive', 'Not Sensitive'),
        ('mildly_sensitive', 'Mildly Sensitive'),
        ('moderately_sensitive', 'Moderately Sensitive'),
        ('very_sensitive', 'Very Sensitive'),
    ], label="How sensitive is your skin?")

    breakouts = forms.ChoiceField(choices=[
        ('rarely', 'Rarely'),
        ('occasionally', 'Occasionally'),
        ('frequently', 'Frequently'),
        ('always', 'Always'),
    ], label="How often do you experience breakouts?")

    oiliness = forms.ChoiceField(choices=[
        ('dry', 'Dry'),
        ('balanced', 'Balanced'),
        ('oily', 'Oily'),
    ], label="How oily is your skin?")

    texture = forms.ChoiceField(choices=[
        ('smooth', 'Smooth'),
        ('rough', 'Rough'),
        ('bumpy', 'Bumpy'),
        ('flaky', 'Flaky'),
    ], label="What is the texture of your skin primarily?")

    complexion_concerns = forms.MultipleChoiceField(choices=[
        ('none', 'None'),
        ('wrinkles', 'Wrinkles/Fine Lines'),
        ('dark_spots', 'Dark Spots'),
        ('redness', 'Redness'),
        ('acne_scars', 'Acne Scars'),
    ], label="Do you have concerns with any of the following?", widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Profile
        fields = ['hydration', 'sensitivity', 'breakouts', 'oiliness', 'texture', 'complexion_concerns']

    def save(self, *args, **kwargs):
        commit = kwargs.pop('commit', True)
        profile = super(SkinTypeForm, self).save(commit=False, *args, **kwargs)
        profile.skin_type = self.determine_skin_type()

        if commit:
            profile.save()
        return profile

    def determine_skin_type(self):
        # determine skin type based on combo of answers
        data = self.cleaned_data 
        hydration = data['hydration']
        sensitivity = data['sensitivity']
        breakouts = data['breakouts']
        oiliness = data['oiliness']
        texture = data['texture']
        complexion_concerns = data.get('complexion_concerns', [])

        if sensitivity in ['very_sensitive', 'moderately_sensitive'] or 'redness' in complexion_concerns:
            return 'Sensitive'
        elif breakouts in ['frequently', 'always'] or oiliness == 'oily':
            return 'Oily'
        elif hydration in ['very_dry', 'dry'] or texture == 'flaky':
            return 'Dry'
        elif oiliness == 'balanced' and texture == 'smooth' and 'wrinkles' not in complexion_concerns:
            return 'Normal'
        else:
            return 'Combination'