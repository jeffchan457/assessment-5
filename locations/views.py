from django.shortcuts import render, redirect
import requests as req
from .models import Site, Review, Note
from .forms import SiteForm, ReviewForm, NoteForm
from django.http import HttpResponse, JsonResponse


def search_form(request):
    return render(request, 'locations/search_form.html')

def locations_list(request):
    zip = request.POST['zip']
    alt_fuel_url = _generate_alt_fuel_url(zip)
    response = req.get(alt_fuel_url)
    data = response.json()
    location_data = []
    for location in data['fuel_stations'][:10]:
        new_location = {
            'name': location['station_name'],
            'address': location['street_address'],
            'phone': location['station_phone'],
            'ev_network': location['ev_network'],
            'ev_network_web': location['ev_network_web'],
            'latitude': location['latitude'],
            'longitude': location['longitude']
        }
        location_data.append(new_location)
    modified_location_data = _generate_google_maps_url(location_data)
    html_data = {
        'zip': zip,
        'locations': modified_location_data
    }
    return render(request, 'locations/locations_list.html', html_data)

def _generate_alt_fuel_url(zip):
    return f"https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=ELEC&access=public&zip={ zip }&limit=all&api_key=OWCWkTrTJnxg5LrwmOzTV2LCtfyfCdGEvTpivbVl"

def _generate_google_maps_url(location_data):
    for location in location_data:
        latitude = location['latitude']
        longitude = location['longitude']
        location['site'] = f"https://www.google.com/maps/embed/v1/place?key=AIzaSyCH8NrqyjTmUijRqekgmis-vWGw4mVsu5o&q={ latitude },{ longitude }&zoom=18&maptype=satellite"
    return location_data

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def sites(request):
    all_sites = Site.objects.all()
    return render(request, 'sites/sites.html', {'all_sites': all_sites})

def site_detail(request, site_id):
    site = Site.objects.get(id=site_id)
    return render(request, 'sites/site_detail.html', {'site': site})

def new_site(request):
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.save()
            return redirect('site_detail', site_id=site.id)
    else:
        form = SiteForm()
    return render(request, 'sites/site_form.html', {'form': form, 'type': 'New'})

def site_edit(request, site_id):
    site = Site.objects.get(id=site_id)
    if request.method == "POST":
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            site = form.save(commit=False)
            site.save()
            return redirect('site_detail', site_id=site.id)
    else:
        form = SiteForm(instance=site)
    return render(request, 'sites/site_form.html', {'form': form, 'type': 'Edit'})

def site_delete(request, site_id):
    if request.method == "POST":
        site = Site.objects.get(id=site_id)
        site.delete()
    return redirect('sites')

def review_detail(request, site_id, review_id):
    site = Site.objects.get(id=site_id)
    review = Review.objects.get(id=review_id)
    return render(request, 'sites/review_detail.html', {'site': site, 'review': review})

def new_review(request, site_id):
    site = Site.objects.get(id=site_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('review_detail', site_id=site.id, review_id=review.id)
    else:
        form = ReviewForm(initial={'site': site})
    return render(request, 'sites/review_form.html', {'form': form, 'type': 'New', 'site': site})

def review_edit(request, site_id, review_id):
    site = Site.objects.get(id=site_id)
    review = Review.objects.get(id=review_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.save()
            return redirect('review_detail', site_id=site.id, review_id=review.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'sites/review_form.html', {'form': form, 'type': 'Edit', 'site': site})

def review_delete(request, site_id, review_id):
    if request.method == "POST":
        review = Review.objects.get(id=review_id)
        review.delete()
    return redirect('site_detail', site_id=site_id)

def reviews(request):
    all_reviews = Review.objects.all()
    return render(request, 'sites/reviews.html', {'all_reviews': all_reviews})





def note_detail(request, site_id, note_id):
    site = Site.objects.get(id=site_id)
    note = Note.objects.get(id=note_id)
    return render(request, 'sites/note_detail.html', {'site': site, 'note': note})

def new_note(request, site_id):
    site = Site.objects.get(id=site_id)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', site_id=site.id, note_id=note.id)
    else:
        form = NoteForm(initial={'site': site})
    return render(request, 'sites/note_form.html', {'form': form, 'type': 'New', 'site': site})

def note_edit(request, site_id, note_id):
    site = Site.objects.get(id=site_id)
    note = Note.objects.get(id=note_id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_detail', site_id=site.id, note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'sites/note_form.html', {'form': form, 'type': 'Edit', 'site': site})

def note_delete(request, site_id, note_id):
    if request.method == "POST":
        note = Note.objects.get(id=note_id)
        note.delete()
    return redirect('site_detail', site_id=site_id)

def notes(request):
    all_notes = Note.objects.all()
    return render(request, 'sites/notes.html', {'all_notes': all_notes})