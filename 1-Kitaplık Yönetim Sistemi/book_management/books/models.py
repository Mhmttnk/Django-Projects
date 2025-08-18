from django.db import models
import datetime

year_choices = [(r, r) for r in range(1900, datetime.date.today().year+1)]

class Book_Management(models.Model):
    book_name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    page=models.PositiveIntegerField()
    type=models.CharField(max_length=50)
    publication_date=models.PositiveSmallIntegerField(choices=year_choices, default=datetime.date.today().year)

    def __str__(self):
        return f"{self.book_name},{self.author},{self.page},{self.page},{self.publication_date}"
