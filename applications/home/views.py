from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'arrays.html'

    def get_context_data(self, **kwargs):
        # Datos proporcionados
        nombres = ["Juan", "María", "Carlos", "Ana", "Luis"]
        apellidos = ["Pérez", "González", "Ramírez", "López", "Martínez"]
        edades = [25, 30, 22, 28, 35]

        # Crear una lista de diccionarios
        personas = [
            {"nombre": nombres[i], "apellido": apellidos[i], "edad": edades[i]}
            for i in range(len(nombres))
        ]

        # Añadir los datos al contexto
        context = super().get_context_data(**kwargs)
        context['personas'] = personas
        return context
