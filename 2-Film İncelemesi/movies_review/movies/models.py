from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

year_choices=[(r,r) for r in range(1980,datetime.date.today().year+1)]

class Movie(models.Model):
    name=models.CharField(max_length=25)
    genre=models.CharField(max_length=20)
    year=models.PositiveSmallIntegerField(choices=year_choices, default=datetime.date.today().year)
    director=models.CharField(max_length=25, blank=True, null= True)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}, {self.genre}, {self.year},{self.director}'

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,  related_name='reviews', null=True, blank=True)
    comment=models.TextField(max_length=100)
    rating=models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
                MinValueValidator(1),
                MaxValueValidator(10)
            ]
        )
    
    def __str__(self):
        return f'{self.comment}, {self.rating}'
            