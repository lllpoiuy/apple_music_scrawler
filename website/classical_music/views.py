from .models import Conductor, Album, Song
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q

def show_conductor(request, id):
    conductor = Conductor.objects.get(conductor_id=str(id))
    template = loader.get_template('conductor/conductor.html')
    # name, url, id, image, introduction, albums
    context = {
        'name': conductor.name,
        'url': conductor.url,
        'id': conductor.conductor_id,
        'image': conductor.image,
        'introduction': conductor.introduction,
        'albums': conductor.albums
    }
    return HttpResponse(template.render(context, request))

def show_album(request, id):
    album = Album.objects.get(album_id=str(id))
    template = loader.get_template('album/album.html')
    # name, url, id, image, conductor_id, songs
    context = {
        'name': album.name,
        'url': album.url,
        'id': album.album_id,
        'image': album.image,
        'conductor_id': album.conductor_id,
        'songs': album.songs,
        'conductor_name': album.conductor_name
    }
    return HttpResponse(template.render(context, request))

def show_song(request, id):
    song = Song.objects.get(song_id=str(id))
    template = loader.get_template('song/song.html')
    # id, name, album_id, conductor_id, composer, url, movements
    context = {
        'id': song.song_id,
        'name': song.name,
        'album_id': song.album_id,
        'conductor_id': song.conductor_id,
        'composer': song.composer,
        'url': song.url,
        'movements': song.movements,
        'conductor_name': song.conductor_name,
        'album_name': song.album_name,
        'album_image': song.album_image
    }
    return HttpResponse(template.render(context, request))

def show_conductors(request):
    conductors_list = Conductor.objects.all()
    
    # Set up pagination with 6 conductors per page (2x3 grid)
    paginator = Paginator(conductors_list, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    template = loader.get_template('conductor/conductors.html')
    context = {
        'page_obj': page_obj
    }
    return HttpResponse(template.render(context, request))

def show_albums(request):
    albums_list = Album.objects.all()
    
    # Set up pagination with 6 albums per page (2x3 grid)
    paginator = Paginator(albums_list, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    template = loader.get_template('album/albums.html')
    context = {
        'page_obj': page_obj
    }
    return HttpResponse(template.render(context, request))

def show_songs(request):
    songs_list = Song.objects.all()
    
    # Set up pagination with 5 songs per page
    paginator = Paginator(songs_list, 5)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    template = loader.get_template('song/songs.html')
    context = {
        'page_obj': page_obj
    }
    return HttpResponse(template.render(context, request))

def search(request):
    query = request.GET.get('query', '')
    
    if query:
        # Search in all three models
        conductors = Conductor.objects.filter(
            Q(name__icontains=query) | 
            Q(introduction__icontains=query)
        )
        
        albums = Album.objects.filter(
            Q(name__icontains=query) | 
            Q(conductor_name__icontains=query)
        )
        
        songs = Song.objects.filter(
            Q(name__icontains=query) | 
            Q(composer__icontains=query) | 
            Q(conductor_name__icontains=query) | 
            Q(album_name__icontains=query)
        )
    else:
        conductors = Album.objects.none()
        albums = Album.objects.none()
        songs = Song.objects.none()
    
    template = loader.get_template('base/search.html')
    context = {
        'query': query,
        'conductors': conductors,
        'albums': albums,
        'songs': songs
    }
    
    return HttpResponse(template.render(context, request))

def home(request):
    # Import for random selection
    import random
    
    # Get all conductors, albums, and songs
    all_conductors = list(Conductor.objects.all())
    all_albums = list(Album.objects.all())
    all_songs = list(Song.objects.all())
    
    # Randomly select 3 featured conductors (or fewer if there aren't enough)
    featured_conductors = random.sample(all_conductors, min(3, len(all_conductors))) if all_conductors else []
    
    # Randomly select 3 featured albums (or fewer if there aren't enough)
    featured_albums = random.sample(all_albums, min(3, len(all_albums))) if all_albums else []
    
    # Randomly select 3 featured songs (or fewer if there aren't enough)
    featured_songs = random.sample(all_songs, min(3, len(all_songs))) if all_songs else []
    
    # Get one featured item for each category display
    featured_conductor = random.choice(all_conductors) if all_conductors else None
    featured_album = random.choice(all_albums) if all_albums else None
    featured_song = random.choice(all_songs) if all_songs else None
    
    template = loader.get_template('base/home.html')
    context = {
        'featured_conductors': featured_conductors,
        'featured_albums': featured_albums,
        'featured_songs': featured_songs,
        'featured_conductor': featured_conductor,
        'featured_album': featured_album,
        'featured_song': featured_song
    }
    return HttpResponse(template.render(context, request))