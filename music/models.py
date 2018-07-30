from django.db import models

# Create your models here.

class Artist(models.Model):
    name=models.CharField(max_length=250)
    music_type=models.CharField(max_length=250)
    def __str__(self):
        return self.name +" "+self.music_type

class Album(models.Model):
    artist=models.ForeignKey(Artist,on_delete= models.CASCADE)
    album_title=models.CharField(max_length=500)
    genre = models.CharField(max_length =100)
    album_logo = models.CharField(max_length= 1000)
    def __str__(self):
        return self.album_title
        

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type= models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
    def __str__(self):
        return self.song_title
        




