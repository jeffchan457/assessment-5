from django.contrib import admin
from .models import Site, Review

admin.site.register([Site, Review])