from django.urls import path
from . import views

urlpatterns = [
    path('', views.trail_list, name='trail_list'),
    path('new', views.new_trail, name='new_trail'),
    path('<int:trail_id>', views.trail_detail, name='trail_detail'),
    path('<int:trail_id>/edit', views.edit_trail, name='edit_trail'),
    path('<int:trail_id>/delete', views.delete_trail, name='delete_trail'),
    path('<int:trail_id>/reviews', views.review_list, name='review_list'),
    path('<int:trail_id>/reviews/new', views.new_review, name='new_review'),
    path('<int:trail_id>/reviews/<int:review_id>', views.review_detail, name='review_detail'),
    path('<int:trail_id>/reviews/<int:review_id>/edit', views.edit_review, name='edit_review'),
    path('<int:trail_id>/reviews/<int:review_id>/delete', views.delete_review, name='delete_review'),
]
