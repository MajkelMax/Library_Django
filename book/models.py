from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=50, verbose_name="Tytuł")
    author = models.CharField(max_length=50, verbose_name="Autor")
    pub_date = models.DateField(verbose_name="Data publikacji (RRRR-MM-DD)")
    isbn = models.IntegerField(verbose_name="Numer ISBN")
    pages = models.PositiveIntegerField(verbose_name="Liczba stron")
    language = models.CharField(max_length=10, verbose_name="Język test")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})

