from django.forms import ModelForm
from main.models import MoodEntry
from django.utils.html import strip_tags
from django import forms


class MoodEntryForm(ModelForm):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Choices for 1-5 stars

    rating = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect)  # Add rating field

    class Meta:
        model = MoodEntry
        fields = ["mood", "feelings", "mood_intensity", "rating"]  # Include rating in form
