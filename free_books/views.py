from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Genre


class Home(ListView):
    model = Book
    template_name = 'free_books/index.html'
    context_object_name = 'books'  # объект в шаблоне который будет заполняться данными
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Django powered'
        return context


class GetBook(DetailView):
    model = Book  # это значит моделью будет именно эта модель из файла моделей
    template_name = 'free_books/single.html'
    context_object_name = 'book'  # здесь мы вручную задаем имя переменной контекста для лучшей читабельности

    def get_context_data(self, *, object_list=None, **kwargs):  # нужен для увеличения количества просмотров
        context = super().get_context_data(**kwargs)
        self.object.book_views = F('book_views') + 1  # класс Ф нужен для обновления количества просмотров.
    #     мы обращаемся к атрибуту вьюс объекта бук и добавляем к имеющемуся там значению еще один просмотр
        self.object.save()  # метод сэйв сохраняет количество просмотров
        self.object.refresh_from_db()  # перезапрашиваем данные из базы данных после сохранения
        return context


class BooksByGenre(ListView):
    template_name = 'free_books/index.html'
    context_object_name = 'books'
    paginate_by = 2
    allow_empty = False  # чтобы при запросе пустой либо несуществующей категории у нас была ошибка 404

    def get_queryset(self):
        return Book.objects.filter(book_genre__genre_slug=self.kwargs['genre_slug'])
        #  через поле book_genre обращаемся к полю genre_slug модели Genre и запрашиваем книги у которых genre_slug
        #  равен полученному

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_title'] = Genre.objects.get(genre_slug=self.kwargs['genre_slug'])
        return context
