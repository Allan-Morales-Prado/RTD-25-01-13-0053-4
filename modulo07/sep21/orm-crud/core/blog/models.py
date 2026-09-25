from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    contenido = models.TextField(unique=True)
    fecha_de_creacion = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_de_creacion']
        constraints = [
            models.UniqueConstraint(
                fields=["titulo", "contenido"],
                name="unique_titulo_contenido",
            )
        ]

    def __str__(self):
        return f"[{self.fecha_de_creacion}]: {self.titulo}"