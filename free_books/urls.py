from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('book/<str:book_slug>', GetBook.as_view, name='book'),
    path('genre/<str:genre_slug>/', BooksByGenre.as_view(), name='genre'),
    # path('genre/<str:genre_slug>', get_genre, name='genre'),
]
