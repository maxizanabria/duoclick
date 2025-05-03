
from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.nombre} - {self.email}"