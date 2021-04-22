from django import forms
from .models import Trail, Review


class TrailForm(forms.ModelForm):
    class Meta:
        model = Trail
        fields = ('hike_name', 'hike_location', 'hike_difficulty', 'hike_milage', 'hike_description')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('trail', 'difficulty', 'review', 'username')
