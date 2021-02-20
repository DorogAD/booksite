# from django import template
# from free_books.models import Genre
#
# register = template.Library()
#
#
# @register.inclusion_tag('free_books/menu_tpl.html')
# def show_menu(menu_class='menu'):
#     genres = Genre.objects.all()
#     return {"genres": genres, "menu_class": menu_class}
