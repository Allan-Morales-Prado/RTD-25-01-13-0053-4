# models.py
from django.contrib.auth.models import User
from django.db import models

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username