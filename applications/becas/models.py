from django.db import models

class Becas(models.Model):
    idBeca = models.AutoField(primary_key=True)  # AUTO_INCREMENT y PK
    nombreBeca = models.CharField(max_length=255, null=False)  # VARCHAR(255), NOT NULL
    tipoBeca = models.CharField(max_length=20, null=False)  # VARCHAR(20), NOT NULL
    bActivo = models.BooleanField(null=True)  # BOOLEAN, puede ser NULL

    def __str__(self):
        return self.nombreBecas  # Representación legible del objeto
