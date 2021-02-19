from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"book_slug": ("book_title",)}
    save_as = True
    save_on_top = True
    list_display = (  # указываем поля которые будем показываеть в админке при просмотре общего списка книг
    'book_title', 'book_slug', 'book_author', 'book_annotation', 'created_at', 'get_photo', 'book_offer',
    'book_owner', 'book_views')
    list_display_links = ('book_slug', 'book_title')  # поля которые будут отображаться как ссылки
    search_fields = ('book_title',)  # поле по которому будет производиться поиск
    list_filter = ('book_genre',)  # поля по которым будем фильтровать
    readonly_fields = ('book_views', 'created_at', 'get_photo')  # поля только для чтения
    fields = (  # указываем поля которые будем показывать внутри книги, порядок указания - это порядок отображения
    'book_title', 'book_slug', 'book_author', 'book_genre', 'book_annotation', 'created_at', 'get_photo', 'book_photo',
    'book_offer', 'book_owner', 'book_views')

    def get_photo(self, obj):
        if obj.book_photo:
            return mark_safe(f'<img src="{obj.book_photo.url}" width="50"')
        return '-'

    get_photo.short_description = 'миниатюра'


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"genre_slug": ("genre_title",)}


class TownAdmin(admin.ModelAdmin):
    prepopulated_fields = {"town_slug": ("town_title",)}


class OfferAdmin(admin.ModelAdmin):
    prepopulated_fields = {"offer_slug": ("offer_title",)}


class OwnerAdmin(admin.ModelAdmin):
    prepopulated_fields = {"owner_slug": ("owner_name",)}


admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(Owner, OwnerAdmin)
