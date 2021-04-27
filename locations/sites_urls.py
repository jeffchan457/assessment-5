from django.urls import path, include
from . import views

urlpatterns = [
    # Sites urls
    path('', views.sites, name='sites'),
    path('<int:site_id>', views.site_detail, name='site_detail'),
    path('new', views.new_site, name='new_site'),
    path('<int:site_id>/edit', views.site_edit, name='site_edit'),
    path('<int:site_id>/delete', views.site_delete, name='site_delete'),

    # Reviews urls
    path('<int:site_id>/reviews/<int:review_id>', views.review_detail, name='review_detail'),
    path('<int:site_id>/reviews/new', views.new_review, name='new_review'),
    path('<int:site_id>/reviews/<int:review_id>/edit', views.review_edit, name='review_edit'),
    path('<int:site_id>/reviews/<int:review_id>/delete', views.review_delete, name='review_delete'),
    path('reviews', views.reviews, name='reviews'),

    # Notes urls
    path('<int:site_id>/notes/<int:note_id>', views.note_detail, name='note_detail'),
    path('<int:site_id>/notes/new', views.new_note, name='new_note'),
    path('<int:site_id>/notes/<int:note_id>/edit', views.note_edit, name='note_edit'),
    path('<int:site_id>/notes/<int:note_id>/delete', views.note_delete, name='note_delete'),
    path('notes', views.notes, name='notes'),
]