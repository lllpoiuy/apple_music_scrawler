from django.db import models


class Conductor(models.Model):
    # name, url, id, image, introduction, albums
    name = models.CharField(max_length=100, unique=False)
    url = models.URLField(max_length=200, unique=False)
    conductor_id = models.CharField(max_length=50, unique=True)
    image = models.URLField(max_length=200, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    albums = models.JSONField(default=list, blank=True)

class Album(models.Model):
    # id, name, url, conductor_id, image, songs
    name = models.CharField(max_length=100, unique=False)
    url = models.URLField(max_length=200, unique=False)
    album_id = models.CharField(max_length=50, unique=True)
    image = models.URLField(max_length=200, blank=True, null=True)
    conductor_id = models.CharField(max_length=50, blank=True, null=True)
    songs = models.JSONField(default=list, blank=True)
    conductor_name = models.CharField(max_length=100, blank=True, null=True)

class Song(models.Model):
    # id, name, album_id, conductor_id, composer, url, movements
    name = models.CharField(max_length=100, unique=False)
    song_id = models.CharField(max_length=50, unique=True)
    album_id = models.CharField(max_length=50, blank=True, null=True)
    conductor_id = models.CharField(max_length=50, blank=True, null=True)
    composer = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    movements = models.JSONField(default=list, blank=True)
    conductor_name = models.CharField(max_length=100, blank=True, null=True)
    album_name = models.CharField(max_length=100, blank=True, null=True)
    album_image = models.URLField(max_length=200, blank=True, null=True)