from django.db import models

# Create your models here.
class Produccion(models.Model):
    nombre = models.TextField(default='', blank=False)
    temporadas = models.IntegerField(default=0, blank=False)
    capitulos = models.IntegerField(default=0, blank=False)
    duracion = models.IntegerField(default=0, blank=False)
    clasificacion = models.TextField(default='', blank=False)
    categoria = models.TextField(default='', blank=False)
    idioma = models.TextField(default='', blank=False)
    plataforma = models.TextField(default='', blank=False)
    director = models.TextField(default='', blank=False)
    protagonista = models.TextField(default='', blank=False)
    resena = models.TextField(default='', blank=False)