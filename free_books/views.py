from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'free_books/index.html')


# def get_genre(request, genre_slug):
#     return render(request, 'free_books/genre.html')
