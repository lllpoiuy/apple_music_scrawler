import json
import os
import sys

def main():
    with open('../classical_music_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    from classical_music.models import Conductor
    print(Conductor.objects.all())
    Conductor.objects.all().delete()

    for item in data["conductors"]:
        # albums = []
        # for album in item.get("albums", []):
        #     albums.append(album.get("id", ""))
        conductor, created = Conductor.objects.get_or_create(
            conductor_id = item["id"],
            defaults={
                'name': item["name"],
                'url': item["url"],
                'image': item.get("image", ""),
                'introduction': item.get("introduction", ""),
                'albums': item.get("albums", [])
            }
        )
        if created:
            print(f"Created new conductor: {conductor.name}")
        else:
            print(f"Conductor already exists: {conductor.name}")
    
    from classical_music.models import Album
    print(Album.objects.all())
    Album.objects.all().delete()

    for item in data["albums"]:
        # songs = []
        # for song in item.get("songs", []):
        #     songs.append(song.get("id", ""))
        conductor_name = ""
        conductor_id = item.get("conductor_id", "")
        if conductor_id:
            conductor = Conductor.objects.filter(conductor_id=conductor_id).first()
            if conductor:
                conductor_name = conductor.name
        album, created = Album.objects.get_or_create(
            album_id=item["id"],
            defaults={
                'name': item["name"],
                'url': item["url"],
                'image': item.get("image", ""),
                'conductor_id': item.get("conductor_id", ""),
                'songs': item.get("songs", []),
                'conductor_name': conductor_name
            }
        )
        if created:
            print(f"Created new album: {album.name}")
        else:
            print(f"Album already exists: {album.name}")

    from classical_music.models import Song
    print(Song.objects.all())
    Song.objects.all().delete()

    for item in data["songs"]:
        # movements = []
        # for movement in item.get("movements", []):
        #     movements.append(movement.get("id", ""))
        album_name = ""
        album_image = ""
        album_id = item.get("album_id", "")
        if album_id:
            album = Album.objects.filter(album_id=album_id).first()
            if album:
                album_name = album.name
                album_image = album.image
        conductor_name = ""
        conductor_id = item.get("conductor_id", "")
        if conductor_id:
            conductor = Conductor.objects.filter(conductor_id=conductor_id).first()
            if conductor:
                conductor_name = conductor.name
        song, created = Song.objects.get_or_create(
            song_id=item["id"],
            defaults={
                'name': item["name"],
                'album_id': item.get("album_id", ""),
                'conductor_id': item.get("conductor_id", ""),
                'composer': item.get("composer", ""),
                'url': item.get("url", ""),
                'movements': item.get("movements", []),
                'conductor_name': conductor_name,
                'album_name': album_name,
                'album_image': album_image,
            }
        )
        if created:
            print(f"Created new song: {song.name}")
        else:
            print(f"Song already exists: {song.name}")

from django.core.management import execute_from_command_line
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')
    execute_from_command_line(sys.argv)
    main()