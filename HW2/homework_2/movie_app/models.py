from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True, null=False, max_length=11)
    title = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length = 500, null=True)
    director = models.CharField(max_length = 100, null=True)
    release_year = models.CharField(max_length = 50, null=True)
    budget = models.CharField(max_length = 50, null=True)
    runtime = models.CharField(max_length = 50, null=True)
    rating = models.CharField(max_length = 50, null=True)
    genre = models.CharField(max_length = 50, null=True)

class User(models.Model):
    user_id = models.AutoField(max_length=11, null=False, primary_key=True)
    username = models.CharField(max_length = 50, null=False)
    password = models.CharField(max_length = 50, null=False)
    first_name = models.CharField(max_length = 50, null=True)
    last_name = models.CharField(max_length = 50, null=True)
    email = models.CharField(max_length = 100, null=True)

def __str__(self):
    return self.username



