from django.contrib import admin
from .models import Docentes  # Importa tu modelo


# Registra tu modelo en el administrador
admin.site.register(Docentes)