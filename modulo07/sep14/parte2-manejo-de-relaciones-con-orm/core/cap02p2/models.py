from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.titulo

class Autor(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    
    libros = models.ManyToManyField(
        Libro, 
        through="AutorLibro", 
        related_name="autores"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class AutorLibro(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    
    traduccion = models.CharField(max_length=30)
    edicion = models.PositiveSmallIntegerField(null=False, default=1)
    creado_por = models.CharField(max_length=50, null=False, blank=False)
    creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} - {self.libro} (por {self.creado_por})"