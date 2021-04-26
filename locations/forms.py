from django import forms
from django.db import models
from django.forms import fields
from .models import Site, Review

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['topic', 'site']