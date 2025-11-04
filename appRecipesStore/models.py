from django.db import models

# Create your models here.
# appRecipesStore/models.py
from django.db import models

class TipoPlato(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(default="Sin descripcion")

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(default="Sin descripcion")

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    nombre = models.CharField(max_length=200)
    tipo_plato = models.ForeignKey(TipoPlato, on_delete=models.CASCADE, related_name='recetas')
    ingredientes = models.ManyToManyField(Ingrediente, related_name='recetas')
    tiempo_preparacion = models.IntegerField(help_text="Tiempo en minutos")
    instrucciones = models.TextField()
    imagen = models.CharField(max_length=500, blank=True, null=True, help_text="Ruta de la imagen en static/appRecipesStore/img/")

    def __str__(self):
        return self.nombre