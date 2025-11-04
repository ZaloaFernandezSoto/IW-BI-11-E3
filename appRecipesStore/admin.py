from django.contrib import admin
from .models import TipoPlato, Ingrediente, Receta


# Register your models here.
@admin.register(TipoPlato)
class TipoPlatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_plato', 'tiempo_preparacion', 'imagen')
    list_filter = ('tipo_plato',)
    search_fields = ('nombre', 'instrucciones')
    filter_horizontal = ('ingredientes',)
    fieldsets = (
        ('Información General', {
            'fields': ('nombre', 'tipo_plato', 'tiempo_preparacion')
        }),
        ('Contenido', {
            'fields': ('ingredientes', 'instrucciones')
        }),
        ('Imagen', {
            'fields': ('imagen',),
            'description': 'Guarda la imagen en static/appRecipesStore/img/ y escribe aquí solo el nombre del archivo (ej: paella.jpg)'
        }),
    )