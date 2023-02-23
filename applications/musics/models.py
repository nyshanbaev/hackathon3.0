from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator



User = get_user_model()


class Category(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre   


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default='*')
    image = models.ImageField(upload_to='uploads/author/images')

    def __str__(self):
        return f'{self.name + " " + self.surname}'


class Song(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='musics')
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='songs', verbose_name='Исполнитель')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='songs', verbose_name='Жанр')
    song = models.FileField(upload_to='uploads/music', validators=[FileExtensionValidator(allowed_extensions=['mp3'])])


    def __str__(self):
        return f'{self.title}'

class SongImage(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='images')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='uploads/song/images')

    def __str__(self):
        return f'{self.song.title}'

class Playlist(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='playlists')  
    genre = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='playlists' )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='playlists')
    songimage = models.ForeignKey(SongImage, on_delete=models.CASCADE, related_name='playlists')      

    def __str__(self):
        return f'Now is plaing {self.song}'