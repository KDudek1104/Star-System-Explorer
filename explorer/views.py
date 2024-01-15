from .utils import sort_stars_by_distance
from django.http import HttpResponse
import json
from django.shortcuts import render, get_object_or_404
from .models import StarSystem, Star
from .forms import SystemForm, StarForm, SearchForm
from django.shortcuts import redirect


def index(request):
    systems = StarSystem.objects.all()
    stars = Star.objects.all()

    # Dodaj kilka przykładowych gwiazd, jeśli nie ma żadnych w bazie danych
    if not stars.exists():
        # Zakładając, że masz wcześniej zdefiniowane systemy, możemy teraz dodać więcej gwiazd do tych systemów
        system_sirius = StarSystem.objects.create(name='Sirius System')
        system_alpha_centauri = StarSystem.objects.create(name='Alpha Centauri System')
        system_orion = StarSystem.objects.create(name='Orion System')

        # Dodaj więcej gwiazd do systemu Sirius
        Star.objects.create(name='Sirius A', distance=8.6, system=system_sirius)
        Star.objects.create(name='Sirius B', distance=8.6, system=system_sirius)

        # Dodaj więcej gwiazd do systemu Alpha Centauri
        Star.objects.create(name='Alpha Centauri A', distance=4.37, system=system_alpha_centauri)
        Star.objects.create(name='Alpha Centauri B', distance=4.37, system=system_alpha_centauri)
        Star.objects.create(name='Proxima Centauri', distance=4.24, system=system_alpha_centauri)

        # Dodaj więcej gwiazd do systemu Orion
        Star.objects.create(name='Betelgeuse', distance=427, system=system_orion)
        Star.objects.create(name='Rigel', distance=860, system=system_orion)
        Star.objects.create(name='Bellatrix', distance=243, system=system_orion)

    # Przetwarzaj formularz wyszukiwania
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        star_name = search_form.cleaned_data['star_name']
        if star_name:
            stars = stars.filter(name__icontains=star_name)

    # Użyj zaimplementowanej funkcji sortującej
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


def download_data(request):
    # Pobierz wszystkie gwiazdy z widoku index
    stars = Star.objects.all()

    sorted_stars = sort_stars_by_distance(stars)

    # Przygotuj dane gwiazd w formacie JSON
    star_data = [
        {"name": star.name, "distance": star.distance}
        for star in sorted_stars    
    ]

    # Zapisz dane do pliku JSON
    file_path = "star_data.json"
    with open(file_path, 'w') as json_file:
        json.dump(star_data, json_file)

    # Pobierz plik JSON
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="star_data.json"'
        return response


def load_data(request):
    if request.method == 'POST' and request.FILES.get('data_file'):
        uploaded_file = request.FILES['data_file']

        try:
            # Odczytaj dane z pliku JSON
            data = json.load(uploaded_file)

            # Utwórz system, jeśli nie istnieje
            system, created = StarSystem.objects.get_or_create(name='Loaded System')

            # Dodaj gwiazdy na podstawie danych z pliku
            for entry in data:
                name = entry.get('name', '')
                distance = entry.get('distance', 0)

                # Utwórz gwiazdę w systemie
                Star.objects.create(name=name, distance=distance, system=system)

            # Przekieruj użytkownika do strony index.html po pomyslnym wczytaniu danych
            return redirect('explorer:index')

        except json.JSONDecodeError:
            # Komunikat o błędzie w pliku JSON
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
