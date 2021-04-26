from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.search_form, name='search_form'),
    path('locations_list', views.locations_list, name='locations_list'),
]