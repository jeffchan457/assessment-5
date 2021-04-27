from django.contrib import admin
from .models import Site, Review, Note

admin.site.register([Site, Review, Note])