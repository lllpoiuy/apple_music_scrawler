from django.urls import path, include
import classical_music.views as views

urlpatterns = [
    path('conductor/<str:id>', views.show_conductor),
    path('album/<str:id>', views.show_album),
    path('song/<str:id>', views.show_song),
    path('conductors', views.show_conductors),
    path('albums', views.show_albums),
    path('songs', views.show_songs),
]
