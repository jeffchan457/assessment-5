from django import forms
from django.db import models
from django.forms import fields
from .models import Site, Review, Note

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['topic', 'site']



class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['topic', 'site']