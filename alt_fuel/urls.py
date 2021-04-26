from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # I newly added this:
    path('accounts/', include('accounts.urls')),
    
    path('accounts/', include('django.contrib.auth.urls')),

    # I newly added this:
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('search/', include('locations.search_urls')),
    path('sites/', include('locations.sites_urls')),
]