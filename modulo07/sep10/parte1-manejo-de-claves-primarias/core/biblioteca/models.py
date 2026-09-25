from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    
    class Meta:
      db_table = 'libros'

    def __str__(self):
        return self.titulo
