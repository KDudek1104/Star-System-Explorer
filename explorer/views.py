from .utils import sort_stars_by_distance
from django.http import HttpResponse
import json
from django.shortcuts import render, get_object_or_404, redirect
from .models import StarSystem, Star
from .forms import StarForm, SearchForm

def index(request):
    systems = StarSystem.objects.all()
    stars = Star.objects.all()
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        star_name = search_form.cleaned_data['star_name']
        if star_name:
            stars = stars.filter(name__icontains=star_name)

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

def delete_all_stars(request):
    Star.objects.all().delete()
    return redirect('explorer:index')

def download_data(request):
    stars = Star.objects.all()
    sorted_stars = sort_stars_by_distance(stars)
    star_data = [
        {"name": star.name, "distance": star.distance}
        for star in sorted_stars
    ]

    file_path = "star_data.json"
    with open(file_path, 'w') as json_file:
        json.dump(star_data, json_file)

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="star_data.json"'
        return response

import json
from django.shortcuts import render
from .models import StarSystem, Star

import json
from django.shortcuts import render
from .models import StarSystem, Star

def load_data(request):
    if request.method == 'POST' and request.FILES.get('data_file'):
        uploaded_file = request.FILES['data_file']
        try:
            data = uploaded_file.read()
            data = json.loads(data.decode('utf-8'))
            system, created = StarSystem.objects.get_or_create(name='Loaded System')
            count = 0
            existing_star_names = set(Star.objects.filter(system=system).values_list('name', flat=True))

            for entry in data:
                name = entry.get('name', '')
                distance = entry.get('distance', 0)

                # Sprawdzenie, czy gwiazda o danej nazwie już istnieje w systemie
                if name not in existing_star_names:
                    Star.objects.create(name=name, distance=distance, system=system)
                    existing_star_names.add(name)
                    count += 1

            object_count = count

            return render(request, 'explorer/load_success.html', {'object_count': object_count})

        except json.JSONDecodeError:
            error_message = 'Invalid JSON file'
            return render(request, 'explorer/load_data.html', {'success': False, 'message': error_message})
    else:
        return render(request, 'explorer/load_data.html')


from django.shortcuts import render, redirect
from .forms import StarForm
from .models import StarSystem, Star

def add_star(request):
    if request.method == 'POST':
        form = StarForm(request.POST)
        if form.is_valid():
            star_name = form.cleaned_data['name']
            star_distance = form.cleaned_data['distance']
            system_name = form.cleaned_data['system_name']

            existing_star = Star.objects.filter(name=star_name).first()
            if existing_star:
                return render(request, 'explorer/add_star.html', {'form': form, 'error_message': 'This star already exists'})

            system, created = StarSystem.objects.get_or_create(name=system_name)
            new_star = Star.objects.create(name=star_name, distance=star_distance, system=system)
            return redirect('explorer:star_detail', system_id=system.id, star_id=new_star.id)
    else:
        form = StarForm()
    return render(request, 'explorer/add_star.html', {'form': form})
