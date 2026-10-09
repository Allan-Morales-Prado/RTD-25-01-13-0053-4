from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    horario = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.titulo
