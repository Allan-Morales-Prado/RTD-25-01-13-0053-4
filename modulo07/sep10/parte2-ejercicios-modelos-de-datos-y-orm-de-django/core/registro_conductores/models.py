from django.db import models

class Conductor(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)

    class Meta:
      db_table = 'conductor'

    def __str__(self):
        return f"{self.rut} | {self.nombre} | {self.apellido}"

class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    dpto = models.CharField(max_length=10, null=False)
    comuna = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)
    conductor = models.OneToOneField(Conductor, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'direccion'

    def __str__(self):
        return f"{self.calle} #{self.numero}"

class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, unique=True)
    marca = models.CharField(max_length=50, null=False)
    modelo = models.CharField(max_length=50, null=False)
    year = models.DateField(null=False)
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vehiculo'

    def __str__(self):
        return f"{self.patente}"