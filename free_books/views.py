from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book


def index(request):
    return render(request, 'free_books/index.html')


# def get_genre(request, genre_slug):
#     return render(request, 'free_books/genre.html')


class Home(ListView):
    model = Book
    template_name = 'free_books/index.html'
    context_object_name = 'books'  # объект в шаблоне который будет заполняться данными
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Django powered'
        return context


class GetBook(DetailView):
    model = Book  # это значит моделью будет именно эта модель из файла моделей
    template_name = 'free_books/single.html'
    context_object_name = 'book'  # здесь мы вручную задаем имя переменной контекста для лучшей читабельности

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1  # класс Ф нужен для обновления количества просмотров.
        # мы обращаемся к атрибуту вьюс объекта бук и добавляем к имеющемуся там значению еще один просмотр
        self.object.save()  # метод сэйв сохраняет количество просмотров
        self.object.refresh_from_db()  # перезапрашиваем данные из базы данных после сохранения
        return context
