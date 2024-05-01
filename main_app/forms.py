from django import forms
from .models import Profile

class SkinTypeForm(forms.ModelForm):
    #questions for user's skin condition
    hydration = forms.ChoiceField(choices=[
        ('very_dry', 'Very Dry'),
        ('dry', 'Dry'),
        ('normal', 'Normal'),
        ('oily', 'Oily'),
    ], label="How would you describe your skin hydration?"
    )

    reaction = forms.ChoiceField(choices=[
        ('never_reacts', 'Never reacts'),
        ('sometimes_reacts', 'Sometimes reacts'),
        ('often_reacts', 'Often reacts'),
        ('always_reacts', 'Always reacts'),
    ], label="How often does your skin react negatively to new products or changes?"
    )

    breakouts = forms.ChoiceField(choices=[
        ('never', 'Never'),
        ('occasionally', 'Occasionally'),
        ('frequently', 'Frequently'),
        ('always', 'Always'),
    ], label="How often do you experience breakouts?"
    )

    t_zone = forms.ChoiceField(choices=[
        ('dry', 'Dry'),
        ('balanced', 'Balanced'),
        ('oily', 'Oily'),
        ('very_oily', 'Very Oily'),
    ], label="What is the condition of your T-zone (forehead, nose, chin)?"
    )

    class Meta:
        model = Profile
        fields = []

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
        conditions = [data['hydration'], data['reaction'], data['breakouts'], data['t_zone']]

        if 'very_oily' in conditions or 'oily' in conditions:
            if 'always_reacts' in conditions or 'often_reacts' in conditions:
                return 'Oily and Sensitive'
            return 'Oily'
        elif 'very_dry' in conditions or 'dry' in conditions:
            if 'always_reacts' in conditions or 'often_reacts' in conditions:
                return 'Dry and Sensitive'
            return 'Dry'
        return 'Normal'