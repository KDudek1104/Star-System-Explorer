from .utils import sort_stars_by_distance
from django.http import HttpResponse
import json
from django.shortcuts import render, get_object_or_404
from .models import StarSystem, Star
from .forms import SystemForm, StarForm, SearchForm
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from .models import Star
from django.db import transaction


def index(request):
    systems = StarSystem.objects.all()
    stars = Star.objects.all()

    # Search form
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        star_name = search_form.cleaned_data['star_name']
        if star_name:
            stars = stars.filter(name__icontains=star_name)

    # Use the implemented function for sorting the stars (uses QuickSort)
    sorted_stars = sort_stars_by_distance(stars)

    return render(request, 'explorer/index.html',
                  {'systems': systems, 'stars': sorted_stars, 'search_form': search_form})


def delete_star(request, system_id, star_id):
    star = get_object_or_404(Star, pk=star_id)
    star.delete()
    return redirect('explorer:index')

def system_detail(request, system_id):
    system = get_object_or_404(StarSystem, pk=system_id)
    return render(request, 'explorer/system_detail.html', {'system': system})

def star_detail(request, system_id, star_id):
    star = get_object_or_404(Star, pk=star_id)
    return render(request, 'explorer/star_detail.html', {'star': star})

def add_system(request):
    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            system_name = form.cleaned_data['name']
            new_system = StarSystem.objects.create(name=system_name)
            return redirect('explorer:index')  # Przekieruj na stronę główną po dodaniu systemu
    else:
        form = SystemForm()

    return render(request, 'explorer/add_star.html', {'form': form})

def show_gallery(request):
    systems = StarSystem.objects.all()
    return render(request, 'explorer/show_gallery.html', {'systems': systems})

def delete_all_stars(request):
    # Usuń wszystkie gwiazdy
    Star.objects.all().delete()
    return redirect('explorer:index')  # After deleting all stars stay on the same page (index.html)

def download_data(request):
    # Load all stars from the gallery
    stars = Star.objects.all()

    sorted_stars = sort_stars_by_distance(stars)

    # Prepare star details in JSON
    star_data = [
        {"name": star.name, "distance": star.distance}
        for star in sorted_stars
    ]

    # Save data into the JSON file
    file_path = "star_data.json"
    with open(file_path, 'w') as json_file:
        json.dump(star_data, json_file)

    # Download the JSON file
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="star_data.json"'
        return response

@transaction.atomic  # To make the database more consistent
def load_data(request):
    if request.method == 'POST' and request.FILES.get('data_file'):
        uploaded_file = request.FILES['data_file']

        try:
            data = json.load(uploaded_file)
            system, created = StarSystem.objects.get_or_create(name='Loaded System')
            count = 0
            for entry in data:
                name = entry.get('name', '')
                distance = entry.get('distance', 0)
                Star.objects.get_or_create(name=name, distance=distance, system=system)
                count += 1
            object_count = count
            # object_count = len(data)

            return render(request, 'explorer/load_success.html', {'object_count': object_count})

        except json.JSONDecodeError:
            error_message = 'Invalid JSON file'
            return render(request, 'explorer/load_data.html', {'success': False, 'message': error_message})

    else:
        return render(request, 'explorer/load_data.html')

def add_star(request):
    if request.method == 'POST':
        form = StarForm(request.POST)
        if form.is_valid():
            star_name = form.cleaned_data['name']
            star_distance = form.cleaned_data['distance']
            system_name = form.cleaned_data['system_name']  # Dodaj  pole system_name do formularza
            system, created = StarSystem.objects.get_or_create(name=system_name)
            new_star = Star.objects.create(name=star_name, distance=star_distance, system=system)
            return redirect('explorer:star_detail', system_id=system.id, star_id=new_star.id)
    else:
        form = StarForm()

    return render(request, 'explorer/add_star.html', {'form': form})
