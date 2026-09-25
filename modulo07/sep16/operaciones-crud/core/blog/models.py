from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_de_publicacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'post'
        ordering = ['-fecha_de_publicacion']
        constraints = [
            models.UniqueConstraint(
                fields=["titulo", "contenido"],
                name="unique_titulo_contenido",
            )
        ]
    
    def __str__(self):
        return self.titulo
