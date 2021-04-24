from django.shortcuts import render, redirect, HttpResponse
from .models import Trail, Review
from .forms import TrailForm, ReviewForm
from django.http import Http404
from django import forms
import http.client
import base64

# Create your views here.

def get_trail(trail_id):
    try:
        trail = Trail.objects.get(id=trail_id)
        weather_api()
    except Trail.DoesNotExist:
        raise Http404
    return trail

def trail_list(request):
    trails = Trail.objects.all()
    return render(request, 'trails/trails_list.html', {'trails': trails})

def trail_detail(request, trail_id):
    trail = get_trail(trail_id)
    reviews = trail.reviews.all()
    return render(request, 'trails/trail_detail.html', {'trail': trail, 'reviews': reviews})

def new_trail(request):
    if request.method == "POST":
        form = TrailForm(request.POST, request.FILES)
        if form.is_valid():
            trail = form.save(commit=False)
            trail.hike_image = base64.b64encode(
                trail.hike_image_file.file.read())
            trail.hike_image_file = None
            trail.save()
            return redirect('trail_detail', trail_id=trail.id)
    else:
        form = TrailForm()
    return render(request, 'trails/trail_form.html', {'form': form, 'type_of_request': 'New'})

def edit_trail(request, trail_id):
    trail = get_trail(trail_id)
    if request.method == "POST":
        form = TrailForm(request.POST, instance=trail)
        if form.is_valid():
            trail = form.save(commit=False)
            trail.save()
            return redirect('trail_detail', trail_id=trail.id)
    else:
        form = TrailForm(instance=trail)
    return render(request, 'trails/trail_form.html', {'form': form, 'type_of_request': 'Edit'})

def delete_trail(request, trail_id):
    if request.method == "POST":
        trail = get_trail(trail_id)
        trail.delete()
    return redirect('trail_list')


def get_review(review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        raise Http404
    return review


def review_list(request, trail_id):
    trail = get_trail(trail_id)
    reviews = trail.reviews.all()
    return render(request, 'reviews/reviews_list.html', {'trail': trail, 'reviews': reviews})


def review_detail(request, trail_id, review_id):
    trail = get_trail(trail_id)
    review = get_review(review_id)
    return render(request, 'reviews/review_detail.html', {'trail': trail, 'review': review})


def new_review(request, trail_id):
    trail = get_trail(trail_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.trail = trail
            review.save()
            return trail_detail(request, trail_id)
    else:
        form = ReviewForm()
        form.initial['trail'] = trail_id
        form.fields['trail'].widget = forms.HiddenInput()
    return render(request, 'reviews/review_form.html', {'form': form, 'type_of_request': 'New', 'trail': trail})


def edit_review(request, trail_id, review_id):
    trail = get_trail(trail_id)
    review = get_review(review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('review_detail', review_id=review.id, trail_id=trail_id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_form.html', {'form': form, 'type_of_request': 'Edit'})


def delete_review(request, trail_id, review_id):
    if request.method == "POST":
        review = get_review(review_id)
        review.delete()
    return trail_detail(request, trail_id)
  
def weather_api():
    conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "d7cb94f27dmsh96d3dabd8b73ea8p1e8114jsn6514282cc8de",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    conn.request("GET", "/weather?q=Estes%20Park&lat=0&lon=0&callback=test&id=2172797&lang=null&units=%22metric%22%20or%20%22imperial%22&mode=xml%2C%20html", headers=headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

