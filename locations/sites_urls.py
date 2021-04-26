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
]