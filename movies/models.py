from django.db import models

# Create your models here.
class Movie(models.Model):
    # CharField(String) 는 반드시 max_length 를 지정해 줘야 된다.
    title = models.CharField(max_length=100)
    title_origin = models.CharField(max_length=100)
    vote_count = models.IntegerField()
    open_date = models.CharField(max_length=30)
    genre = models.CharField(max_length=20)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
