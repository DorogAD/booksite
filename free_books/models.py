from django.db import models
from django.urls import reverse


class Genre(models.Model):
    genre_title = models.CharField(default='Без жанра', max_length=50)
    genre_slug = models.SlugField(max_length=50, verbose_name='genre_url', unique=True)

    def __str__(self):
        return self.genre_title

    def get_absolute_url(self):
        return reverse('genre', kwargs={"genre_slug": self.genre_slug})

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['genre_title']


class Town(models.Model):
    town_title = models.CharField(max_length=50)
    town_slug = models.SlugField(max_length=50, verbose_name='town_url', unique=True)

    def __str__(self):
        return self.town_title

    def get_absolute_url(self):
        return reverse('town', kwargs={"town_slug": self.town_slug})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['town_title']


class Offer(models.Model):
    offer_title = models.CharField(max_length=50)
    offer_slug = models.SlugField(max_length=50, verbose_name='offer_url', unique=True)

    def __str__(self):
        return self.offer_title

    def get_absolute_url(self):
        return reverse('offer', kwargs={"offer_slug": self.offer_slug})

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'
        ordering = ['offer_title']


class Owner(models.Model):
    owner_name = models.CharField(max_length=100, verbose_name='Владелец книги')
    owner_slug = models.SlugField(max_length=100, verbose_name='owner_url', unique=True)
    owner_email = models.EmailField(blank=False, unique=True)
    owner_town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='owner_town', verbose_name='Город')

    def __str__(self):
        return self.owner_name

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
        ordering = ['owner_name']

    def get_absolute_url(self):
        return reverse('owner', kwargs={"owner_slug": self.owner_slug})


class Book(models.Model):
    book_title = models.CharField(max_length=255, verbose_name='Название книги')
    book_slug = models.SlugField(max_length=255, verbose_name='book_url', unique=True)
    book_author = models.CharField(max_length=100, verbose_name='Автор книги')
    book_annotation = models.TextField(verbose_name='Аннотация')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    book_photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    book_views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    book_owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='book_owner', verbose_name='Владелец книги')
    book_genre = models.ManyToManyField(Genre, related_name='book_genre', verbose_name='Жанр')
    book_offer = models.ForeignKey(Offer, on_delete=models.CASCADE, related_name='book_offer', verbose_name='Вариант')

    def __str__(self):
        return self.book_title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created_at']
        permissions = (("can_post", "can post"),)

    def get_absolute_url(self):
        return reverse('book', kwargs={"book_slug": self.book_slug})
        # маршрут book
