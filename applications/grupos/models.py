from django.db import models

class Grupos(models.Model):
    idGrupo = models.AutoField(primary_key=True)  # AUTO_INCREMENT y PK
    cveGrupo = models.CharField(max_length=10, unique=True, null=False)  # UNIQUE, NOT NULL
    nombreGrupo = models.CharField(max_length=20, null=False)  # VARCHAR(20), NOT NULL
    cuatrimestreGrupo = models.CharField(max_length=30, null=False)  # VARCHAR(30), NOT NULL
    aulaNombre = models.CharField(max_length=30, null=False)  # VARCHAR(30), NOT NULL
    aulaUbicacion = models.CharField(max_length=100, null=False)  # VARCHAR(100), NOT NULL
    bActivo = models.BooleanField(null=True)  # BOOLEAN, puede ser NULL

    def __str__(self):
        return f"{self.cveGrupos} - {self.nombreGrupo}"  # Representación legible del objeto
