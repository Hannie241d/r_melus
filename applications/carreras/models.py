from django.db import models

class Carreras(models.Model):
    idCarrera = models.AutoField(primary_key=True)  # AUTO_INCREMENT y PK
    cveCarrera = models.CharField(max_length=10, unique=True, null=False)  # UNIQUE, NOT NULL
    nombreCarrera = models.CharField(max_length=255, null=False)  # VARCHAR(255), NOT NULL
    areaCarrera = models.CharField(max_length=30, null=False)  # VARCHAR(30), NOT NULL
    planEstudios = models.CharField(max_length=30, null=False)  # VARCHAR(30), NOT NULL
    bActivo = models.BooleanField(null=True)  # BOOLEAN, puede ser NULL

    def __str__(self):
        return self.nombreCarreras  # Representación legible del objeto
