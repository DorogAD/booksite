from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('genre/<str:genre_slug>', get_genre, name='genre'),
]
