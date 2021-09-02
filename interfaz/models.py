from django.db import models

# Create your models here.

class ingredientes(models.Model):
    nombre = models.CharField(max_length=50)
    ingrediente1 = models.CharField(max_length=50)
    ingrediente2 = models.CharField(max_length=50)
    ingrediente3 = models.CharField(max_length=50)
    ingrediente4 = models.CharField(max_length=50)
    ingrediente5 = models.CharField(max_length=50)
    receta = models.CharField(max_length=1500)
    imagen = models.ImageField(null=True)

    def __str__(self):
        return f'{self.id} {self.nombre}: {self.ingrediente1} {self.ingrediente2} {self.ingrediente3} {self.ingrediente4} {self.receta} {self.imagen}'