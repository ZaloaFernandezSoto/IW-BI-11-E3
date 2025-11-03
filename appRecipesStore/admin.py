from django.contrib import admin
from .models import TipoPlato, Ingrediente, Receta


# Register your models here.
admin.site.register(TipoPlato)
admin.site.register(Ingrediente)
admin.site.register(Receta)