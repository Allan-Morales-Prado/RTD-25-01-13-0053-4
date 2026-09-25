from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    cantante = models.BooleanField(default=False)
    instrumento = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'artistas'
    
    def __str__(self):
        return f"{self.nombre}"
  
class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_creacion = models.DateField(null=False)
    
    class Meta:
        db_table = 'grupos'
    
    def __str__(self):
            return f"{self.nombre}"
  
class Album(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    year = models.PositiveSmallIntegerField(null=False)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'albums'
        
    def __str__(self):
            return f"{self.titulo} ({self.year})"
  
class ArtistaGrupo(models.Model):
    artista = models.ForeignKey(Artista, on_delete=models.DO_NOTHING)
    grupo = models.ForeignKey(Grupo, on_delete=models.DO_NOTHING)
    fecha_ingreso = models.DateField()
    creacion_registro = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'artista_grupo'
    
    def __str__(self):
        return f"{self.artista.nombre}, de {self.grupo.nombre}"