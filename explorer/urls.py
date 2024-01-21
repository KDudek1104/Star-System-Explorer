from django.urls import path
from .views import index, system_detail, load_data, star_detail
from .views import show_gallery, add_system, add_star, delete_star, download_data, delete_all_stars

app_name = 'explorer'

urlpatterns = [
    path('', index, name='index'),
    path('add_system/', add_system, name='add_system'),
    path('add_star/', add_star, name='add_star'),
    path('add_star/<int:system_id>/', add_star, name='add_star'),
    path('load_data/', load_data, name='load_data'),
    path('download_data/', download_data, name='download_data'),
    path('show_gallery/', show_gallery, name='show_gallery'),
    path('<int:system_id>/', system_detail, name='system_detail'),
    path('<int:system_id>/<int:star_id>/', star_detail, name='star_detail'),
    path('delete_all_stars/', delete_all_stars, name='delete_all_stars'),
    path('<int:system_id>/delete_star/<int:star_id>/', delete_star, name='delete_star'),
]

