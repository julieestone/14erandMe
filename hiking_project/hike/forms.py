from django import forms
from .models import Trail, Review


class TrailForm(forms.ModelForm):
    hike_image = forms.CharField(required=False, widget=forms.HiddenInput())
    hike_image_file = forms.FileField(required=False)
    class Meta:
        model = Trail
        fields = ('hike_name', 'hike_location', 'hike_city', 'hike_difficulty', 'hike_milage', 'hike_description', 'hike_image_file', 'hike_image')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('trail', 'difficulty', 'review', 'username')
