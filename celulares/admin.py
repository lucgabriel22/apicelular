from django.contrib import admin
from .models import CelularesBase, Avaliacao

@admin.register(CelularesBase)
class CelularesAdmin(admin.ModelAdmin):
    list_display = (
    'modelo', 
    'ano', 
    'preco',
    'marca'
)
    

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = (
    'celular', 
    'nome', 
    'avaliacao',
    'comentario'
)

