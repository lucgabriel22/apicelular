from django.contrib import admin
from .models import CelularesBase, Avaliacao

@admin.register(CelularesBase)
class CelularesAdmin(admin.ModelAdmin):
    list_display = (
    'marca',
    'modelo', 
    'ano', 
    'preco',
    'criacao',
    'atualizacao',
    'ativo'
)
    

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = (
    'celular',
    'nome',
    'email', 
    'avaliacao',
    'comentario',
    'criacao',
    'atualizacao',
    'ativo'
)

