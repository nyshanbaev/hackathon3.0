from django.db import models
from django.contrib.auth import get_user_model
from applications.musics.models import *
from django.core.validators import MaxValueValidator, MinValueValidator 

User = get_user_model()

class Like(models.Model):
    """
       Models of likes
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    song = models.ForeignKey(Song, on_delete=models.CASCADE,related_name='likes' )
    is_like = models.BooleanField(default=False)

    def str(self):
        return f'{self.user} likes  {self.song.title}'

class Dislike(models.Model):
    """
       Models of dislikes
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dislikes') 
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='dislikes')
    is_dislike = models.BooleanField(default=False) 

    def str(self):
        return f'{self.user}  dislikes  {self.song.title}'  


class Rating(models.Model):
    """
        Models of ratings
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='ratings')  
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], blank=True, null=True)

    def str(self):
        return f'{self.user}  {self.song.title}'
   
   
class Favorite(models.Model):
    """
       Models of favorites
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='favorites') 

    def str(self):
        return f"{self.user}'s favorite song is {self.song.title}"

class Feedback(models.Model):
    """
        Models of feedbacks
    """
    CHOICES = (
        ('bad', ':\\'),
        ('awful', '>:('),
        ('not bad', ':|'),
        ('ok', ';)'),
        ('good', '^_^'),
        ('good', '^_^'),
        ("i'm in shock", 'O.o'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='feedbacks')
    feedback = models.CharField(choices=CHOICES, max_length=20)

    def str(self):
        return f'{self.feedback} -> {self.song.title}'