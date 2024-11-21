from django.db import models

class EncargadoBecas(models.Model):
    idEncargado = models.AutoField(primary_key=True)  # AUTO_INCREMENT y PK
    nombreEncargado = models.CharField(max_length=255, null=False)  # VARCHAR(255), NOT NULL
    numeroTrabajador = models.CharField(max_length=20, unique=True, null=False)  # UNIQUE, NOT NULL
    bActivo = models.BooleanField(null=True)  # BOOLEAN, puede ser NULL

    def __str__(self):
        return self.nombreEncargado  # Representación legible del objeto
