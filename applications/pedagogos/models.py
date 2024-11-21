from django.db import models

class Pedagogo(models.Model):
    idPedagogo = models.AutoField(primary_key=True)  # AUTO_INCREMENT y PK
    nombrePedagogo = models.CharField(max_length=255, null=False)  # VARCHAR(255)
    numeroTrabajador = models.CharField(max_length=20, unique=True, null=False)  # UNIQUE, NOT NULL
    bActivo = models.BooleanField(null=True)  # BOOLEAN, puede ser NULL

    def __str__(self):
        return self.nombrePedagogo  # Representación legible del objeto
