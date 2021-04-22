from django.shortcuts import render, redirect, HttpResponse
from .models import Trail, Review
from .forms import TrailForm, ReviewForm
from django.http import Http404
from django import forms


# Create your views here.

def get_trail(trail_id):
    try:
        trail = Trail.objects.get(id=trail_id)
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
        form = TrailForm(request.POST)
        if form.is_valid():
            trail = form.save(commit=False)
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
  
