from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    comentario = models.TextField(blank=True)
    
