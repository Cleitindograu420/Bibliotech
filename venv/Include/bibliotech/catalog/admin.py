from django.contrib import admin
from .models import Autor, Editora, Livro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'editora', 'isbn', 'genero')
    search_fields = ('titulo', 'autor__nome', 'editora__nome', 'isbn', 'genero')
    list_filter = ('genero', 'data_publicacao')

